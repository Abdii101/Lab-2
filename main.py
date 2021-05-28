Task 1  Create a program that converts ANY binary number to decimal numbers.
 
Structural English Model

 Ask user to input any binary number.
If the number is correct;
then move on to next step.
convert from binary to decimal.

Pseudo code

prersdure binary to decimal 
  number equal to n
  decimal_value equal to 0
base equal to 1
temp equal to number
while timp 
      last digit number equal to % 10
        temp equal integer (temp divided by 10)
 decimal_ value is more than or equal last_digit multiplied base
base equal to base multiplied 2
returnt decimal_value

Code
def binaryToDecimal(n):
    num = n;
    dec_value = 0;
     base = 1;
     
    temp = num;
    while(temp):
        last_digit = temp % 10;
        temp = int(temp / 10);
         
        dec_value += last_digit * base;
        base = base * 2;
    return dec_value;
 
num = 10101001;
print(binaryToDecimal(num));
 


Task 2
//////
//////
//////
//////