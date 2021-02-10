with open('AV2.txt','r') as f:
    lista = []
    for line in f:
        #PUA.Win.Trojan.CVE_2012_1431-1:0:0:7f454c46????4a464946
        string1 = line.split('.')[1] #Win
        string2 = line.split('.')[2] #Trojan
        string3 = line.split('.')[3] #CVE_2012_1431-1:0:0:7f454c46????4a464946
       
        string4 = string3.split('-')[1] #1:0:0:7f454c46????4a464946
        string5 = string4.split(':') [0]

        chave = string1 + ',' + string2 + ',' + string3.split('-')[0] + ',' + string5
        lista.append(chave)

    with open('parte1_b.txt','w') as f2:
        for chave in lista:
            f2.write(chave +'\n')
 
