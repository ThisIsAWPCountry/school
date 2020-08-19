#doTest by Jason

from random import shuffle

def x(score):
    """Check score and give user feedback"""
   

    if score in range(1,6):
        a = "poor"
    elif score in range(6,11):
        a = "good"
    else:
        a = "excellent"
    return a

def main():
    print("*** Multiplication Table Practice ***")
    print("Enter 'q' to quit.")

    name = input ("What is your name? ")
    
    while 1:
        num = input("\nNumber to test (2-13): ")
        if num == 'q':
            return
        try:
            num = int(num)
            if num < 2 or num > 13:
                raise ValueError
            else:
                score = doTest(num)
                print("{}, {}".format(x(score), name))
                print("You scored {} out of 11".format(score))
        except ValueError:
            print("Please enter a number from 2 to 13.")

def doTest(n):
    """Takes a number and runs a test. returns score."""
    
    score = 0
    l = list(range(2,13))
    shuffle(l)
    for i in l:
        if input("what is {} times {}? ".format(n, i)) == str(i*n):
            score += 1
            print("Correct.")
        else:
            print("Wrong, the correct answer is {}".format(i*n))
    return score

if __name__ == "__main__":
    main()
    
