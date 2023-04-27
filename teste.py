
# import win32com.client
# import re

# shell = win32com.client.Dispatch("Shell.Application")
# menu_iniciar = shell.NameSpace(0x0)

# while True:
#     nome = input("Digite o nome do programa ou pasta que deseja abrir: ")
#     for i in range(menu_iniciar.Items().Count):
#         item = menu_iniciar.Items().Item(i)
#         if hasattr(item, 'Name'):
#             nome_item = item.Name
#             if re.search(nome, nome_item, re.IGNORECASE):
#                 item.InvokeVerb("open")
#                 break
#     else:
#         print("O programa ou pasta não foi encontrado.")

