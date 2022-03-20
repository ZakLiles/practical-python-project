user_age = int(input("How old are you?\n"))

decades = user_age // 10
years = user_age % 10

print("You are " + str(decades) + " decades and " + str(years) + " years old.")