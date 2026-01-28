n=int(input("Enter size of square matrix: "))
for i in range(0,n):
    for j in range(0,n):
        if j<n-i:
            print("x ",end="")
    print()