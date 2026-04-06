import os
import sys
import subprocess
import shutil
import argparse
import importlib

lib_dir = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, lib_dir)

import xdg_base_dirs  # noqa: E402
import wrapper.libnotify as notify  # noqa: E402


# =========================
# Core helpers
# =========================

def get_venv_path() -> str:
    return os.path.join(str(xdg_base_dirs.xdg_state_home()), "hyde", "python_env")


def get_project_dir() -> str:
    return os.path.dirname(lib_dir)


def get_uv() -> str:
    uv = shutil.which("uv")
    if uv is None:
        raise FileNotFoundError(
            "uv is not installed. Install it with 'pacman -S uv' or "
            "'curl -LsSf https://astral.sh/uv/install.sh | sh'"
        )
    return uv


# =========================
# Execution layer
# =========================

def run_uv(args, venv_path=None, notify_msg=None) -> subprocess.CompletedProcess[str]:
    uv = get_uv()
    venv_path = venv_path or get_venv_path()
    project_dir = get_project_dir()

    env = os.environ.copy()
    env["UV_PROJECT_ENVIRONMENT"] = venv_path

    if notify_msg:
        notify.send("HyDE UV", notify_msg)

    cmd = [uv] + args + ["--project", project_dir]

    result = subprocess.run(cmd, capture_output=True, text=True, env=env)

    if result.returncode != 0:
        err = result.stderr.strip() or result.stdout.strip() or "Unknown error"
        notify.send(
            "HyDE UV",
            f"Error:\n{err}",
            urgency="critical",
        )
        raise RuntimeError(err)

    return result


# =========================
# Venv logic
# =========================

def is_venv_valid(venv_path) -> bool:
    python_exe = os.path.join(venv_path, "bin", "python")
    pyvenv_cfg = os.path.join(venv_path, "pyvenv.cfg")

    if not (os.path.isfile(python_exe) and os.access(python_exe, os.X_OK)):
        return False

    if os.path.exists(pyvenv_cfg):
        try:
            with open(pyvenv_cfg, "r") as f:
                for line in f:
                    key, sep, value = line.partition("=")
                    if sep and key.strip() == "version":
                        venv_version = value.strip()
                        cur_version = f"{sys.version_info.major}.{sys.version_info.minor}"
                        if not venv_version.startswith(cur_version):
                            return False
        except Exception:
            return False

    return True


def create_venv() -> None:
    run_uv(["sync"], notify_msg="⏳ Syncing virtual environment...")
    notify.send("HyDE UV", "✅ Virtual environment ready")


def destroy_venv(venv_path=None) -> None:
    venv_path = venv_path or get_venv_path()
    if os.path.exists(venv_path):
        shutil.rmtree(venv_path)
        notify.send("HyDE UV", "🗑️ Virtual environment removed")


def rebuild_venv() -> None:
    venv_path = get_venv_path()

    if os.path.exists(venv_path) and not is_venv_valid(venv_path):
        notify.send("HyDE UV", "⚠️ Broken venv detected, rebuilding…")
        destroy_venv(venv_path)

    run_uv(["sync"], notify_msg="⏳ Rebuilding virtual environment...")
    notify.send("HyDE UV", "✅ Rebuild complete")


# =========================
# Package management
# =========================

def install_dependencies() -> None:
    run_uv(["sync"], notify_msg="📦 Syncing dependencies...")


def install_package(package) -> None:
    notify.send("HyDE UV", f"Installing {package}...")
    run_uv(["add", package])


def uninstall_package(package) -> None:
    notify.send("HyDE UV", f"Removing {package}...")
    run_uv(["remove", package])


# =========================
# Import helpers
# =========================

def inject_site_packages() -> None:
    venv_path = get_venv_path()
    site_packages = os.path.join(
        venv_path,
        "lib",
        f"python{sys.version_info.major}.{sys.version_info.minor}",
        "site-packages",
    )

    for path in (site_packages, venv_path):
        if path not in sys.path:
            sys.path.insert(0, path)


def v_import(module_name, auto_install=True) -> object:
    inject_site_packages()

    try:
        return importlib.import_module(module_name)
    except ImportError:
        if not auto_install:
            raise ImportError(f"Module '{module_name}' not found and auto_install is disabled")

        notify.send("HyDE UV", f"Installing missing module: {module_name}")
        install_package(module_name)

        inject_site_packages()
        importlib.invalidate_caches()
        
        try:
            module = importlib.import_module(module_name)
            notify.send("HyDE UV", f"{module_name} installed successfully")
            return module
        except ImportError as e:
            notify.send(
                "HyDE UV",
                f"Failed to import {module_name} after installation: {e}",
                urgency="critical",
            )
            raise RuntimeError(f"Failed to import {module_name} after installation: {e}")


# =========================
# CLI commands
# =========================

def cmd_create(_) -> None:
    create_venv()


def cmd_install(args) -> None:
    if args.packages:
        for pkg in args.packages:
            install_package(pkg)
    else:
        install_dependencies()


def cmd_uninstall(args) -> None:
    uninstall_package(args.package)


def cmd_destroy(_) -> None:
    destroy_venv()


def cmd_rebuild(_) -> None:
    rebuild_venv()


COMMANDS = {
    "create": cmd_create,
    "install": cmd_install,
    "uninstall": cmd_uninstall,
    "destroy": cmd_destroy,
    "rebuild": cmd_rebuild,
}


# =========================
# CLI entry
# =========================

def main(argv) -> None:
    parser = argparse.ArgumentParser(description="HyDE Python environment manager")
    subparsers = parser.add_subparsers(dest="command")

    subparsers.add_parser("create")

    install_parser = subparsers.add_parser("install")
    install_parser.add_argument("packages", nargs="*")

    uninstall_parser = subparsers.add_parser("uninstall")
    uninstall_parser.add_argument("package")

    subparsers.add_parser("destroy")
    subparsers.add_parser("rebuild")

    args = parser.parse_args(argv)

    if args.command in COMMANDS:
        COMMANDS[args.command](args)
    else:
        parser.print_help()


def hyde(args) -> None:
    main(args)


if __name__ == "__main__":
    hyde(sys.argv[1:])
