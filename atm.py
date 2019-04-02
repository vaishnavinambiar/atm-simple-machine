  ''' Program to make an ATM machiene'''
import sys         
pin = 1234                                             #card holder's pin number
balance = 50000                                        #card holder's bank balance
raw_input("Welcome to ABC Atm")

def pin_number(pin):
  """ To verify the pin """                            #To verify the pin number is card holder's pin number
    if pin == '1234':
        return True
    else:
        return False

def getPin():
  """To get the pin from the card holder and to check whether the pin is valid or not""" 
    trial = 0
    while trial < 4:                                   #Pin entry only 4 times
        pin = input('Please Enter Your 4 Digit Pin: ')
        if pin_number(pin):
            print("Pin accepted!")
            return True
        else:
            print("Invalid pin")
            trial += 1                                 #Pin entry more then given time blocks the log in
    print("To many incorrect tries. Could not log in")
    return False

def getOption():
  """To correct option from the card holder to do the specific action"""
    getPin()
    print("1: Current Balance")
    print("2: Withdraw")
    print("3: Reset pin")
    print("4: Quit")
    select = int(input("What options do you want to select?")) #options for actions to do
    if select == 1:                                            #action for current balance
        print ("Your current balance is ", balance)

    elif select == 2:                                          #action for withdraw
        withdraw = int(input("Enter the amount to withdraw: "))
        if withdraw > balance:
            print("Cannot withdraw more than available balance")
        else:
            available_balance = balance - withdraw
            print ("balance is",available_balance)
            print_out= raw_input("Do you want receipt?")
            if print_out == str('y'):
                print withdraw
                print available_balance
                print "Thankyou,See you soon!"
    elif select == 3:                                           #action for changing pin number
        confirm_pin = int(input("Enter the old pin"))
        change_pin = int(input("Enter the new 4 digit pin"))
        print ("Your pin has changed successfully")
        
    elif select == 4:                                           #action for quit
        return "Thanks"
    

def getContinued():
  """To continue the the transaction  once if card holder wishes"""
    another_transaction = raw_input("Do you want to continue the transaction?")
    if another_transaction == str('y'):                        #confirming whether continuation needed or not
        getOptions()
    else:
        sys.exit("Ok, Thanks!")
    
if __name__ == "__main__":                                      #main function
    pin_number(pin) 
    getPin()
    print getOption()
    print getContinued()
