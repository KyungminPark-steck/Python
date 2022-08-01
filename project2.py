# -*- coding: utf-8 -*-
"""
Created on Sat Jun 18 14:36:24 2022

@author: 82102
"""

def function(filename):
    f1 = open(filename,"r") #파일 읽기
    data = f1.read()
    f1.close() 
    
    #데이터 전처리 
    data = data.lower()
    data = data.replace('\n',' ').replace(',', '').replace('.', ' ').replace('--','').replace(';',' ').replace(':',' ').replace(' ','  ').split('  ')
    while '' in data:
        data.remove('')
    
    while True:
        w = input("찾고싶은 단어를 입력하세요: ") #input()을 통해 찾고자 하는 단어를 입력받기
        if w == 'q': #q 입력하면 loop에서 빠져나오기 
            break
        elif w in data: #있다면 단어-빈도수 출력
            dc = data.count(w)
            print("'{}' is found - frequency {}".format(w, dc))
        else: #없다면 not found 
            print("not found")

function("desertification.txt")
        
    
    