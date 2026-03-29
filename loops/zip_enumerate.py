# -------- ENUMERATAE
# names = ["Alice", "Bob", "Charlie"]
# for idx,name in enumerate(names):
#     print(idx,name)
#     #print(idx)

#x -------- ZIP
# servers = ["app-01", "app-02", "app-03"]
# for idx,name in enumerate(servers,start=1):
#     print(idx,name)
#     print(servers[2])
#     print(servers)

# EX 3 
errors = ["disk full", "timeout", "connection lost"]
for idx,name in enumerate(errors):
    if idx % 2 == 0:
        print(idx,errors)


