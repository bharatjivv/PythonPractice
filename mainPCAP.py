class Stack():
    def __init__(self):
        print("Hi")
        self.list = []

    def push(self, val):
        self.list.append(val)
    def pop(self):
        val = self.list[-1]
        del self.list[-1]
        return val
pass


class AddingStack(Stack):
    def __init__(self):
        Stack.__init__(self) # Python forces you to initialize superclass's constructor
        self.__sum = 0

pass


if __name__ =='__main__':
    stack_object = Stack()
    print(len(stack_object.list))
    
    stack_object.push(1)
    stack_object.push(2)
    stack_object.push(3)
    stack_object.push(4)
    
    print(stack_object.list)

    print(stack_object.pop())
    print(stack_object.list)
    print(stack_object.pop())
    print(stack_object.list)
    print(stack_object.pop())
    print(stack_object.list)
    print(stack_object.pop())

    print(stack_object.list)    
    
    
    
    
    