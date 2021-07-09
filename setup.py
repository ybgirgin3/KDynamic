# !/usr/bin/python3
import os
from time import sleep
#from tqdm import tqdm
import json
# import scheduler

h = os.path.expanduser('~')
BASE_DIR = os.path.join(h, "/KDynamic")
THEME_DIR = os.path.join(BASE_DIR, "/theme")
PIC_DIR = os.path.join(BASE_DIR, "/pics/")

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
    os_spec_dir = f"{THEME_DIR}/{d_env}" 
    os.makedirs(f"{os_spec_dir}")

    # create pic folders
    for pd in dirs:
        os.makedirs(f"{PIC_DIR}}/{pd}")

    # PICS and TXTs (childs)
    # create theme files
    # get theme names
    # get 3 times
    for count in range(3):
        #tlist.append(input(f"{dirs[count]} theme name: "))
        tlist[dirs[count]] = input(f"{dirs[count]} theme name: ")

    # dump json file
    with open(f'{os_spec_dir}/themes.json', 'w') as f:
        json.dump(tlist, f)



if __name__ == '__main__':
    # desktop env selection
    # $DESKTOP_SESSION env finder command
    desk_env = input('What is your current desktop environment [KDE, GNOME]: ')
    main(desk_env)


        

    
