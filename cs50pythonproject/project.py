import re
import random

def main():
    while True:
        a,b,c,d,x = initializer()
        while True:
            print("    "+eq_print(a,b,c,d))
            if a == 1 and b == 0 and c == 0 and d == x:
                print("Equation Solved!!")
                break
            operation = input("Enter an operation to be carried out on both sides: ")
            if operation.lower() == "solve":
                soln = (d-b)/(a-c)
                print(f"    Solution: x = {x}")
                break
            elif op := re.search("^\+(\d+)$",operation) or re.search("^\-(\d+)$",operation):
                b += int(op[0])
                d += int(op[0])
            elif op := re.search("^\*([+-]*\d+)$",operation):
                if op[1] == "0":
                    print("    Please don't multiply by 0")
                    continue
                else:
                    a *= int(op[1])
                    b *= int(op[1])
                    c *= int(op[1])
                    d *= int(op[1])
            elif op := re.search("^\/([+-]*\d+)$",operation):
                if op[1] == "0":
                    print("    Please don't divide by 0")
                    continue
                elif a%int(op[1]) != 0 or b%int(op[1]) != 0 or c%int(op[1]) != 0 or d%int(op[1]) != 0:
                    print("   This division wil create fractions which are not currently supported. Please try something else. All given equations have integer solutions.")
                    continue
                else:
                    a = a//int(op[1])
                    b = b//int(op[1])
                    c = c//int(op[1])
                    d = d//int(op[1])
            elif op := re.search("^\+(\d+)x$",operation) or re.search("^\-(\d+)x$",operation):
                a += int(op[0].replace('x',''))
                c += int(op[0].replace('x',''))
            elif op := re.search("\/(\d+)x$",operation) or re.search("\*(\d+)x$",operation):
                print("    Multiplication and division are only supported with constants")
                continue
            else:
                print("    Operation not recognised")
        more = input("Solve another equation? ")
        if more.lower() in ['y', 'yes', 'yep','yeah']:
            continue
        else:
            break
        



# Takes the 4 coefficients and prints out a neatly formatted equation
def eq_print(a,b,c,d):
    out_arr = ["","",""," = ","","",""]
    # Initialize Coeffecients and signs
    out_arr[0] = str(a)+"x"
    out_arr[1] = sign_of(b)
    out_arr[2] = str(abs(b))
    out_arr[4] = str(c)+"x"
    out_arr[5] = sign_of(d)
    out_arr[6] = str(abs(d))

    for i in range (len(out_arr)):
        if num := re.search("(\d+)",out_arr[i]): # Make sure to only process digits
            # Handle zero and one case for x term
            if num[0] == "0":
                out_arr[i] = ""
                if i in [0,4]:
                    out_arr[i+1] = out_arr[i+1].replace("+","")
            if num[0] == "1" and i in [0, 4]:
                out_arr[i] = "x"

    # Handle the case where an entire side of the equation is empty
    if out_arr[0]+out_arr[1]+out_arr[2] == "":
        out_arr[1] = "0"
    if out_arr[4]+out_arr[5]+out_arr[6] == "":
        out_arr[5] = "0"

    return "".join(out_arr)

# returns + if x is positive, - if negative and empty string if 0
def sign_of(x):
    if x > 0:
        return " + "
    elif x < 0:
        return " - "
    else:
        return ""

def initializer():
    # Initialise equation with random coeffecients with last coefficient being a placeholder to accomodate desired value of x
    x = random.randint(-15,15)
    a = random.randint(-12,12)
    b = random.randint(-10,10)
    c = random.randint(-12,12)
    d = "d"
    # making sure the coefficients of x on both sides are different so the equation remains solvable
    while a == c:
        a = random.randint(-12,12)
        c = random.randint(-12,12)
    d = a*x - c*x + b
    return (a,b,c,d,x)

if __name__ == '__main__':
    main()