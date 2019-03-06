#!/usr/bin/env python
# -*- coding: utf-8 -*-

def splitN(L, n):
    args = [iter(L)] * n
    return zip(*args)

t = (2, 2, 10, 10, 344, 344, 45, 43, 2, 2, 10, 10, 12, 8, 2, 10)
print splitN(t, 4)
