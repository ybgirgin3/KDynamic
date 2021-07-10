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
comment = 'KDynamic: An Alternative to MacOS Mojave Dynamic Theme and Wallpaper Changer - GNOME'
# print(command)

## creating job is done
def creating_cron_job():
    ## create job
    job = cron.new(command=command, comment = comment)


    ### ne kadar sürede bir olacak ???
    # job.minute.every(1)
    job.hour.every(2)
    cron.write()

    print('cron job created')
    print('for controlling created job use "crontab -l" command')


## controlling if a job existed or not with same name
# if existed disable it and create new one
def controlling_job():
    for c in cron:
        if c.comment == comment:
            cron.remove(c)
    # a = cron.find_comment(command)
    # ## works
    # if a:
    #     print('schedule already created.. removing..')
    #     cron.remove(a)
    #     print('re-creating')
    #     creating_cron_job()

    creating_cron_job()




# controlling_job()
# end file
