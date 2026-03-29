# print(5 == 5)

# print(5 == 2)

# print( 9 >= 12 )

# print(5 <= 3)

# print(10 >= 10)
# print(10 <= 9)

# print(40 != 15)
# print(20 != 20)
# x = (5 != 4)
# print(x)

# a = (13 >= 5)
# print(a)

# pok = ["Mew" , "wafwaf" , "kukuriko"]
# new_list = ["Mew" , "wafwaf" , "kukuriko"]

# print(pok is new_list)
# print(pok == new_list)
# friends = [ "Rolf" , "Bob" , "Jen" ]
# print("Jen" in friends)
# print("Anne" in friends)

# movies = {"The Matrix" , "AliG" , "Inception"}
# user_movie = input("Enter movie you saw")
# print(user_movie in movies)

# print("rix" in "The Matrix")

# movies = {"AliG" , "Watchdogs" , "Sopranos"}
# user_movie = input("Enter a movie have watched recently: ")
# if user_movie in movies:
#     print("We know this movie")
# else:
#     print("we dont know what you tallking about")
        
 
secret_number = 55
user_input = input("Enter Y if you would like to play")
if user_input in ( "y" , "Y" , "Yes" ) : 
    user_number = int(input("Guess a Number from 1-100: "))
if secret_number == user_number:
    print("You got it")
elif abs(secret_number - user_number) == 1 :
    print("You are very close")
#abs() every number turn to positive one (-7 = 7)
else:
    print("You loser")    
if abs(secret_number - user_number) == 1 : 
   print("You were off by one") 
    