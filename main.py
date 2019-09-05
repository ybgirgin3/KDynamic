# !/usr/bin/python3

"""
author: 'Yusuf Berkay Girgin'
created at 5 September 2019 00:32 Turkey/Duzce
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
#  ------> 0   1   2   3
# minutes = [0, 29, 30, 59]

## this function sets of specified functions for changing light theme, light_dark or night theme
def commandHandler(waitWall, termComm, isUsed = False):
    """ needed wait time, terminal command, command handler boolean  """
    if not isUsed:
        print('is used false.. command entering')
        isUsed = True
        if isUsed:
            print('isUsed = True -> waiting')
            if waitWall <= 0:
                isUsed = False
                pass

            else:
                time.sleep(waitWall*3600)


def main():
    while True:
        try:
            # returns current hour as a integer
            currentHour = datetime.now().hour
            # currentHour = 22

            ## !! when clock is ticking 23 program will look like it's freeze do not afraid !!
            ## explained at line 88
            if currentHour == 23:
                print("23 o'clock")
                # 1 hr = 3600 second
                time.sleep(3600)

            ## light theme
            if currentHour >= lightHours[0] and currentHour < lightHours[1]:

                # waiting time will be difference between current hour and last hour of current themes
                waiting = lightHours[1] - currentHour
                print(waiting)

                ## call theme changer func
                command = light()
                commandHandler(waiting, command)


            ## light_dark theme
            elif currentHour >= lightHours[1] and currentHour < lightDarkHours[1]:
                # light plasma theme
                if currentHour >= lightHours[1] and currentHour < lightDarkHours[0]:
                    ## between 15 - 19
                    waiting1 = lightDarkHours[0] - currentHour
                    command1 = light_dark(isDark = False)

                # dark plasma theme
                elif currentHour >= lightDarkHours[0] and currentHour < lightDarkHours[1]:
                    ## between 19 - 21
                    waiting1 = lightDarkHours[1] - currentHour
                    command1 = light_dark(isDark = True)

                print(waiting1)
                commandHandler(waiting1, command1)

            # night theme
            elif currentHour >= lightDarkHours[1] and currentHour < nightHours[0] or currentHour >= 0 and currentHour < nightHours[1]:
                ## NOTE: at 23 o'clock app looks like it's freezing but it's not like that
                ### reason of this;
                #       In the middle of the night I mean when clock is 00:00
                #       datetime module returns clock as a '0' not '24' or smth
                #       so when program trying to find 'waiting' time it's trying solve
                #       0 - 23 equation and naturally can't :(
                #

                # night theme between 15 - 23
                if currentHour >= lightDarkHours[1] and currentHour < nightHours[0]:
                    waiting3 = nightHours[0] - currentHour

                # .. night theme between 0 - 6
                elif currentHour >= 0 and currentHour < nightHours[1]:
                    waiting3 = nightHours[1] - currentHour

                command3 = night()
                print(waiting3)
                commandHandler(waiting3, command3)

        except KeyboardInterrupt as e:
            from sys import exit
            exit(0)

main()
