##Projeto Final do curso de Python do Professor Ivan.
#
##Programa simples para cálculo de média.


##Variáveis:
aluno = 0
prova = 0
trabalho = 0

##Sistema:
import re

print("Olá, neste programa iremos calcular a média do aluno(a) e verificar sua situação na escola!")

##Validação do nome do aluno
valid_aluno = False
while valid_aluno == False:
    aluno = input("Digite o nome do Aluno(a): ")    
    try:
        if aluno.isalpha() == False:
                print("Favor, digitar apenas letras")
        else:
            valid_aluno = True
    except:
            print("Nome inválido. Use apenas letras")
            
##Validação da nota da prova          
valid_prova = False
while valid_prova == False:
    prova = input("Digite a nota da Prova: ")
    try:
        prova = float(prova)
        if prova < 0 or prova > 10:
                print("A nota deve ser entre 0 e 10")    
        else:
             valid_prova = True
    except:
            print("Nota inválida. Use apenas números entre 0 e 10")
            
##Validação da nota do trabalho
valid_trabalho = False
while valid_trabalho == False:
    
    trabalho = input("Agora, a nota do trabalho deste aluno(a): ")
    try:
        trabalho = float(trabalho)
        if trabalho < 0 or trabalho > 10:
                print("A nota deve ser entre 0 e 10")    
        else:
            valid_trabalho = True
    except:
            print("Nota inválida. Use apenas números entre 0 e 10")
            
#Variável
resultado = (prova+trabalho)/2


#Verificar situação do aluno:
print('A nota do aluno(a) ' + aluno + ' é: ' + str(resultado))
if resultado < 6:
    print('Este aluno está: REPROVADO')
else:
    print('Este aluno está: APROVADO!')






