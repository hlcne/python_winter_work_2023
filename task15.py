"""""""'""""

dct={1:1, 2:2, 3:{2:22, 3:{1:111, 2:222, 3:{0:1111, 1:2222, 2:3333}, 1:333}, 1:11,},6:22}

lst=[]
def func(dct):
    for x in dct.keys():
        if type(dct[x])==dict:
            func(dct[x])
        else:
            lst.append(dct[x])
    return lst

print(func(dct))


#task 15-2
import re

str='A123BC78 A123BC783 fd23BC78 A123BCЙ78 X666XX178'

print(re.findall(r'\b[A-Za-zА-Яа-я]\d{3}[A-Za-zА-Яа-я]{2}\d{3}\b',str))

#task 15-3
"""""""'"""""
import re
str1='+7(812)334-2345 5256454-3423-232 +7(921)645-53-42 343-234-4535 345-345-2345'
print(re.findall(r'\b\+7([812,921]\)\d{3}[-]\d{2}[-,]\d{2}\b)', str1))
