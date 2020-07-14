import os
os.system("cls")
a=10
print("="*a*7,"\n")
for i in range(1,a):
    for j in range(1,i+1):
        print(f"{j}*{i}={i*j}",end="\t")
    print()