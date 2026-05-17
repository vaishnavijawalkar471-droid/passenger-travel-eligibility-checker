print(" PASSENGER TRAVEL CHECKER")
print("Hello! This program checks if you can travel")
name = input("what's your name? ")
print("hey " + name + "!")
print("")

try:
    age = int(input("how old are you: "))
    if age <= 0:
        raise ValueError
        print("")
except ValueError:
    print("bro, that's not even a number, lol")
    print("restart the program and enter properly")
    exit()

places_visited = input("countries you've visited before: ")
print("")

if places_visited == "":
    print("first time traveling internationally huh")
    print("no worries")
else:
    print("nice! " + places_visited)

print("")
print("ok now checking your documents")
print("")

print("SECURITY CHECK")
try:
    banned_status = input("banned from any country? yes/no: ").lower()

    if banned_status != "yes" and banned_status != "no":
        raise ValueError("dude just type yes or no")

    if banned_status == "yes":
        print("")
        print("NOT ELIGIBLE")
        print("can't travel if you're banned sorry")
        print("contact the authorities or something")
        exit()  
    else:
        print("cool no bans")
except ValueError as e:
    print("error -", e)
    exit()  

print("")

print("PASSPORT CHECK")
try:
    passport_real = input("passport is real right? not fake? yes/no: ").lower()

    if passport_real != "yes" and passport_real != "no":
        raise ValueError("come on just say yes or no")

    if passport_real == "no":
        print("")
        print("NOT ELIGIBLE")
        print("yeah you cant use fake passport")
        print("thats literally illegal")
        exit() 
    else:
        print("passport is legit")
except ValueError as e:
    print("error -", e)
    exit()  

print("")

try:
    passport_valid = int(input("passport valid for how many months: "))

    if passport_valid < 6:
        print("")
        print("NOT ELIGIBLE")
        print("passport expiring too soon")
        print("needs atleast 6 months validity")
        print("renew it before traveling")
        exit() 
    else:
        print("passport good for " + str(passport_valid) + " months")
except:
    print("enter numbers only not letters")
    exit()  

print("")

print("VISA CHECK")

try:
    visa_ok = input("got valid visa? yes/no: ").lower()

    if visa_ok != "yes" and visa_ok != "no":
        raise ValueError("please answer yes or no only")

    if visa_ok == "no":
        print("")
        print("NOT ELIGIBLE")
        print("visa is mandatory")
        print("apply for it first")
        exit()  
    else:
        print("visa is there")
except ValueError as e:
    print("error -", e)
    exit()  

print("")

try:
    visa_months = int(input("visa valid for how many months: "))

    if visa_months < 3:
        print("")
        print("NOT ELIGIBLE") 
        print("visa expiring soon")
        print("minimum 3 months needed")
        print("get it renewed")
        exit()  
    else:
        print("visa validity is " + str(visa_months) + " months")
except:
    print("type a number dude")
    exit() 

print("")

# id card
print("ID CARD CHECK")

try:
    id_valid = input("valid government ID card? yes/no: ").lower()

    if id_valid != "yes" and id_valid != "no":
        raise ValueError("yes or no thats it")

    if id_valid == "no":
        print("")
        print("NOT ELIGIBLE")  
        print("need proper ID")
        print("get it from govt office")
        exit()
    else:
        print("ID looks good")
except ValueError as e:
    print("error -", e)
    exit()

print("")

print("HEALTH CHECK")
print("checking if any health issues")
print("")

health = input("got any health problems? type none if no: ").lower()
bad_health = ["fever", "asthma", "pregnancy", "heart problem", "chicken pox"]
got_problem = False

for i in range(len(bad_health)):
    if bad_health[i] in health:
        got_problem = True

if got_problem == True:
    print("")
    print("NOT ELIGIBLE") 
    print("you have some health condition")
    print("need medical clearance certificate from doctor")
    print("get that first then you can travel")
    exit()  
else:
    if health == "none" or health == "":
        print("no health issues great")
    else:
        print("ok noted: " + health)
        print("carry your meds")

print("")

print("LAST QUESTION")

try:
    heights = input("scared of heights? yes/no: ").lower()

    if heights != "yes" and heights != "no":
        raise ValueError("seriously just yes or no")

    if heights == "yes":
        print("alright we'll not give you a window seat")
    else:
        print("ok got it")

except ValueError as e:
    print("error -", e)
    exit()  # FIX: Added exit() to stop on invalid input

print("")
print("========================================")
print("    YOU'RE ELIGIBLE TO TRAVEL!")
print("========================================")
print("")
print("congrats " + name + " all good")
print("")
print("summary of everything:")
print("-------------------") 
print("name: " + name)
print("age: " + str(age))
print("passport valid: " + str(passport_valid) + " months")
print("visa valid: " + str(visa_months) + " months")
print("countries visited: " + places_visited)
print("health: " + health)
print("fear heights: " + heights)
print("-------------------")
print("")
print("you can travel now")
print("reach airport 3 hours early btw")
print("")
print("thanks for using this")
print("safe travels!")
