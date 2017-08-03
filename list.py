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
