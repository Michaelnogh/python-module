# print("Start")
# def hello():
#     print("Hello")    
    
# hello()    
# print("End")

# def ask_age():
#     age = int(input("What is your Age?: "))
#     age_in_seconds = age * 365 * 24 * 60 * 60
#     print(f"Your Age in Second is : {age_in_seconds}")
    
# ask_age()  


# animals_sound = ["mew" , "wafawf" , "kukuriko"]

# def animal():
#     global animals_sound
#     pok = animals_sound
#     duck = ["QuakQuak"]
#     animals_sound = pok + duck
#     #animals_sound.append("MEEE")
#     print(animals_sound)
# animal()    
# animal()
# animal()
# animal()



#* 3_5 HANDS ON LAB GUARD CLAUSES AND INPUT VALIDATION
def prosses_data_guarded(x):
    if not isinstance(x, list) : 
        print("No data provided + kosomo")
    else:    
        print(len(x))
        print(f"Proceccing {len(x)} Items")
    

prosses_data_guarded([])
prosses_data_guarded([1, 2, 3])
prosses_data_guarded("ABS")
prosses_data_guarded(10)

# prosses_data_guarded() # N ARG SO ITS ERR ( TYPE ERR )
print(type(prosses_data_guarded))

 