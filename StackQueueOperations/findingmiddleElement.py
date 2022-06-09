
list1 =[]
print('enter how many elements do you want to add to list:')
for i in  range(0,int(input())):
    list1.append(input())

print('how many mid elements you want:')
k = int(input())

startindex= (len(list1)//2)-(k//2)
endindex = (len(list1)//2)+(k//2)

result =[]

for j in range(len(list1)):
    if j>=startindex and j<endindex:
        result.append(list1[j])

print('extracted mid elements are',str(result))