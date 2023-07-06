def twit_len(twit):
    if len(twit) <= 140:
        print("Your twit is is ready for posting.")
    else:
        new_twit = twit[:140]
        length_twit = len(twit)
        print(f"Your twit is {length_twit} so the twit should be '{new_twit}' which is {len(new_twit)} in length.")


my_twit = input("Enter your twit: ")
twit_len(my_twit)
