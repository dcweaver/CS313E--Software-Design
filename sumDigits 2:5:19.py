def sumDigits(s):

    sum = 0

    for char in s:
        try:
            sum += int(char)
            print("I added",char,"to sum")
        except ValueError:
            print("Skipped ",char)
    return sum





def main():

    print(sumDigits("1234"))            #should print 10
    print(sumDigits("a1b2c3"))          #should print 6
    print(sumDigits("abcdefgh"))        #should print 0
    
main()
