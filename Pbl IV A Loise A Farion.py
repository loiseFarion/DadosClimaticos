#----------------------------------Funções------------------------------------
  
def mediatemp (dados_csv , informacoes): 
 media_dia_mes = []
 linha = dados_csv.iloc[0]
 data = linha['Data']
 datacompleta = data.split('/') #separa string (elemento da coluna)  
 Mes = datacompleta[1]
 soma = linha[informacoes]
 numero = 1
 contador = 1
  
 while contador < len(dados_csv): 
            linha = dados_csv.iloc[contador]
            data = linha['Data']
            datacompleta = data.split('/') #separa string (elemento da coluna)
            contador += 1
            if datacompleta[1] == Mes:
                soma += linha[informacoes]
                numero +=1
                
            else:
                media = soma/numero
                numero = 1
                media_dia_mes.append(media)
                Mes = datacompleta[1]
                soma = linha[informacoes]
               
                 
 media = soma/numero
 media_dia_mes.append(media)           
 return media_dia_mes

def mediaumid (dados_csv , informacoes_umid):
 media_umid_dia_mes = []
 linha = dados_csv.iloc[0]
 data = linha['Data']
 datacompleta = data.split('/') #separa string (elemento da coluna)  
 Mes = datacompleta[1]
 soma = linha[informacoes_umid]
 numero = 1
 contador = 1
  
 while contador < len(dados_csv): 
            linha = dados_csv.iloc[contador]
            data = linha['Data']
            datacompleta = data.split('/') #separa string (elemento da coluna)
            contador += 1
            if datacompleta[1] == Mes:
                soma += linha[informacoes_umid]
                numero +=1
                
            else:
                media = soma/numero
                numero = 1
                media_umid_dia_mes.append(media)
                Mes = datacompleta[1]
                soma = linha[informacoes_umid]
             
                 
 media = soma/numero
 media_umid_dia_mes.append(media)           
 return media_umid_dia_mes

def listamesestempacima (dados_csv,valor):
    meses_temp_acima = []
    mediatempquente = mediatemp(dados_csv,'Temperatura')
    Mes = 0
    for i in mediatempquente:
        Mes += 1
        if i > valor:
            meses_temp_acima.append(Mes)

    return meses_temp_acima       


def listamesesumidabaixo (dados_csv,valor):
    meses_umid_abaixo = []
    mediaumidade = mediaumid(dados_csv,'Umidade')
    Mes = 0
    for i in mediaumidade:
        Mes += 1
        if i < valor:
            meses_umid_abaixo.append(Mes)
    return meses_umid_abaixo     
        

#-------------------------------Programa principal-----------------------------

import pandas as pd 

dfdados = pd.read_csv('DadosClimaticos2018Londrina.csv', sep=';')

print(' Opção 0: Encerrar o programa')
print(' Opção 1: Média de temperatura em cada mês do ano')
print(' Opção 2: Média de umidade relativa do ar em cada mês do ano')
print(' Opção 3: Lista dos meses com temperatura média acima da temperatura média informada')
print(' Opção 4: Lista dos meses com umidade média relativa do ar inferior a umidade média relativa do ar informada')


while True:#while infinito
    opcao_escolhida = int(input('Escolha a opção da informação que deseja 0,1,2,3 ou 4? '))
    
    if opcao_escolhida == 0:
        print('Obrigado(a) por utilizar o programa.')
        break
    if opcao_escolhida == 1:
        media = mediatemp(dfdados,'Temperatura')
        print('\n--------Média de temperatura em cada mês do ano--------\n')
        print('Temperatura média do mês Janeiro:   ',media[0])
        print('Temperatura média do mês Fevereiro: ',media[1])
        print('Temperatura média do mês Março:     ',media[2])
        print('Temperatura média do mês Abril:     ',media[3])
        print('Temperatura média do mês Maio:      ',media[4])
        print('Temperatura média do mês Junho:     ',media[5])
        print('Temperatura média do mês Julho:     ',media[6])
        print('Temperatura média do mês Agosto:    ',media[7])
        print('Temperatura média do mês Setembro:  ',media[8])
        print('Temperatura média do mês Outubro:   ',media[9])        
        print('Temperatura média do mês Novembro:  ',media[10])    
        print('Temperatura média do mês Dezembro:  ',media[11])
        
    if opcao_escolhida == 2:
        umidade = mediaumid(dfdados,'Umidade')
        print('\n--------Média de umidade relativa do ar em cada mês do ano--------\n')
        print('Umidade média do mês Janeiro:   ',umidade[0])
        print('Umidade média do mês Fevereiro: ',umidade[1])
        print('Umidade média do mês Março:     ',umidade[2])
        print('Umidade média do mês Abril:     ',umidade[3])
        print('Umidade média do mês Maio:      ',umidade[4])
        print('Umidade média do mês Junho:     ',umidade[5])
        print('Umidade média do mês Julho:     ',umidade[6])
        print('Umidade média do mês Agosto:    ',umidade[7])
        print('Umidade média do mês Setembro:  ',umidade[8])
        print('Umidade média do mês Outubro:   ',umidade[9])        
        print('Umidade média do mês Novembro:  ',umidade[10])    
        print('Umidade média do mês Dezembro:  ',umidade[11])
     

    if opcao_escolhida == 3:
         valor_limite = float(input('Entre com uma temperatura média: '))
         tempmediaacima = listamesestempacima(dfdados,valor_limite)         
         print('Informações referencias de cada mês: \n'
               'Janeiro  (mês 1)   -  Fevereiro (mês 2)  -  Março    (mês 3)\n'
               'Abril    (mês 4)   -  Maio      (mês 5)  -  Junho    (mês 6)\n'
               'Julho    (mês 7)   -  Agosto    (mês 8)  -  Setembro (mês 9)\n'
               'Outubro  (mês 10)  -  Novembro   (mês 11) - Dezembro  (mês 12)\n'
               'Sem referência ( [] )\n'
               '\nLista dos Meses com temperatura média acima do valor de ' + str(valor_limite) + ':')
         print(tempmediaacima)
        
           
    if opcao_escolhida == 4:
         limiteumid = float(input('Entre com uma umidade média relativa do ar: '))
         umidabaixo = listamesesumidabaixo(dfdados,limiteumid)        
         print('Informações referencias de cada mês: \n'
               'Janeiro  (mês 1)   -  Fevereiro (mês 2)  -  Março    (mês 3)\n'
               'Abril    (mês 4)   -  Maio      (mês 5)  -  Junho    (mês 6)\n'
               'Julho    (mês 7)   -  Agosto    (mês 8)  -  Setembro (mês 9)\n'
               'Outubro  (mês 10) -  Novembro   (mês 11) - Dezembro  (mês 12)\n'
               'Sem referência ( [] )\n'
               '\nLista dos Meses com umidade média relativa do ar abaixo do valor de ' + str(limiteumid) + ':')
         print( umidabaixo)


    elif opcao_escolhida != 0 and opcao_escolhida != 1 and opcao_escolhida != 2 and opcao_escolhida != 3 and opcao_escolhida != 4:
         print('Erro........ Opção escolhida inválida. Insira um opção válida.')
