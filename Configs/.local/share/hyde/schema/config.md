---
HyDE exposes `xdg_config/hyde/config.toml` file for users to modify. This lets users have the ability to interact the scripts without using command arguments.

Users are encouraged to use an editor that support schema validation to ensure the configuration file is valid.

"$schema" = "https://raw.githubusercontent.com/HyDE-Project/HyDE/refs/heads/master/Configs/.local/share/hyde/schema/config.toml.json"
---
### [wallpaper]

Wallpaper configuration.

| Key | Description | Default |
| --- | ----------- | ------- |
| custom_paths | List of paths to search for wallpapers. | [] |
| backend | Wallpaper backend, requires 'wallpaper.<backend>.sh' as handler script in $PATH | swww |

### [wallpaper.swww]

swwwallselect.sh configuration.

| Key | Description | Default |
| --- | ----------- | ------- |
| framerate | Transition framerate. | 60 |
| duration | Transition duration. | 1 |
| transition_next | Transition type for next wallpaper. | grow |
| transition_prev | Transition type for previous wallpaper. | outer |
| transition_default | Transition type for default wallpaper. | grow |

### [rofi]

Global rofi configuration.

| Key | Description | Default |
| --- | ----------- | ------- |
| scale | Rofi default scaling. | 10 |

### [rofi.hyprlock]

'hyprlock.sh select' configuration.

| Key | Description | Default |
| --- | ----------- | ------- |
| scale | Scaling for hyprlock. | 10 |

### [rofi.animation]

'animation.sh select' configuration.

| Key | Description | Default |
| --- | ----------- | ------- |
| scale | Scaling for animation. | 10 |

### [rofi.glyph]

glyph-picker.sh configuration.

| Key | Description | Default |
| --- | ----------- | ------- |
| scale | Scaling for glyph picker. | 10 |

### [rofi.launch]

rofilaunch.sh configuration.

| Key | Description | Default |
| --- | ----------- | ------- |
| scale | Scaling for launch. | 5 |
| drun_args | Additional arguments for drun mode. | [] |
| run_args | Additional arguments for run mode. | [] |
| window_args | Additional arguments for window mode. | [] |
| filebrowser_args | Additional arguments for filebrowser mode. | [] |

### [rofi.cliphist]

cliphist.sh configuration.

| Key | Description | Default |
| --- | ----------- | ------- |
| scale | Scaling for cliphist. | 10 |

### [rofi.wallpaper]

swwwallselect.sh configuration.

| Key | Description | Default |
| --- | ----------- | ------- |
| scale | Scaling for wallpaper. | 10 |

### [rofi.emoji]

emoji-picker.sh configuration.

| Key | Description | Default |
| --- | ----------- | ------- |
| style | Style for emoji picker. | 1 |
| scale | Scaling for emoji picker. | 10 |

### [rofi.theme]

themeselect.sh configuration.

| Key | Description | Default |
| --- | ----------- | ------- |
| scale | Scaling for theme selector. | 6 |

### [wlogout]

wlogout configuration.

| Key | Description | Default |
| --- | ----------- | ------- |
| style | Style for wlogout. | 2 |

### [battery.notify]

batterynotify.sh configuration.

| Key | Description | Default |
| --- | ----------- | ------- |
| timer | Timer for battery notifications. | 120 |
| notify | Notification threshold. | 1140 |
| interval | Interval for battery notifications. | 5 |
| dock | Dock status for battery notifications. | true |

### [battery.notify.threshold]

Thresholds for battery notifications.

| Key | Description | Default |
| --- | ----------- | ------- |
| full | Full battery threshold. | 90 |
| critical | Critical battery threshold. | 10 |
| low | Low battery threshold. | 20 |
| unplug | Unplug battery threshold. | 100 |

### [battery.notify.execute]

Commands to execute for battery notifications.

| Key | Description | Default |
| --- | ----------- | ------- |
| unplug | Command to execute when unplugged. |  |
| low | Command to execute when battery is low. |  |
| critical | Command to execute when battery is critical. | systemctl suspend |
| charging | Command to execute when charging. |  |
| discharging | Command to execute when discharging. |  |

### [rofi.keybind.hint]

keybind_hint.sh configuration.

| Key | Description | Default |
| --- | ----------- | ------- |
| delimiter | Delimiter for keybind hints. | 	 |
| width | Width for keybind hints. | 40em |
| height | Height for keybind hints. | 40em |
| line | Number of lines for keybind hints. | 16 |

### [screenshot]

screenshot.sh configuration.

| Key | Description | Default |
| --- | ----------- | ------- |
| annotation_tool | Annotation tool for screenshots. | satty |
| annotation_pre_command | Pre command for annotation tool. | [] |
| annotation_post_command | Post command for annotation tool. | [""] |

### [wallbash]

wallbash configuration.

| Key | Description | Default |
| --- | ----------- | ------- |
| skip_template | Templates to skip when using wallbash. | [""] |

### [waybar]

waybar configuration.

| Key | Description | Default |
| --- | ----------- | ------- |
| font | Font for waybar. | JetBrainsMono Nerd Font |
| scale | Total scaling for waybar. | 10 |
| icon_size | Icon size for waybar. | 10 |

### [weather]

Weather configuration.

| Key | Description | Default |
| --- | ----------- | ------- |
| temperature_unit | Temperature unit ('c' or 'f'). | c |
| time_format | Time format ('12h' or '24h'). | 24h |
| windspeed_unit | Windspeed unit ('km/h' or 'mph'). | km/h |
| show_icon | Show the weather icon in waybar. | true |
| show_location | Show the location in waybar. | true |
| show_today | Show detailed description of today in tooltip. | true |
| forecast_days | Number of days to show forecast (0-3). | 3 |
| location | Location/coordinates string for the weather output. |  |

### [cava.stdout]

'cava.sh stdout' configuration.

| Key | Description | Default |
| --- | ----------- | ------- |
| max_instances | Maximum number of cava instances. | 1 |
| bar | Bar characters for cava. | ▁▂▃▄▅▆▇█ |
| width | Width of the cava output. | 20 |
| range | Number of bars minus one. | 7 |
| standby | Standby character for cava. | 🎶 |

### [cava.hyprlock]

'cava.sh hyprlock' configuration.

| Key | Description | Default |
| --- | ----------- | ------- |
| max_instances | Maximum number of cava instances. | 1 |
| bar | Bar characters for cava. | ▁▂▃▄▅▆▇█ |
| width | Width of the cava output. | 20 |
| range | Number of bars minus one. | 7 |
| standby | Standby character for cava. | 🎶 |

### [cava.waybar]

'cava.sh waybar' configuration.

| Key | Description | Default |
| --- | ----------- | ------- |
| max_instances | Maximum number of cava instances. | 1 |
| bar | Bar characters for cava. | ▁▂▃▄▅▆▇█ |
| width | Width of the cava output. | 20 |
| range | Number of bars minus one. | 7 |
| standby | Standby character for cava. | 🎶 |

### [hypr.config]

Hypr configuration.

| Key | Description | Default |
| --- | ----------- | ------- |
| sanitize | List of regex to sanitize in the theme.config. | [".*rgba\(.*,.*,.*,.*\)"] |

### [volume]

volumecontrol.sh configuration.

| Key | Description | Default |
| --- | ----------- | ------- |
| notify | Enable notifications for volume control. | true |
| steps | Number of steps to increase/decrease volume. | 5 |
| boost | Enable volume boost. | false |
| boost_limit | Volume boost limit. | 120 |

### [brightness]

brightnesscontrol.sh configuration.

| Key | Description | Default |
| --- | ----------- | ------- |
| notify | Enable notifications for brightness control. | true |
| steps | Number of steps to increase/decrease brightness. | 5 |

### [sysmonitor]

sysmonlaunch.sh configuration.

| Key | Description | Default |
| --- | ----------- | ------- |
| execute | Default command to execute. |  |
| commands | Fallback command options. | [""] |

### [notification]

Notification script configuration.

| Key | Description | Default |
| --- | ----------- | ------- |
| font | Font for notifications. | mononoki Nerd Font |
| font_size | Font size for notifications. | 10 |

### [hyprland]

Hyprland configuration.

| Key | Description | Default |
| --- | ----------- | ------- |
| browser | Browser. | firefox |
| editor | Editor. | code |
| explorer | File manager. | dolphin |
| idle | Idle manager. | hypridle |
| lockscreen | Lockscreen. | lockscreen.sh |
| terminal | Terminal. | kitty |
| quickapps | Quick apps. | kitty |
| bar | Bar. | waybar |
| color_scheme | Color scheme. | prefer-dark |
| gtk_theme | GTK theme. | Wallbash-Gtk |
| icon_theme | Icon theme. | Tela-circle-dracula |
| cursor_size | Cursor size. | 24 |
| cursor_theme | Cursor theme. | Bibata-Modern-Ice |
| button_layout | Button layout. (gtk only) |  |
| document_font_size | Document font size. | 10 |
| font | Font. | Canterell |
| font_antialiasing | Font antialiasing. | rgba |
| font_hinting | Font hinting. | full |
| font_size | Font size. | 10 |
| monospace_font | Monospace font. | CaskaydiaCove Nerd Font Mono |
| monospace_font_size | Monospace font size. | 9 |
| background_path | LockScreen's Background path. |  |

### [hyprland_start]

Hyprland start configuration.

| Key | Description | Default |
| --- | ----------- | ------- |
| apptray_bluetooth | Bluetooth applet. | blueman-applet |
| auth_dialogue | Authentication dialogue. | polkitkdeauth.sh |
| bar | Bar. | hyde-shell waybar --watch |
| battery_notify | Battery notification script. | batterynotify.sh |
| dbus_share_picker | DBus share picker. | dbus-update-activation-environment --systemd --all |
| idle_daemon | Idle daemon. | hypridle |
| image_clipboard | Image clipboard. | wl-paste --type image --watch cliphist store |
| network_manager | Network manager. | nm-applet --indicator |
| notifications | Notifications. | swaync |
| removable_media | Removable media manager. | udiskie --no-automount --smart-tray |
| systemd_share_picker | Systemd share picker. | systemctl --user import-environment QT_QPA_PLATFORMTHEME WAYLAND_DISPLAY XDG_CURRENT_DESKTOP |
| text_clipboard | Text clipboard. | wl-paste --type text --watch cliphist store |
| wallpaper | Wallpaper script. | $scrPath/wallpaper.sh --global |
| xdg_portal_reset | XDG portal reset script. | resetxdgportal.sh |

### [mediaplayer]

mediaplayer.py configuration.

| Key | Description | Default |
| --- | ----------- | ------- |
| prefix_playing | Prefix for playing media. |  |
| prefix_paused | Prefix for paused media. |    |
| max_length | Max length of song and artist string. | 70 |
| standby_text | To display on standby. |   Music |
| artist_track_separator | Separator symbols to display between artist and track. |    |

