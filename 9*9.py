i = 1
while i <= 9:

    j=1
    while j <= 9:
        print(f"{i}*{j}={j*i}\t",end='')
        j=j+1

    i=i+1
    print()

print()
print()
print()


for x in range(1,10):
    for y in range(1,x+1):
        print(f"{y}*{x}={x*y}\t",end='')
    print()