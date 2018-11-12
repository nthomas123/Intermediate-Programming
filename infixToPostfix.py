#Noble Thomas
#03/30/2017 Assignment
#18 Create a program that converts infix notation to postfix noration
class Stack:
    def __init__(self):
        self.items = []
    def isEmpty(self):
        return self.items == []
    def push(self, item):
        self.items.append(item)
    def pop(self):
        return self.items.pop()
    def peek(self):
        return self.items[len(self.items)-1]
    def size(self):
        return len(self.items)

def infixToPostfix(infixexpr):
    #Sets the importance of operator
    prec = {}
    prec["*"] = 3
    prec["/"] = 3
    prec["+"] = 2
    prec["-"] = 2
    prec["("] = 1
    #holds the value of operator
    opStack = Stack()
    #holds the list
    postfixList = []
    #seprate the list with spaces
    tokenList = infixexpr.split()

    
    for token in tokenList:
        #If there is a  capital or number append to list
        if token in "ABCDEFGHIJKLMNOPQRSTUVWXYZ" or token in "0123456789":
            postfixList.append(token)
        elif token == '(':
            opStack.push(token)
        elif token == ')':
            topToken = opStack.pop()
            while topToken != '(':
                postfixList.append(topToken)
                topToken = opStack.pop()
        else:
            #while the stack the stack is empty and the value of the operator on top
            #is greater than the other operator, add it to the list
            while (not opStack.isEmpty()) and \
               (prec[opStack.peek()] >= prec[token]):
                  postfixList.append(opStack.pop())
            opStack.push(token)

    while not opStack.isEmpty():
        postfixList.append(opStack.pop())
    #Adds the characters together
    return " ".join(postfixList)

def main():
    #Set Value to convert infix to postfix
    print("Infix Value: A * B * C + F")
    print("Postfix Value: ", infixToPostfix("A * B * C + F"))
    #User Input value to convert infix to postfix
    tokenList= input("Enter an Infix Value: ")
    print("Postfix value: ", infixToPostfix(tokenList))
