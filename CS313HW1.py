#  File: Equations.py
#  Description: algorithm to linear and quadratic functions
#  Student's Name: David Chase Weaver
#  Student's UT EID: dcw2269
#  Course Name: CS 313E 
#  Unique Number: XXXXX
#
#  Date Created: February 6, 2019
#  Date Last Modified: February 8, 2019
class LinearEquation:

    def __init__(self,m,b):
        
        self.m = m  #slope of line
        self.b = b  #Y-intercept of line
        
    def __str__(self):
        
        slope = self.m
        intercept = self.b
        equation = "" 
        mSign = ""
        bSign = ""

        #If statements to correctly print out the equations
        
        if (slope < 0):
            mSign = "- " + str(abs(slope)) + "x" 
            #slope = abs(slope)
        elif (slope == 0):
            mSign = ""
        else:
            mSign = str(slope) + "x "

        if (intercept < 0):
            bSign = " - "+ str(abs(intercept))
        elif (intercept == 0):
            bSign = ""
        else:
            bSign = "+ " + str(intercept)

        if(slope == 0) and (intercept > 0):
            bSign = str(intercept)
            
        #return the entire concatenated linear equation
        return mSign + bSign 
        

    def evaluate(self, x):
        
        #function to evaluate a linear equation at a given x-value
        return (self.m * x + self.b)
    
    def __add__(self, otherLE):

        #function to add two linear equations together and return their sum
        added = LinearEquation(self.m + otherLE.m, self.b + otherLE.b)
        return added

    def __sub__(self, otherLE):
        #function to subtract two linear equations together and return their difference
        subtracted = LinearEquation(self.m - otherLE.m,self.b - otherLE.b)
        return subtracted

    def __mul__(self, otherLE):
        #Function to multiply two linear equations together and return their product, which will be a quatratic
        mul = QuadraticEquation(self.m*otherLE.m, (self.m*otherLE.b) + (self.b*otherLE.m), self.b*otherLE.b)
        return mul
                                
        
    def compose(self, otherLE):
        
        compose1 = self.m * otherLE.m
        compose2 = (self.m * otherLE.b) + self.b
        return LinearEquation(compose1,compose2)

class QuadraticEquation:

    def __init__(self,a,b,c):
        self.a = a
        self.b = b
        self.c = c

    def __str__(self):
        
        #Creating variables for the coefficients and intercept in a quadratic equation

        
        coefA = self.a
        coefB = self.b
        intercept = self.c
        aSign = ""
        bSign = ""
        cSign = ""

        #if statements to account for every sign of the coeffients

        if(coefA == -1):
            aSign = "- "
            coefA = ""
            
        elif (coefA < 0):
            aSign = "-"
            coefA = abs(coefA)
            
        #Addressing if the coefficient is 1  
        elif(coefA == 1):
            coefA = ""

        else:
            aSign = ""

        if(coefB < 0):
            bSign = " - " + str(abs(coefB)) + "x"
            
        elif (coefB == 1):
            coefB = "x"
            bSign = " + " + str(coefB)
        elif (coefB == 0):
            coefB = " + "
        else:
            bSign = " + " + str(coefB)+ "x"

        if(intercept < 0):
            cSign = " - "
            intercept = abs(intercept)
        else:
            cSign = " + "

        #printing the concatenated quadratic equation
        outString = aSign + str(coefA) + "x\u00B2" + bSign + cSign + str(intercept)  
        return outString
        

    def evaluate(self, x):
        return (self.a * (x**2) + self.b * x + self.c)

    def __add__(self, otherQE):

        added = QuadraticEquation(self.a + otherQE.a, self.b + otherQE.b, self.c + otherQE.c)
        return added
    
    def __sub__(self, otherQE):

        subtracted = QuadraticEquation(self.a - otherQE.a, self.b - otherQE.b, self.c - otherQE.c)
        return subtracted




def main():

   f = LinearEquation(5,3)
   print("f(x) =",f)
   print("f(3) =",f.evaluate(3),"\n")
         
   g = LinearEquation(-2,-6)
   print("g(x) =",g)
   print("g(-2) =",g.evaluate(-2),"\n")

   h = f + g
   print("h(x) = f(x) + g(x) =",h)
   print("h(-4) =",h.evaluate(-4),"\n")

   j = f - g
   print("j(x) = f(x) - g(x) =",j)
   print("j(-4) =",j.evaluate(-4),"\n")

   k = f.compose(g)
   print("k(x) = f(g(x)) =",k,"\n")
   
   m = g.compose(f)
   print("m(x) = g(f(x)) =",m,"\n")

   n = f * g
   print("n(x) = f(x) * g(x) =",n,"\n")

   g = LinearEquation(5,-3)
   print("g(x) =",g)
   print("g(-2) =",g.evaluate(-2),"\n")
   
   h = f + g
   print("h(x) = f(x) + g(x) =",h)
   print("h(-4) =",h.evaluate(-4),"\n")

   j = f - g
   print("j(x) = f(x) - g(x) =",j)
   print("j(-4) =",j.evaluate(-4),"\n")
   
   p = QuadraticEquation(1,1,-6)
   print("p(x) =",p)
   print("p(3) =",g.evaluate(3),"\n")
   
   q = QuadraticEquation(2,1,4)
   print("q(x) =",q)
   print("q(-3) =",q.evaluate(-3),"\n")
   
   r = p + q
   print("r(x) = p(x) + q(x) =",r)
   print("r(-2) =",r.evaluate(-2),"\n")

   s = p - q
   print("s(x) = p(x) - q(x) =",s)
   print("s(1) =",s.evaluate(1),"\n")
   
main()

