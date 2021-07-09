import os

def theme_change(env, data):
    """
    env  : desktop env
    data : theme name
    """

    if env in ('kde','KDE', 'Kde'):
        cmd = "kvantummanager --set {}".format(data)

    elif env in ('gnome', 'GNOME', 'Gnome'):
        cmd = 'gsettings set org.gnome.desktop.wm.preferences theme "{}"'.format(data)

def wallp_change(env, data):
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



