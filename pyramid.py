#! python3

i = 10
k=0
astr = '*'
space = ""
print(i)

while i != 0:
    for j in range(i-1):
            print(" ", end='')
    print(astr)
    i -= 1
    astr += "**"


if i == 0:
    i-1
    k=10    

for t in range(k):
    print(space, end='')
    for p in range(k-2):
            print("*", end='')
    k -= 2
    print("")
    space += " "    
