# print(10 > 5)

# print(10 < 5)

# print(10 == 10)

# print(10 == 5)

# user_name = input("What's your name? ")

# hourly_rate = float(input("What's your hourly rate? "))

# hours_worked = int(input("How much hours did you work? "))

# salary = hourly_rate * hours_worked

# print(f"Hello, {user_name}")
# print(f"Your salary is {salary}")

# if salary >= 7000:
#     print("Your salary is high!")
# elif salary >= 5000:
#     print("Your salary is medium!")
# else:
#     print("Your salary is low!")

# candidate_name = input("What's your name? ")

# candidate_age = int(input("What's your age? "))

# language_level = input("What's your English level? ")

# months_exp = int(input("How much experience months do you have in Python? "))

# if candidate_age >= 18 and (language_level == "B2" or language_level == "C1" or language_level == "C2") and months_exp >= 6:
#     print(f"{candidate_name} is strong candidate")
# elif candidate_age >= 18 and (language_level == "B2" or language_level == "C1" or language_level == "C2") and months_exp < 6:
#     print(f"{candidate_name} is junior candidate")
# else:
#     print("The candidate in not ready yet")

# Access checker

user_age = int(input("What's your age? "))
has_id = input("Do you have an id? ") == "Yes"
is_banned = input("Is you banned? ") == "Yes"

if user_age >= 18 and has_id and not is_banned:
    print("Access granted!")
else:
    print("Access denied!")