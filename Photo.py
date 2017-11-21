#!/usr/bin/env python
# -*- coding: utf-8 -*-
import os,sys
import subprocess as sp

def main(directory):
    Parse = []

    for root,_,photos in os.walk(directory):
        for p in photos:
            if ".jpg" in os.path.join(root,p) or ".JPG" in os.path.join(root,p):
                x = sp.Popen(["EXIF.py",os.path.join(root,p)],stdin=sp.PIPE,stdout=sp.PIPE,stderr=sp.PIPE)
                out, err = x.communicate()

                if out and not err:
                    line = out.split("\n")

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
                                NewName = os.path.dirname(os.path.join(root,p))
                                NewName = NewName + "/" +Year + "-" + Month + "-" +Day
                                NewName = NewName + " " + Hour + "-" + Minute + "-" + Second
                                NewName = NewName+".jpg"

                                sp.call(["mv",os.path.join(root,p),NewName])
                                print os.path.join(root,p) + "  >> " + NewName

                else:
                    os.system("echo" + os.path.join(root,p) + ">> error.log")

if __name__=='__main__':
    if len(sys.argv) != 2:
        print 'Directory argument is missing'
    directory = sys.argv[1]
    main(directory)
