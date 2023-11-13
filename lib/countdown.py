# your code goes here!

import time


def countdown(int_param):
    while int_param > 0:
        if int_param > 1:
            print(f"{int_param} SECONDS!")
        elif int_param == 1:
            print("1 SECOND!")
        int_param -= 1
    print("HAPPY NEW YEAR!")


def countdown_with_sleep(int_param):
    while int_param > 0:
        if int_param > 1:
            time.sleep(1)
            print(f"{int_param} SECONDS!")
        elif int_param == 1:
            time.sleep(1)
            print("1 SECOND!")
        int_param -= 1
    time.sleep(1)
    print("HAPPY NEW YEAR!")
        