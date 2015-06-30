import numpy as np
def bxlumi(x):
    return '%d %.3f %.3f'%(x[0],x[1],x[2])
def bxintensity(x):
    return '%d %.4e %.4e'%(x[0],x[1],x[2])

def lumiunit(x,scalefactor):
    '''
    return lumiunit according to scalefactor 
    if x does not contain string /ub, do nothing
    special if scalefactor is about 23, return hz/ub
    else:
        if scalefactor>=1.0e-03 and scalefactor<1, replace /ub with /mb
        if scalefactor>=1 and scalefactor<1e3, keep /ub
        if scalefactor>=1e3 and scalefactor<1e6, replace /ub with /nb
        if scalefactor>=1e6 and scalefactor<1e9, replace /ub with /pb
        if scalefactor>=1e9 and scalefactor<1e12, replace /ub with /fb
        if scalefactor>=1e12 and scalefactor<1e15, replace /ub with /ab
    '''
    if x.find('(/ub)')==-1: return x
    if int(scalefactor) == 23: return x.replace('(/ub)','(hz/ub)')
    if (scalefactor>=1.0e-09) and (scalefactor<1.0e-06): return x.replace('(/ub)','(/kb)')
    if (scalefactor>=1.0e-06) and (scalefactor<1.0e-03): return x.replace('(/ub)','(/b)')
    if (scalefactor>=1.0e-03) and (scalefactor<1.0): return x.replace('(/ub)','(/mb)')
    if (scalefactor>=1.0) and (scalefactor<1.0e3): return x
    if (scalefactor>=1.0e3) and (scalefactor<1.0e6): return x.replace('(/ub)','(/nb)')
    if (scalefactor>=1.0e6) and (scalefactor<1.0e9): return x.replace('(/ub)','(/pb)')
    if (scalefactor>=1.0e9) and (scalefactor<1.0e12): return x.replace('(/ub)','(/fb)')
    if (scalefactor>=1.0e12) and (scalefactor<1.0e15): return x.replace('(/ub)','(/ab)')
    return x

def guesslumiUnit(inverseubval):
    '''
    input:
        float value in 1/ub
    output:
        printable value (value(float),unit(str)) unit in [1/kb,1/b,1/mb,1/ub,1/nb,1/pb,1/fb]
    '''
    denomitor = 1.0
    if inverseubval>=1.0e-09 and inverseubval<1.0e-06:
        denomitor=1.0e-09
        unitstring='/kb'
        return (float(inverseubval)/float(denomitor),unitstring)
    if inverseubval>=1.0e-06 and inverseubval<1.0e-03:
        denomitor=1.0e-06
        unitstring='/b'
        return (float(inverseubval)/float(denomitor),unitstring)
    if inverseubval>=1.0e-03 and inverseubval<1.0:
        denomitor=1.0e-03
        unitstring='/mb'
        return (float(inverseubval)/float(denomitor),unitstring)
    if inverseubval>=1.0 and inverseubval<1.0e3:
        unitstring='/ub'
        return (inverseubval,unitstring)
    if inverseubval>=1.0e3 and inverseubval<1.0e06:
        denomitor=1.0e3
        unitstring='/nb'
        return (float(inverseubval)/float(denomitor),unitstring)
    if inverseubval>=1.0e6 and inverseubval<1.0e9:
        denomitor=1.0e6
        unitstring='/pb'
        return (float(inverseubval)/float(denomitor),unitstring)
    if inverseubval>=1.0e9 and inverseubval<1.0e12:
        denomitor=1.0e9
        unitstring='/fb'
        return (float(inverseubval)/float(denomitor),unitstring)
    if inverseubval>=1.0e12 and inverseubval<1.0e15:
        denomitor=1.0e12
        unitstring='/ab'
        return (float(inverseubval)/float(denomitor),unitstring)
    return (float(inverseubval),denomitor,'/ub')



