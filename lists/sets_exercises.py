ports_list = [8080 , 8443 , 22 , 8080 , 443]

uniq_ports = set(ports_list)
print(uniq_ports)

server_name = {"web01" , "web02" , "web03" }

is_present = 22 in uniq_ports
print(is_present)

maybe = 22 in server_name
print(maybe)
uniq_ports.add(3000)
print(uniq_ports)
uniq_ports.remove(22)
print(uniq_ports)
uniq_ports.discard(22)
print(uniq_ports)

valid_set = {(1,2) , (3,4)}

pok = (32 , 32 , 42 , 32 , 21 , 15 , 16 , 15)
print(pok)
new_pok = set(pok)
print(new_pok)


original_list = [ 1, 2 , 2 , 3 , 3 , 4]
print(original_list)

new_original_list = set(original_list)
print(new_original_list)

check = 1 in original_list
print(check)