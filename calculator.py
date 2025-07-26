class calculator:
    def __init__(self,x,y):
        self.x = x
        self.y = y
    def addition(self):
        print("Result = ",self.x+self.y)
    def subtraction(self):
        print("Result = ",self.x-self.y)
    def multiplication(self):
        print("Result = ",self.x*self.y)
    def division(self):
        if self.y != 0:
            print("Result =", self.x / self.y)
        else:
            print("Error: Division by zero is not allowed.")
    def remainder(self):
        if self.y != 0:
            print("Result =", self.x % self.y)
        else:
            print("Error: Division by zero is not allowed.")

def main():
    while True:
        try:
            x = int(input("Enter the first no = "))
            y = int(input("Enter the second no = "))
            while True:
                print('Enter\n "1" for addition\n "2" for subtraction\n "3" for division\n "4" for multiply\n "5" for remainder')
                c = int(input("Enter the operation = "))
                if c in [1, 2, 3, 4, 5]:
                    break
                else:
                    print("Invalid operation. Please enter a number between 1 and 5.")           
            e = calculator(x,y)
            if c == 1:
                e.addition()
            elif c == 2:
                e.subtraction()
            elif c == 3:
                e.division()
            elif c == 4:
                e.multiplication()
            elif c == 5:
                e.remainder()
            else :
                print("Enter a valid operation")
        except ValueError:
            print("Invalid Input! please enter valid input")
        again = input("Do you want to perform another calculation? (yes/no): ").strip().lower()
        if again != "yes":
            print("Thank you for using the calculator!")
            break

main()
