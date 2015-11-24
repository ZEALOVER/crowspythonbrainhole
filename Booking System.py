tkt_bk = 1
#Print current time
ticket_book = 1
ticket_booked = 0
print "====================================WELCOME=====================================\n"

#IMPORT & LISTS
import time
print time.strftime("%Y-%m-%d %H:%M:%S")
hour = time.strftime("%H")
name=["David" , "Clark"]
passport_no=["3689" , "8507"]
destination=[]
date=[]
travel_opt=[]
verify_code=["A", "B", "C","D","E","F","G", "H", "I","J","K","L","M", "N", "O","P","Q","R","S", "T", "U","V","W","X", "Y", "Z", "1", "2", "3", "4", "5", "6" "7", "8", "9", "0"]
passengers=[]
credit=[150000, 5000]
card_no = [123456789,987654321]
security = [1234,1234]
import random
import calendar
number_pass_add = 0
time_wait = random.randrange(2,8)
ticket_book = 1
today_date_str = time.strftime("%d")
today_day_int = int(today_date_str)
today_month = time.strftime("%m")
today_month_int = int(today_month)



#VERIFY CODE
for random_times in range (6):
    verify1 = verify_code[random.randrange(35)]
    verify3 = verify_code[random.randrange(35)]
    verify2 = verify_code[random.randrange(35)]
    verify = verify1+verify2+verify3
    verify4 = verify_code[random.randrange(35)]
    verify6 = verify_code[random.randrange(35)]
    verify5 = verify_code[random.randrange(35)]
    verify_new = verify4+verify6+verify5
    break








#LOGIN
for tkt_bk in range (tkt_bk):
    #Login & Register
    name_user = raw_input("Please Enter Your Name. \n")
    trys = 1
    for trys in range (trys):
        if name_user in name:#To see if the input is in the list
            print "Hello", name_user , "!"
            #Here goes password authentication
            pass_index = name.index(name_user)
            pass_correct = passport_no[pass_index]
            pass_user = raw_input ("Please input your password ")
            print verify
            verify_user = raw_input ("Please Input your Verification Code (All Capital)\n")


            if pass_user == pass_correct and verify_user == verify:
                print "Login Suscessful!"
                break
            
            else:
                print "Password Incorrect or Verification Code Incorrect. Please try again!"
                pass_user = raw_input ("Please re-input your password")
                trys = trys+1
                
                print verify_new
                verify_user = raw_input ("Please Input your Verification Code (All Capital)\n")
            if pass_user == pass_correct and verify_user == verify_new:
                print "Login Suscessful!"
                break
            else:
                print "Password Incorrect. Your will be automatically exited. Bye."
                exit()





#REGISTER
    else:
        print "Sorry, we do not have you on record. Would you like to register?\n"
        register_stat = raw_input ("Y / N \n")

        if register_stat == "Y":
            name.append (name_user)
            pass_regist = raw_input ("\nPlease type in your new password\n")
            security_code = raw_input ("Please enter your four-digit security code. \nThis is EXTREMELY IMPORTANT\n")
            if int(security_code) - 1000 < 0 or security_code.isalpha() or int(security_code) > 9999:
                print "This is not a four digit code. Please Enter again."
                security_code = raw_input ("Please enter your four-digit security code. \nThis is EXTREMELY IMPORTANT\n")
            else:
                security.append(security_code)
            passport_no.append(pass_regist)
            if pass_regist in passport_no:
                 print "Registeration Suscessful!"
                 break
            else:
                print "Regist Unsuscessful! Please Try Again"

        elif register_stat == "N" or "n":
            print "Did You Entered the wrong username: \n "
            print "[1]Yes. \n"
            print "[2]No.\n"
            forgot_stat = input ("Please enter: ")
            if forgot_stat == 1:
                name_user = raw_input("Please Enter Your Name. \n")
                if name_user in name:#To see if the input is in the list
                    print "Hello", name_user , "!"
                    #Here goes password authentication
                    pass_index = name.index(name_user)
                    pass_correct = passport_no[pass_index]
                    pass_user = raw_input ("Please input your password ")
                    print verify
                    verify_user = raw_input ("Please Input your Verification Code (All Capital)\n")


                    if pass_user == pass_correct and verify_user == verify:
                        print "Login Suscessful!"
                        break
                    
                    else:
                        print "Password Incorrect or Verification Code Incorrect. Please try again!"
                        pass_user = raw_input ("Please re-input your password")
                        trys = trys+1
                        
                        print verify_new
                        verify_user = raw_input ("Please Input your Verification Code (All Capital)\n")
                    if pass_user == pass_correct and verify_user == verify_new:
                        print "Login Suscessful!"
                        break
                    else:
                        print "Password Incorrect. Your will be automatically exited. Bye."
                        exit()
        else:
            break
            exit()
 







while ticket_booked in range (ticket_book):
    ticket_book = raw_input ("How many tickets do you want to book?\n")
    a = 0
    while a < 3:
        if ticket_book.isalpha():
            print "This is not a valid input. Pls Try Again"
            ticket_book = raw_input ("How many tickets do you want to book?\n")
            a = a+1
        else:
            break
    ticket_book = int(ticket_book)
    ticket_price = 0
    destination_set = raw_input ("\n\nPlease Enter your destination city! \n")
    destination.append (destination_set)
    travel_opt_set = raw_input("How would you like to get there? \n By Plane / Train / Car? \n")
    travel_opt.append (travel_opt_set)
    if travel_opt == "Plane" or "plane":
        ticket_price = random.randrange (500, 1000)
    elif travel_opt == "Train" or "train":
        ticket_price = random.randrange (100, 500)
    elif travel_opt == "Car" or "car":
        ticket_price = random.randrange (10, 100)
    else:
        print "Sorry, Invalid Input. Please try again."
        travel_opt_set = raw_input("How would you like to get there? \n By Plane / Train / Car? \n")
    departure_month = input ("\nAt Which Month would you like to depart? \nPlease Enter like 02\n")
    if departure_month < today_month_int:
        print "Are you a silly B? You cannot book ticket before today!"
        departure_month = input ("\nAt Which Month would you like to depart? \nPlease Enter like 02\n")
    departure_year = input ("\nPlease input your departure year like 2015\n")
    if departure_year < 2015:
        print "Are you a silly B? You cannot book ticket before today!"
        departure_year = input ("\nPlease input your departure year like 2015\n")
    departure_cal = calendar.month(departure_year, departure_month)
    print departure_cal
    departure_date = input ("\nHere's the calendar. Please pick a departure date.\n")
    if departure_date < today_day_int:
        print "Are you a silly B? You cannot book ticket before today!"
        print departure_cal
        departure_date = input ("\nHere's the calendar. Please pick a departure date.\n")

    add_pass = raw_input ("Would you like to add other passengers?\nPlease enter [1]Yes / [2]No\n")
    if add_pass ==  "1":
        for ticket_book in range (ticket_book):
            new_pass = raw_input ("Please, enter the name of the passenger")
            passengers.append(new_pass)
            print "Thank You, Mr. / Mrs. ", name_user, ". We are trying to get you a ticket. This may take a while."

            time.sleep(time_wait)

            ticket_number = random.randrange (1038478594, 3849385879)
            print "\n"
            print "\n"
            print "T H A N K  Y O U \n"
            print "YOUR ORDER IS SUSCESSFULLY PROCESSED. \n"
            print "Name: Mr. / Mrs. ", name_user, "\n"
            print "Ticket Number:", ticket_number
            print "Destination: ", destination_set, "\n"
            print "Method: ", travel_opt_set, "\n"
            print "Other Passengers:",passengers
            print "Price Before Tax:" ,ticket_price, "\n"
            print "Tax is 10 Percent. \n"
            print "GRAND TOTAL   ", ticket_price*1.1, "\n"
            time.sleep(2)
            print "ON YOUR CELL PHONE:"
            print "\n"
            print "Your card",card, "Had been charged",ticket_price,"."
            ticket_booked = ticket_booked + 1


    elif add_pass == "2":
        card = raw_input ("Please enter your credit card number:\n")
        print "Thank You, Mr. / Mrs. ", name_user, ". We are trying to get you a ticket. This may take a while."

        time.sleep(time_wait)

        ticket_number = random.randrange (1038478594, 3849385879)
        print "\n"
        print "\n"
        print "T H A N K  Y O U \n"
        print "YOUR ORDER IS SUSCESSFULLY PROCESSED. \n"
        print "Name: Mr. / Mrs. ", name_user, "\n"
        print "Ticket Number:", ticket_number
        print "Destination: ", destination_set, "\n"
        print "Method: ", travel_opt_set, "\n"
        print "Price Before Tax:" ,ticket_price, "\n"
        print "Tax is 10 Percent. \n"
        print "GRAND TOTAL   ", ticket_price*1.1, "\n"
        time.sleep(2)
        print "ON YOUR CELL PHONE:"
        print "\n"
        print "Your card",card, "Had been charged",ticket_price,"."
        ticket_booked = ticket_booked + 1

    
    else:
        for i in range (2):
            print "Wrong input. Pls try again"
            add_pass = raw_input ("Would you like to add other passengers?\nPlease enter [1]Yes / [2]No\n")
            if add_pass ==  "1":
                for ticket_book in range (ticket_book):
                    new_pass = raw_input ("Please, enter the name of the passenger")
                    passengers.append(new_pass)
                    print "Thank You, Mr. / Mrs. ", name_user, ". We are trying to get you a ticket. This may take a while."

                    time.sleep(time_wait)

                    ticket_number = random.randrange (1038478594, 3849385879)
                    print "\n"
                    print "\n"
                    print "T H A N K  Y O U \n"
                    print "YOUR ORDER IS SUSCESSFULLY PROCESSED. \n"
                    print "Name: Mr. / Mrs. ", name_user, "\n"
                    print "Ticket Number:", ticket_number
                    print "Destination: ", destination_set, "\n"
                    print "Method: ", travel_opt_set, "\n"
                    print "Other Passengers:",passengers
                    print "Price Before Tax:" ,ticket_price, "\n"
                    print "Tax is 10 Percent. \n"
                    print "GRAND TOTAL   ", ticket_price*1.1, "\n"
                    time.sleep(2)
                    print "ON YOUR CELL PHONE:"
                    print "\n"
                    print "Your card",card, "Had been charged",ticket_price,"."
                    ticket_booked = ticket_booked + 1


            elif add_pass == "2":
                card = raw_input ("Please enter your credit card number:\n")
                print "Thank You, Mr. / Mrs. ", name_user, ". We are trying to get you a ticket. This may take a while."

                time.sleep(time_wait)

                ticket_number = random.randrange (1038478594, 3849385879)
                print "\n"
                print "\n"
                print "T H A N K  Y O U \n"
                print "YOUR ORDER IS SUSCESSFULLY PROCESSED. \n"
                print "Name: Mr. / Mrs. ", name_user, "\n"
                print "Ticket Number:", ticket_number
                print "Destination: ", destination_set, "\n"
                print "Method: ", travel_opt_set, "\n"
                print "Price Before Tax:" ,ticket_price, "\n"
                print "Tax is 10 Percent. \n"
                print "GRAND TOTAL   ", ticket_price*1.1, "\n"
                time.sleep(2)
                print "ON YOUR CELL PHONE:"
                print "\n"
                print "Your card",card, "Had been charged",ticket_price,"."
                ticket_booked = ticket_booked + 1
        
    print "THANK YOU FOR BOOKING WITH PYTHON HOLIDAY HOLDINGS. \nWISH YOU HAVE A PLEASENT HOLIDAY."    
        
    



    continue_stat = input ("\n\nWould you like to make another booking? \n[1]Yes\n[2]No\n\nPlease make a choice: ")
    if continue_stat == 1:
        print "Okay, redirecting......"
        time.sleep(2)
        print "\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n"
        continue
        
    else:
        print "Thank you for travelling with us. Wish you a pleasent day."
        time.sleep(2)
        exit()
