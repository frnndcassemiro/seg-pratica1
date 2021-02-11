import sys 

arq = sys.argv[1]
erros = open('T1p1b_erros.txt','w') 
with open(arq,'r') as f:
    lista = []
    for line in f:
        try:
            string1 = line.split('.')[1] 
            string2 = line.split('.')[2] 
            string3 = line.split('.')[3] 
        
            string4 = string3.split('-')[1]
            string5 = string4.split(':')[0]

            chave = string1 + ',' + string2 + ',' + string3.split('-')[0] + ',' + string5
            lista.append(chave)
        
        except:
            erros.write('Linha nao interpretada(fora do padrao):' + line)

    with open('T1p1b.txt','w') as f2:
        for chave in lista:
            f2.write(chave + '\n')
    
erros.close()
 
