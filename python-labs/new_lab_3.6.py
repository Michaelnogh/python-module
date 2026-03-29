# a = input("Enter Your Numbers: ")
# b = a.split()
# my_tupple = []
# for i in range (len(b)):
#     c = (int(b[i]))
#     my_tupple.append(c)
    
# new_tupple = tuple(my_tupple)    

# def pok(new_tupple):
#     result = sum(new_tupple)
#     count = len(new_tupple)
#     avrage = result / count
    
#     print(f"The Result of the numbers:{result} \n Total numbers:{count} \nAvrage:{avrage}")
        
# pok(new_tupple)
 
 #* ----------- 3.6.1 EX 2 -------------
 
# a = (input("Enter Your Number: "))
# b = a.split()
# my_tupple = []
# for i in range (len(b)):
#     c = (int(b[i]))
#     my_tupple.append(c)
    
# new_tupple = tuple(my_tupple)

# # def lowest_higest(data_tuple):
# #     low = min(data_tuple) 
# #     high =max(data_tuple)   
# #     return low , high

# # result = lowest_higest(new_tupple)
# # print(f"Lowerst: {result[0]}, \nHighest: {result[1]}")

# def lowest_highest():
#     low = min(my_tupple)
#     high = max(my_tupple)
#     print(f"Higest Number : {high} \nLowest Number: {low}")


# lowest_highest()         

#* ------------------- EX 3

# a = input("Enter Numbers: ")
# b = a.split()
# my_list = []
# for i in range (len(b)):
#     c = (int(b[i]))
#     my_list.append(c)
# #new_list = my_list

# def zugi_ole(my_list):
#     num = 2
#     zugi = [n for n in my_list if n % 2 == 0 ]
#     ole = [ sorted(my_list) ]
#     print(f"Zugi : {zugi} \nOle : {ole}")

# zugi_ole(my_list)        

#* ----------------- PART 2 EX 4 -----
# a = input("Enter Your Numbers: ")
# b = a.split()
# my_list = []
# for i in range (len(b)):
#     c = (int(b[i]))
#     my_list.append(c) 
    
# def even_odd(my_list):
#     if my_list[0] % 2 == 0:
#         print("Even")
#     else:
#         print("Not even")            

# even_odd(my_list)     

#* PART 2 EX 5

# a = input("Enter Your Scores: ")
# b = a.split()   
# my_scores = []
# for i in range (len(b)):
#     c = (int(b[i]))
#     my_scores.append(c)
    
# def scores(my_scores):
#     print("These are the Scores more then 60: ")
#     for score in my_scores:
#         if score >= 60:
#             print(score)
    
    
#     # if my_scores[0] >= 60:
#     #      print(f"More then sixty , theres are the number more then 60 {my_scores}")
#     # else:
#     #     print("Less then 60") 
         
#* --------------- PART 2 EX 6
# scores(my_scores)    
    
# a = input("Enter Your Numbers")
# b = a.split()
# pop = []
# for i in range (len(b)):
#     c = (int(b[i]))
#     pop.append(c)

# def rek():
#     if not pop:
#         print("No Numbers in the list")
#     else:
#         result = sum(pop)
#         count = len(pop)
#         avrage = result / count
#         print(avrage) 
        
# rek()        
#* ------------------------- PART 3 EX 7
# x = 10
# list = [32 , 13 ,12 ,15 ,16, 4 , 2 , x ]
# def para(list , x=10):
#     for list in list : 
#         if list >= 10:
#             print(f"All the numbers above 10 : these are the numbers {list}")
        
        
# para(list)

#* -------------------- PART 4 EX 9 ---------------------



# def Vans (*args):
    
#     print(max(args))

# Vans(32 , 12 , 41 , 22 )    
    
    

#* --------- PART 4 EX 10 ----------

# def Nike (*args):
#     for args in args:
#         if args % 2 == 0:
#             print(f"The Even Numbers in the number is {args} ")
        
# Nike(23 , 12 , 14 , 16)    

#*---------------------- PART 5 EX 11 ----------------------

# def Adidas(name,age):
#     print(f"Hello {name} , You are {age} Years old" )

# Adidas(age=32,name="Muhammad")
#* -------------------- PART 5 EX 12 ------------------------
# list = [41 , 21 , 12 , 51 , 66 , 12]
# def NewBalance():
#     pok = sum(list)
#     shmok = min(list)
#     hnok = max(list)
#     print(f"The Sum is {pok} \nThe Min is {shmok} \nThe Max is {hnok}")
    

#NewBalance()
#* -------------------- PART 6 EX 13 
# def Crocs(x , y):
#     int(x) + int(y) 
#     def Kappa():
#     Crocs()
#     print(Crocs)
 
# Crocs(6,7)
# Kappa(6,7)
     
#* -----------------------EX 13
# def cor():
#         def kor(*args):
#             s = sum(args)
#             print(s)
#         kor(22,31)
# cor()            
#* ================================== EX 14 PART 6

# def Mew():
#     print(x)
# x = "david"
# Mew()
# #* ================= EX 15

# def Epstien():
#     eli = "sababa"
#     def in_epstien():
#             nonlocal eli
#             print(eli + " Ahlagever")
#     in_epstien()
#Epstien()
#* ===================== EX 16 
#! LASHEVET IM FITUSSI
# my_list = [13 , 15 , 11 , 41 , 21]
# def Trump(t):
#     return t + 7 

# def Malezia(original_list, func):
#    my_new_list = []
#    for i in original_list:
#         result = func(i)
#         my_new_list.append(result)
#    return my_new_list        
        

# new_list = Malezia(my_list , Trump)
# print(new_list)
#*----------------- EX 17 
# def func(x=1):
#     n = x * 2
#     print(n)
    
# def combined_func(x,a):
#     a(x)
# combined_func(30,func)
    
#* -------------- EX 18 
#! ASK FITUSSI 
my_list = [4 ,42 ,15 ,16]
def get_list (x=10):
    for my_list in my_list:
        if my_list >= 10:
            print(my_list)
    if my_list >= 10:
    if my_list  True:
            print(reversed(my_list))
