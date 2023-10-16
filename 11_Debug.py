import random as r

def randomNumber(upper):
    num = r.randint(1, upper)
    return num

def main():
    repeat=True
    num1 = randomNumber(5)
    num2 = randomNumber(5)
    output = num1 + num2

    while repeat:
        ans = input("Enter the sum of " + str(num1) + "+" + str(num2) + ":")

        if ans.isdigit():
            if int(ans) == output:
                print("You Have entered correct Answer. Congrats!")
                repeat = False
            else:
                print("You have entered incorrect answer. Please try again !")
        else:
            print("Only Positive Numbers are accepted. Try Again ...")

if __name__ == '__main__' :
    main()