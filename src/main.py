import matplotlib.pyplot as plt
import random
from time import time
import numpy as np


def Burbuja(a,n):
    for i in range(1,n):
        for j in range(0,n-i):
            if(a[j] > a[j+1]):
                k = a[j+1]
                a[j+1] = a[j]
                a[j] = k;

def Insercion(a,n):
    for i in range(1,n):
        v=a[i]
        j=i-1
        while j >= 0 and a[j] > v:
            a[j+1] = a[j]
            j=j-1
        a[j+1]=v

def Seleccion(a,n):
    for i in range(0,n-1):
        min=i
        for j in range(i+1,n):
            if a[min] > a[j]:
                min=j
        aux=a[min]
        a[min]=a[i]
        a[i]=aux