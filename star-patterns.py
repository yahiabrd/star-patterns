n = 5

#square
for i in range(n):
    for j in range(n):
        print("*", end=" ")
    print()

print()

#empty square
for i in range(n):
    for j in range(n):
        if(i==0 or j ==0 or i == n-1 or j==n-1):
            print("*", end=" ")
        else:
            print(" ", end=" ")
    print()

print()

#triangle
for i in range(n):
    for j in range(n-i-1):
        print(" ", end=" ")
    for k in range(n//n+i*2):
        print("*", end=" ")
    print()

print()

#reserved triangle
for i in range(n):
    for j in range(n//n+i-1):
        print(" ", end=" ")
    for k in range(n-i-1):
        print("*", end=" ")
    for l in range(n-i):
        print("*", end=" ")
    print()

#empty triangle
for i in range(n):
    for j in range(n-i-1):
        print(" ", end=" ")
    for k in range(n//n+i*2):
        if(k==i*2 or k==0 or i==n-1):
            print("*", end=" ")
        else:
            print(" ", end=" ")
    print()

print()

#descending pyramid model
for i in range(n):
    for j in range(n-i):
        print("*", end=" ")
    print()

print()

for i in range(n):
    for j in range(n//n+i-1):
        print(" ", end=" ")
    for j in range(n-i):
        print("*", end=" ")
    print()

print()

#ascending pyramid model
for i in range(n):
    for j in range(n//n+i):
        print("*", end=" ")
    print()

print()

for i in range(n):
    for j in range(n-i-1):
        print(" ", end=" ")
    for j in range(n//n+i):
        print("*", end=" ")
    print()

print()

#rhombus
for i in range(n):
    for j in range(n-i):
        print("*", end=" ")
    for k in range(n//n+i-1):
        print(" ", end=" ")
    for l in range(n//n+i-1):
        print(" ", end=" ")
    for m in range(n-i):
        print("*", end=" ")
    print()

for i in range(n):
    for j in range(n//n+i):
        print("*", end=" ")
    for k in range(n-i-1):
        print(" ", end=" ")
    for l in range(n-i-1):
        print(" ", end=" ")
    for m in range(n//n+i):
        print("*", end=" ")
    print()

print()

#rhombus
for i in range(n):
    for j in range(n-i):
        if(n-1==j+i):
            print("*", end=" ")
        else:
            print(" ", end=" ")
    for k in range(n//n+i-1):
        print("*", end=" ")
    for l in range(n//n+i-1):
        print("*", end=" ")
    for m in range(n-i):
        if(n-1==m+i+j):
            print("*", end=" ")
        else:
            print(" ", end=" ")
    print()

for i in range(n):
    for j in range(n//n+i):
        if(j==i):
            print("*", end=" ")
        else:
            print(" ", end=" ")
    for k in range(n-i-1):
        print("*", end=" ")
    for l in range(n-i-1):
        print("*", end=" ")
    for m in range(n//n+i):
        if(m==0):
            print("*", end=" ")
        else:
            print(" ", end=" ")
    print()