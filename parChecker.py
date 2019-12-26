class Stack:

    def __init__(self):
        self.items = [ ]

    def push(self,item):
        self.items.append(item)

    def pop(self):
        return self.items.pop()

    def peek(self):
        return self.items[-1]
    
    def isEmpty(self):
        return self.items == []

    def size(self):
        return len(self.__items)



def parChecker(symbolString):

    s = Stack()
    balanced = True
    index = 0

    while index < len(symbolString) and balanced:

        symbol = symbolString[index]

        if symbol in "([{":
            s.push(symbol)
        else:
            #it's a right side, and it had better match the top of the stack!
            if s.isEmpty():
                balanced = False
            else:
                top = s.pop()
                if not matches(top,symbol):
                    balanced = False
                
        index += 1 
    if balanced:
        return True
    else:
        return False


def matches(openP, closeP):
    opens = "([{"
    closes = ")}]"
    return opens.index(openP) == closes.index(closeP)




def main():

    example1 = "()[ () ]"
    print(example1, ":", parChecker(example1))
    example2 = "([]) ({})"
    print(example2, ":", parChecker(example2))


main()
