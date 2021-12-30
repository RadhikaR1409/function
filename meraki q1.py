def eligible_for_vote():
    age=int(input("enter your age : "))
    if age<18:
        print("you are not eligible for voting")
    else:
        print("you are eligible")

eligible_for_vote()
