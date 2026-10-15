# 5! = 5 x 4 x 3 x 2 x 1 = 120
num = int(input("Enter the no.: "))
ans = 1
for i in range(1,num+1):
    ans = ans * i
print(ans)