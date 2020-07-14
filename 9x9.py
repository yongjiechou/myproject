for i in range(1,10):
    for j in range(1,10):
        k=i*j
        print("%2d*%-2d=%-4d"%(j,i,k),end="")
    print()