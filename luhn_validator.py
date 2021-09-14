creditcard = int(input("Credit card number: "))
Reverse = 0
while(creditcard > 0):
    Reminder = creditcard % 10
    Reverse = (Reverse * 10) + Reminder
    creditcard = creditcard // 10

creditcard_str = str(Reverse)
sum1 = 0
sum2 = 0


def last_digit(num):
    num = str(num)
    return int(num[len(num)-1])


for i, element in enumerate(creditcard_str):
    if i % 2 == 0:
        sum1 += int(element)
    elif i % 2 != 0:
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
