# set_of_tupels = {(1, 2), (3,4)}
# print(set_of_tupels)
# print((1,2) in set_of_tupels , (1,3) in set_of_tupels)

# developers = {"Alice", "Bob", "Charlie"}
# admins = {"Alice", "David"}
# print("Alice" in developers | admins)

# print(developers.union(admins))
# print(developers | admins)

# print(developers.intersection(admins))
# print(developers & admins)

# print(developers.difference(admins))
# print(developers - admins)

# print(developers.intersection_update(admins))

# developers = {"Alice", "Bob", "Charlie"}
# print(developers.intersection(admins))

friends = {"Bob", "Rolf", "Anne"}
abroad = {"Bob", "Anne"}
print(friends)
print(abroad)
# מי נמצא ב פרינדס אבל לא באבורד
local = friends.difference(abroad)
print(local)

print(abroad.difference(friends))

mew = set()
print (mew)

local = {"Rolf"}
abroad = {"Bob", "Anne"}
friend = local.union(abroad)
print(friend)
print(local | abroad)
art = {"Bob", "Jen", "Rolf", "Charlie"}
science = {"Bob", "Jen", "Adam", "Anne"}
print(art.intersection(science))
x = print(art & science)
print("Bob" in art)
print("Anne" in art)
both = x
print(f"Common Elements {x}")

print(art.difference(science))
print(science.difference(art))

print(art.union(science))
print(science.union(art))

print(art.intersection(science))
print(science.intersection(art))