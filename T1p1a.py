import sys 

arq = sys.argv[1]
erros = open('T1p1a_erros.txt','w') 

with open(arq,'r') as f:
    dic = {}
    for line in f:
        try: 
            string1 = line.split('.')[1] 
            string2 = line.split('.')[2] 
            string3 =  string1 + '.' + string2
            chave = string3.split('-')[0]
            if chave not in dic:
                dic[chave] = 1
            else:
                dic[chave] += 1
        except:
            erros.write('Linha nao interpretada(fora do padrao):' + line)
  
    lista_chaves = list(dic.keys())
    lista_chaves.sort()

    with open('T1p1a.txt','w') as f2:
        for chave in lista_chaves:
            f2.write(chave + '-' + str(dic[chave])+'\n')
 
    erros.close()
