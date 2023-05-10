import sqlite3

class Model:
    
    def insertDb(caminho):
        
        banco = sqlite3.connect('myApp.db')
        cursor = banco.cursor()
        cursor.execute('CREATE TABLE IF NOT EXISTS diretorio (nome text, caminho text )')
        cursor.execute(f"INSERT INTO diretorio VALUES (? , ? )", ('base', caminho) )
        banco.commit()
        banco.close()
        
    def selectDb():
        banco = sqlite3.connect('myApp.db')
        cursor = banco.cursor()
        cursor.execute('CREATE TABLE IF NOT EXISTS diretorio (nome text, caminho text )')
        cursor.execute('SELECT * FROM diretorio order by nome desc limit 1')
        result = cursor.fetchall()
        banco.close()
        return result

    def deleteDataDb():
        banco = sqlite3.connect('myApp.db')
        cursor = banco.cursor()
        cursor.execute('CREATE TABLE IF NOT EXISTS diretorio (nome text, caminho text )')
        cursor.execute(f"DELETE FROM diretorio")
        banco.commit()
        banco.close()




