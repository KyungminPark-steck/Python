# -*- coding: utf-8 -*-
"""
Created on Sat Jun 18 22:32:09 2022

@author: 82102
"""

def function1(filename):
    f1 = open(filename,"r") #파일 읽기
    data = f1.read()
    f1.close() 
    data = data.lower() #데이터 전처리
    result = data.replace('\n','    ').replace('(','').replace(')','').replace(',', '').replace('.', '   ').replace(' --','').replace(';','').replace(':',' ').replace('"','').replace(' ','  ').split('  ')
#___________________________________________________________
    import re 
    p = re.compile("^com(ing|es|e)|^came") #come 활용형 찾기
    come = [] #come 앞 뒤 세 단어 담을 리스트
    count = 0
    for w in result: 
        come_result = p.search(w)
        if come_result != None:
            a =("{} {} {} {} {} {} {}".format(result[count-3],result[count-2], result[count-1], result[count], result[count+1], result[count+2],result[count+3]))
            come.append(a)
        count = count+1
        
    print("come 원형과 활용형을 포함한 빈도수: {}".format(len(come))) #단어와 빈도 콘솔 출력
    f2 = open("come_concor.txt",'w')
    for i in range(len(come)):
        concor = ("{}.{}".format(i+1, come[i]))
        print(concor, '\n') #앞 뒤 세 단어 출력
        f2.write(concor) #앞 뒤 세 단어 파일 쓰기
        f2.write('\n')
    f2.close()
#____________________________________________________________
    p = re.compile("^tak(ing|en|e)|^took") #take 활용형 찾기
    take = [] #take 앞 뒤 세 단어 담을 리스트
    count = 0
    for w in result:
        take_result = p.search(w)
        if take_result != None:
            threewords =("{} {} {} {} {} {} {}".format(result[count-3],result[count-2], result[count-1], result[count], result[count+1], result[count+2],result[count+3]))
            take.append(threewords)
        count = count+1
        
    print("take 원형과 활용형을 포함한 빈도수: {}".format(len(take))) #단어와 빈도 콘솔 출력
    f2 = open("take_concor.txt",'w')
    for i in range(len(take)):
        concor = ("{}.{}".format(i+1, take[i]))
        print(concor, '\n') #앞 뒤 세 단어 출력
        f2.write(concor) #앞 뒤 세 단어 파일 쓰기
        f2.write('\n')
    f2.close()
#___________________________________________________________
    p = re.compile("^mak(ing|es|e)$|^made") #make 활용형 찾기
    make = [] #make 앞 뒤 세 단어 담을 리스트
    count = 0
    for w in result:
        make_result = p.search(w)
        if make_result != None:
            threewords =("{} {} {} {} {} {} {}".format(result[count-3],result[count-2], result[count-1], result[count], result[count+1], result[count+2],result[count+3]))
            make.append(threewords)
        count = count+1
        
    print("make 원형과 활용형을 포함한 빈도수: {}".format(len(make))) #단어와 빈도 콘솔 출력
    f2 = open("make_concor.txt",'w')
    for i in range(len(make)):
        concor = ("{}.{}".format(i+1, make[i]))
        print(concor, '\n') #앞 뒤 세 단어 출력
        f2.write(concor) #앞 뒤 세 단어 파일 쓰기
        f2.write('\n')
    f2.close()
#___________________________________________________________
#함수호출
function1("Obama_speech.txt")
    
