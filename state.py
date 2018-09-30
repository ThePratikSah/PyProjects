while True:
    state = input("please Enter your state: ")
    if state == "bihar":
        print("patna is the capital of {}".format(state))
    elif state == "jharkhand":
        print("Ranchi is the capital of jharkhand")
    elif state == "rajasthan":
        print("jaipur is the capital of Rajasthan")
    else:
        print("not found")
    option = input("if you want to quit type Y for Yes")
    if option == "y":
        break
