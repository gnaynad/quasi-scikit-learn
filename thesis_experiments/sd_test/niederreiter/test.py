from ctypes import *
import os
import numpy as np

# dir_path = os.path.dirname(os.path.realpath(__file__))
# lib = CDLL('%s/niederreiter.so' % dir_path)
lib = WinDLL('./niederreiter_lib.dll')

# int dim_num, int n, int base, int skip, double r[], 
#   char *output_filename


def main():
    dim_num = c_int(3)
    n = c_int(200)
    base = c_int(2)
    seed = pointer(c_int(2))
    skip = c_int(0)
    r = (c_double * 600)()
    # output_filename = pointer(c_wchar_p("sequence"))
    output_filename = c_wchar_p("sequence.txt")
    
    lib.niederreiter_generate(dim_num,n,base,seed,r)
    lib.niederreiter_write(dim_num,n,base,skip,r,output_filename)

if __name__ == "__main__":
    main()