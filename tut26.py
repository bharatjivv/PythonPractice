# Reading and writing files

f = open("bharat.txt", "rt")
# r - read in text mode
# rt - also read in text mode
# rb - read in binary mode

# content = f.read(344)
# # content = f.read(3) - it will read only 3 characters
# print("1", content)
# content = f.read(344)
# print("2", content)

# for line in content:
#     print(line, end="")

# print(f.readline())
# print(f.readline())
# print(f.readline())
# print(f.readline())

print(f.readlines())

f.close()
