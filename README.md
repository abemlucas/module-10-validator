# Module 10-Algorithm
Python based interpretation of the Luhn Algorithm.

Program checks if the credit card inputted is valid or not.

## How the Algorithm Works

```
Reverse the order of the credit card numbers.
```
```
Take the digits found in the odd places of the reversed credit card number.
```
```
Add those numbers and create a variable named s1.
```
```
Take the digits found in the even places of the reversed credit card number.
```
```
Multiply these digits each by 2.
```
```
Record the digits if they are >9 to create partial sums. Otherwise keep the new number.
```
```
Sum up the new partial numbers or regular numbers*2 to create a variable named s2.
```
```
If s1 + s2 = a number ending with 0 -> VALID or else -> FAKE
```
