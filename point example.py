class Point:

    def __init__(self,xCoord,yCoord):
        self.x = xCoord
        self.y = yCoord

    def __str__(self):
        outString = "(" + str(self.x) + "," + str(self.y) + ")"
        return outString
    def __eq__(self, other):
        return (self.x == other.x) and (self.y == other.y)
    #This is ~deep~ equality

def main():
    
    p4 = Point(6,6)

    p5 = p4
    print("p4 = ",p4)
    print("p5 = ",p5)

    if p4 == p5:
        print("equal")
    else:
        print("not equal")

    p6 = Point(6,6)

    if p4 == p6:
        print("equal")
    else:
        print("not equal")    

main()
