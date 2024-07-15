# x = [2,4,6,8,10]
# y = [3,5,7,9,10,12]
# z =[]
# # for i in range(len(x)):
# #     if x[i]%2 == 0 and x[i] not in y:
# #         z.append(x[i])
# # print(z)

# z = [i for i in x if i not in y and i%2 == 0]
# print(z)

# age = 36
# text = "My age is {}"
# print(text.format(age))

# p = [1,2,3,4]
# o = [5 * i for i in range(1,len(p))]
# print(o)

# name = "Akshai"
# years = 20
# city = "Ballari"
# job = "CSE Student"
# college = "BITM"
# detail = "I'm {}, ".format(name) + "I'm {} years old".format(years) + ", i stay in {}".format(city) + " and I'm a {}".format(job) + " from {}".format(college) + " college"
# print(detail)

# text = "Once i was a great warrior"
# space = text.count("i")
# print(space)
# arr = [0,1,2,3]
# print(len(arr))

# def dog_age(age):
#     res = age*7
#     return res
# num = int(input())
# print(dog_age(num))

# # print(result)

numberes = [1,2,3,4,5,6,7,8,9]
res = [i**2 for i in numberes if i % 2 == 0]
print(res)