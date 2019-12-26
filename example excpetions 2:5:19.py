def main():

    while True:

        val = input("Enter an integer: ")

        try:
            val = int(val)
            print("The Square of the number you entered is ", val*val)
            break

        except ValueError:
            print(val, "is not an integer")


    print("Go do other stuff. . .")
main()

#Raise allows you to raise an exception
