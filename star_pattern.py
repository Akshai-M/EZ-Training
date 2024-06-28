n = 5
for i in range(n):
    print(" "*(n-i) + "* "*(i+1))

print("\n")

for j in range(n):
    print(" "*(j+1) + "* "*(n-j))

print("\n")


def right_angle(num):
    for k in range(num+1):
        print("* "*k)

right_angle(5)

print("\n")

t1 = (1,2,3,2,4,1)
t2 = set(t1)

print(t2)


