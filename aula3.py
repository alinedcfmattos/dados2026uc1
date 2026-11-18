# Crie um algootmi para dizer se uma pessoa é maior de idade ou não

idade = int (input("Qual a sua idade? "))

if idade >= 18: 
    print ("Você é maior de idade")
    print ("Pode tirar a carteira de motorista.")
else:
    print("Você é menor de idade.")
    faltam= 18 - idade
    print(f"Faltam {falam} ano(s) para completar 18.")


print("Fim do programa.")

