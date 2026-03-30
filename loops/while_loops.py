# while loops basics
#-------------------------------------------

# user_input = input("Would you like to play? (n/y) :")

# while user_input != "n": 
#     print("Game is Running")
#     user_input = input("Would you liketo play again (n/y): ")




# while True:
#     user_input = input("would you like to play? (n/y): ")

#     if user_input == "n":
#         break
#     print("Game is running")

# num = 1
# while num <=5:
#     print(num)
#     num+=1
# EX 2

# num = 5
# while num >=1:
#     print(num)
#     num -=1

#Ex 3

# num = 1
# while num <= 10:
#     if num % 2 == 0:
#         print(num)
#     num += 1 

#EX 4


# num = 1
# total = 0
# while num <= 5:
#     total += num
#     num += 1

# print(stotal)    

#ex 5

# while num < 10:
#     if num % 3 == 0:
#         print(num)
#     num +=1    

#EX 6

# num =int(input("Enter Your number"))
# count = 0
# while count < 5:
#     print(num)
#     count += 1
    
#EX 7

# num = int(input("Enter Your number"))
# count = 1
# while count <= num:
#     print(count)
#     count += 1

 #EX 8
# num = int(input("Enter Numbers"))
# while num != 0:
#     num = int(input("Enter again"))

# print("nice")

#EX 9
# num = int(input("Enter Password"))
# while num != 1234:
#     num = int(input("Password incorrect"))

# print("Connected Succsecfully")   

#EX 10

# num = input("Enter y to cotinume or n to stop")
# while num == "y":
#     print("You Choose to continume")
#     num = input("Enter y to continue or n to stop: ")

# if num == "n":
#     print("You choose to Stop")    

#EX 11
# n = 1
# while n <= 10:
#     n += 1
#     if n % 2 == 0:
#         print(n)    
#ex 12
# N = 1
# P = 0
# while N <= 20:
#     N+=1    
#     if N % 2 == 0: 
#         P = P + 1
        
# print(P)       
    
#Ex 13
# N = 0
# P = 0
# while N <= 9:
#     N+=1
#     if N % 2 == 1:
#         P = P + N  

# print(P)        
#EX 14

# while True:
#     x = input("enter number or q to quit: ")
#     if x == "q":
#         break
#     num = int(x)
#     num % 2 
#     if num % 2 == 0:
#         print("Even")
#     else:
#         print("odd")
#EX 15
# num = 1
# max_num = int(input("Enter Number"))
# while num <= 5:
#     num += 1 
#     T = int(input("Enter Number"))
#     if T > max_num:
#         max = T

# print(max)

#EX 16
# x = input("Say something")
# while x != "exit":
#     x = input("say again someting")


# print(x)

#EX 17 
# x = 0
# while x <= 10:
#     x += 1
#     if x <= 7:
#         print(x)

#EX 18
# asad = 0
# x = int(input("Enter numbers"))
# while x >= 0:
#    x = int(input("Enter Number"))
#    asad = x + asad

# print(asad)    
#EX 19 ----------
#lucky_number = 6
# x = int(input("Guess a number: "))
# while x != 6:
#     x = int(input("Try again"))

# print("Nice ya manyak")   
#Ex 20
x = input("Say someting")
while x != "stop":
    x = input("Try again")

print("nice manyak")
