chars = ['A', 'B', 'C']
fruits = ('Apple', 'Banana', 'Cherry')
info = {'name':'Mike', 'ref':'Python', 'sys':'Mac'}

print("\nElements:\t", end = "")
for item in chars:
    print(item, end = "")
print("\nEnumerated\t", end = "")
for item in enumerate(chars):
    print(item, end = "")


print("\nZipped: \t", end = "")
for item in zip(chars, fruits):
    print(item, end = "")

print("\nPaired:")
for key, value in info.items():
    print(key, "=", value)
