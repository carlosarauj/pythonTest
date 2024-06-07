nome = input("Digite seu nome: ")
idade = input("Digite sua idade: ")

if nome and idade:
    print(f'Seu nome é {nome}')
    print(f'Sua idade é {idade}')
    
    if ' ' in nome:
        print('Seu nome contém espaços')
    else:
        print('Seu nome nao tem espaços')

    print(f'Seu nome tem {len(nome)} letras')
    print(f'Seu nome ao contrário é {nome[::-1]}')
    print(f'A primeira letra do seu nome é {nome[0]}')
    print(f'A ultima letra do seu nome é {nome[-1]}')

else:
    print('faltou')

#python py.py
#ctrl ; para comentar