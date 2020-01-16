# !/usr/bin/python3
import os
from time import sleep
# import scheduler
homedir = os.path.expanduser('~')

## breeze and kvantum theme added


###### light_plasma txtleri içinde path oluşturucu koy

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
    print('Required package "crontab" will install during session !')
    sleep(.5)
    print('[-] home directory detecting..')
    sleep(2)
    print('[+] done..')
    sleep(.5)
    ### create wallpapers directory
    ## light theme wallpapers
    # go to home directory
    os.chdir(homedir)
    ## light pics
    os.makedirs('{}/KDynamic/Pictures/'.format(homedir))
    # light_dark pics
    os.chdir('{}/KDynamic/Pictures/'.format(homedir))

    print('[-] Light Theme Wallpapers Folder Creating...')
    os.makedirs('light')
    os.chdir('{}/KDynamic/Pictures/light'.format(homedir))
    txt_creator('light.txt')
    sleep(1)
    print('[+] done..')

    print('[-] Light Dark Theme Wallpapers Folder Creating...')
    os.chdir('{}/KDynamic/Pictures/'.format(homedir))
    os.makedirs('light_dark')
    os.chdir('{}/KDynamic/Pictures/light_dark'.format(homedir))
    txt_creator('light_dark.txt')
    sleep(1)
    print('[+] done..')

    print('[-] Night Theme Wallpapers Folder Creating...')
    os.chdir('{}/KDynamic/Pictures/'.format(homedir))
    os.makedirs('night')
    os.chdir('{}/KDynamic/Pictures/night'.format(homedir))
    txt_creator('night.txt')
    sleep(1)
    print('[+] done..')

    ## Breeze Theme Folder
    os.chdir('{}/KDynamic/'.format(homedir))
    print('[-] Breeze Theme Folder Creating..')
    sleep(1)
    os.makedirs('{}/KDynamic/Breeze/'.format(homedir))
    os.chdir('{}/KDynamic/Breeze/'.format(homedir))

    print('[-] Theme Files Creating..')
    txt_creator('light_plasma_theme.txt')
    txt_creator('night_plasma_theme.txt')
    sleep(1)
    print('[+] done..')

    os.chdir('{}/KDynamic/'.format(homedir))

    ## Breeze Theme Folder
    print('[-] Kvantum Theme Folder Creating...')
    sleep(1)
    os.makedirs('{}/KDynamic/Kvantum/'.format(homedir))
    os.chdir('{}/KDynamic/Kvantum/'.format(homedir))
    print('[-] Theme Files Creating..')

    txt_creator('light_plasma_theme.txt')
    txt_creator('night_plasma_theme.txt')
    print('[+] done..')
    sleep(1)
    print('[+] all done..')
    print('Files located at {}/KDynamic'.format(homedir))
    print('Required package installing')
    os.system('pip3 install python-crontab')
    print('python-crontab successfully installed')
    # print('After moving your favorite pictures to created directories run this command\n    ~$ python3 scheduler.py')
    print('Run scheduler script of your wished theme type\ne.g: for kvantum themes\n\tpython3 kvantum_scheduler.py')
    print('Don\'t forget to make changes in <theme>.txt files and <wallpapers>.txt files otherwise program will not work.')
    print("""
        NOTE: Some Application May Need Restart to Effect Changed Kvantum Theme..
        """)




if __name__ == '__main__':
    print("""
          KDynamic: KDE Plasma 5 Theme Changer
          author: Yusuf Berkay Girgin

          """)
    installer()
