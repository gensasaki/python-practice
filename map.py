# map

def triple(n):
    return n * 3

print(list(map(triple, [1, 2, 3])))

num_arr = [2, 3, 4]
print(list(map(triple, num_arr)))
print(num_arr)

# lambda args: process
print(list(map(lambda n: n * 3, [1, 2, 3])))
