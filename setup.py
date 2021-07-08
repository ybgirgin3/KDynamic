# !/usr/bin/python3
import os
from time import sleep
from tqdm import tqdm
# import scheduler
homedir = os.path.expanduser('~')

tloc = ['light', 'night', 'light_dark']
ploc = ['light', 'night', 'light_dark']


def kde():
    """
    install for kde desktop env
    """

    def fcreate(name: list) -> None:
        # for themes
        if name == 'tloc':
            for n in name:
                os.makedirs(f"{homedir}/KDynamic/kde/themes/{n}/")

        # for pictures
        elif name == 'ploc':
            for p in name:
                os.makedirs(f"{homedir}/KDynamic/kde/pictures/{n}/")

    # create folders
    print("creating folders.. please wait")
    #range_ = len(tloc) + len(ploc)
    #for i in tqdm.trange(range_):
    # folders need to be created
    # theme
    #   light
    #   night
    #   light_dark
    # pictures
    #   light
    #   dark
    #   light_dark

    # theme folder create
    fcreate(tloc)
    # picture folder create
    fcreate(ploc)






def gnome():
    pass

if __name__ == '__main__':
    # desktop env selection
    # $DESKTOP_SESSION env finder command
    desk_env = input('What is your current desktop environment [KDE, GNOME]: ')
    if desk_env in ('kde', 'KDE', 'Kde'):
        kde()
    elif desk_env in ('gnome', 'GNOME', 'Gnome'):
        gnome()


        

    
