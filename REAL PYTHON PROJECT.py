print("WELCOME! SIR I AM MATHEMAGIX PROGRAM. \nI WILL CHECK AND TELL YOU IF YOU CAN ARRANGE THE EGGS IN THE BASKET IN THAT MANNER OR NOT.")
print("\n")
print("MAGIC SQUARE :- [A square divided into smaller squares each containing a number,\n                 such that the figures in each vertical, horizontal, and diagonal row add up to the same value.]")
print("\n")
n=int(input("ENTER THE SIZE OF SQUARE MATRIX SHAPED BASKET YOU HAVE: "))
print("\n")
print("ENTER THE NO. OF EGGS BELOW, WHICH YOU WANT IN EACH SECTION OF THE BASKET.")
print("\n")
a=[]
for i in range (n):
    b=[]
    for j in range (n):
        j=int(input("Enter The Number of EGGS = "))  
        b.append(j)
    a.append(b)
if j<=(n*n):
    print("\n")
    print("THE BASKET ARRANGEMENT is ......")
    print("\n")
    for i in range(n):
        for j in range (n):
            print(a[i][j],end=" ")
        print()
    sum1d=0
    sum2d=0
    for i in range(n):
        for j in range(n):
            if i==j:
                sum1d=sum1d+a[i][j]
            if i+j==n-1:
                sum2d=sum2d+a[i][j]
    if sum1d!=sum2d:
        z=5
    else:
        for i in range(n):
            sumr=0
            sumc=0
            for j in range(n):
                sumr=sumr+a[i][j]
                sumc=sumc+a[j][i]
            if sumr!=sum1d:
                z=1
            elif sumc!=sum1d:
                z=1
            else:
                z=0
    if z==0:
        print("\n")
        print("YES SIR! YOU CAN ARRANGE YOUR BASKET WITH THE EGGS IN THAT MANNER.\nIT WILL RESULT IN FORMING A MAGIC SQUARE.")
    else:
        print("\n")
        print("UH OH! SORRY SIR YOU CAN'T ARRANGE YOUR EGGS LIKE THAT! \nIT DOESN'T FORM A MAGIC SQUARE.")
else:
    print("\n")
    print("THE NO. OF EGGS ENTERED IN ANY SLOT HAS MORE VALUE/VALUES GREATER THAN n².(i.e.- OVER THE CAPACITY OF THAT SLOT OF THE BASKET.)\nPLEASE RE-RUN THE PROGRAM AND RE-ENTER THE VALUES OF NO. OF EGGS PROPERLY !")
