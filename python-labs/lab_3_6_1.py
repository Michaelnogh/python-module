
a = (input("Enter Your Numbers: "))
b = a.split()
my_tupple = []
for i in range (len(b)):
    c = (int(b[i])) 
    my_tupple.append(c)
         
new_tupple = tuple(my_tupple)
def expa(new_tupple):
    result = sum(new_tupple)
    count = len(new_tupple)
    avrage = result / count
    
    return result , count , avrage

answer = expa(new_tupple)   
print(f"Sum: {answer[0]}, Count: {answer[1]}, Average: {answer[2]}")    



input_number = ()
def bibi():
    