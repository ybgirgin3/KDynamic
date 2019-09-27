# !/usr/bin/python3

"""
author: 'Yusuf Berkay Girgin'
created at 5 September 2019 00:32 Turkey/Duzce
for using kvantum themes 
"""

from light import *        # light theme module
from light_dark import *   # light_dark theme module
from night import *        # night theme module

from datetime import datetime
import time

## hours
## --------> first hour, last hour
lightHours = [7, 15]
## --------> last hour (light_dark's first hour is lights' last hour)
lightDarkHours = [19, 21]
## --------> middle hour, last hour
nightHours = [23, 6]

## common minutes
#  --------> 0   1   2   3
# minutes = [0, 29, 30, 59]


def main():
    try:
        # returns current hour as a integer
        currentHour = datetime.now().hour
        # currentHour = 18

        ## light theme
        # if currentHour in range(lightHours[0], lightHours[1]+1):
        if currentHour >= lightHours[0] and currentHour < lightHours[1]:
            ## call theme changer func
            light()


        ## light_dark theme
        elif currentHour >= lightHours[1] and currentHour < lightDarkHours[1]:
            # light plasma theme
            if currentHour >= lightHours[1] and currentHour < lightDarkHours[0]:
                ## between 15 - 19
                light_dark(isDark = False)

            # dark plasma theme
            elif currentHour >= lightDarkHours[0] and currentHour < lightDarkHours[1]:
                ## between 19 - 21
                light_dark(isDark = True)

            # print(waiting1)
            # commandHandler(waiting1, command1)

        # night theme
        elif currentHour >= lightDarkHours[1] and currentHour < nightHours[0] or currentHour >= 0 and currentHour < nightHours[1]:
            # night theme between 15 - 23
            night()

    except KeyboardInterrupt as e:
        from sys import exit
        exit(0)
