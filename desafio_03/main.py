class Heroi:
    def __init__(self, nome, idade, tipo):
        self.nome = nome
        self.idade = idade
        self.tipo = tipo

    def atacar(self):
        ataques = {
            "mago": "magia",
            "guerreiro": "espada",
            "monge": "artes marciais",
            "ninja": "shuriken"
        }
        if self.tipo.lower() in ataques:
            ataque = ataques[self.tipo.lower()]
        else:
            ataque = "um ataque desconhecido"
        print(f"O {self.tipo} atacou usando {ataque}")

def criar_heroi():
    nome = input("Digite o nome do herói: ")
    idade = int(input("Digite a idade do herói: "))
    while True:
        tipo = input("Digite o tipo do herói (mago, guerreiro, monge ou ninja): ").lower()
        if tipo in ["mago", "guerreiro", "monge", "ninja"]:
            break
        else:
            print("Tipo inválido. Por favor, escolha entre mago, guerreiro, monge ou ninja.")
    return Heroi(nome, idade, tipo)

# Programa principal
herois = []
while True:
    heroi = criar_heroi()
    herois.append(heroi)
    
    continuar = input("Deseja criar outro herói? (s/n): ").lower()
    if continuar != 's':
        break

print("\nAtaques dos heróis criados:")
for heroi in herois:
    heroi.atacar()