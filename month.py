# Created by: Logan Sweeney
# Created on: Dec.13, 2021
# This program gets a number from the user and
# displays the month connectde to that number.


def find_month(month):
    months = {
        1: "{} represents January.". format(month),
        2: "{} represents February.". format(month),
        3: "{} represents March.". format(month),
        4: "{} represents April.". format(month),
        5: "{} represents May.". format(month),
        6: "{} represents June.". format(month),
        7: "{} represents July.". format(month),
        8: "{} represents August.". format(month),
        9: "{} represents September.". format(month),
        10: "{} represents October.". format(month),
        11: "{} represents November.". format(month),
        12: "{} represents December.". format(month),
    }
    return months.get(month, "Error, Try again?")


if __name__ == "__main__":
    user_month = int(input("Enter the number of a month: "))
    print(find_month(user_month))
