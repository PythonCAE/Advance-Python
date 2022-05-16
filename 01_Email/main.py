def email_validation(email):
    if(len(email)>=8): #Cheking if len of email is greater then 8 or not
        if email[0].isalpha(): #Checking the 1st string is alphabet or not
            if email[-4]=="." or email[-3]==".": #Checking if fourth last and third last is . or not.
                if "@" in email and email.count("@") ==1: #Checking in email if @ is present or not if present then must occur once at time.
                    if email[-3:]=="com" or email[-2:]=="in": #Checking after . that is com or in
                        for e in email: # Iterating email string in loop.
                            if  e.isspace(): #checking itered value is space or not if space print wrong email otherwise continue
                                print("Wrong email due to space in email")
                                break
                            elif e.isalpha():#checking itered value is alphabet or not
                                if e.isupper():# Checking iterated value is in upper case or not
                                    print("Wrong email due to Uppercase in email")
                                    break
                            elif e =="." or e =="_" or e =="@": #Checking iterated value is .,_and @ if yes then continue other wise print wrong email
                                continue
                            elif e.isdigit(): #Checking iterated value is digit or not
                                continue
                            else: #checking rest of all condition donot match.
                                print("Wrong Email")
                                break
                        else:
                            print("Right Email")        
                    else:
                        print("wrong email due to the 'com' and 'in' right palce")
                else:
                    print("Wrong email due to the @ problem ")
            else:
                print("Wrong email due to the . not in the correct position")    
        else:
            print("Wrong email due to first chracter isnot alphabet")  
    else:
        print("Wrong Email Due to the length problem")

while True:
    def suggation():
      print("Enter 1 for Checking email validation:") 
      print("Enter 2 for exit")
    num = int(input("Enter 1 or 2 :"))
    if num == 1:
       email = input("Enter the email:") #To enter the email string from user
       email_validation(email)
    elif num == 2:
        print("Good bye!!!")
        break
    else:
         suggation()
         




