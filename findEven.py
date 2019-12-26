def findEven(alist):

    #return the first even integer cotained in "alist"
    #   or print a message and generate an error

    try:
        for val in alist:

            if val % 2 == 0:
                return val


        raise ValueError("Enter stupid redundant error messae")

    except ValueError:
        
        print("Only odd numbers  found in this list: return -1")
        return -1

    
def main():

    print("Result: ",findEven( [3,6,7] ))       #result : 6
    print("Result: ",findEven( [3,5,7] ))       #result: error
    print("Result: ",findEven( [2,8,9,5] ))     #result" 2


main()
