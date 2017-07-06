#!/usr/bin/python
# -*- coding: UTF-8 -*-

import sys

def printHelpInfo():
    print ' -l 列出所有目录\n -rm <path> 删除指定目录\n -i  <path> 插入目录\n -clear 清空目录\n -h 帮助\n'
    return

argv_len = len(sys.argv)

if argv_len == 2:
    if sys.argv[1] == '-l':
        #list
        print '\n'
    elif sys.argv[1] == '-clear':
        #clear
        print '\n'
    elif sys.argv[1] == '-h':
        #help
        printHelpInfo()
    else:
        print '参数错误：',str(sys.argv)
elif argv_len == 3:
    if sys.argv[1] == '-rm':
        #delete
        print '\n'
    elif sys.argv[1] == '-i':
        #insert
        print '\n'
else:
    print '参数错误：',str(sys.argv)

