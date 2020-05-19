"""
Minimal demonstration for https://github.com/numpy/numpy/issues/16277

1. compile:
f2py -c -m minimal_fortran minimal_fortran.pyf XERBLA.f FORTRAN_CALLER.f

2. execute this script.
"""

# Import compiled f2py module
import minimal_fortran


# Define callback function
def python_callback(caller, arg):
    """Print the arguments the Fortran subroutine calls us with"""
    print("caller: {}, arg: {}".format(caller, arg))


# register callback for Fortran module
minimal_fortran.python_callback = python_callback

# Call Fortran routine, which calls XERBLA, which should call the registered
# callback
minimal_fortran.fortran_caller(1)
