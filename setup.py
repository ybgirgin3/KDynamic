# !/usr/bin/python3
import os
from time import sleep
from pathlib import Path
#from tqdm import tqdm
import json
# import scheduler

#h = os.path.expanduser('~')
h = Path.home()
BASE_DIR = os.path.join(h, "KDynamic")
THEME_DIR = os.path.join(BASE_DIR, "theme")
PIC_DIR = os.path.join(BASE_DIR, "pics/")

# paths
dirs = ["light", "night", "light_dark"]
#pdir = [""pics/light", "pics/night", "pics/light_dark"]

# folder locations

tlist = {}
#plist = []

# strings
def command(n):
    return """
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
    """.format(n)

# create folders 
def fcreate(d_env: str) -> None:
    # FOLDERS (parents)
    # create theme folders
    # os_spec_dir = f"{THEME_DIR}/{d_env.upper()}" 
    # os.makedirs(f"{os_spec_dir}")

    # create pic folders
    for pd in dirs:
        os.makedirs(f"{PIC_DIR}/{pd}")
        # create command txt to pic in pic folder

    # PICS and TXTs (childs)
    # create theme files
    # get theme names
    # get 3 times
    for count in range(3):
        #tlist.append(input(f"{dirs[count]} theme name: "))
        tlist[dirs[count]] = input(f"{dirs[count]} theme name: ")

    # dump json file
    with open(f'{THEME_DIR}/themes.json', 'w') as f:
        json.dump(tlist, f)



if __name__ == '__main__':
    # desktop env selection
    # $DESKTOP_SESSION env finder command
    # install needed libs
    from termcolor import colored
    print(colored('please be sure you installed requirement libs', 'green'))
    sleep(1)
    desk_env = input('What is your current desktop environment [KDE, GNOME]: ')
    os.makedirs(BASE_DIR)
    with open(os.path.join(BASE_DIR, 'd_env.txt'), 'w') as f:
        f.write(f'{desk_env.upper()}')
    fcreate(desk_env)


        

    
