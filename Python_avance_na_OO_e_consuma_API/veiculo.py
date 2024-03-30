"""
1 - Crie uma Classe Pai (Veiculo): Implemente uma classe chamada Veiculo com um construtor que aceita dois parâmetros, marca e modelo. 
A classe deve ter um atributo protegido _ligado inicializado como False por padrão.

2 - Construa o Método Especial str: Adicione um método especial str à classe Veiculo que retorna uma mensagem formatada com a marca, 
modelo e o estado de ligado/desligado do veículo.

3 - Crie uma Classe Filha (Carro): Agora, crie uma classe chamada Carro que herda da classe Veiculo. No construtor da classe Carro, 
inclua um novo atributo chamado portas que indica a quantidade de portas do carro.

4 - Implemente o Método Especial str na Classe Filha: Adicione um método especial str à classe Carro que estenda o método da classe pai (Veiculo) 
e inclua a informação sobre a quantidade de portas do carro.

5 - Crie uma Classe Filha (Moto): Similarmente, crie uma classe chamada Moto que também herda de Veiculo. Adicione um novo atributo chamado 
tipo ao construtor, indicando se a moto é esportiva ou casual.

6 - Implemente o Método Especial str na Classe Filha (Moto): Adicione um método especial str à classe Moto que estenda o método da classe pai (Veiculo) 
e inclua a informação sobre o tipo da moto.

7 - Crie um Arquivo Main (main.py): Crie um arquivo chamado main.py no mesmo diretório que suas classes.

8 - Importe e Instancie Objetos: No arquivo main.py, importe as classes Carro e Moto. Em seguida, crie três instâncias de Carro e Moto com diferentes marcas, modelos, quantidade de portas e tipos.
Exiba as Informações: Para cada instância, imprima no console as informações utilizando o método str.

9 - Crie uma classe chamada Veiculo com um método abstrato chamado ligar.

10 - No mesmo arquivo, crie um construtor para a classe Veiculo que aceita os parâmetros marca e modelo.

11 - Crie uma nova classe chamada Carro que herda da classe Veiculo.

12 - No construtor da classe Carro, utilize o método super() para chamar o construtor da classe pai e atribua o atributo específico cor à classe filha.

13 - Em um arquivo chamado main.py, importe a classe Carro.

14 - No arquivo main.py, instancie três objetos da classe Carro com diferentes características, como marca, modelo e cor.
"""

class Veiculo:
    def __init__(self, marca, modelo, ligado = False):
        self.marca = marca
        self.modelo = modelo
        self._ligado = ligado

    def __str__(self):
        return f"O veículo é do seguinte modelo: {self.modelo} e da marca {self.marca}. O veículo está {'ligado' if self._ligado else 'desligado'}."
    
    def ligar(self):
        self._ligado = not self._ligado
        print(f"O veículo foi {'ligado' if self._ligado else 'desligado'}")

    
class Carro(Veiculo):
    def __init__(self, marca, modelo, ligado, portas):
        super().__init__(marca, modelo, ligado)
        self.portas = portas

    def __str__(self):
        return f"O carro do modelo {self.modelo}, da marca {self.marca}, está {'ligado' if self._ligado else 'desligado'}. Ele possui {self.portas} portas."

class Moto(Veiculo):
    def __init__(self, marca, modelo, ligado, tipo):
        super().__init__(marca, modelo, ligado)
        self.tipo = tipo

    def __str__(self):
        return f"A moto é da marca {self.marca}, modelo {self.modelo}, ela está {'ligada' if self._ligado else 'desligada'}. Ela é do tipo {self.tipo}."
    