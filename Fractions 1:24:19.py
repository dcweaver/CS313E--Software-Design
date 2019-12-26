#define way to add fractions without using decimal numbers.

class Fraction:

    def __init__(self,top,bot):

        self.num = top
        self.den = bot

#__str__:
    #used when you want a string representation for an object of that class
    #Takes no arguments except "self"
    #Always returns strings
    #Most of the time, use this to print the object


    def __str__(self):
        return (str(self.num) + "/" + str(self.den))

    def __add__(self, other):
        newNum = (self.num* other.den) + (other.num * self.den)
        newDen = self.den * other.den
        return Fraction(newNum,newDen)
    
def main():

    twothirds = Fraction(2,3)
    threefourths = Fraction(3,4)

    #print automatically calls __str__
    print(twothirds)
    print(threefourths)

    sum = twothirds + threefourths 
    print(sum)
    

main()
