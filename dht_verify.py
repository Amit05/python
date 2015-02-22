#!/usr/bin/python

#Get the hash value of a file.

import ctypes
import sys
 
glusterfs = ctypes.cdll.LoadLibrary("libglusterfs.so.0")
 
def gf_dm_hashfn(filename):
    return ctypes.c_uint32(glusterfs.gf_dm_hashfn(
        filename,
        len(filename)))
 
def 

if __name__ == "__main__":
    hash_val=hex(gf_dm_hashfn(sys.argv[1]).value)
    print hash_val
