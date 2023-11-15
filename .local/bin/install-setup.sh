sudo pacman -Syu base-devel yay git rofi zsh flameshot firefox pipewire pipewire-audio pipewire-pulse pavucontrol qbittorrent lxappearance mpv gimp piper vim nvim networkmanager htop picom libreoffice zathura zathura-djvu zathura-pdf-mupdf
yay -Syu jellyfin-server jellyfin-web jellyfin-ffmpeg jellyfin-media-player vscodium-bin librewolf-bin upscayl-bin
sudo -v && wget -nv -O- https://download.calibre-ebook.com/linux-installer.sh | sudo sh /dev/stdin
git clone https://git.suckless.org/dwm ~/
git clone https://git.suckless.org/st ~/
cd ~/dwm
sudo make clean install
cd ~/st
sudo make clean install
