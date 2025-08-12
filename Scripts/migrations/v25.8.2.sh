#!/usr/bin/env bash

if command -v hyde-shell >/dev/null 2>&1; then
    echo "Reloading Hyde shell shaders..."
    hyde-shell shaders --reload
fi
