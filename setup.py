# !/usr/bin/python3
from scheduler import controlling_job
from pathlib import Path
from time import sleep
from utils.utils import word_derivatives
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
dirs = ["light", "light_dark", "night"]

# folder locations

tlist = {}

# create folders 
def fcreate(env: str, wm) -> None:
    # FOLDERS (parents)
    # create theme folders
    # os_spec_dir = f"{THEME_DIR}/{env.upper()}" 
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

    tlist['env'] = env
    tlist['wm'] = wm

    
    """
    light_icon = input('Light Icon Theme: ')
    night_icon = input('Night Icon Theme: ')
    """
    
    """
    tlist['light_i'] = light_icon
    tlist['night_i'] = night_icon
    """
        
    # dump json file
    with open(f'{THEME_DIR}/themes.json', 'w') as f:
        json.dump(tlist, f)

if __name__ == '__main__':
    # desktop env selection
    # install needed libs
    from termcolor import colored
    print(colored('please be sure you installed requirement libs', 'red'))
    sleep(1)
    desk_env = input('What is your current desktop environment [KDE, GNOME, CINNAMON]: ')
    os.makedirs(BASE_DIR)
    
    #if desk_env in ('kde','KDE', 'Kde'):
    if 'KDE' in word_derivatives(desk_env):
        wm = input('Breeze or Kvantum: ').upper()
        #wm = q if q in word_derivatives(q) else print('nopee')
    else: wm = ""
    controlling_job()

    fcreate(desk_env, wm)
    
