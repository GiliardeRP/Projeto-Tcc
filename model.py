import sqlite3

banco = sqlite3.connect('myApp.db')

cursor = banco.cursor()

#cursor.execute('CREATE TABLE diretorio (nome text, caminho text )')
# cursor.execute("INSERT INTO diretorio VALUES ('pastinha', 'C:\\Users\\gilia\\OneDrive\\Área de Trabalho\\teste' )")

# banco.commit()

cursor.execute('SELECT * FROM diretorio')


print(cursor.fetchall())

