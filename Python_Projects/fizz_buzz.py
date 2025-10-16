#Loop through numbers from 1 to 20
for i in range(1,100):
    if i % 3 == 0 and i % 5 == 0:
        #Print FizzBuzz for numbers divisible by both 3 and 5
        print("FizzBuzz")
    elif i % 3 == 0:
        #Print Fizz for numbers divisible by 3
        print("Fizz")
    elif i % 5 == 0:
        #Print Buzz for numbers divisible by 5
        print("Buzz")
    else:
        #Print the number itself if none of the above conditions are met
        print(i)