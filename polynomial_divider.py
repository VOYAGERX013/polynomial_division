def divide_polynomial(divisor, dividend):
    quotient = []
    curr_coef = dividend[0]
    quotient.append(curr_coef)
    n = len(dividend)
    for k in range(1,n):
        curr_coef = dividend[k] + divisor * curr_coef
        quotient.append(curr_coef)

    remainder = quotient[-1]
    quotient.pop()

    return [quotient,remainder]

divisor = int(input("Enter a linear divisor: "))
dividend = input("Enter a dividend: ").split(",")

for i in range(0,len(dividend)):
    dividend[i] = int(dividend[i])

output = divide_polynomial(divisor, dividend)
quotient = output[0]
remainder = output[1]

print(quotient)
print(remainder)

