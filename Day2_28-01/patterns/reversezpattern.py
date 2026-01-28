n=int(input("Enter size of square matrix: "))
for i in range(0,n):
    for j in range(0,n):
        if i==0 or i==n-1 or i==j:
           print("* ",end="")
        else:
            print("  ",end="")
    print()
