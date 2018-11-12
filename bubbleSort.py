#Noble Thomas
# This program gets user input value of numbers and sorts the list using the bubble sort method
sample = [ ]
length=len(sample)
def getInput():
    number = eval(input("Enter a sequence of whole numbers, Enter -999 to indicate the end of the list"))
    sample.append(number)
    while number != -999:
       number= eval(input("Enter another number"))
       if number!= -999:
           sample.append(number)
    return sample
        
def bubbleSort():
    print("Intial Sample:", sample)
    length=len(sample)
    for i in range(length-1):
        for j in range(length-1-i):
            if (sample[j] > sample[j+1]):
                sample[j], sample[j+1] = sample[j+1], sample[j]
    print("Sorted list:", sample)
    
def main():
    getInput()
    bubbleSort()
