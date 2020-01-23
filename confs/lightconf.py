# there is some username areas in the config file fuck 'em up

# algo
# read the file 
# make needed changes
# save new version of file

# reads default conf file and changes needed areas and saves it
# can use for changing color values and even for the image names

import re
import os
 
def replace_words(text, word_dic):
    rc = re.compile('|'.join(map(re.escape, word_dic)))
    def translate(match):
        return word_dic[match.group(0)]
    return rc.sub(translate, text)
 
# copy original config file
from shutil import copyfile, move
srcpth = '{}/.config'.format(os.path.expanduser('~'))
srcFile = '/kdeglobals'
dst = '{}/OriginalConfigFile'.format(os.getcwd())
copyfile(srcpth+srcFile, dst)


exampleFile = open(dst, 'r')
f = exampleFile.read()
exampleFile.close()


# dark to light
word_dic = {
        # username
        'fakeuser'                          : os.environ['USER'],
        # [Colors:Button]
        "BackgroundAlternate=77,77,77"      : 'BackgroundAlternate=189,195,199',
        "BackgroundNormal=101,101,101"      : "BackgroundNormal=255,255,255",
        "DecorationHover=49,91,239"         : "DecorationHover=83,143,255",
        "ForegroundInactive=189,195,199"    : "ForegroundInactive=120,120,120",
        "ForegroundNormal=222,222,222"      : "ForegroundNormal=36,36,36",
        "DecorationFocus=49,91,239"         : "DecorationFocus=30,146,255",
        "DecorationHover=49,91,239"         : "DecorationHover=61,174,230",
        "ForegroundActive=246,116,0"        : "ForegroundActive=49,91,239",
        "ForegroundInactive=136,136,136"    : "ForegroundInactive=120,120,120",
        "ForegroundNegative=237,21,21"      : "ForegroundNegative=231,76,60",
        "ForegroundNeutral=201,206,59"      : "ForegroundNeutral=253,188,75",
        "ForegroundNormal=222,222,222"      : "ForegroundNormal=239,240,241",
        "ForegroundPositive=17,209,22"      : "ForegroundPositive=46,204,113",
        "ForegroundVisited=49,91,239"       : "ForegroundVisited=120,120,120",
        # [Colors:Selection]
        "BackgroundAlternate=79,127,239"    : "BackgroundAlternate=74,124,239",
        "DecorationHover=255,255,255"       : "DecorationHover=83,143,255",
        "ForegroundInactive=130,156,239"    : "ForegroundInactive=135,163,239",
        "ForegroundVisited=128,152,239"     : "ForegroundVisited=127,160,239",
        # [Colors:Tooltip]
        "BackgroundNormal=51,51,51"         : "BackgroundNormal=36,36,36",
        "DecorationHover=49,91,239"         : "DecorationHover=83,143,255",
        "ForegroundActive=49,91,239"        : "ForegroundActive=61,174,233",
        "ForegroundInactive=189,195,199"    : "ForegroundInactive=120,120,120",
        "ForegroundLink=49,91,239"          : "ForegroundLink=41,128,185",
        # [Colors:View]
        "BackgroundAlternate=48,48,48"      : "BackgroundAlternate=239,239,239",
        "BackgroundNormal=36,36,36"         : "BackgroundNormal=255,255,255",
        "DecorationHover=49,91,239"         : "DecorationHover=83,143,255",
        "ForegroundInactive=136,136,136"    : "ForegroundInactive=120,120,120",
        "ForegroundNormal=222,222,222"      : "ForegroundNormal=36,36,36",
        "ForegroundVisited=120,120,120"     : "ForegroundVisited=127,140,141",
        # [Colors:Window]
        "BackgroundAlternate=66,66,66"      : "BackgroundAlternate=238,238,238",
        "BackgroundNormal=51,51,51"         : "BackgroundNormal=245,245,245",
        "DecorationHover=49,91,239"         : "DecorationHover=83,143,255",
        "ForegroundActive=49,91,239"        : "ForegroundActive=61,174,233",
        "ForegroundInactive=136,136,136"    : "ForegroundInactive=120,120,120",
        "ForegroundLink=49,91,239"          : "ForegroundLink=41,128,185",
        "ForegroundNormal=222,222,222"      : "ForegroundNormal=36,36,36",
        "ForegroundVisited=120,120,120"     : "ForegroundVisited=127,140,141",
        # [WM]
        "activeBackground=51,51,51"         : "activeBackground=245,245,245",
        "activeBlend=171,171,171"           : "activeBlend=86,86,86",
        "activeForeground=222,222,222"      : "activeForeground=66,66,66",
        "inactiveBackground=66,66,66"       : "inactiveBackground=238,238,238",
        "inactiveBlend=85,85,85"            : "inactiveBlend=102,102,102"
}


# this will change fakeuser name with real username
newDefaultFile = replace_words(f, word_dic)
# print(newDefaultFile)
customConf = 'globFiles/convertedFiles/lightconf'
with open(customConf, 'w') as glob:
    glob.write(newDefaultFile)
    glob.close()

# customConf dosyasını config dosyası içine taşı
# os.system('cp -r globFiles/convertedFiles/lightconf ~/Masaüstü')
move(customConf, srcpth)

print('We just replace your system config file for colorscheme changing. But don\'t worry. Config file copied to {}'.format(os.getcwd()))
