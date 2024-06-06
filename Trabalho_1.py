import math

while(True):
    init = int(input("Digite um número de 1 a 7:\n 1-Verificar triângulo\n 2-Calcular equação do segundo grau\n 3-Conferir data\n 4-Verificar tamanho do texto\n 5-Analisar CPF\n 6-Contar caracteres\n 7-Sair\n"))
    if init == 1:
        a = int(input("Digite o valor de A:"))
        b = int(input("Digite o valor de B:"))
        c = int(input("Digite o valor de C:"))
        if a + b > c and a + c > b and b + c > a:
            if a == b or a == c or b == c:
                print("É um triângulo isósceles!!\n")
            elif  a != b or a != c or b != c:
                print("É um triângulo escaleno!!\n")
            elif a == b and b == c:
                print("É um triângulo equilátero!!\n")
        else:
            print("Não é um triângulo!!\n")

    elif init == 2:
        a2 = float(input("Digite o valor de A:"))
        b2 = float(input("Digite o valor de B:"))
        c2 = float(input("Digite o valor de C:"))

        if a2 == 0:
            print("Não se trata de uma equação de segundo grau!!\n")
        else:
            Delta = b2**2 - 4*a2*c2
            if Delta < 0:
                print("Não foi possível calcular, porque não possui raízes reais!!\n")
            elif Delta == 0:
                Raiz = -b2 / (2*a2)
                print("Raíz única:",Raiz,"\n")
            else:
                raizM = (-b2 + math.sqrt(Delta)) / (2*a2)
                raizm = (-b2 - math.sqrt(Delta)) / (2*a2)
                print("Raízes:",raizM, " e ",raizm,"\n")

    elif init == 3:
        dia = int(input("Digite o dia:"))
        mes = int(input("Digite o mês:"))
        ano = int(input("Digite o ano:"))

        if dia < 1 or dia > 31:
            print("Data inválida!!\n")
        if mes < 1 or mes > 12:
            print("Mês inválido!!\n")
        elif mes in [1,3,5,7,8,10,12]:
            if dia >= 1 and dia <= 31:
                print("Data valida!!\n")
        elif mes in [4,6,9,11]:
            if dia >= 1 and dia <= 30:
                print("Data valida!!\n")
        elif mes == 2:
            if dia >= 1 and dia <= 29:
                print("Data valida!!\n")
        else:
            print("Data inválida!!\n")

    elif init == 4:
        txt = input("Digite seu texto: ")
        txtL = len(txt)
        if txtL < 5:
            print("Texto muito pequeno!!\n")
        elif txtL >= 5 and txtL < 15:
            print("Texto médio!!\n")
        elif txtL >= 15 and txtL < 20:
            print("Texto grande!!\n")
        else:
            print("Texto inválido!!\n")

    elif init == 5:
        cpf = input("Digite seu CPF apenas com números: ")
        cpfL = len(cpf)
        cpfV = cpf.isdigit()
        if cpfV == True and cpfL == 11 :
            print("CPF valido!!\n")
        else:
            print("CPF inválido!!\n")

    elif init == 6:
        texto = input("Digite seu texto: ")
        vezes_vogal = sum(texto.count(vogal) for vogal in ['a', 'e', 'i', 'o', 'u','á', 'à', 'â', 'ã', 'é', 'ê', 'í', 'ó', 'ô', 'õ', 'ú', 'ü'])
        vezes_space = texto.count(" ")
        vezes_especiais = sum(texto.count(especiais)for especiais in ['b', 'c', 'd','f','g','h','j','k','l','m','n','p','q','r','s','t','v','w','x','y','z','!','@','#','$','%','¨','&','*','_','-','?',',','.',':',';','ç','~','´','`','0','1','2','3','4','5','6','7','8','9'])
        print("Existem ",vezes_vogal," vogais no seu texto!!\n")
        print("Existem ",vezes_space," espaços no seu texto!!\n")
        print("Existem ",vezes_especiais," caracteres especiais no seu texto!!\n")  

    elif init == 7:
        print("Obrigado por utilizar nosso sistema!!\n")  
        break

    else:
        print("Número inválido...\nencerrando o programa...\n") 
        break           