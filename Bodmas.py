class Stack:
    def __init__(self):
        self.items = []
    def push(self,data):
        self.items.append(data)
    def pop(self):
        return self.items.pop()
    def size(self):
        return len(self.items)
    


S=Stack()

# S.push(10)
# S.push(20)
# S.push(30)
# S.push(40)
# print(S.items)
# print(S.pop())
# print(S.items)
# print(S.size())

e= "[3+7{52/11(3+5)}]"
S=Stack()
OB="[{("
CB = ")}]"
flag = 0
for i in e:
    if i in OB:
        S.push(i)
    if i in CB:
        x = S.pop()
        if x=="(" and i == ")":
            pass
        elif x=="{" and i == "}":
            pass
        elif x=="[" and i == "]":
            pass
        else:
            flag = 1
            break

if flag == 0 and S.size()==0:
    print("Valid")
else:
    print("invalid")

print(S.size())