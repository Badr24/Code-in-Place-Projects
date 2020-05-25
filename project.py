


""""
This program is a blood group test, the program first will ask to register  an account with username and blood type
then it will store it in a dictionary as key and value. 
The next the program will store the accounts in csv file in append mode to make sure not to overwrite the file
following the program will show a the result of the  blood compatibilities with a donor and recipient types 

"""
NAMELENGTH = 14
CANVAS_WIDTH = 800
CANVAS_HEIGHT = 600
CONTROL_TYPES = ['A+', 'A-', 'B+', 'B-', 'O+', 'O-', 'AB+', 'AB-']
def main():
    print("--- Welcome to Blood Types Compatibilities Program --- \n This program shows your blood type Compatibilities"  )
    accounts = create_account()
    store_accounts(accounts)
    blood_result(accounts)


def create_account():
    """
    input: the user will input username
    output: the register_users dictionary will updated
    """
    # create empty list
    registered_users = {}
    # prompt user to enter his account information username and password
    register_open = True
    while register_open:
        # user enter username and check if the blood_types minimum is 2 ch and whithin given range
       username = enter_user(NAMELENGTH)
       print("\n")

       # user enter blood_type and check if the blood_type minimum is 2 ch
       blood_type = enter_blood_type()

       # check if confirmed_password match password
       confirm_blood_type = input("please confirm your blood type: ")
       while blood_type != confirm_blood_type :
           print(" your confirmed  blood type does not match your blood_type")
           confirm_blood_type = input("please confirm your blood type: ")

       # stores responses in the dictionary
       registered_users[username] = blood_type

       # ask user if he want to register another account
       repeat = input("\n Hit any key to register another name or hit no to proceed: ")
       if repeat == "no":
           register_open = False

    # counts will show how many usres regigsterd
    count = count_users(registered_users)
    print("\n --- the total registered users are " + str(count) + " ---")


    return registered_users


def enter_blood_type():
    print("Please enter your blood type \n Blood type should be one of the following blood types :" + "\n" + str(CONTROL_TYPES))
    blood_type = input(" Enter  Blood type: ")
    # check if the blood type  within given types

    while not in_control (blood_type):
        print("your blood type is not valid, it  should be one of the following blood types :" + "\n" + str(CONTROL_TYPES))
        blood_type = input("please  re-enter valid  blood type : ")
    return blood_type

def enter_user(length):
    print("your name should be not more than " + str(NAMELENGTH)+ " characters")
    username = input("Enter your name: ")
    # check if the username minimum tryies is 6 ch
    count = 3
    while len(username) > length:
        print("your username should  " + str(NAMELENGTH)+ " characters ")
        username = input("please  re-enter valid  username: ")
        count += 1
        if count == 3:
            exit()

    # todo not repeated username
    return username

def count_users(userdict):
    count = 0
    for key in userdict:
        if isinstance(userdict[key], dict):
            count += count_keys(userdict[key])
        count += 1
    return count


def store_accounts(registered_accounts):
    #create csv to store accounts and will use append mode to not overwrite the file

    with open("output_data.csv","a") as out_file:
        for key,value in registered_accounts.items():
            out_file.write(str(key) + ',' + str(value))
            out_file.write("\n")


def in_control (blood_type1):
    # loob in each element in the control list and return true if there is match
    for i in range (len(CONTROL_TYPES)):
        if blood_type1 == CONTROL_TYPES[i]:
            return True


def blood_result(accounts):
    for key, value in accounts.items():
        # loop over the dictionary to get the result , each type separatley
        if value == CONTROL_TYPES[0]: #A+
            intro = ("hi " + str(key) + ", your blood type is " + str(value) +".")
            # According to the Stanford School of Medicine, in the United States:
            info = "People with the blood type A+ represent about 35.7% of the adult population."
            donator = " you can donate to A+ AB+"
            recipient = " you can receive from A+ A- O+ O-"
            print(intro)
            print(info)
            print(donator)
            print(recipient)
            print("Thank you!")
            print("\n")

        if value == CONTROL_TYPES[1]: #A-
            intro = ("hi " + str(key) + ", your blood type is " + str(value) +".")
            # According to the Stanford School of Medicine, in the United States:
            info = "People with the blood type A- represent about 6.3% of the adult population."
            donator = " you can donate to A+ A- AB+ AB-"
            recipient = " you can receive from A- O-"
            print(intro)
            print(info)
            print(donator)
            print(recipient)
            print("Thank you!")
            print("\n")



        if value == CONTROL_TYPES[2]: #B+
            intro = ("hi " + str(key) + ", your blood type is " + str(value) +".")
            # According to the Stanford School of Medicine, in the United States:
            info = "People with the blood type B+ represent about 8.5% of the adult population."
            donator = " you can donate to B+ AB+"
            recipient = " you can receive from B+ B- O+ O-"
            print(intro)
            print(info)
            print(donator)
            print(recipient)
            print("Thank you!")
            print("\n")

        if value == CONTROL_TYPES[3]: #B-
            intro = ("hi " + str(key) + ", your blood type is " + str(value) +".")
            # According to the Stanford School of Medicine, in the United States:
            info = "People with the blood type B- represent about 1.5% of the adult population."
            donator = " you can donate to B+ B- AB+ AB-"
            recipient = " you can receive from B- O-"
            print(intro)
            print(info)
            print(donator)
            print(recipient)
            print("Thank you!")
            print("\n")

        if value == CONTROL_TYPES[4]:  # O+
            intro = ("hi " + str(key) + ", your blood type is " + str(value) +".")
            # According to the Stanford School of Medicine, in the United States:
            info = "People with the blood type O+ represent about 37.4% of the adult population."
            donator = " you can donate to O+ A+ B+ AB+"
            recipient = " you can receive from O+ O-"
            print(intro)
            print(info)
            print(donator)
            print(recipient)
            print("Thank you!")
            print("\n")

        if value == CONTROL_TYPES[5]:  # O-
            intro = ("hi " + str(key) + ", your blood type is " + str(value) +".")
            # According to the Stanford School of Medicine, in the United States:
            info = "People with the blood type O- represent about 6.6% of the adult population."
            donator = " you can donate to Everyone"
            recipient = " you can receive from O-"
            print(intro)
            print(info)
            print(donator)
            print(recipient)
            print("Thank you!")
            print("\n")

        if value == CONTROL_TYPES[6]:  # AB+
            intro = ("hi " + str(key) + ", your blood type is " + str(value) +".")
            # According to the Stanford School of Medicine, in the United States:
            info = "People with the blood type AB+ represent about 3.4% of the adult population."
            donator = " you can donate to AB+"
            recipient = " you can receive from Everyone"
            print(intro)
            print(info)
            print(donator)
            print(recipient)
            print("Thank you!")
            print("\n")

        if value == CONTROL_TYPES[7]:  # AB-
            intro = ("hi " + str(key) + ", your blood type is " + str(value) +".")
            # According to the Stanford School of Medicine, in the United States:
            info = "People with the blood type AB- represent about 0.6% of the adult population."
            donator = " you can donate to AB+ AB-"
            recipient = " you can receive from AB- A- B- O-"
            print(intro)
            print(info)
            print(donator)
            print(recipient)
            print("Thank you!")
            print("\n")








if __name__ == '__main__':
    main()