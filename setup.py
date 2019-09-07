# !/usr/bin/python3
import os
from time import sleep
# import scheduler
homedir = os.path.expanduser('~')


###### light_plasma txtleri içinde path oluşuturucu koy

def txt_creator(theme):
    """
        txt_creator('light_plasma_theme.txt')
        txt_creator('night_plasma_theme.txt')
    """
    with open(theme, 'w') as f:
        if theme == 'light_plasma_theme.txt' or theme == 'night_plasma_theme.txt':
            f.write('enter your favorite theme name here (only name of it not path !! )')

        else:
            f.write('# replace here with this command \nqdbus org.kde.plasmashell /PlasmaShell org.kde.PlasmaShell.evaluateScript \'var allDesktops = desktops();print (allDesktops);for (i=0;i<allDesktops.length;i++) {d = allDesktops[i];d.wallpaperPlugin = "org.kde.image";d.currentConfigGroup = Array("Wallpaper", "org.kde.image", "General");d.writeConfig("Image", "file:///home/<username>/<theme_file_path>/<image_name>.jpg")}\'\n within filling needed spaces.. and of course for each of pics.. :(')

def installer():
    print('! Please wait until process end... !')
    sleep(1)
    print('[-] home directory detecting..')
    sleep(2)
    print('[+] done..')
    sleep(.5)
    ### create wallpapers directory
    ## light theme wallpapers
    # go to home directory
    print('[-] directory changing to home directory..')
    os.chdir(homedir)
    sleep(1)
    print('[+] done..')
    sleep(.5)
    # create files for light theme
    sleep(.5)
    print('[-] KDynamic files creating for light theme wallpapers..')
    os.makedirs('{}/KDynamic/Pictures/light/'.format(homedir))
    sleep(1)
    print('[+] done..')
    sleep(.5)
    print('txt files creating for plasma themes..')
    os.chdir('{}/KDynamic/'.format(homedir))
    txt_creator('light_plasma_theme.txt')
    txt_creator('night_plasma_theme.txt')
    sleep(1)
    print('[+] done..')
    sleep(.5)
    print('[-] light.txt file creating..')
    os.chdir('{}/KDynamic/Pictures/light'.format(homedir))
    txt_creator('light.txt')
    sleep(1)
    print('[+] done..')
    sleep(1)
    # get into KDynamic/Pictures file
    print('[-] KDynamic files creating for light_dark theme wallpapers..')
    os.chdir('{}/KDynamic/Pictures'.format(homedir))
    sleep(1)
    # create file for light dark theme
    os.makedirs('light_dark')
    sleep(1)
    print('[-] light_dark.txt file creating..')
    os.chdir('{}/KDynamic/Pictures/light_dark'.format(homedir))
    txt_creator('light_dark.txt')
    sleep(1)
    print('[+] done..')
    sleep(.5)
    print('[-] KDynamic files creating for night theme wallpapers')
    # create file for night theme
    os.chdir('{}/KDynamic/Pictures/'.format(homedir))
    os.makedirs('night')
    sleep(1)
    print('[+] done..')
    sleep(1)
    print('[-] night.txt file creating..')
    os.chdir('{}/KDynamic/Pictures/night'.format(homedir))
    txt_creator('night.txt')
    sleep(1)
    print('[+] done..')
    print('File creating and locating completely done..')
    sleep(.5)
    print('Task schedule creating..')
    sleep(.5)
    # scheduler.controlling_job()
    print('[+] all done..')
    print('Files located in {}/KDynamic/'.format(homedir))
    print('After moving your favorite pictures to created directories run this command\n    ~$ python3 scheduler.py')


if __name__ == '__main__':
    print("""
          KDynamic: KDE Plasma 5 Theme Changer
          author: Yusuf Berkay Girgin

          """)
    installer()
