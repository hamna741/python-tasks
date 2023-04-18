number_list=[]
for i in range(2000,3601):
    if i%7==0 and i%5!=0:
        number_list.append(i)
print(number_list)

