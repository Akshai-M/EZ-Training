inp = input("Enter expression: ")

operators = ['+', '-', '*', '/', '//', '**']
for op in operators:
   
    if op in inp:
        res = list(map(float, inp.split(op)))
        if op == '+':
            print(res[0] + res[1])
        elif op == '-':
            print(res[0] - res[1])
        elif op == '*':
            print(res[0] * res[1])
        elif op == '/':
            print(res[0] / res[1])
        elif op == '//':
            print(res[0] // res[1])
        elif op == '**':
            print(res[0] ** res[1])
        break
