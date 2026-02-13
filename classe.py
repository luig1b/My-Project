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

class pessoajuridica(pessoa):
    def __init__(self, nome, email, endereco, cnpj):
        self.cnpj = cnpj
        super().__init__(nome, email, endereco)
    pass

pessoa = pessoa('alceu', 'alceu@gmail.com', 'rua teixeira')
pessoafisica = pessoafisica("vitor", 'joao@gmail.com', 'faria lima', 'hhhhhh-90')
pessoajuridica = pessoajuridica('hhhh', 'kkkkkk', 'lllll', 'oooooo')

print(pessoa.nome, pessoa.email, pessoa.endereco)
print(pessoafisica.nome, pessoafisica.email, pessoafisica.endereco, pessoafisica.cpf)

pessoa.nome = 'antony'
pessoafisica.email = 'vitor@gmail.com'
pessoajuridica.cnpj = '345678-90'

print('...dados...')
print(f'dados do usuario pessoa alterado: {pessoa.nome}')
print(f'dado alterado do ususario pessoafisica: {pessoafisica.email}')
print(f'dados alterados de pessoajuridica {pessoajuridica.cnpj}')
