#Noble Thomas
#Assignment 03/14/2017

# Create a fraction class that checks to make sure that the numerator and denominator are both 
# integers. If either is not an integer the constructor should raise an exception

class Fraction:
    #Constructor that defines the terms
    def __init__(self,top,bottom):
        #Checks to see if the value is a valid integer
        if isinstance(top, int):
            self.num= top
        else:
            print ("Top is not an integer, the program will exit")
            exit()
            
        #Checks to see if the value is a valid integer           
        if isinstance(bottom, int):
            self.den = bottom
        else:
            print ("Bottom is not an integer, the program will exit")
            exit()

        common = gcd(self.num,self.den)
        self.num = self.num//common
        self.den = self.den//common
        
    #Defintion that arranges the value into string format
    def __str__(self):
        return str(self.num)+"/"+str(self.den)

    #Definition that adds two fractions
    def __add__(self,otherfraction):
        newnum = self.num*otherfraction.den + self.den*otherfraction.num
        newden = self.den * otherfraction.den
        return Fraction(newnum,newden)
    
    #Definition that finds out if values are equal
    def __eq__(self, other):
        firstnum = self.num * other.den
        secondnum = other.num * self.den
        return firstnum == secondnum

    def getNum(self):
        return self.num

    def getDen(self):
        return self.den
#Definition that finds the greates common denominator   
def gcd(m,n):
    while m%n != 0:
        oldm = m
        oldn = n
        m = oldn
        n = oldm%oldn
    return n

#Main Function that excutes the code
def main():    
    f1=Fraction(1,3.3)
    f2=Fraction(1,2)
    f3=f1+f2
    print(f3)
    
