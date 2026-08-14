# for i in range(1,31):
#     if i % 5 == 0 and i % 3 == 0:
#         print("FizzBuzz")
#     elif i % 3 == 0:
#             print("Fizz")
#     elif i % 5 == 0:
#         print("Buzz")
#     elif i % 2 == 0:
#         print(f"Even: {i}")
#     else:
#         print(f"Odd: {i}")

# number = 11

# while number > 1:
#     number -= 1
#     print(number)

# password = input("Password: ")

# while password != "python123":
#     print("Access denied")
#     password = input("Password: ")

# print ("Access granted")

# while True:
#     number = int(input("Enter number: "))
    
#     if number == 0:
#         break
    
#     print(number)

# print ("Goodbye!")

# for i in range(1,11):
#     if i % 2 == 0:
#         continue
    
#     print(f"Odd: {i}")

# Number Analyzer

while True:
    number = int(input("Enter number: "))
    if number == 0:
        break
    elif number < 0:
        continue
    elif number % 2 == 0:
        print(f"Number is even({number})")
    else:
        print(f"Number is odd({number})")
    
print("Goodbye!")