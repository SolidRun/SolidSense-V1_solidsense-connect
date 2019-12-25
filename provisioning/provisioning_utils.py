#-------------------------------------------------------------------------------
# Name:        provisioning_utils
# Purpose:
#
# Author:      Laurent
#
# Created:     27/11/2019
# Copyright:   (c) Laurent 2019
# Licence:     <your licence>
#-------------------------------------------------------------------------------

import platform
import os
import subprocess
import sys
import datetime

def isWindows():
    pl_str=platform.platform()
    # print("System platform:",pl_str)
    return pl_str.startswith('Windows')

def systemCtl(action, service):
    args=['systemctl']
    args.append(action)
    args.append(service)
    print('Executing:',args)
    c=subprocess.run(args,stderr=sys.stderr)
    print('result:',c)
    return c.returncode



def checkCreateDir(dir) :
    if isWindows() :
        return
    if not os.path.lexists(dir):
        os.mkdir(dir)

def write_header(fd):
    t=datetime.datetime.now()
    header=t.strftime("# Generated by SolidSense provisioning system on %d-%b-%Y %H:%M:%S\n")
    fd.write(header)

def str2bool(s):
    if s == 'true':
        return True
    elif s == 'false' :
        return False
    else:
        raise(ValueError)

def bool2str(b):
    if b :
        return 'true'
    else :
        return 'false'


def main():
    pass

if __name__ == '__main__':
    main()
