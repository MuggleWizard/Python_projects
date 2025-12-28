#Loop through numbers from 1 to 20
# for i in range(1,100):
#     if i % 3 == 0 and i % 5 == 0:
#         #Print FizzBuzz for numbers divisible by both 3 and 5
#         print("FizzBuzz")
#     elif i % 3 == 0:
#         #Print Fizz for numbers divisible by 3
#         print("Fizz")
#     elif i % 5 == 0:
#         #Print Buzz for numbers divisible by 5
#         print("Buzz")
#     else:
#         #Print the number itself if none of the above conditions are met
#         print(i)

# for num in range(1,101):
#     if num % 3 == 0 and num % 5 == 0:
#         print("Magic")
#     elif num % 5 == 0:
#         print("Tada")
#     elif num % 3 == 0:
#         print("Oose")
#     else:
#         print(num)

# def fizzbuzz(n):
#     for n in range(1, n+1):
#         if n % 3 == 0 and n % 5 == 0:
#             print("alohamora")
#         elif n % 5 == 0:
#             print("leviosa")
#         elif n % 3 == 0:
#             print("expeliamos")
#         else:
#             print(n)

# fizzbuzz(15)

# def snowFizz(n):
#     for i in range(1, n+1):
#         if i % 3 == 0 and i % 5 == 0:
#             print("Swish swish", i)
#         elif i % 3 == 0:
#             print("Boom", i)
#         elif i % 5 == 0:
#             print("Tada" , i)
#         else:
#             print("Magic")

# snowFizz(10)

def goldFish(num):
    for n in range (1, num + 1):    
        if n % 3 == 0 and n % 5 == 0:
            print("Both")
        elif n % 3 == 0:
            print("3")
        elif n % 5 == 0:
            print("5")
        else:
            print("Pineapple")

goldFish(50)