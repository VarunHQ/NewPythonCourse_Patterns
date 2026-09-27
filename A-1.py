print("Half-Pattern Pyramid of Stars (*)")
n = int(input("Enter the number of rows: "))
#outer loop for no. of rows
for i in range(n):
    #inner loop for no. of colums
    for j in range(i+1):
        print("* ", end="")
    print()