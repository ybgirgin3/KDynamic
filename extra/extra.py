import os

def theme_change(env: str, data: str, wm=None) -> None:
    """
    env  : desktop env
    data : theme name
    """

    if env in ('kde','KDE', 'Kde'):
        print('kde env')
        if wm in ('KVANTUM', 'kvantum', 'Kvantum'):
            cmd = "kvantummanager --set {}".format(data)
            
        elif wm in ('BREEZE', 'breeze', 'Breeze'):
            cmd = "kwriteconfig5 --file ~/.config/plasmarc --group Theme --key name {}".format(data)

    elif env in ('gnome', 'GNOME', 'Gnome'):
        print('gnome env')
        cmd = 'gsettings set org.gnome.desktop.interface gtk-theme "{}"'.format(data)
        
    os.system(cmd)

def wallp_change(env: str, data: str) -> None:
    """
    env  : desktop env
    data : img path
    """

    if env in ('kde','KDE', 'Kde'):
        cmd = ("""
        dbus-send --session --dest=org.kde.plasmashell --type=method_call /PlasmaShell org.kde.PlasmaShell.evaluateScript 'string:
        var Desktops = desktops();
        for (i=0;i<Desktops.length;i++) {
            d = Desktops[i];
            d.wallpaperPlugin = "org.kde.image";
            d.currentConfigGroup = Array("Wallpaper",
                                        "org.kde.image",
                                        "General");
            d.writeConfig("Image", "file:///{}");
        }'
        """.format(data))

    elif env in ('gnome', 'GNOME', 'Gnome'):
        cmd = "gsettings set org.gnome.desktop.background picture-uri file:///{}".format(data)


    os.system(cmd)

