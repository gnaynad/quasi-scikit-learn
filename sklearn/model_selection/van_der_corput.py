#! /usr/bin/env python3
#
def r8vec_transpose_print(n, a, title):
    # *****************************************************************************80
    #
    ## R8VEC_TRANSPOSE_PRINT prints an R8VEC "transposed".
    #
    #  Discussion:
    #
    #    An R8VEC is a vector of R8's.
    #
    #  Example:
    #
    #    A = (/ 1.0, 2.1, 3.2, 4.3, 5.4, 6.5, 7.6, 8.7, 9.8, 10.9, 11.0 /)
    #    TITLE = 'My vector:  '
    #
    #    My vector:   1.0    2.1    3.2    4.3    5.4
    #                 6.5    7.6    8.7    9.8   10.9
    #                11.0
    #
    #  Licensing:
    #
    #    This code is distributed under the GNU LGPL license.
    #
    #  Modified:
    #
    #    28 March 2016
    #
    #  Author:
    #
    #    John Burkardt
    #
    #  Parameters:
    #
    #    Input, integer N, the number of components of the vector.
    #
    #    Input, real A(N), the vector to be printed.
    #
    #    Input, string TITLE, a title.
    #
    title_length = len(title)

    for ilo in range(0, n, 5):

        if (ilo == 0):
            print(title, end='')
        else:
            blanks = ''
            for i in range(0, title_length):
                blanks = blanks + ' '
            print(blanks, end='')

        print('  ', end='')

        ihi = min(ilo + 5 - 1, n - 1)

        for i in range(ilo, ihi + 1):
            print('  %12g' % (a[i]), end='')
        print('')

    return


def r8vec_transpose_print_test():
    # *****************************************************************************80
    #
    ## R8VEC_TRANSPOSE_PRINT_TEST tests R8VEC_TRANSPOSE_PRINT.
    #
    #  Licensing:
    #
    #    This code is distributed under the GNU LGPL license.
    #
    #  Modified:
    #
    #    28 March 2016
    #
    #  Author:
    #
    #    John Burkardt
    #
    import platform
    from r8vec_uniform_01 import r8vec_uniform_01

    n = 12
    seed = 123456789

    print('')
    print('R8VEC_TRANSPOSE_PRINT_TEST')
    print('  Python version: %s' % (platform.python_version()))
    print('  R8VEC_TRANSPOSE_PRINT prints an R8VEC "tranposed",')
    print('  that is, placing multiple entries on a line.')

    x, seed = r8vec_uniform_01(n, seed)

    r8vec_transpose_print(n, x, '  The vector X:')
    #
    #  Terminate.
    #
    print('')
    print('R8VEC_TRANSPOSE_PRINT_TEST')
    print('  Normal end of execution.')
    return


def timestamp():
    # *****************************************************************************80
    #
    ## TIMESTAMP prints the date as a timestamp.
    #
    #  Licensing:
    #
    #    This code is distributed under the GNU LGPL license.
    #
    #  Modified:
    #
    #    06 April 2013
    #
    #  Author:
    #
    #    John Burkardt
    #
    #  Parameters:
    #
    #    None
    #
    import time

    t = time.time()
    print(time.ctime(t))

    return None


def timestamp_test():
    # *****************************************************************************80
    #
    ## TIMESTAMP_TEST tests TIMESTAMP.
    #
    #  Licensing:
    #
    #    This code is distributed under the GNU LGPL license.
    #
    #  Modified:
    #
    #    03 December 2014
    #
    #  Author:
    #
    #    John Burkardt
    #
    #  Parameters:
    #
    #    None
    #
    import platform

    print('')
    print('TIMESTAMP_TEST:')
    print('  Python version: %s' % (platform.python_version()))
    print('  TIMESTAMP prints a timestamp of the current date and time.')
    print('')

    timestamp()
    #
    #  Terminate.
    #
    print('')
    print('TIMESTAMP_TEST:')
    print('  Normal end of execution.')
    return


def vdc(i):
    # *****************************************************************************80
    #
    ## VDC computes an element of the van der Corput sequence.
    #
    #  Discussion:
    #
    #    The van der Corput sequence is often used to generate a "subrandom"
    #    sequence of points which have a better covering property
    #    than pseudorandom points.
    #
    #    The van der Corput sequence generates a sequence of points in [0,1]
    #    which never repeats.  The elements of the van der Corput sequence
    #    are strictly less than 1.
    #
    #    The van der Corput sequence writes an integer in a given base 2,
    #    and then its digits are "reflected" about the decimal point.
    #    This maps the numbers from 1 to N into a set of numbers in [0,1],
    #    which are especially nicely distributed if N is one less
    #    than a power of the base.
    #
    #    The generation is quite simple.  Given an integer I, the expansion
    #    of I in base 2 is generated.  Then, essentially, the result R
    #    is generated by writing a decimal point followed by the digits of
    #    the expansion of I, in reverse order.  This decimal value is actually
    #    still in base 2, so it must be properly interpreted to generate
    #    a usable value.
    #
    #  Example:
    #
    #    I        I         van der Corput
    #    decimal  binary    binary   decimal
    #    -------  ------    ------   -------
    #        0  =     0  =>  .0     = 0.0
    #        1  =     1  =>  .1     = 0.5
    #        2  =    10  =>  .01    = 0.25
    #        3  =    11  =>  .11    = 0.75
    #        4  =   100  =>  .001   = 0.125
    #        5  =   101  =>  .101   = 0.625
    #        6  =   110  =>  .011   = 0.375
    #        7  =   111  =>  .111   = 0.875
    #        8  =  1000  =>  .0001  = 0.0625
    #
    #  Licensing:
    #
    #    This code is distributed under the GNU LGPL license.
    #
    #  Modified:
    #
    #    09 August 2016
    #
    #  Author:
    #
    #    John Burkardt
    #
    #  Reference:
    #
    #    John Halton,
    #    On the efficiency of certain quasi-random sequences of points
    #    in evaluating multi-dimensional integrals,
    #    Numerische Mathematik,
    #    Volume 2, pages 84-90, 1960.
    #
    #    John Hammersley,
    #    Monte Carlo methods for solving multivariable problems,
    #    Proceedings of the New York Academy of Science,
    #    Volume 86, pages 844-874, 1960.
    #
    #    Johannes van der Corput,
    #    Verteilungsfunktionen I & II,
    #    Nederl. Akad. Wetensch. Proc.,
    #    Volume 38, 1935, pages 813-820, pages 1058-1066.
    #
    #  Parameters:
    #
    #    Input, integer I, the index of the element of the sequence.
    #    I = 0 is allowed, and returns R = 0.
    #
    #    Output, real R, the I-th element of the van der Corput sequence.
    #

    #
    #  Isolate the sign, and only work with the integer part of I.
    #
    if (i < 0):
        s = -1
    else:
        s = +1

    t = abs(int(i))
    #
    #  Carry out the computation.
    #
    base_inv = 0.5

    r = 0.0

    while (t != 0):
        d = (t % 2)
        r = r + d * base_inv
        base_inv = base_inv / 2.0
        t = (t // 2)
    #
    #  Recover the sign.
    #
    r = r * s

    return r


def vdc_test():
    # *****************************************************************************80
    #
    ## VDC_TEST tests VDC.
    #
    #  Licensing:
    #
    #    This code is distributed under the GNU LGPL license.
    #
    #  Modified:
    #
    #    09 August 2016
    #
    #  Author:
    #
    #    John Burkardt
    #
    import platform

    print('')
    print('VDC_TEST')
    print('  Python version: %s' % (platform.python_version()))
    print('  VDC returns the I-th element of a van der Corput sequence.')
    print('')
    print('    I          VDC(I)')
    print('')

    for i in range(-10, 11):
        r = vdc(i)
        print('  %3d  %14.8f' % (i, r))
    #
    #  Terminate.
    #
    print('')
    print('VDC_TEST')
    print('  Normal end of execution.')
    return


def vdc_base(i, b):
    # *****************************************************************************80
    #
    ## VDC_BASE computes an element of the van der Corput sequence in any base.
    #
    #  Licensing:
    #
    #    This code is distributed under the GNU LGPL license.
    #
    #  Modified:
    #
    #    09 August 2016
    #
    #  Author:
    #
    #    John Burkardt
    #
    #  Parameters:
    #
    #    Input, integer I, the index of the element of the sequence.
    #    I = 0 is allowed, and returns R = 0.
    #
    #    Input, integer B, the base of the sequence.  The standard sequence
    #    uses B = 2, and this function expects 2 <= B.
    #
    #    Output, real R, the I-th element of the van der Corput sequence.
    #
    from sys import exit
    #
    #  2 <= B.
    #
    if (b < 2):
        print('')
        print('VDC_BASE - Fatal error!')
        print('  2 <= B is required.')
        exit('VDC_BASE - Fatal error!')
    #
    #  B should be an integer.
    #
    b = int(b)
    #
    #  Isolate the sign, and only work with the integer part of I.
    #
    if (i < 0):
        s = -1
    else:
        s = +1

    t = abs(int(i))
    #
    #  Carry out the computation.
    #
    base_inv = 1.0 / b

    r = 0.0

    while (t != 0):
        d = (t % b)
        r = r + d * base_inv
        base_inv = base_inv / b
        t = (t // b)
    #
    #  Recover the sign.
    #
    r = r * s

    return r


def vdc_base_test():
    # *****************************************************************************80
    #
    ## VDC_BASE_TEST tests VDC_BASE.
    #
    #  Licensing:
    #
    #    This code is distributed under the GNU LGPL license.
    #
    #  Modified:
    #
    #    09 August 2016
    #
    #  Author:
    #
    #    John Burkardt
    #
    import platform

    print('')
    print('VDC_BASE_TEST')
    print('  Python version: %s' % (platform.python_version()))
    print('  VDC_BASE returns the I-th element of a van der Corput')
    print('  sequence in base B.')
    print('')
    print('    I          VDC_BASE(I,2)   VDC_BASE(I,3)   VDC_BASE(I,5)')
    print('')

    for i in range(-10, 11):
        r2 = vdc_base(i, 2)
        r3 = vdc_base(i, 3)
        r5 = vdc_base(i, 5)
        print('  %3d         %14.8f  %14.8f  %14.8f' % (i, r2, r3, r5))
    #
    #  Terminate.
    #
    print('')
    print('VDC_BASE_TEST')
    print('  Normal end of execution.')
    return


def vdc_inverse(r):
    # *****************************************************************************80
    #
    ## VDC_INVERSE inverts an element of the van der Corput sequence.
    #
    #  Licensing:
    #
    #    This code is distributed under the GNU LGPL license.
    #
    #  Modified:
    #
    #    09 August 2016
    #
    #  Author:
    #
    #    John Burkardt
    #
    #  Parameters:
    #
    #    Input, real R, the I-th element of the van der Corput sequence.
    #    |R| < 1.0
    #
    #    Output, integer I, the index of the element of the sequence.
    #
    from sys import exit

    if (r < 0.0):
        s = -1
    else:
        s = +1

    t = abs(r)

    if (1.0 <= t):
        print('')
        print('VDC_INVERSE - Fatal error!')
        print('  |R| < 1.0 is required.')
        exit('VDC_INVERSE - Fatal error!')

    i = 0
    p = 1

    while (t != 0.0):
        t = t * 2.0
        d = t - (t % 1.0)
        i = i + d * p
        p = p * 2
        t = (t % 1.0)
    #
    #  Recover the sign.
    #
    i = i * s

    return i


def vdc_inverse_test():
    # *****************************************************************************80
    #
    ## VDC_INVERSE_TEST tests VDC_INVERSE.
    #
    #  Licensing:
    #
    #    This code is distributed under the GNU LGPL license.
    #
    #  Modified:
    #
    #    09 August 2016
    #
    #  Author:
    #
    #    John Burkardt
    #
    import platform

    print('')
    print('VDC_INVERSE_TEST')
    print('  Python version: %s' % (platform.python_version()))
    print('  VDC_INVERSE inverts an element of a van der Corput sequence.')
    print('')
    print('    I        R=VDC(I)  VDC_INVERSE(R)')
    print('')

    for i in range(-10, 11):
        r = vdc(i)
        i2 = vdc_inverse(r)
        print('  %3d  %14.8f  %3d' % (i, r, i2))
    #
    #  Terminate.
    #
    print('')
    print('VDC_INVERSE_TEST')
    print('  Normal end of execution.')
    return


def vdc_sequence(i1, i2):
    # *****************************************************************************80
    #
    ## VDC_SEQUENCE computes a sequence of elements of the van der Corput sequence.
    #
    #  Discussion:
    #
    #    This function could be rewritten to take advantage of MATLAB's
    #    vectorization capabilities.
    #
    #  Licensing:
    #
    #    This code is distributed under the GNU LGPL license.
    #
    #  Modified:
    #
    #    09 August 2016
    #
    #  Author:
    #
    #    John Burkardt
    #
    #  Parameters:
    #
    #    Input, integer I1, I2, the indices of the first and last elements.
    #
    #    Output, real R(|I2+1-I1|), elements I1 through I2 of the van der
    #    Corput sequence.
    #
    import numpy as np

    n = abs(i2 - i1) + 1
    r = np.zeros(n)

    if (i1 <= i2):
        i3 = +1
    else:
        i3 = -1

    j = 0
    #
    #  The syntax of the Python RANGE function strikes again!
    #
    for i in range(i1, i2 + i3, i3):
        #
        #  Isolate the sign, and only work with the integer part of I.
        #
        if (i < 0):
            s = -1
        else:
            s = +1

        t = abs(int(i))
        #
        #  Carry out the computation.
        #
        base_inv = 0.5

        r[j] = 0.0

        while (t != 0):
            d = (t % 2)
            r[j] = r[j] + d * base_inv
            base_inv = base_inv / 2.0
            t = (t // 2)
        #
        #  Recover the sign.
        #
        r[j] = r[j] * s

        j = j + 1

    return r


def vdc_sequence_test():
    # *****************************************************************************80
    #
    ## VDC_SEQUENCE_TEST tests VDC_SEQUENCE.
    #
    #  Licensing:
    #
    #    This code is distributed under the GNU LGPL license.
    #
    #  Modified:
    #
    #    09 August 2016
    #
    #  Author:
    #
    #    John Burkardt
    #
    import platform

    print('')
    print('VDC_SEQUENCE_TEST')
    print('  Python version: %s' % (platform.python_version()))
    print('  VDC_SEQUENCE returns elements I1 through I2 of ')
    print('  a van der Corput sequence.')

    i1 = 7
    i2 = 7
    n = abs(i2 - i1) + 1
    r = vdc_sequence(i1, i2)
    print('')
    r8vec_transpose_print(n, r, '  R=VDC_SEQUENCE(  7,  7):')

    i1 = 0
    i2 = 8
    n = abs(i2 - i1) + 1
    r = vdc_sequence(i1, i2)
    print('')
    r8vec_transpose_print(n, r, '  R=VDC_SEQUENCE(  0,  8):')

    i1 = 8
    i2 = 0
    n = abs(i2 - i1) + 1
    r = vdc_sequence(i1, i2)
    print('')
    r8vec_transpose_print(n, r, '  R=VDC_SEQUENCE(  8,  0):')

    i1 = -3
    i2 = +5
    n = abs(i2 - i1) + 1
    r = vdc_sequence(i1, i2)
    print('')
    r8vec_transpose_print(n, r, '  R=VDC_SEQUENCE( -3,  5):')

    i1 = 100
    i2 = 105
    n = abs(i2 - i1) + 1
    r = vdc_sequence(i1, i2)
    print('')
    r8vec_transpose_print(n, r, '  R=VDC_SEQUENCE(100,105):')
    #
    #  Terminate.
    #
    print('')
    print('VDC_SEQUENCE_TEST')
    print('  Normal end of execution.')
    return


def van_der_corput_test():
    # *****************************************************************************80
    #
    ## VAN_DER_CORPUT_TEST tests the VAN_DER_CORPUT library.
    #
    #  Licensing:
    #
    #    This code is distributed under the GNU LGPL license.
    #
    #  Modified:
    #
    #    09 August 2016
    #
    #  Author:
    #
    #    John Burkardt
    #
    import platform

    print('')
    print('VAN_DER_CORPUT_TEST')
    print('  Python version: %s' % (platform.python_version()))
    print('  Test the VAN_DER_CORPUT library.')

    vdc_test()
    vdc_inverse_test()
    vdc_sequence_test()
    vdc_base_test()
    #
    #  Terminate.
    #
    print('')
    print('VAN_DER_CORPUT_TEST:')
    print('  Normal end of execution.')
    return


if (__name__ == '__main__'):
    timestamp()
    van_der_corput_test()
    timestamp()