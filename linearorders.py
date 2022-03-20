from itertools import permutations, combinations
import random

linearorders3 = [list(p) for p in permutations(range(1, 4))]
linearorders4 = [list(p) for p in permutations(range(1,5))]
# print("3 vertices: \n",linearorders3)
# print(len(linearorders3))
# print("4 vertices: \n",linearorders4)
# print(len(linearorders4))

f = open("3vertices.txt", "w")
for i in range(len(linearorders3)):
    lst = [list(p) for p in combinations(linearorders3, i+1)]
    #print("Number of linear orders: %d\n"%(i+1))
    f.write("Number of linear orders: %d\n"%(i+1))
    for j in lst:
        #print(str(j))
        # f.write(str(j)+'\n')
        f.write(('-'.join(str(k) for k in j))+'\n')
f.close()

f = open("4vertices1.txt", "w")
for i in range(len(linearorders4)//4):
    lst = [list(p) for p in combinations(linearorders4, i+1)]
    #print("Number of linear orders: %d\n"%(i+1))
    f.write("Number of linear orders: %d\n"%(i+1))
    limit = 100
    counter = 0
    length =  len(lst)
    if(length > 100):
        indices = random.sample(lst, 100)
        lst = indices
         
    for j in lst:
        f.write(('-'.join(str(k) for k in j))+'\n')
        counter+=1
f.close()

f = open("4vertices2.txt", "w")
for i in range(len(linearorders4)//4):
    lst = [list(p) for p in combinations(linearorders4, (len(linearorders4)//4)+i+1)]
    #print("Number of linear orders: %d\n"%(i+1))
    f.write("Number of linear orders: %d\n"%((len(linearorders4)//4)+i+1))
    limit = 100
    counter = 0
    length =  len(lst)
    if(length > 100):
        indices = random.sample(lst, 100)
        lst = indices
         
    for j in lst:
        f.write(('-'.join(str(k) for k in j))+'\n')
        counter+=1
f.close()

f = open("4vertices3.txt", "w")
for i in range(len(linearorders4)//4):
    lst = [list(p) for p in combinations(linearorders4, (len(linearorders4)//2)+i+1)] 
    #print("Number of linear orders: %d\n"%(i+1))
    f.write("Number of linear orders: %d\n"%((len(linearorders4)//2)+i+1))
    limit = 100
    counter = 0
    length =  len(lst)
    if(length > 100):
        indices = random.sample(lst, 100)
        lst = indices
         
    for j in lst:
        f.write(('-'.join(str(k) for k in j))+'\n')
        counter+=1
f.close()

f = open("4vertices4.txt", "w")
for i in range(len(linearorders4)//4):
    lst = [list(p) for p in combinations(linearorders4, (3*len(linearorders4)//4)+i+1)]
    #print("Number of linear orders: %d\n"%(i+1))
    f.write("Number of linear orders: %d\n"%((3*len(linearorders4)//4)+i+1))
    limit = 100
    counter = 0
    length =  len(lst)
    if(length > 100):
        indices = random.sample(lst, 100)
        lst = indices
         
    for j in lst:
        f.write(('-'.join(str(k) for k in j))+'\n')
        counter+=1
f.close()

print("FINISH!!!!!!!!!!!!!!!")

# CONVERTING STRING INPUT TO LIST OF INTEGERS
# f = open("3vertices.in", "r")
# convertedInput = []
# groupedInput = []
# index = 0
# for i in f:
#     if i[0] == 'N':
#         convertedInput.append(groupedInput)
#         groupedInput = []
#         print()
#         continue
#     x = i.strip('\n').split('-')
#     perSet = []
#     for j in x:
#         converted = [int(num) for num in j.strip('[]').split(',')]
#         perSet.append(converted)
#     print(perSet)
#     groupedInput.append(perSet)
# convertedInput.append(groupedInput)

# for i in convertedInput:
#     print(i)
#     print()