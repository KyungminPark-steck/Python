# -*- coding: utf-8 -*-
"""
Created on Sat Jun 18 13:08:10 2022

@author: 82102
"""

f1 = open("Obama_speech.txt","r") #파일 읽기
data = f1.read()
f1.close() 
data = data.lower()
data = data.replace('\n',' ').replace('(','').replace(')','').replace(',', '').replace('.', ' ').replace('--','').replace(';','').replace(':',' ').replace('"',' ').replace(' ','  ').split('  ')
word = [] #데이터 전처리 완료. 공백 지우는 과정.
for i in data:
    if i == (''):
        continue
    else:
        word.append(i)

w_freq = {} #단어와 빈도 구하기 
for w in word:
    w_freq[w] = data.count(w)

import operator
w_freq = sorted(w_freq.items(), key = operator.itemgetter(1), reverse = True)
print(w_freq)

print("빈도 기준 상위 5개 단어 출력") #상위 5개 콘솔 출력
for i in range(5):
    print("{0}. {1}: {2}".format(i+1, w_freq[i][0], w_freq[i][1]))

f2 = open("freq.txt", "w") #전체 결과 freq.txt저장
for i in range(len(w_freq)):
    f2.write("{}. {}: {}\n".format(i+1, w_freq[i][0], w_freq[i][1]))
f2.close()










    

    