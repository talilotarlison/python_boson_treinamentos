# pardigima de programação - programação orientada a objetos
#  Conceitos de POO: Encapsulamento, Herança, Polimorfismo, Sobrescrita de métodos e Sobrecarga de métodos
#  Encapsulamento: é o conceito que define que uma classe não deve permitir que seus atributos sejam acessados diretamente.

# polimorfismo: é a capacidade de um objeto poder ser referenciado de várias formas, ou seja, um objeto pode ser referenciado por meio de uma classe pai ou de uma classe filha.
#  A sobrescrita de métodos seria criar um novo método na classe filha contendo a mesma assinatura e mesmo tipo de retorno do método sobrescrito. 
# (Override). Ja o sobrecarga, ele no caso seria, o que permite métodos de mesmo nome, mas com suas assinaturas diferentes,
#  ex argumentos diferentes.
#  A sobrescrita  de métodos é quando estamos trabalhando com orientação a objetos e temos uma classe (filha)
#  que acaba herdando de uma outra classe(mãe). Caso a classe filha precise modificar algum comportamento herdado da classe mãe,
#  podemos fazer uma sobrescrita (overwritten) do método diretamente da classe filha.

class Veiculos:
    def __init__(self, modelo, fabricante):# atributos
        # encapsulamento
        self.__modelo = modelo
        self.__fabricante = fabricante
        self.__num_do_registro = None
    # metodos
    def movimentar(self):
        print(f"O veículo {self.__modelo} está se movimentando.")
    # Getters
    def get_modelo(self):
        return self.__modelo

    def get_registro(self):
        return self.__num_do_registro
    # setters
    def num_do_registro(self, registro):
        self.__num_do_registro = registro
# herança
class Carro(Veiculos):
    def __init__(self, modelo, fabricante, num_portas):
        super().__init__(modelo, fabricante)
        self.__num_portas = num_portas

    def abrir_portas(self):
        print(f"O carro {self.get_modelo()} está com as portas abertas.")

    def fechar_portas(self):
        print(f"O carro {self.get_modelo()} está com as portas fechadas.")
  
    # polimorfismo
    def movimentar(self):
        print(f"O veículo {self.__modelo} está se movimentando.")

if __name__ == "__main__":
    # Exemplo de uso
    veiculo = Veiculos("Modelo X", "Fabricante Y")
    veiculo.num_do_registro("123456")
    veiculo.movimentar()
    print(veiculo.get_registro())

    meu_carro = Carro("Modelo A", "Fabricante B", 4)
    meu_carro.abrir_portas()
    print(meu_carro.get_modelo())