
number1=123
number2=123.4
print(number1)
print(number1+number2)

string1='string'
print(string1[1:])
print(len(string1[1:]))

string2='It is a hello world' + str(38)
for x in string2.split():
    print(x.upper())

string3 = string2.replace("world", "kitty")
print(string3)

print("%s length is %d" % (string3, len(string3)))

where= string3.find('is')+2
print(string3[:where] + " not" + string3[where:])


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

file1=open('data.text', 'w')
file1.write('line1\n')
file1.write('line2\n')
file1.close()

file1 = open('data.text')
data = file1.read()
print(data.split())


file2 = open('data.text')
data2 = file1.read()
print(data2.split())
