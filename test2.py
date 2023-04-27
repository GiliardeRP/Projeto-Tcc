import win32com.client

shell = win32com.client.Dispatch("Shell.Application")
menu_iniciar = shell.NameSpace(0x0)

for i in range(menu_iniciar.Items().Count):
    item = menu_iniciar.Items().Item(i)
    nome_item = item.Name
    print(nome_item)
