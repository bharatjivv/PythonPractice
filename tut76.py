# Else and finally in try except
f1 = open("bharat.txt")
try:
    f = open("does.txt")

except Exception as e:
    print(e)

finally:
    print("Run This anyway...")
    # f.close()
    f1.close()

print("Important Stuff")