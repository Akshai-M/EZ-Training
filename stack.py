class stk:

    def __init__(self):
        self.lst=[]

    def push(self,exp):
        for i in exp:
            if i=="[" or i=="{" or i=="(":
                self.lst.append(i)
        
    def pop(self,exp):
        for i in exp:
            if i=="]" and self.lst[-1]=="[":
                self.lst.pop()
            elif i=="}" and self.lst[-1]=="{":
                self.lst.pop()
            elif i==")" and self.lst[-1]=="(":
                self.lst.pop()

exp=input("Enter the expression: ")
s=stk()
s.push(exp)
print(s.lst)
s.pop(exp)

n=len(s.lst)
if n>0:
    print("Invalid statment")
elif n==0:
    print("valid statment")