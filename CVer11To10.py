# -*- coding: utf-8 -*-
'''
Created on 2014-01-30

@author: AmiKawashima

'''

import sys, os, re

VER_DICT = {'11GR2':'V11.02.00', 
            '11GR1':'V11.01.00', 
            '10GR2':'V10.02.01'}

class ExtException(Exception):
    """Self-Defined exception"""
    def __str__(self):
        return ">> (>_<) Oops...\nFile format error."
            
def convert(_file):
    _ver = ver(_file)
    if _ver is None:
        print ">> (O.o) Unknown Oracle version."
    elif _ver == '10GR2':
        print ">> Ahhhh..Without conversion."
    else:
        try:
            fp=open(_file, 'rb+')
            try:
                #Get '10GR2'
                _ver = VER_DICT.get('10GR2')
                #Set version information from 10 bytes to 19 bytes
                fp.seek(10, 0)
                fp.write(_ver)
                return True
            except IOError, ie:
                print ">>Convert:%s" % ie
            finally:
                fp.close()
        except IOError, ie:
            print ">> Convert:%s" % ie
    return False
            
def ver(_file):
    """Get the oracle version from 'dmp' file"""
    try:
        ext = os.path.splitext(_file)[1]
        if ext != '.dmp': raise ExtException
        fp=open(_file, 'rb')
        try:
            #Get version information from 10 bytes to 19 bytes
            fp.seek(10)
            _ver = fp.read(9)
            #Finding this version from dictionary
            for key in VER_DICT:
                if VER_DICT[key] == _ver: return key
            return None
        except IOError, ie:
            print ">> Version:%s" % ie
        finally:
            fp.close()
    except (IOError, ExtException), e:
        print ">> Version:%s" % e

def state():
    print("Oracle 11g R1 or R2 exported dmp converted to be used for Oracle 10g R2."
          "\nCreated on Jan 30, 2014\nAuthor: AmiKawashima")
    
if __name__ == '__main__':
    if len(sys.argv) < 2:
        print ">> (>_<) Oops... Not enough argv!\n"
        os.system('echo Press any key to exit & pause > nul')
        exit()
    state()
    if convert(sys.argv[1]): print ">> Successful conversion."
    else: print ">> Conversion failed!"
    os.system('echo Press any key to exit & pause > nul')