import math
import datetime

history = []       # List to store the history of calculations

def home_page():
    while True :
        print("\n== Home Page ==")
        print("\nChoose the Operations..")
        print("1. CALCULATOR")
        print("2. Expression Evaluator")
        print("3. History")
        print("4. EXIT")

        try :
            choice = int(input("\nEnter Operation no.:"))
            
            if choice == 1:
                calculator()
            elif choice == 2:
                expression_solver()
            elif choice == 3:
                show_history()
            elif choice == 4:
                print("\nEXITING...!")
                break 
            else:
                print("\nError : Invalid Input !!")
                print("\nEnter Valid Operation no. !!")
        except Exception as e:
            print(f"\nUnexpected Error : {e}")

def now():
    return datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")

def calculator():

    print("\n==Calculator==")
    print("\nSelect the Operation")
    print("1. Addition             (+)")
    print("2. Subtraction          (-)")
    print("3. Multiplication       (*)")
    print("4. Division             (/)")
    print("5. Modulus/Remainder (a % of b)")
    print("6. Exponentiation       (**)")
    print("7. Floor Division       (//)")
    print("8. Percentage           (%)")
    print("9. Square Root          (√)")
    print("10. Cube Root           (∛)")
    print("0. Back to home page")

    while True :
        try :
            p = int(input("\nEnter your Operation : "))

            if p == 0:
                print("\nReturning to Home Page...")
                return

            if p in [1,2,3,4,5,6,7,8]:
                a = float(input("Enter 1st no. ="))
                b = float(input("Enter 2nd no. = "))

                if p == 1:
                    print(f"Addition : {a} + {b} = ", a+b)
                    history.append(f"[{now()}]{a} + {b} = {a+b}")
                    again = input("\nCalculate again? (y/n): ")
                    if again.lower() == 'n':
                        return
                elif p == 2:
                    print(f"Subtraction : {a} - {b} = ", a-b)
                    history.append(f"[{now()}]{a} - {b} = {a-b}")
                    again = input("\nCalculate again? (y/n): ")
                    if again.lower() == 'n':
                        return
                elif p == 3:
                    print(f"Multiplication : {a} * {b} = ", a*b)
                    history.append(f"[{now()}]{a} * {b} = {a*b}")
                    again = input("\nCalculate again? (y/n): ")
                    if again.lower() == 'n':
                        return
                elif p == 4:
                    if b != 0:
                        print(f"Division : {a} / {b} = ", a/b)
                        history.append(f"[{now()}]{a} / {b} = {a/b}")
                        again = input("\nCalculate again? (y/n): ")
                        if again.lower() == 'n':
                            return
                    else:
                        print("\nError : DivisionByZero !!")
                elif p == 5:
                    print(f"Modulus : {a} % {b} = ", a%b)
                    history.append(f"[{now()}]{a} % {b} = {a%b}")
                    again = input("\nCalculate again? (y/n): ")
                    if again.lower() == 'n':
                        return
                elif p == 6:
                    print(f"Exponentiation : {a}**{b} = ", a**b)
                    history.append(f"[{now()}]{a}**{b} = {a**b}")
                    again = input("\nCalculate again? (y/n): ")
                    if again.lower() == 'n':
                        return
                elif p == 7:
                    if b != 0:
                        print(f"Floor Division : {a} // {b} = ", a//b)
                        history.append(f"[{now()}]{a} // {b} = {a//b}")
                        again = input("\nCalculate again? (y/n): ")
                        if again.lower() == 'n':
                            return
                    else:
                        print("\nError : DivisionByZero !!")
                elif p == 8:
                    if b != 0:
                        print(f"Percentage : {a} % of {b} = ", (a/b)*100)
                        history.append(f"[{now()}]{a} % of {b} = {(a/b)*100}")
                        again = input("\nCalculate again? (y/n): ")
                        if again.lower() == 'n':
                            return
                    else:
                        print("\nError : DivisionByZero !!")
            elif p in [9,10]:
                a = float(input("Enter no. = "))
                if a < 0:
                    print("\nError : Cannot calculate root of a negative number !!")
                elif p == 9:
                    print(f"Square Root of {a} = ", a**(1/2))
                    history.append(f"[{now()}]Square Root of {a} = {a**(1/2)}")
                    again = input("\nCalculate again? (y/n): ")
                    if again.lower() == 'n':
                        return
                elif p == 10 :
                    print(f"Cube Root of {a} = ", a**(1/3))
                    history.append(f"[{now()}]Cube Root of {a} = {a**(1/3)}")
                    again = input("\nCalculate again? (y/n): ")
                    if again.lower() == 'n':
                        return
                else:
                    print("\nError : Invalid Input !!")
        
        except ValueError:
            print("\nError : Invalid Input !!")

        except Exception as x :
            print(f"\nUnexpected Error : {x}")


def expression_solver():
    print("\n== Expression Evaluator ==")
    print("\nEnter mathematical expressions to evaluate.")
    print("You can use basic operators (+ , - , * , / , ** , % , // ) ")
    print(" math functions (math.sqrt(), math.sin(), etc.).")
    print("Press Enter or 'q' to quit")
    while True:
        expr = input("\nEnter expression : ")
        if expr == "" or expr.lower() == "q":   # quick exit
            break
        try:
            result = eval(expr, {"__builtins__": None}, {"math": math})
            print("Result : ", result)
            history.append(f"[{now()}]{expr} = {result}")
        except Exception as e:
            print("Error : ", e)
        

def show_history():
    print("\n== Calculation History ==")
    if not history:
        print("\nNo calculations done yet !")
    else:
        for i, entry in enumerate(history, 1):
            print(f"  {i}. {entry}")

    input("\nPress Enter to go back...")


if __name__ == "__main__":
    home_page()            # Calling the home page function to start the program                
