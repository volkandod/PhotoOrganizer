#!/usr/bin/env python
# -*- coding: utf-8 -*-
import os,sys,re
import subprocess as sp

def isFormattedBefore(myString):
    if re.match(r".*(\d{4})-(\d{2})-(\d{2}) (\d{2})-(\d{2})-(\d{2}).*",myString):
        return True
    else:
        return False

def isVideoFormat(myString):
    if re.match(r".*VID_20(\d{6})_(\d{6}).mp4",myString):
        return True
    else: 
        return False

def isWhatsappFormat(myString):
    if re.match(r".*IMG-(\d{8})-WA(\d{4}).*",myString):
        return True
    else:
        return False

def isGoogleAnimationGifFormat(myString):
    if re.match(r".*IMG_(\d{8})_(\d{6})-ANIMATION.gif",myString) \
    or re.match(r".*VID_(\d{8})_(\d{6})-ANIMATION.gif",myString):
        return True
    else:
        return False

def isGoogleCollageFormat(myString):
    if re.match(r".*IMG_(\d{8})_(\d{6})-COLLAGE.jpg",myString):
        return True
    else:
        return False

def isHHT_HDRFormat(myString):
    if re.match(r".*IMG_(\d{8})_(\d{6})_HHT.jpg",myString) \
    or re.match(r".*IMG_(\d{8})_(\d{6})_HDR.jpg",myString):
        return True
    else:
        return False



def main(directory):
    Parse = []

    for root,_,photos in os.walk(directory):
        for p in photos:
            isNameChanged = True
            Path = os.path.join(root,p)

            NewName = os.path.dirname(Path) + "/"
            if isFormattedBefore(Path):
                isNameChanged = False

            elif isVideoFormat(Path):
                NewName += p[4:8] + "-" + p[8:10] + "-" + p[10:12] + " " + p[13:15] + "-" + p[15:17] + "-" + p[17:19] + p[-4:] 

            elif isWhatsappFormat(Path):
                NewName += p[4:8] + "-" + p[8:10] + "-" + p[10:12] + " " + p[13:]
            elif isGoogleAnimationGifFormat(Path) or isGoogleCollageFormat(Path) or isHHT_HDRFormat(Path):
                NewName += p[4:8] + "-" + p[8:10] + "-" + p[10:12] + " " + p[13:15] + "-" + p[15:17] + "-" + p[17:]
            else:
                x = sp.Popen(["EXIF.py",Path],stdin=sp.PIPE,stdout=sp.PIPE,stderr=sp.PIPE)
                out, err = x.communicate()

                if out and not err:
                    line = out.split("\n")
                    isNameChanged = False

                    for l in line:
                        if "DateTimeOriginal" in l:
                            Parse = l.split(':')
                            if len(Parse) > 5:
                                Year = Parse[1].split(" ",1)[1]
                                Month = Parse[2]
                                Day = Parse[3].split(" ",1)[0]
                                Hour= Parse[3].split(" ",1)[1]
                                Minute = Parse[4]
                                Second = Parse[5]
                                NewName += Year + "-" + Month + "-" +Day
                                NewName = NewName + " " + Hour + "-" + Minute + "-" + Second
                                NewName = NewName+".jpg"
                                isNameChanged = True
                else:
                    isNameChanged = False



            if isNameChanged:
                sp.call(["mv",os.path.join(root,p),NewName])
                print os.path.join(root,p) + "  >> " + NewName


if __name__=='__main__':
    if len(sys.argv) != 2:
        print 'Directory argument is missing'
    directory = sys.argv[1]
    main(directory)
