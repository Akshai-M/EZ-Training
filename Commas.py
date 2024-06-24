def number(number):
    number_str = str(number)[::-1]  
    result = ""
    if number > 999:
        for i in range(len(number_str)):
            # print(i)
            if i > 0 and i % 3 == 0:
                result += ","
            result += number_str[i]

        return result[::-1]  
numb = 10000

print(number(numb))
# num = 999000
# formatted_number = number(num)
# count = formatted_number.count(",")
# print(count)
# print(formatted_number)  


# def count_commas_in_range(n):
#     comma_count = 0

#     for i in range(n):
#         formatted_number = f"{i:,}"  
#         comma_count += formatted_number.count(',')

#     return comma_count


# n = 1000000
# print(count_commas_in_range(n))  
