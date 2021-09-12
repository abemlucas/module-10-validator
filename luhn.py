# Input to store the credit card number.
creditcard = int(input("Credit card number: "))
creditcard_str = str(creditcard)
sum1 = 0
sum2 = 0


def last_digit(num):
    num = str(num)
    return int(num[len(num)-1])


# For the construction of s1.
for i, element in enumerate(creditcard_str):
    if i % 2 == 0:
        sum1 += int(element)

# For the even digit placement
for i, element in enumerate(creditcard_str):
    if i % 2 != 0:
        partial_sum = int(element)*2

        if partial_sum > 9:
            new_sum = partial_sum-9
            sum2 += int(new_sum)
        else:
            sum2 += int(partial_sum)

total = sum1+sum2

if (last_digit(total) == 0):
    print("VALID CARD")
else:
    print("INVALID CARD")
