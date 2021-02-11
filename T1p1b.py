import sys 

arq = sys.argv[1] #AV1.txt
erros = open('T1p1b_erros.txt','w') 
with open(arq,'r') as f:
    lista = []
    for line in f: #percorre o arquivo AV1.txt linha por linha
        try: 
            string1 = line.split('.')[1]  #string1 eh a Plataforma/Linguagem
            string2 = line.split('.')[2]  #string2 eh o Tipo
            string3 = line.split('.')[3]  #string3 é o Subtipo + o resto da linha
        
            string4 = string3.split('-')[1]  #string4 é o Subtipo
            string5 = string4.split(':')[0]  #string5 é a Variante

            #formata a saida
            chave = string1 + ',' + string2 + ',' + string3.split('-')[0] + ',' + string5

            #inclui a chave (linha formatada) na lista
            lista.append(chave)
        
        except:
            erros.write('Linha nao interpretada(fora do padrao):' + line)

    with open('T1p1b.txt','w') as f2:
        for chave in lista: #percorre a lista gravando os dados no arquivo de saida
            f2.write(chave + '\n')
    
erros.close()
 
