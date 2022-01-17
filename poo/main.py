# Classe: Entidade/Projeto/Blueprint/Planta que gera objetos
# Objeto: Gerado pela classe. Tem atributos e métodos.
# Atributos: Características do objeto (cor, altura, peso, nome) 
# Métodos: Ações que podem ser realizadas pelo objeto (andar(), comer())

# Objeto do tipo lista

class Pessoa():
    
    def __init__(self, cpf, name, age, city, gender):
        self.cpf = cpf
        self.name = name
        self.age = age
        self.city = city
        self.gender = gender
    
    
    def __str__(self) -> str:
        return (f"\nCPF: {cpf}\n"
                f"Nome: {self.name}\n"
                f"Idade: {self.age}\n"
                f"Cidade: {city}\n"
                f"Gênero: {gender}")
      
        
    def eat(self, food):
        print(f"A/O {self.name} está comendo {food}.")
    
    
    def study(self, subject):
        print(f"A/O {self.name} está estudando {subject}.")
    
    def sleep(self):
        print(f"A/O {self.name} está a mimir.")
        
    def play(self, game):
        print(f"A/O {self.name} está jogando {game}.")
    
cpf = input("Informe seu cpf: ")
name = input("Informe seu nome: ")
age = input("Informe sua idade: ")
city = input("Informe sua cidade: ")
gender = input("Informe seu gênero: ")
food =  input("Informe uma comida: ")
subject = input("Informe um assunto: ")
game = input("Informe um jogo: ")

pessoa = Pessoa(cpf, name, age, city, gender)
pessoa.eat(food)
pessoa.study(subject)
pessoa.sleep()
pessoa.play(game)
print(pessoa)
