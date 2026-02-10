class pessoa:
    def __init__(self, nome, email, endereco):
        self.nome = nome
        self.email = email
        self.endereco = endereco
    pass

class pessoafisica(pessoa):
    def __init__(self, nome, email, endereco, cpf):
        self.cpf = cpf
        super().__init__(nome, email, endereco)
    pass

class pessoajuridica(pessoafisica):
    def __init__(self, nome, email, endereco, cpf, cnpj):
        self.cnpj = cnpj
        super().__init__(nome, email, endereco, cpf)
    pass

pessoa = pessoa('alceu', 'alceu@gmail.com', 'rua teixeira')
pessoafisica = pessoafisica("vitor", 'joao@gmail.com', 'faria lima', 'hhhhhh-90')
pessoajuridica = pessoajuridica('hhhh', 'kkkkkk', 'lllll', 'jjjjj', 'oooooo')

print(pessoa.nome, pessoa.email, pessoa.endereco)
print(pessoafisica.nome, pessoafisica.email, pessoafisica.endereco, pessoafisica.cpf)
