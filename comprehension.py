# comprehension

# 0 - 9
print([i for i in range(10)])
print([i * 3 for i in range(10)])
print([i * 3 for i in range(10) if i % 2 == 0])

print((i * 3 for i in range(10) if i % 2 == 0))
print(i * 3 for i in range(10) if i % 2 == 0) # generator
print({i * 3 for i in range(10) if i % 2 == 0}) # collection
