#!/usr/bin/env sh

echo "Replacing rofi-wayland to rofi"

sudo pacman -Sy
sudo pacman -Rns --noconfirm rofi-wayland
sudo pacman -S --noconfirm rofi
