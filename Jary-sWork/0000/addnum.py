#!/usr/bin/env python
# -*- coding: utf-8 -*- 

' a test module '

__author__ = 'Jary'
from PIL import Image,ImageFilter,ImageDraw,ImageFont
def addnum(img):
        draw=ImageDraw.Draw(img)
        font=ImageFont.truetype('Arial.ttf',36)
        w,h=img.size
        draw.text((w-30,5),'4',font=font,fill='#FF0000')
        img.save('new.jpg','jpeg')
                
if __name__=='__main__':
        try:
                image=Image.open('cat.jpg')
                addnum(image)
                print u'成功'
        except:
                print u'失败'
