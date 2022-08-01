# -*- coding: utf-8 -*-
"""
Created on Sat Jun 18 15:26:40 2022

@author: 82102
"""

data = '''Every year we go to Florida. We like to go to the beach. My favorite beach is called Emerson Beach. It is very long, with soft sand and palm trees. It is very beautiful. I like to make sandcastles and watch the sailboats go by. Sometimes there are dolphins and whales in the water! Every morning we look for shells in the sand. I found fifteen big shells last year. I put them in a special place in my room. This year I want to learn to surf. It is hard to surf, but so much fun! My sister is a good surfer. She says that she can teach me. I hope I can do it!'''
data = data.lower() #데이터 처리해서 중복 단어 제거된 단어 리스트 만들기
word = data.replace('.',' ').replace('!',' ').replace(',',' ').split()
sen = data.replace('. ','#').replace('! ','#').replace('!','').split('#')

def function(data, tp, a=len(word)): #매개변수 세 개: 데이터 변수이름, word or sentence 선택, 출력할 단어/문장 수
     
    if tp == word: #단어선택
       leng = {}
       for i in word: 
           leng[i] = len(i) #딕셔너리에 {'단어': 단어 길이} 넣기
            
       import operator #단어 길이 내림차순으로 저장
       leng = sorted(leng.items(), key = operator.itemgetter(1), reverse = True) 
       
       leng_list = [] #전체 단어 리스트
       for i in range(len(leng)):
           ll = ("{}. {}: {}".format(i+1, leng[i][0], leng[i][1]))
           leng_list.append(ll)
       
       if a> len(word): #단어 수보다 더 큰 수 입력 시
           print("Please, enter a number less than {}".format(len(word)))#입력 받은 수 만큼 반복
       
       elif a < len(word): #단어 수보다 작은 수 입력 시 입력한 수만큼 출력
           for i in range(a):
               print(leng_list[i])
       
       else: #단어 수 입력하지 않으면 단어 전체 리스트 출력
           print(leng_list)
           
           
    if tp == sen: #문장선택
        s_l = [] #전체 문장 리스트 
        for i in range(0,len(sen)):
            s_l.append('{0}. {1}'.format(i+1,sen[i])) #리스트에 문장번호. 문장 넣기
            
        if a == len(word): #문장 수 입력하지 않을 시
            print(s_l)
            
        elif a > len(sen): #문장 수보다 더 큰 수 입력 시
            print("Please, enter a number less then {}".format(len(sen)))
           
        elif a < len(sen): #문장 수보다 작은 수 입력시 입력한 수만큼 출력
            for i in range(a):
                print(s_l[i])
               
function(data,word, 5)  
function(data,sen,3)

function(data,word)

function(data,sen)

function(data,word,200)
function(data,sen, 100)

