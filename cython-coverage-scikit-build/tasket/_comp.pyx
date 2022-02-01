# cython: linetrace=True

from libc.math cimport sin, cos

cpdef double sin_squared(double x):
    return sin(x * x)

cpdef double cos_squared(double x):
    return cos(x * x)
