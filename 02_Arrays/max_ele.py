n = int(input())
# marks = []
# for i in range(n):
#     m = int(input())
#     marks.append(m)

# split() --> string to list of sub-string
marks = list(map(int,input().split())) # marks = '65 89 72 95 81 76'
# marks = ['65','89','72','95','81','76']

high = marks[0]
for i in range(1,len(marks)):
    if marks[i]>high:
        high = marks[i]
print(high)