Using a C shared library with Python's ctypes module
####################################################
:author: Elyézer Rezende
:category: Python
:tags: python
:status: published

To demonstrate how to create a shared C library and using it with Python's
`ctypes`_ library we are going to create a shared C library. First create the C
header file `mean.h`:

.. code-block:: c

    // Returns the mean of passed parameters
    double mean(double, double);

Next create the C file `mean.c`:

.. code-block:: c

    #include "mean.h"

    double mean(double a, double b) {
        return (a+b)/2;
    }

Now we can create the shared C library by compiling it using `gcc`:

.. code-block:: console

    $ gcc -shared -o libmean.so.1 mean.c

Finally we can import the shared C library using the ctypes Python module,
consider the following interative shell:

.. code-block:: python

    >>> import ctypes
    >>> libmean = ctypes.CDLL('./libmean.so.1') # loads the shared library
    >>> libmean.mean.restype = ctypes.c_double # define mean function return type
    >>> libmean.mean(ctypes.c_double(10), ctypes.c_double(3)) # call mean function needs cast arg types
    6.5
    >>> libmean.mean.argtypes = [ctypes.c_double, ctypes.c_double] # define arguments types
    >>> libmean.mean(10, 3) # call mean function does not need cast arg types
    6.5
    >>> type(libmean.mean(10, 5)) # returned value is converted to python types
    <class 'float'>


This was tested using Python 3.6.4 and gcc 7.3.1 on Fedora 27. Check the
`ctypes`_ documentation for more information.


.. _ctypes: https://docs.python.org/3/library/ctypes.html
