# -*- coding: utf-8 -*-
"""
Created on Sat Jun 18 15:01:50 2022

@author: 82102
"""

f1 = open("desertification.txt","r") #파일 읽기
data = f1.read()
f1.close() 

#데이터 전처리
data = data.lower()
data = data.replace(',', '').replace(';','').replace(':','').replace('.', ' ').replace('\n',' ') 
# ',', ';', ':'가 앞 뒤로 있는 단어쌍은 한 단어로 처리. 줄바꿈 혹은 문장 종료시 연속된 단어에서 배제
    
ww = input("찾고싶은 연속된 단어를 입력하세요: ") #연속된 두 단어 입력받기
#검색결과
if ww in data: #있다면 단어-빈도수 
    dc = data.count(ww)
    print("'{}' is found - frequency {}".format(ww, dc))
else: #없다면 not found 
    print("not found")