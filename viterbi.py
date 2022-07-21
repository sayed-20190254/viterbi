# -*- coding: utf-8 -*-
"""
Created on Wed May 11 17:31:59 2022

@author: dell
"""

pss=.8
prr=.6
psh=.8
prg=.6
psr=.2
ps=.6
psg=.2
prs=.4
pr=.4
prh=.4

s=[]
#mode=['h','h','g','g','g','g','h']
mode=['g','g','h','h','h','h','g']
if mode[0]=='h':
    
    suny=ps*psh
    rany=pr*prh
else:
    suny=ps*psg
    rany=pr*prg
if suny<rany:
    s.append('rany')
else:
    s.append('suny')

for i in range(1,len(mode)):
    if mode[i]=='h':
        suny1=max(psh*suny*pss,psh*rany*prs)
        rany1=max(prh*rany*prr,prh*suny*psr)
    else:
        suny1=max(psg*suny*pss,psg*rany*prs)
        rany1=max(prg*rany*prr,prg*suny*psr)
    print('sany= '+str(suny))
    print('rany= '+str(rany))
    suny=suny1
    rany=rany1
    if suny<rany:
        s.append('rany')
    else:
        s.append('suny')
    
print('sany= '+str(suny))
print('rany= '+str(rany))
print(s)





