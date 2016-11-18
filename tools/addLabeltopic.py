# -*- coding: utf-8 -*-
import os
import shutil
import string

root=r"/opt/share0/dl_data/datasets/CASIA-WebFace/CASIA-WebFace"
foldername = os.listdir(root)
w = 0
for i in foldername:
    folder = "%s/%s"%(root,i)
    print "complete ", w," ... ", folder
    # print folder
    w = w + 1

    pic = os.listdir(folder)
    for j in pic:
        print j
        print w
        oldname = "%s/%s" % (folder, j)
        print oldname
        newname = "%s/%d%s%s" % (folder, w, '_', j)
        print newname
        # newname = "%s/%s%s%s" % (folder, i, '_', j)  #将人物的名字信息加入到每张图片之中
        os.rename(oldname, newname)