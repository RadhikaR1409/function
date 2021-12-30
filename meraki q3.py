# def primeorNot(num):

#     if num > 1:
#         for i in range(2,num):
#             if (num % i) == 0:
#                 print(num,"is not a prime number")
#                 print(i,"times",num//i,"is",num)
#                 break
#             else:
#                 print(num,"is a prime number")
#     else:
#         print(num,"is not a prime number")

# primeorNot(406)





def sumofdigits(number):
    sum = 0
    modulus = 0
    while number!=0 :
        modulus = number%10
        sum+=modulus
        number//=10
    return sum

print(sumofdigits(123))