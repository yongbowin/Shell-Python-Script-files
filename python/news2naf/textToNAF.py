# -*- coding: utf-8 -*-
"""
Created on Wed Nov 30 09:55:59 2016

@author: zuoxiaolei
"""
import os
import time
import hashlib
import sys
import csv
csv.field_size_limit(1000000000)

m = hashlib.md5()

def text2NAF(mydir,content,date,title,publicId,url):
    '''
    生成规定格式的NAF文件
    params:
          mydir：输出naf的文件夹
          content:新闻内容
          date:新闻日期 为标准时间格式 %Y-%m-%dT%H:%M:%SZ
          title:新闻标题
          publicId:新闻id
          url:新闻的链接
    '''
    if os.path.exists(mydir):
        pass
    else:
        os.mkdir(mydir)

    with open(mydir+publicId+".naf",'w') as fh:
        #fh.write('<?xml version="1.0" encoding="utf-8"?>'+'\n')
        fh.write('<NAF xml:lang="en" version="v3">'+'\n')
        fh.write("<nafHeader>\n")
        title = title.replace('"', "'").replace("&", "&amp;").replace("<", "&lt;").replace(">", "&gt;")
        url = "http://official.aitech.xin:8080/en_chaorder_articles/" + publicId + ".naf"
        fh.write("<fileDesc creationtime="+'"'+date+'"'+" title="+'"'+title+'"'+" />"+"\n")
        fh.write("<public publicId="+'"'+publicId+'"'+" uri="+'"'+url+'"'+" />"+"\n")
        fh.write("</nafHeader>"+"\n")
        fh.write("<raw><![CDATA["+content+"]]></raw>"+"\n")
        fh.write("</NAF>")

if __name__ == "__main__":
    #测试例子
    csv_reader = csv.reader(open(r"US_Stock_News.csv"))
    count = 0
    for row in csv_reader:
        if count!=0:
            #url,title,abstract,source,date,text,features = row
            title,url,text,abstract,source,date = row
            content = text
            m.update(content)
            publicId = m.hexdigest()
            date = time.strftime('%Y-%m-%dT%H:%M:%SZ',time.localtime(float(date)))
            text2NAF("US_Stock_News/",title+". "+content,date,title,publicId,url)
        count+=1
    print count
    print "finish!"
