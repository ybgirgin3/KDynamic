#!/usr/bin/python3
# Filename scheduler.py

## uses cron to make app scheduled
from crontab import CronTab
import os

# bu dosya crontab için bir ayarlama oluşturmayacak çünkü o iş setup.py'ın

## saatlerde daha sonradan yapılabilecek olan değişiklikleri göz önünde bulundurarak
## aynı isimli bir task var mı diye kontrol et, eğer varsa sil.
## main_old dosyasındaki belirli saatleri buraya çek ve onları cron'a ekle

## username for cron
user = os.environ['USER']

cron = CronTab(user=user)

## get current path)
command = f"/usr/bin/python3 {os.getcwd()}/theme_cfg/tmain.py"
# print(command)

## creating job is done
def creating_cron_job():
    ## create job
    job = cron.new(command=command, comment = 'KDynamic: An Alternative to MacOS Mojave Dynamic Theme and Wallpaper Changer - GNOME')

    ## çalışmıyor
    # job = cron.new(command = 'python3 /home/berkay/MEGA/kod/PYTHON/Kendi_Denemelerim/Python_ile_Uygulama_Çalışmaları/Python_Masaüstü_Uygulama_Prototipi_Serisi/PythonProjectsSeries/ThemeChanger/0.3/cron_try/hello.py', comment= 'deneme')

    ## bu alttaki komut çalışıyor
    # job = cron.new(command = 'touch /tmp/foobar123', comment= 'deneme')

    ### ne kadar sürede bir olacak ???
    # job.minute.every(1)
    job.hour.every(2)
    cron.write()

    print('cron job created')
    print('for controlling created job use "crontab -l" command')


## controlling if a job existed or not with same name
# if existed disable it and create new one
def controlling_job():
    a = cron.find_comment(command)
    ## works
    if a:
        print('schedule already created.. removing..')
        cron.remove(a)
        print('re-creating')
        creating_cron_job()

    if not a:
        creating_cron_job()




# controlling_job()
# end file
