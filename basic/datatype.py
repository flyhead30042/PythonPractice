
number1=123
number2=123.4
print(number1)
print(number1+number2)

string1='string'
print(string1[1:])
print(len(string1[1:]))

list1=[[1,5],[2],['a','b',3, True]]
print(list1[2][1:])
print(len(list1[2]))
print(type(list1[2][0]))
col1 = [row[0] for row in list1 if type(row[0]).__name__ !='str']
print(col1)

list2 = [x.upper() for x in string1]
print(list2)

dict1={'name':'peter', 'age':12, 'fav fruit':'Apple'}
print (dict1['fav fruit']=='Apple')

dict2={'a':1, 'f':2, 'c':3}
print(dict2.keys())
print(dict2.values())

for key in sorted(dict2.keys()):
    print(dict2[key])

