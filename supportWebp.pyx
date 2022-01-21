# cython: language_level=3
# distutils: language = c++
from libcpp.map cimport map
from cython.operator cimport dereference, preincrement
from libc.string cimport strstr,strlen,memset
from libc.stdlib cimport atoi,rand,srand
version_list = {b'Firefox':65,
                b'Chrome':32,
                b'Edge':18,
                b'AppleWebKit':605, # Safari 14
                b'OPR':19,
                b'UCBrowser':12,
                b'SamsungBrowser':4,
                b'QQBrowser':10,
                }
cdef map[char*, int] version_list_c
version_list_c = version_list
cpdef bint check_Version(char* ua):
    cdef map[char*,int].iterator end = version_list_c.end()
    cdef map[char*,int].iterator it = version_list_c.begin()
    cdef char* key
    cdef int value
    cdef char[5] ua_version = ''
    cdef int i1 = 0
    cdef int index
    with nogil:
        while it != end:
            key = dereference(it).first
            value = dereference(it).second
            index = strindex(ua, dereference(it).first)
            if index == -1:
                preincrement(it)
                continue
            i1 = index+strlen(key) + 1
            while b'0' <= ua[i1] <= b'9':
                ua_version[strlen(ua_version)] = ua[i1]
                i1 += 1
            if atoi(ua_version) >= value:
                return True
            memset(ua_version,0,strlen(ua_version));
            preincrement(it)

cdef int strindex(char* a,char* b) nogil:
    cdef int n = 0
    cdef int len = strlen(a)
    cdef int result = -1
    if len > 0:
        result = strstr(a, b) - a
    if 0 <= result <= len:
        return result
    return -1