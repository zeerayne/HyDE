#!/usr/bin/env bash
[[ $HYDE_SHELL_INIT -ne 1 ]] && eval "$(hyde-shell init)"
lockscreen="${HYPRLAND_LOCKSCREEN:-$lockscreen}"
lockscreen="${LOCKSCREEN:-hyprlock}"
lockscreen="${HYDE_LOCKSCREEN:-$lockscreen}"
case $1 in
--get)
    echo "$lockscreen"
    exit 0
    ;;
esac
unit_name="hyde-lockscreen.service"
args=(-u "$unit_name" -t service)
if which "$lockscreen.sh" 2>/dev/null 1>&2; then
    printf "Executing $lockscreen wrapper script : %s\n" "$lockscreen.sh"
    app2unit.sh "${args[@]}" -- "$lockscreen.sh" "$@"
else
    printf "Executing raw command: %s\n" "$lockscreen"
    app2unit.sh "${args[@]}" -- "$lockscreen" "$@"
fi
