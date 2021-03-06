# KDynamic: An Alternative to MacOS Mojave Dynamic Theme and Wallpaper Changer for KDE Plasma 5

## Description

KDynamic is a multiple python script which makes whole system theme light or dark by specified hours using cron scheduler

KDynamic uses native K Desktop Environment (KDE) terminal commands so nothing unfamiliar

## Configuration

KDynamic need some paths;
- Where your favorite light plasma theme located
- Where your favorite dark plasma theme located
- Where your favorite wallpapers which categorized by you

to make your desktop like these

*light theme*

<img src='images/light.png'/>

*light_dark isDark=False*

<img src='images/light_dark_false.png'/>

*light_dark isDark=True*

<img src='images/light_dark_true.png'/>

*night theme*

<img src='images/night.png'/>


but don't worry setup.py will make this boring stuff for you

```sh
~/$ git clone https://github.com/ybgirgin3/KDynamic.git
~/$ cd KDynamic
~/$ python3 setup.py
```

## What you need to do for make program run ?

- First things first you need to pick up some wallpapers for each of theme maybe from [unsplash.com](http://unsplash.com) or somewhere you love

- Move images to the specified folders

- Make needed changes into the txt file


**after installation done and moved favorite wallpapers carefully run**

```sh
~/$ python3 scheduler.py
```
**this will add a schedule to Cron and it's will not use your cpu while doing nothing***


**This script created with python3**


**Script includes print functions so you can see what's going on while this little script running if you want**

for this run program manually;

```sh
~/$ python3 main.py
```

## UPDATE v2
Program will not run in background anymore. Running will happen with Cron the Task Scheduler

## UPDATE v3
Kvantum themes support added !!

Now you can choose which theme type you want to use e.g. for kvantum theme

```sh
~/$ python kvantum_scheduler.py
```
## UPDATE v4
KDE configuration file modifier has been added.<br>
We can say it's just simply beta extension. So scripts may need some change..<br>
It's force to change system colors via replacing ***~/.config/kdeglobals*** file. So **USE IT AT YOUR OWN RISK**<br>
to make it work, after your installation done;

i.e for getting dark theme colors;

```sh
cd conf && python3 darkconf.py
```
and it's done..


**This script developed and tested on**
  * **KDE Plasma 5.17.5**
  * **Qt 5.13.2**
  * **Kernel 5.3.0-26-generic**
