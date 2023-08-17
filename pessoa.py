class Pessoa:
    def __init__(self, nome, email, senha, contato, endereco, cpf, genero):
        self.nome = nome
        self.email = email
        self.senha = senha 
        self.contato = contato
        self.endereco = endereco
        self.cpf = cpf
        self.genero = genero


    @property
    def nome(self):
        return self._nome
    
    @nome.setter
    def nome(self, nome):
        self._nome = nome

    @property
    def email(self):
        return self._email
    
    @email.setter
    def email(self, email):
        self._email = email

    @property
    def senha(self):
        return self._senha
    
    @senha.setter
    def senha(self, senha):
        self._senha = senha

    @property
    def contato(self):
        return self._contato
    
    @contato.setter
    def contato(self, contato):
        self._contato = contato

    @property
    def endereco(self):
        return self._endereco
    
    @endereco.setter
    def endereco(self, endereco):
        self._endereco = endereco

    @property
    def cpf(self):
        return self._cpf
    
    @cpf.setter
    def cpf(self, cpf):
        self._cpf = cpf

    @property
    def genero(self):
        return self._genero
    
    @genero.setter
    def genero(self, genero):
        self._genero = genero

    def Falar(self):
        print("Falando")

    def Ouvir(self):
        print("Andando")

    def Andar(self):
        print("Ouvindo")

    def Informacoes_pessoa(self):
        nome = 'Suelaine' 
        email = 'suelaine1@email.com'
        senha = '123456'
        contato = '(87)98826-1364'
        endereco = 'Rua X no.18'
        cpf = '111.111.111-11'
        genero = 'Feminino'

        print("Nome: ", nome)
        print("E-mail: ", email)
        print("Senha: ******")
        print("Contato: ", contato)
        print("Endereco: ", endereco)
        print("CPF: ", cpf)
        print("Genero: ", genero)




    def Registrar_pessoa(self):

        print("---REGISTRO PESSOA----")
        nome = input("Digite o nome: ")
        email = input("Digite o e-mail: ")
        senha =  input("Digite a senha: ")
        contato = input("Digite o contato: ")
        endereco = input("Digite o endereco: ")
        cpf = input("Digite o cpf: ")
        genero = input("Digite o genero: ")

        print("Nome: ", nome)
        print("E-mail: ", email)
        print("Senha: ******")
        print("Contato: ", contato)
        print("Endereco: ", endereco)
        print("CPF: ", cpf)
        print("Genero: ", genero)

        
p1 = Pessoa('', '', '', '', '', '', '')
p1.Registrar_pessoa()
