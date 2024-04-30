# titulo = "PIM"
# print(f"{titulo:^30}")
#
# for i in range(1, 31):
#     if i % 4 == 0:
#         print("PIM")
#     else:
#         print(i)

#Antonio
#Cores

print("Pim exercicio")
red = '\033[91m'
blue = '\033[94m'
reset = '\033[0m'
print("\npula linha")
print("\ttab")
print("\033[91mvermelho\033[0m")
print("outra cor")
for i in range(1, 30 + 1):
    if i % 4 == 0:
        print(f"{red}Pim{reset}")
    else:
        print(f'{blue}{i}{reset}')
