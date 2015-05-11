#!/usr/bin/env python
# -*- coding: utf-8 -*- 

' a test module '

__author__ = 'Jary'
import random
def randcha():
        num2cha=chr(random.randint(48,57))
        word2cha=chr(random.randint(65,90))
        flag=random.randint(0,1)
        if flag:
                return num2cha
        return word2cha
def makelist(num):
        yhq=[]
        for i in range(0,num):
                t=randcha()
                yhq.append(t)
        return ''.join(yhq)
def makeacc(weishu,geshu):
        acc={}
        for x in range(0,geshu):
                acc[x+1]=makelist(weishu)
                print acc[x+1]
        return acc
if __name__=='__main__':
        t=makeacc(12,50)
                
