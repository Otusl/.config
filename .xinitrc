/usr/bin/pipewire &
/usr/bin/pipewire-pulse &
/usr/bin/pipewire-media-session &

# Set wallpaper
xwallpaper --zoom ~/Pictures/catppuccin-leaves.png &

# Reload the previous color scheme settings
# wal -R &

sxhkd &
# dwmblocks &
picom &

# protonvpn
gnome-keyring-daemon --start &
nm-applet &

# Launch dwm 
~/.config/chadwm/scripts/run.sh
