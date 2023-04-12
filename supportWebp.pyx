# cython: language_level=3
# distutils: language = c++
from libcpp.map cimport map
from cython.operator cimport dereference, preincrement
from libc.string cimport strstr,strlen,memset
from libc.stdlib cimport atoi,rand,srand


cdef struct BrowserVersion:
    char* name
    int version

cdef BrowserVersion[8] version_list = [
    BrowserVersion(b'Firefox', 65),
    BrowserVersion(b'Chrome', 32),
    BrowserVersion(b'Edge', 18),
    BrowserVersion(b'AppleWebKit', 605), # Safari 14
    BrowserVersion(b'OPR', 19),
    BrowserVersion(b'UCBrowser', 12),
    BrowserVersion(b'SamsungBrowser', 4),
    BrowserVersion(b'QQBrowser', 10)
]

cpdef bint check_version(char* ua):
    cdef char[5] ua_version
    cdef int i1 = 0
    cdef int index
    with nogil:
        for i in version_list:
            index = strindex(ua, i.name)
            if index == -1:
                continue
            i1 = index + strlen(i.name) + 1
            memset(&ua_version[0], 0, sizeof(ua_version))
            while b'0' <= ua[i1] <= b'9':
                ua_version[strlen(ua_version)] = ua[i1]
                i1 += 1
            if atoi(ua_version) >= i.version:
                return True

cdef int strindex(char* a,char* b) nogil:
    cdef int n = 0
    cdef int len = strlen(a)
    cdef int result = -1
    if len > 0:
        result = strstr(a, b) - a
    if 0 <= result <= len:
        return result
    return -1
