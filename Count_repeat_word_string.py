# -*- coding: utf-8 -*-
"""
Created on Sat Dec 30 17:11:31 2017

@author: dipte

Check number of word in a space seperated string

input-cat bat dog bat cat  output- bat 

input: cat bat mat bat cat yat
output:bat

"""

st=input("Enter your space seperated string")
stx=st.split()
c=0
for i in range(0,len(stx)):
    for j in reversed(range(0,i)):
        if (stx[i]==stx[j]):
            print(stx[i])
            c=1
            break
    if(c==1):break
            #quit()

    