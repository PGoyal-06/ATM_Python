class ATM(object):
    def __init__(self,number,pin):
        self.number = number
        self.pin = pin
    def BalanceEnquiry(self):
        print("Your Balance is: $100" )
        def CashWithdrawal(self,amount):
        new_amount = 100-amount
        print("You withdrawerd:" + str(amount) + "Your remaining balance is:" + str(new_amount))

def main():
    name = input("Hello, what is your name?")
    print("Hello," + name)
    number = input("Enter your card number:")
    pin = input("Enter your PIN:")
    new_user = ATM(number,pin)

    print("Choose your activity")
    print("1. Balance Enquiry")
    print("2. Cash Withdrawal")
    activity = input("Enter your choice:")

    if activity == 1:
        new_user.BalanceEnquiry()
    elif (activity == 2):
        amount = input("Enter the amount:")
        new_user.CashWithdrawal(amount)
    else:
        print("Enter a valid number")
        