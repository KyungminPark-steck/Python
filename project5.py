# -*- coding: utf-8 -*-
"""
Created on Sat Jun 18 21:15:38 2022

@author: 82102
"""

def function1(filename): #파일 읽기 함수
    f1 = open(filename,"r") 
    data = f1.read()
    f1.close() 
    return data

def function2(data): #데이터 전처리 함수
    data = data.lower()
    result = data.replace('\n',' ').replace('(','').replace(')','').replace(',', '').replace('.', ' ').replace('--','').replace(';','').replace(':',' ').replace('"',' ').replace(' ','  ').split('  ')
    return result
    
def function3(result): #인칭대명사 빈도 구하는 함수
    pronoun1 = ['i', 'my', 'me', 'mine']
    pronoun1s = ['we', 'our', 'us', 'ours']
    for p1 in pronoun1:
        freq = {}
        freq[p1] = result.count(p1)
        print(freq)
    for p1s in pronoun1s:
        freq1s = {}
        freq1s[p1] = result.count(p1s)
        print(freq1s)
        
#함수1,2,3 호출
data = function1("Obama_speech.txt")
result = function2(data)
function3(result)
        

        
        