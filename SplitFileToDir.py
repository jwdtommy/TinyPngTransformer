# -*- coding: UTF-8 -*-
import os
import sys
import os.path
import shutil
import glob
import os
import sys


def split(maxCount):
    folderIndex = 1
    os.mkdir("./dst/png" + str(folderIndex))
    index=0
    for filename in glob.glob("./*.png"):
        # print str(i)
        name=os.path.split(filename)[1]
        if (index == maxCount):
            index = 0
            folderIndex += 1
            os.mkdir("./dst/png" + str(folderIndex) + "/")
        print str(index)
        shutil.copyfile("./"+name,"./dst/png" + str(folderIndex) + "/"+name)
        index += 1

if os.path.exists("./dst"):
    shutil.rmtree("./dst")
os.mkdir("./dst")
split(500)
