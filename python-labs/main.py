# ==============================
# My Profile App - Project
# ==============================
name = input("Enter Your Name: ")
age =  input("Enter Your Age: ")
city = input("Enter Your City: ")

hobbies = input("Type Your 3 Hobbies, use ',' after evry Hobbie: ").split(",")
popular_hobbies = ("music", "sports", "gaming", "reading")

print(f'Hello: {name} \n Your age is: {age} \n You live in: {city} \n Your Hobbies Are: {", ".join(hobbies)}')

x = hobbies[0] in popular_hobbies
y = hobbies[1] in popular_hobbies
p = hobbies[2] in popular_hobbies
# print(f"{hobbies[1]} --> {x}")

print(f"{hobbies[0]} -> {x}")
print(f"{hobbies[1]} -> {y}")
print(f"{hobbies[2]} -> {p}")      

print(f"Unique hobbies:{set(hobbies)}")

print(f"Total Hobbies: {len(hobbies)}")
print(f"Unique Hobbies: {len(set(hobbies))}")      

print(f"Hello {name} , You have {len(hobbies)} Hobbies")