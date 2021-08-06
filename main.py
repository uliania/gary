def main():
    string = "This is a string!"
    integer = 8
    bool = True
    float = 5.2

    #print(string)

    acceptableChars = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"



    username = input("enter a user:\n")

    age = int(input("enter your age:\n"))

    #print("Hi!!!  My favorite number is " + integer)



    number = "11"
    number = int(number)




    acceptedUser = ""

    for i in username:
        for j in acceptableChars:
             if i == j:
                acceptedUser += i

    if acceptedUser == username:
        print(username + " is " + str(age) + " years old")
    else:
        print("Invalid Username")





if __name__ == '__main__':
    main()
