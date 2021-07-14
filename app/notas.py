def notas():
    nota1 = int(input("Primeira nota:"))
    nota2 = int(input("Segunda nota:"))
    nota3 = int(input("Terceira nota:"))
    nota4 = int(input("Quarta nota:"))
    soma = nota1 + nota2 + nota3 + nota4
    media = soma / 4
    print(f"Media: {media}")
    if media >= 7:
        print('Aprovado')
    else:
        print('Reprovado')
notas()