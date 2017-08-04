# list and tuple
# - slice
# collection type
# dictionary type

# list
scores = [40, 50]
print(scores[0]) # 40
scores[0] = 45
print(len(scores))# 2
scores.append(100)
print(scores)

for score in scores:
    print(score)

for i, score in enumerate(scores):
    print("{0}: {1}".format(i, score))

# touple can not be reassigned
# items = (50, "apple", 32.5)
# print(items[1])
# items[1] = "pen"

print(list((1, 3, 5))) # convert touple to list
print(tuple([1, 3, 5])) # convert list to tuple

# slice
num_arr = [40, 50, 60, 70, 80, 90]
print(num_arr[1:4]) # 50, 60, 70
print(num_arr[:2]) # 40, 50
print(num_arr[3:]) # 70, 80, 90
print(num_arr[-3:]) # 70, 80, 90

s = "hello"
print(s[1:4])
<<<<<<< HEAD

# set not allow same value
# a = set([5, 6, 7, 8])
# a = {5, 6, 7, 8}
# print(a)
# print(5 in a) # True
# a.add(2)
# a.remove(5)
# print(a)
# print(len(a))

a = {1, 3, 5, 7}
b = {2, 3, 5, 8}

print(a | b)
print(a & b)
print(a - b)

# dictionary

sales = {"sasaki": 200, "tanaka": 400}
print(sales["sasaki"])
sales["sasaki"] = 300
sales["additional"] = 500
del(sales["tanaka"])
print(sales)

for key, value in sales.items():
    print("{0}: {1}".format(key, value))
