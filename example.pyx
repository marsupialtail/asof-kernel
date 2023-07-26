# distutils: language=c++

from pyarrow.lib cimport *


def get_array_length(obj):
    # Just an example function accessing both the pyarrow Cython API
    # and the Arrow C++ API
    cdef shared_ptr[CArray] arr = pyarrow_unwrap_array(obj)
    if arr.get() == NULL:
        raise TypeError("not an array")
    return arr.get().length()

def check_arr_equal(obj1, obj2):
    # Just an example function accessing both the pyarrow Cython API
    # and the Arrow C++ API
    cdef shared_ptr[CArray] arr1 = pyarrow_unwrap_array(obj1)
    if arr1.get() == NULL:
        raise TypeError("not an array")
    cdef shared_ptr[CArray] arr2 = pyarrow_unwrap_array(obj2)
    if arr1.get() == NULL:
        raise TypeError("not an array")
    return arr1.get().equals(arr2.get())
