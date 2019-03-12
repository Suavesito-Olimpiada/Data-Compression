#!/bin/python3.7
from heapq import heappush, heappop, heapify
import numpy as np
import magic
from PIL import Image
import sys
import os
import copy as cp

def arithmetic_encode_float(model, sequence):
    """
    Receives the model as a list of two
    lists and the sequence as a list.
    Return the number asociated to the
    model and the sequence introduced.
    It use the mid-numer to return the
    number asociated.
    """
    lo = 0.0
    wide = 1.0
    _model = cp.copy(model[0])
    intg = sum(_model)
    _model = [float(sym)/float(intg) for sym in _model]
    for sym in sequence:
        lo = lo+wide*sum(_model[:model[1].index(sym)])
        wide *= _model[model[1].index(sym)]
    return lo+wide/2.0


def arithmetic_decode_float(model, number, n):
    """
    Receives the model as a list of two
    list and the number to decode.
    Return the sequence of symbols that
    form the number in a the form of a
    list.
    """
    _model = cp.copy(model[0])
    intg = sum(_model)
    _model = [float(sym)/float(intg) for sym in _model]
    cmt = np.array([sum(_model[:i]) for i in range(0, len(_model)+1)])
    code = []
    for i in range(0, n):
        prv = cmt[cmt<number].max()
        idx = np.where(cmt == prv)[0][0]
        code.append(model[1][idx])
        number = (number-prv)/_model[idx]
    return code
    

def arithmetic_encode(model, sequence):
    """
    Model is given as a list of integers
    that represent the probabilities for
    each different value.
    """
    return 0

def arithmetic_decode(model, number, n):
    return 0

if __name__ == '__main__':
    model = [[2, 3, 5], ['a1', 'a2', 'a3']]
    sequence = ['a1', 'a1', 'a3', 'a2', 'a3', 'a1']
    code_e = arithmetic_encode_float(model=model, sequence=sequence)
    print("{0:1.10f}".format(code_e))
    code_d = arithmetic_decode_float(model=model, number=code_e, n=len(sequence))
    print("{}\n{}".format(code_d, code_d==sequence))
    
    test=0.63215699
    arithmetic_decode_float(model=model, number=test, n=10)
    
    
