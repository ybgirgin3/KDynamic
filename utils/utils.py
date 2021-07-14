import os

def theme_change(env: str, data: str, wm) -> None:
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
        # file running from theme_cfg/tmain.py
        # so python finds the current dir theme_cfg and can't find walpapers_kde.sh
        cmd = f"/bin/sh ../utils/wallpaper_kde.sh {data}"
        

    elif env in ('gnome', 'GNOME', 'Gnome'):
        cmd = "gsettings set org.gnome.desktop.background picture-uri file:///{}".format(data)


    os.system(cmd)

