from dbhelper import DBHelper

def main():
    db = DBHelper()

    while True:
        print()
        print("***********WELCOME***********")
        print()
        print("PRESS 1 to insert new user:")
        print("PRESS 2 to display all user:")
        print("PRESS 3 to delete user:")
        print("PRESS 4 to update user:")
        print("PRESS 5 to exit the program")
        print()
        print("*****************************")
        print()

        try:
            choice = int(input())

            if choice==1:
                #insert
                uid = int(input("Enter the user Id:"))
                uname = input("Enter the user Name:")
                uphone = input("Enter the user Phone Number:")
                db.insert_user(uid,uname,uphone)

            elif choice==2:
                #display
                db.fetch_all()

            elif choice==3:
                #delete
                db.fetch_all()
                uid = int(input("Enter the user Id you want to delete:"))
                db.delete_user(uid)

            elif choice==4:
                #update
                db.fetch_all()
                uid = int(input("Enter the user Id:"))
                uname = input("Enter the user Name you want to update:")
                uphone = input("Enter the user Phone Number you want to update:")
                db.update_user(uid,uname,uphone)

            elif choice==5:
                break

            else:
                print("Inavlid input!!! Try Again...")

        except Exception as e:
            print(e)
            print("Invalid Details!!! Try Again...")


if __name__=="__main__":
    main()












#main coding
# helper = DBHelper()

# # helper.insert_user(125, "Ankit", "123456")
# # helper.insert_user(130, "Mohit", "156789")

# # helper.fetch_all()

# # helper.fetch_specific(130)

# # helper.delete_user(130)

# # helper.fetch_all()

# helper.update_user(125, "Ankit Das", "567894")