#!/usr/bin/python
# -*- coding: UTF-8 -*-

import sys
import os

def printHelpInfo():

    print ' qcd <数字> 切换目录\n qcd 切换到目录1或2\n ----------------\n',\
            ' -l 列出所有目录\n rm <path> 删除指定目录\n append <path> 追加指定目录\n -i  <path> 插入目录\n clear 清空目录\n -h 帮助\n'
    return

def changeDir(n):
    fd = open(qcd_path,"r")
    lines = fd.readlines()
    fd.close()
    if len(lines) < n:
        print '未知行 ：'+str(n)
    else :
        targe_path = lines[n-1][:-1]
        try:
            fd_tmp = open(tmp_path,'w+')
            fd_tmp.write(targe_path)
            fd_tmp.close()
        except:
            print '写入临时目录出错 '+tmp_path

    return

argv_len = len(sys.argv)

qcd_dir = str(os.path.expandvars('$HOME'))+'/.qcd/'

if not os.path.exists(qcd_dir):
    os.makedirs(qcd_dir)

qcd_path = qcd_dir + 'qcd_dirs'
tmp_path = qcd_dir + 'tmp_dir'

if not os.path.exists(qcd_path):
    os.mknod(qcd_path)

if not os.path.exists(tmp_path):
    os.mknod(tmp_path)

if argv_len == 2:
    fd = open(qcd_path,"r+")
    if sys.argv[1] == '-l':
        #list
        line_count = 1
        for line_str in fd:
            print str(line_count) + ' ' + line_str,
            line_count+=1

    elif sys.argv[1] == 'clear':
        #clear
        fd.truncate()

    elif sys.argv[1] == '-h':
        #help
        printHelpInfo()

    elif sys.argv[1].isdigit():
        num = int(sys.argv[1])
        changeDir(num)

    else:
        print '参数错误：',str(sys.argv[1])
    fd.close()
elif argv_len == 3:

    targe_path = sys.argv[2]

    if sys.argv[1] == 'rm':
        #delete
        fd = open(qcd_path,"r")
        num = int(sys.argv[2])
        lines = fd.readlines()
        fd.close()

        if len(lines) < num:
            print '未知行 ：'+str(num)
        else :
            del lines[num-1]

        fd = open(qcd_path,"w")
        for line in lines:
            fd.write(line)
        fd.close()
    elif sys.argv[1] == '-i' or sys.argv[1] == 'append':
        #insert
        if not os.path.exists(targe_path):
            print '目录不存在！'
        else:
            fd = open(qcd_path,"r")
            buff = fd.read()
            fd.close()

            targe_path += '\n'
            buff = targe_path + buff

            if sys.argv[1] == '-i':
                fd = open(qcd_path,"w")
                fd.write(buff)
            else:
                fd = open(qcd_path,"a")
                fd.write(targe_path)
            fd.close()
    else:
        print 'error argument :'+ sys.argv[1]
elif argv_len == 1:
    #切换到最近目录
    fd = open(qcd_path,"r")
    lines = fd.readlines()
    fd.close()

    if len(lines) <= 0:
        print '常用目录列表为空'
    else:
        if str(lines[0][:-1]) != str(os.getcwd()):
            changeDir(1)
        elif len(lines) >=2 :
            changeDir(2)
else:
    print '参数错误：',str(sys.argv)

