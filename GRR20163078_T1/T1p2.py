import sys 
import re  

arq = sys.argv[1] #community.rules
arq2 = sys.argv[2] #sid-msg.map
file1 = open(arq,'r')
file3 = open('T1p2.txt','w')
erros = open('T1p2_erros.txt','w') 

for line in file1:
    try:
        prot = re.search(r'[# ]*alert ([a-z]+).*',line).group(1) #expressao regular para reconhecer o protocolo
        port = re.search(r'^.+ ([0-9|a-z|A-Z|\_|\$|\:|[\[|\]|\,]+) \(',line).group(1) #expressao regular para reconhecer a porta
        sid = re.search(r'^.+sid:([0-9]+).*',line).group(1) #expressao regular para reconhecer o sid
      
        sid_def = None
        file2 = open(arq2,'r')
        for line2 in file2: # procura o arquivo sid-msg.map a descricao do sid correspondente
            if str(sid) == str(line2.split(' || ')[0]): #
                sid_def = str(line2.split(' || ')[1])
                sid_def = sid_def.replace("\n", "")
                break
        file2.close()
        
        saida = None
        
        #formata a saida:
        if prot == 'ip':
            saida = '0,'+ port +','+ str(sid_def)
        if prot == 'tcp':
            saida = '1,'+ port +','+ str(sid_def)
        if prot == 'udp':
            saida = '2,'+ port +','+ str(sid_def)
        if prot == 'icmp':
            saida = '3,'+ port +','+ str(sid_def)
        
        file3.write(saida)
        file3.write('\n')
    
    except:
        erros.write('Linha nao interpretada(fora do padrao):' + line)


file1.close()
file3.close()
erros.close()