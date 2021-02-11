import sys 

arq = sys.argv[1] #AV2.txt
erros = open('T1p1a_erros.txt','w') 

with open(arq,'r') as f:  
    dic = {}
    for line in f: #percorre o arquivo AV2.txt linha por linha
        try: 
            string1 = line.split('.')[1] #string1 == tipo de codigo malicioso
            string2 = line.split('.')[2] #string2 == familia-variante 
            string3 =  string1 + '.' + string2 #string3 == malicioso.familia-variante
            chave = string3.split('-')[0] #chave == malicioso.familia
            
            #conta o numero que cada chave aparece no arquivo para calcular o numero de variantes
            if chave not in dic:
                dic[chave] = 1
            else:
                dic[chave] += 1
        except:
            erros.write('Linha nao interpretada(fora do padrao):' + line)
  
    lista_chaves = list(dic.keys())
    lista_chaves.sort() #ordena as chaves alfabeticamente

    with open('T1p1a.txt','w') as f2:
        for chave in lista_chaves: #percorre o dicionario gravando os dados no arquivo de saida
            f2.write(chave + '-' + str(dic[chave])+'\n')
 
    erros.close()
