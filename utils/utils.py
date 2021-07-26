import os
from itertools import product

# find derivates
def word_derivatives(word: str) -> list:
    list_ = [(c, c.upper()) if not c.isdigit() else (c,) for c in word.lower()]
    return ["".join(item) for item in product(*list_)]


# theme change
def theme_change(env: str, data: str, wm) -> None:
    """
    env  : desktop env
    data : theme name
    """

    #if env in ('kde','KDE', 'Kde'):
    if 'KDE' in word_derivatives(env):
        print('kde env')
        #if wm in ('KVANTUM', 'kvantum', 'Kvantum'):
        if 'KVANTUM' in word_derivatives(wm):
            cmd = "kvantummanager --set {}".format(data)
            
        #elif wm in ('BREEZE', 'breeze', 'Breeze'):
        elif 'BREEZE' in word_derivatives(wm):
            cmd = "kwriteconfig5 --file ~/.config/plasmarc --group Theme --key name {}".format(data)

    #elif env in ('gnome', 'GNOME', 'Gnome'):
    elif 'GNOME' in word_derivatives(env):
        print('gnome env')
        cmd = 'gsettings set org.gnome.desktop.interface gtk-theme "{}"'.format(data)

    #elif env in ('cinnamon', 'CINNAMON', 'Cinnamon'):
    elif 'CINNAMON' in word_derivatives(env):
        print('cinnamon env')
        cmd = 'gsettings set org.cinnamon.desktop.interface gtk-theme "{}"'.format(data)
        
    os.system(cmd)

# wallpaper change
def wallp_change(env: str, data: str) -> None:
    """
    env  : desktop env
    data : img path
    """

    #if env in ('kde','KDE', 'Kde'):
    if 'KDE' in word_derivatives(env):
        # file running from theme_cfg/tmain.py
        # so python finds the current dir theme_cfg and can't find walpapers_kde.sh
        cmd = f"/bin/sh ../utils/wallpaper_kde.sh {data}"
        

    #elif env in ('gnome', 'GNOME', 'Gnome'):
    elif 'GNOME' in word_derivatives(env):
        cmd = "gsettings set org.gnome.desktop.background picture-uri file:///{}".format(data)


    #elif env in ('cinnamon', 'CINNAMON', 'Cinnamon'):
    elif 'CINNAMON' in word_derivatives(env):
        cmd = "gsettings set org.cinnamon.desktop.background picture-uri file:///{}".format(data)

    os.system(cmd)


# icon change
def icon_change(env: str, data: str) -> None:
    # need fix, disabled
    if data is not None:
        #if env in ('kde','KDE', 'Kde'):
        if 'KDE' in word_derivatives(env):
            print('kde icon changes')
            cmd = "kwriteconfig5 --file ~/.config/kdeglobals --group Icons --key Theme {}"

        #elif env in ('gnome', 'GNOME', 'Gnome'):
        elif 'GNOME' in word_derivatives(env):
            print('gnome icon changes')
            cmd = "gsettings set org.gnome.desktop.interface icon-theme {}".format(data)

        #elif env in ('cinnamon', 'CINNAMON', 'Cinnamon'):
        elif 'CINNAMON' in word_derivatives(env):
            cmd = "gsettings set org.cinnamon.desktop.interface icon-theme {}".format(data)

        os.system(cmd)
    else: pass

# NOTE: only kde utils (for now)
# colorscheme change
def color_change(env: str, data: str) -> None:
    if data is not None:
        if 'KDE' in word_derivatives(env):
            print('kde colorscheme changing')
            cmd = "kwriteconfig5 --file ~/.config/kdeglobals --group General --key ColorScheme '{}'".format(data)

        # NOTE: gnome da renk olarak ayrı bir tema yok
        #elif 'GNOME' in word_derivatives(env):
        #    print('gnome colorscheme changing')
        #        cmd = ""

    os.system(cmd)


# gtk apps in kde
def gtk_theme_for_kde(env: str, data: str) -> None:
    print('gtk apps specific theme changing')
    if 'KDE' in word_derivatives(env):
        cmd = "kwriteconfig5 --file ~/.config/gtk-3.0/settings.ini --group Settings --key gtk-theme-name '$1'"

    os.system(cmd)



# change plasma theme
def plasma_theme_change(env: str, data: str) -> None:
    print('plasma theme changing')
    if 'KDE' in word_derivatives(env):
        cmd = "kwriteconfig5 --file ~/.config/plasmarc --group Theme --key name '{}'".format(data)

    os.system(cmd)



