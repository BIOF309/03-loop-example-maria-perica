# example of a loop and conditional
div_5 = [1, 2, 5, 10, 13, 20, 25, 300]
for number in div_5:
    if number%5 == 0:
        print(number, "is divisible by 5! Yay!")
    else:
        print(number, "is not divisble by 5. Boo.")
