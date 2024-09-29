from cal_fun import do_addition,do_subtraction
from multiply import do_multiplication

def main():
    print("Welcome to calculator app")
    print(""" 
        Select the function from the given options:
          1. Add
          2. Subtract
          3. Multiply
        """)
    user_input=input("Select the function :")
    x=int(input("enter value for x :"))
    y=int(input('enter value for y :'))

    if user_input == "1":
        result=do_addition(x,y)
    elif user_input == "2":
        result=do_subtraction(x,y)
    elif user_input == "3":
        result=do_multiplication(x,y)
    print(result)



if __name__ == "__main__":
    main()