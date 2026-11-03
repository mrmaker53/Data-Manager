import json
# printing

def printing(database, username):
        print("\n--- Review Successfully Saved! ---")
        print("👤 Username:", database[username]["username"])
        print("📞 Phone   :", database[username]["phone"])
        print("📧 Email   :", database[username]["email"])
        print("📝 Review  :", database[username]["review"])
        print("⭐ Rating  :", database[username]["rating"], "/5")
# printing end 
print("-----Initialising Code-----")
print("Are u a Staff or Consumer")
code = 5683
operator = int(input("For Staff enter '0' \nFor consumer enter '1'\n:--"))
# staff
if(operator == 0):
    code_check = int(input("Confirm the Code:-- "))
    if(code == code_check):
        username = input("Enter the Username u wanna search\n:-----")
        found = False
        with open("database.txt", "r") as file:
            for line in file:
                userdata = json.loads(line)
                if username in userdata:
                    printing(userdata,username)
                    found = True
                    changes = int(input("Do U wanna Alter the Input\n if Yes enter 0 \nelse enter anything\n:-----"))
                    if(changes == 0):
                        print("for changing Username enter 1\nfor changing Phone-No enter 2\nfor changing Email enter 3\nfor changing Review enter 4\nfor changing Rating enter 5\n")
                        choice = int(input(":-----"))
                        val = None
                        if(choice == 1):
                            val = input("Enter the new Username\n:-----")
                            userdata[username]["username"] = val
                            userdata[val] = userdata.pop(username)  # Renames the main tracking key
                            username = val
                        elif(choice == 2):
                            val = int(input("Enter the new Phone-NO\n:-----"))
                            userdata[username]["phone"] = val
                        elif(choice == 3):
                            val = input("Enter the new Email\n:-----")
                            userdata[username]["email"] = val
                        elif(choice == 4):
                            val = input("Enter the new Review\n:-----")
                            userdata[username]["review"] = val
                        elif(choice == 5):
                            val = int(input("Enter the new Rating\n:-----"))
                            userdata[username]["rating"] = val
                        with open("database.txt", "r") as f:
                            file_data = f.read()
                        new_line = json.dumps(userdata) + "\n"
                        updated_data = file_data.replace(line, new_line)
                        with open("database.txt", "w") as f:
                            f.write(updated_data)           
                        print(" Old data deleted and fresh changes saved successfully!")
                        printing(userdata, username)
                    else:
                        print("Thanks For ur Services")
                    break
        if not found:
            print("Username doesnt exist staff")     

    else:
        print("something went wrong...")
# consumer
elif(operator == 1):
    task = int(input("Do u Wanna Check a Existing Data or Create a new Review\nFor Checking Enter '0'\nFor Creating New Data Enter '1'\n:----"))
    if(task == 0):
        username = input("Enter the Username\n:-----")
        found = False
        with open("database.txt", "r") as file:
            for line in file:
                userdata = json.loads(line)
                if username in userdata:
                    printing(userdata,username)
                    found = True
                    break
        if not found:
            print("Username doesnt exist but we would Love to help u create one")     
    elif(task == 1):
        username = input("Enter your Username\n:-----")
        phone_no = int(input("Enter the Phone Number\n:-----"))
        email = input("Enter your Email Id\n:-----")
        review = input("Write Your feedback\n:-----")
        star = int(input("How much would u rate it out of 5\n:-----"))
        database = {}
        database[username] = {
            "username": username,
            "phone": phone_no,
            "email": email,
            "review": review,
            "rating": star
            }
        with open("database.txt", "a") as file:
            file.write(json.dumps(database) + "\n")
        printing(database, username)
    else:
        print("somethin went wrong")
else:
    print("Somethin went wrong....")