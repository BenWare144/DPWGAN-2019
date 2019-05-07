# Utils
import pandas as pd
import numpy as np
import os
import math
import itertools

def i_iter():
    i=0
    while 1: yield i; i+=1

def pairs(*argv):
    it=[iter(collection) for collection in argv]
    for i in range(0,len(argv[0])):
        yield (x.__next__() for x in it)

def ipairs(*argv):
    it=[i_iter()]+[iter(collection) for collection in argv]
    for i in range(0,len(argv[0])):
        yield (x.__next__() for x in it)
def transpose(l): return list(map(list, zip(*l)))

def display_full(x): 
    # displayed full pandas dataframe
    pd.set_option('display.max_rows', len(x))
    pd.set_option('display.width', 2000)
    pd.set_option('display.max_colwidth', -1)
    display(x)
    pd.reset_option('display.max_rows')
    pd.reset_option('display.width')
    pd.reset_option('display.float_format')

def print_list(L): 
    for x in L: print(x)
        
def lists_with(L,x): 
    if type(x)==type([]):
        if len(x)==0: return L
        return lists_with(lists_with(L,x[0]),x[1:]) 
    return [e for e in L if x in e]

def lists_without(L,x):
    if type(x)==type([]):
        if len(x)==0: return L
        return lists_without(lists_without(L,x[0]),x[1:]) 
    return [e for e in L if not x in e]

def are_lists_equal(list1,list2):
    # all but last element
    for x, y in pairs(list1[:-1],list2[:-1]):
        if x != y: return False
    return True

def is_element_in_list(L,x):
    for y in L:
        if are_lists_equal(x,y):
            return True
    return False

def _combine_lists(list1,list2):
    for x in list2:
        if not is_element_in_list(list1,x):
            list1=list1+[x]
    return list1

def combine_lists(list1,list2):
    # prioritizes list1 elements
    list1=lists_without(list1,None)
    list2=lists_without(list2,None)
    list1=_combine_lists(list1,list2)
    list1.sort()
    global full_run_list
    list1=_combine_lists(list1,full_run_list)
    list1=lists_without(list1,None)+lists_with(list1,None)
    return list1

def get_value_from_list(x,L):
    for y in L:
        if x[1]==y[1] and x[3]==y[3] and x[4]==y[4]:
            return y
    else: return x

def fill_values_from_list(L1,L2):
    L3=[]
    for x in L1:
        L3+=[get_value_from_list(x,L2)]
    return L3

def lists_with(L,x): 
    if type(x)==type([]):
        if len(x)==0: return L
        return lists_with(lists_with(L,x[0]),x[1:]) 
    return [e for e in L if x in e]

def lists_without(L,x):
    if type(x)==type([]):
        if len(x)==0: return L
        return lists_without(lists_without(L,x[0]),x[1:]) 
    return [e for e in L if not x in e]

def lists_with2(Ls,x): return [lists_with(L,x) for L in Ls]

def lists_without2(Ls,x): return [lists_without(L,x) for L in Ls]

def lists_with_and(L,x): 
    if type(x)==type([]):
        if len(x)==0: return L
        return [lists_with_and(L,xi) for xi in x]
    return [e for e in L if x in e]

def lists_with_and2(Ls,x,r=[]): 
    if len(Ls)==0: 
        return r
    else: 
        return lists_with_and2(Ls[1:],x,r=r+lists_with_and(Ls[0],x))

def values(L): return [x[-1] for x in L]

def values2(Ls): return [values(L) for L in Ls]

def values3(Ls): 
    dicts={[values(L) for L in Ls]}
    dicts["Model"]=[x[2] for x in Ls[0]]
    return [values(L) for L in Ls]

def make_print_index(Ls):
    iterables = [["AUROC"],['DPWGAN ϵ = 1', 'WGAN'], ['KCCR','KCCFD','MNIST']]
    pd.MultiIndex.from_product(iterables, names=['', '',''])

def group_by(L,ind):
    xs=list(set([x[ind] for x in L]))
    return [[e for e in L if e[ind] == x] for x in xs]

def group_by2(Ls,ind,r=[]):
    if len(Ls)==0: return r
    else: return group_by2(Ls[1:],ind,r=r+group_by(Ls[0],ind))

def ave(L): return sum([x for x in L if not x=="N/A"])/len([x for x in L if not x=="N/A"]) if len([x for x in L if not x=="N/A"]) else 0

def ave2(Ls): return [ave(L) for L in Ls]
