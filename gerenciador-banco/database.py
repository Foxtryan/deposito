''' DOC '''
import sqlite3
from vxencypt import ash

def toBinary(string):
    ''' Converte para byte string'''
    return bytes(string, 'UTF-8')

class Login(object):
    "Toda estrutura para SQL."
    def __init__(self, database):
        "Cria o arquivo BD. "
        self.connected = False
        self.user = ''
        self.__senha = ''
        self._db = database
        self._conn = sqlite3.connect(database)
        self.create_table()

    def create_table(self):
        " Cria o BD caso não exista. "
        self._conn.execute('CREATE TABLE IF NOT EXISTS CONTAS \
                        (USUARIO TEXT, SENHA TEXT,\
                        SALDO STRING DEFAULT 0, NOTAS TEXT DEFAULT 0)')

    def createAccount(self, username, senha):
        " Cria uma conta. "
        senha = ash(toBinary(senha))
        if not self.checkUsername(username): # Checa se usuario já existe.
            self._conn.execute('INSERT INTO CONTAS (USUARIO, SENHA)\
                                VALUES (\'{username}\',\'{senha}\')'.format(username=username,\
                                        senha=senha))
            self._conn.commit()
            self.connected = True
            self.user = username
            self.__senha = senha
            return True
        else:
            return False

    def connect(self, username, senha):
        " Conecta o usuario. "
        senha = ash(toBinary(senha))
        cursor = self._conn.execute('SELECT USUARIO, SENHA FROM CONTAS')
        for row in cursor:
            if row[0] == username and row[1] == senha:
                self.connected = True
                self.user = username
                self.__senha = senha
                return True
            else:
                return False

    def checkUsername(self, username):
        "Checa se usuario existe na tabela.\nFunção exclusiva para metodo __createAccount__. "
        cursor = self._conn.execute('SELECT USUARIO from CONTAS')
        for row in cursor:
            if row[0] == username:
                return True
            else:
                return False

    def deleteAccount(self):
        """ Deleta a conta do usuario conectado. """
        if self.connected:
            self.conn.execute("DELETE FROM CONTAS WHERE USUARIO=\'{username}\' AND SENHA\
            =\'{senha}\'".format (username = self.user, senha = self.__senha))
            self.conn.commit()
            self.connected = False
            self.user = ''
            return True
        else:
            return False

    def addColumn(self, column, column_type):
        """ Adiciona uma coluna a tabela. """
        if self.user == 'Administrador':
            try:
                self.conn.execute('ALTER table CONTAS add column \'{}\' \'{}\''.format\
                                  (column, column_type))
                return "Coluna adicionado"
            except sqlite3.OperationalError:
                return False
        else:
            return "Somente administradores criam colunas"

    def getColumns(self):
        " Retorna todas as colunas da tabela."
        if self.user == 'Administrador':
            cursor = self.conn.execute('SELECT * from CONTAS')
            descriptions = list()
            for description in cursor.description:
                descriptions.append(description[0])
            return descriptions

    def getAll(self):
        """ Retorna todos os valores da tabela. """
        cursor = self._conn.execute("SELECT * from CONTAS")
        description = list()
        for row in cursor:
            person = dict()
            for i, column in enumerate(row):
                person[cursor.description[i][0]] = column
            description.append(person)
        return description

    def getValue(self, column):
        " Retorna o valor da coluna solicitada."
        values = self.getAll()
        for value in values:
            if value['USUARIO'] == self.user:
                return value[column]

    def setValue(self, column, value):
        self._conn.execute('UPDATE CONTAS SET {c} = {v} WHERE USUARIO = "{u}"'.format(c = column,\
                          v = value, u = self.user))
        self._conn.commit()
        return value

    def sair(self):
        " Desconecta. "
        self.connected = False
        self._conn.close()
        self.user = ''
        self.__senha = ''

if __name__ == '__main__':
    login = Login('Data.db')
    login.createAccount("Administrador", "senha")
    login.connect("administrador", "senha")
    if login.connected:
        print('[+] Conectado como {}'.format(login.user))
    else:
        print('[-] Conexão falhou')
        login.addColumn('SALDO', 'INT')
        login.setValue('SALDO', 10)
        print(login.getColumns())
        print(login.getAll())
        print(login.getValue('SENHA'))
        login.setValue('USUARIO', '\'Junior\'')
"""
login = Login("TESTE.db")
login.createAccount("user 1", "senha")
login.createAccount("user 2", "senha")
login.createAccount("user 3", "senha")
login.createAccount("user 4", "senha")
login.createAccount("user 5", "senha")
login.createAccount("user 6", "senha")
login.createAccount("user 7", "senha")
login.createAccount("user 8", "senha")
login.createAccount("user 9", "senha")
"""