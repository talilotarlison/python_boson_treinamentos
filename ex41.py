# Classe base Pessoa
class Pessoa:
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade
    
    def apresentacao(self):
        # Método de apresentação da pessoa
        return f"Olá, meu nome é {self.nome} e eu tenho {self.idade} anos."

# Classe derivada Estudante que herda de Pessoa
class Estudante(Pessoa):
    def __init__(self, nome, idade, curso):
        # Chama o construtor da classe base Pessoa
        super().__init__(nome, idade)
        self.curso = curso
    
    def apresentacao(self):
        # Método de apresentação do estudante, que sobrescreve o método da classe base
        return f"Olá, meu nome é {self.nome}, eu tenho {self.idade} anos e estou cursando {self.curso}."

# Testando as classes
pessoa = Pessoa("João", 40)
estudante = Estudante("Ana", 22, "Engenharia")

# Chamando os métodos de apresentação (polimorfismo em ação)
print(pessoa.apresentacao())  # Saída: Olá, meu nome é João e eu tenho 40 anos.
print(estudante.apresentacao())  # Saída: Olá, meu nome é Ana, eu tenho 22 anos e estou cursando Engenharia.
