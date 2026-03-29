#EX 1
# lavan=input("enter your name:  ")
# print(lavan)
#EX 2
# city=input("Which city do you live? ")
# print(city)
#EX 3
# AGE=int(input("Enter your age, ill add 10 more years:  "))
# print(AGE + 10)
#6 
# PRICE=float(input("Enter the price: "))
# print(PRICE)
#EX 7
# PRICE=float(input("Enter your price, ill add tax:  "))
# TAX = 0.17 
# print(PRICE * ( 1 + TAX))

#EX 10
# NUM1=float(input("enter first number:  "))
# NUM2=float(input("enter second number"))
# NUM3=float(input("Enter your third number"))
# print((NUM1 + NUM2 + NUM3) / 3 )
SQUARE_FEET=(int(input("Enter house size in square feet: ")))
factor = 0.09290304
sq_t = float( SQUARE_FEET * factor )
print(f"{SQUARE_FEET} square feet is equal to {sq_t:.2f} Square meters")