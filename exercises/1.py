number = int(input("Type your number:"))
ave_of_even = 0
sum_of_even = 0
sum_of_odds = 0
for i in range(1, number + 1):
    if i % 2 == 0:
        sum_of_even += i
    else:
        sum_of_odds += i
ave_of_even = sum_of_even / (number//2)

print("Average of even numbers:\t" + str(ave_of_even))
print("Sum of odd numbers:\t" + str(sum_of_odds))