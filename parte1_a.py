with open('AV1.txt','r') as f:
    dic = {}
    for line in f:
        string1 = line.split('.')[1] 
        string2 = line.split('.')[2] 
        string3 =  string1 + '.' + string2
        chave = string3.split('-')[0]
        if chave not in dic:
            dic[chave] = 1
        else:
            dic[chave] += 1

    
    lista_chaves = list(dic.keys())
    lista_chaves.sort()

    with open('parte1_a.txt','w') as f2:
        for chave in lista_chaves:
            f2.write(chave + '-' + str(dic[chave])+'\n')
 
