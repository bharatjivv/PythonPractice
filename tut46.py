import sklearn

def printhar(string):
    return f"Give it to me now {string}"

def add(num1, num2):
    return num1 + num2 + 5

print("and the name is ", __name__)

if __name__ == '__main__':
    print(printhar("example"))
    o = add(4, 6)
    print(o)