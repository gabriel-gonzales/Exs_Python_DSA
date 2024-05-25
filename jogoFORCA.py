import random

# Inicialização
lista_palavras = ["duvida", "desconforto", "insegurança", "frieza", "racional", "fases"]
palavra_secreta = random.choice(lista_palavras)
letras_tentadas = []
tentativas = 6
representacao = ["_" for _ in palavra_secreta]
vitoria = False

print("\n Esse é um jogo da forca meio EMO! Mas não muito rock, peguei só a parte (><) ")
print("\n Você tem 6 tentativas!")

while tentativas > 0 and not vitoria:
    print("\n Palavra: ", " ".join(representacao))
    print(" Tentativas restantes:", tentativas)
    print(" Letras usadas:", " ".join(letras_tentadas))
    
    letra_tentativa = input("\n \n Digite uma letra: ").lower()
    
    if letra_tentativa in letras_tentadas:
        print("\n \n Você já tentou essa letra! Tente outra.")
        continue
    
    letras_tentadas.append(letra_tentativa)

    if letra_tentativa in palavra_secreta:
        for i, char in enumerate(palavra_secreta):
            if char == letra_tentativa:
                representacao[i] = letra_tentativa
        if "_" not in representacao:
            vitoria = True
    else: 
        tentativas -= 1

if vitoria:
    print("\n \n Parabéns! Você adivinhou a palavra:", palavra_secreta)
else:
    print("\n \n Você perdeu! A palavra era:", palavra_secreta)