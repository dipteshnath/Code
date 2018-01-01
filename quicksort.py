# -*- coding: utf-8 -*-
"""
Created on Sun Dec 31 22:50:46 2017

@author: dipte
"""
def quicksort(arr):
    if len(arr)<=1:
        return arr
    pivot=arr[len(arr)//2]#typecast from int float
    left=[x for x in arr if x<pivot]
    middle=[x for x in arr if x==pivot]
    right=[x for x in arr if x>pivot]
    return quicksort(left)+middle+quicksort(right)

print(quicksort([3,6,8,10,1,2]))

        
