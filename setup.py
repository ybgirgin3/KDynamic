# !/usr/bin/python3
from scheduler import controlling_job
from pathlib import Path
from time import sleep
import json
import os

#from tqdm import tqdm
# import scheduler

#h = os.path.expanduser('~')
h = Path.home()
BASE_DIR = os.path.join(h, "KDynamic")
THEME_DIR = os.path.join(BASE_DIR, "theme")
PIC_DIR = os.path.join(BASE_DIR, "pics/")

# paths
dirs = ["light", "night", "light_dark"]

# folder locations

tlist = {}


# create folders 
def fcreate(d_env: str, wm) -> None:
    # FOLDERS (parents)
    # create theme folders
    # os_spec_dir = f"{THEME_DIR}/{d_env.upper()}" 
    os.makedirs(f"{THEME_DIR}")

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
        tlist[f"{dirs[count]}_t"] = input(f"{dirs[count]} theme name: ")
        tlist[f"{dirs[count]}_h"] = input(f"{dirs[count]} theme start hour: ")
    
    tlist['env'] = d_env
    tlist['wm'] = wm
        
        
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
    desk_env = input('What is your current desktop environment [KDE, GNOME, CINNAMON]: ')
    os.makedirs(BASE_DIR)
    

    if desk_env in ('kde','KDE', 'Kde'):
        wm = input('Breeze or Kvantum: ')
       
    else: wm = ""
    controlling_job()
    fcreate(desk_env, wm)


        

    
