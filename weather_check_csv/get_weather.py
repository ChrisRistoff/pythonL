def get_weather():
    days_of_week = [
        "monday",
        "tuesday",
        "wednesday",
        "thursday",
        "friday",
        "saturday",
        "sunday",
    ]

    choose_day = input(
        "Which day of the week would you like to see the temperature for?\n "
    )
    while choose_day not in days_of_week:
        choose_day = input("Please choose a day of the week: \n")
    chosen_day = days_of_week.index(choose_day) + 1
    return chosen_day
