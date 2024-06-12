a = 5
for i in range(a+1):
    print(i*"* ")
print()
for j in range(1):
    for i in range(a-1):
        space = " "*(a-i)
        print(space+ "* "*(i+1))
    for i in range(a):
        star = " "*(i+1)
        print(star+ "* "*(a-i))


name = "hello world"

for i in range(len(name)):
    print(name[:i+1])

tuple1 = (1,2,3,2,4,1)
t2 = set(tuple1)
print(t2)
dict = {"name":'kumar',"age":20}
print("dict['age]:", dict["age"])

name = "my name is akshai"
