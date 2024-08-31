# PyMediaCalculator

while True: 

    nome = str(input("Digite o Nome do Aluno "))
    nota1 = float(input("Nota do Aluno "))
    nota2 = float(input("Segunda nota do Aluno "))
    limite = 10
    print(f'='*25)

    resultado = nota1+nota2
    media = resultado/2
    limite <= media

    if media > limite:
        print("Erro Media muito Alta")
    else:

        print(F"Nome: {nome}")
        if media >6 :
            print(f"Resultado: APROVADO")
        elif media < 6:
            print(f"Resultado: REPROVADO")
        else:
            print(f"Resultado: Exame")
        print(f"Media:{media}")        
    

    print(f'='*25)


    repetir = int(input("Deseja fazer de outro aluno? caso queira Digite 1 para Sim e 2 para Não \n 1)Sim \n 2)Não"))

    if repetir != 1:
        print("Encerando...")
        break
    else:
      
        print("Recomecando...")
    print(f'='*25)

