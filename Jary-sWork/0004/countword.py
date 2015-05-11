#!/usr/bin/env python
# -*- coding: utf-8 -*- 

' a test module '

__author__ = 'Jary'
import re
def countword(fold):
        with open(fold,'r') as f:
                article=f.read()
        article=article.lower()
        wordlist=re.findall(r'\w+',article)
        wordlistset=set(wordlist)
        worddic={}
        for i in wordlistset:
                if i=='s' or i=='is' or i=='m' or i=='am':
                        worddic['is']=wordlist.count('s')+wordlist.count('is')
                        worddic['am']=wordlist.count('m')+wordlist.count('am')
                        print 'is  ',worddic['is'],'\n'
                        print 'am  ',worddic['am'],'\n'
                        continue                
                worddic[i]=wordlist.count(i)
                print i,' ',wordlist.count(i),'\n'
        return worddic
        
if __name__=='__main__':
        wordic=countword('english.txt')
