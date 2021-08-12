# f = open("bharat.txt", "w")
# a = f.write("Bharat is an extrarodinary kid\n")
# print(a)
# f.close()

# Handle Read And Write Both
f = open("bharat.txt", "r+")
print(f.read())
f.write("thank you")