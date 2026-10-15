# How to use for loop
for ele in "Python":
    print(ele)

# How to use range()
for i in range(8,1,-1):
    print(i)

# demo for loop
s = 'Programming'
i=0
for ele in s:
    print("Index of ",i,"=",ele)
    i+=1

# for loop, break, continue
for i in range(1,5): # range(5)--> 0,1,2,3,4
    if i%2 == 0:
        break
    print(i)

# print 1-10 using while loop
i=1
while i<=10:
    print(i)
    i+=1

for i in range(1,6):
    for j in range(5):
        print(i,j)