#Python lessons 3b by Jason

#MIT License

#Copyright (c) [2020] [Jason]
#Permission is hereby granted, free of charge, to any person obtaining a copy
#of this software and associated documentation files (the "Software"), to deal
#in the Software without restriction, including without limitation the rights
#to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
#copies of the Software, and to permit persons to whom the Software is
#furnished to do so, subject to the following conditions:

#The above copyright notice and this permission notice shall be included in all
#copies or substantial portions of the Software.

#THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
#IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
#FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
#AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
#LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
#OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
#SOFTWARE.

from random import shuffle

def x(score):
    """Check score and give user feedback"""
   

    if score in range(0,5):
        a = "poor"
    elif score in range(5,11):
        a = "good"
    else:
        a = "excellent"
    return a

def main():
    print("*** Power of 3 Table Practice ***")

    name = input ("What is your name? ")
    
    
    xd = input("Are You Ready? (y/n)\n")
    if xd == 'n':
        return
    elif xd == 'y':
             score = doTest(xd)
             print("{}, {}".format(x(score), name))
             print("You scored {} out of 15".format(score))
    
        

def doTest(n):
    """Runs a test. returns score."""
    
    score = 0
    l = list(range(1,16))
    for i in l:
        if input("what is {} to the power of 3? ".format(i)) == str(i**3):
            score += 1
            print("Correct.")
        else:
            print("Wrong, the correct answer is {}".format(i**3))
    return score

if __name__ == "__main__":
    main()
    

    
