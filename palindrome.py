number = int(input('Number:'))
reveres = 0
temp = number

while (temp > 0):
    Remainder = temp % 10
    reveres = (reveres * 10) + Remainder
    temp = temp // 10
if number == reveres: 
    print('Palindrome')
else:
    print('Not Palindrome')