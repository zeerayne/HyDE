#!/usr/bin/env bash

[[ "${HYDE_SHELL_INIT}" -ne 1 ]] && eval "$(hyde-shell init)"
lockscreen="${LOCKSCREEN:-hyprlock}"

case ${1} in
    --get)
        echo "${lockscreen}"
        exit 0
        ;;    
esac

#? To cleanly exit hyprlock we should use a systemd scope unit.
#? This allows us to manage the lockscreen process more effectively.
#? This fix the zombie process issue when hyprlock is unlocked but still running.
unit_id=(-u "hyde-lockscreen.scope")

if app2unit.sh --test "${unit_id[@]}"  -- "${lockscreen}.sh" "${@}"; then
    printf "Executing ${lockscreen} wrapper script : %s\n" "${lockscreen}.sh"
    app2unit.sh  "${unit_id[@]}"  -- "${lockscreen}.sh" "${@}"
else
    printf "Executing raw command: %s\n" "${lockscreen}"
    app2unit.sh "${unit_id[@]}" -- "${lockscreen}" "${@}"
fi
