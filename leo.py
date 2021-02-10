import re  
file2 = open('sid-msg.map','r')

    dic = {}
file1 = open('xablauzin.txt','r')
for line in file1:
    sid = re.search("sid:[0-9]+", line)
    print(sid)
    # sid = re.match(r'(?<=sid:)[0-9]+',line)
    # prot = re.match(r"^.*alert '(.*)' \$.*$",line)
    # porta = re.match(r"^.*alert '(.*)' \$.*$",line)

    with open('parte1_a.txt','w') as f2:
        for chave in lista_chaves:
            f2.write(chave + '-' + str(dic[chave])+'\n')
 


#0 alert tcp $HOME_NET 2589 -> $EXTERNAL_NET any (msg:"MALWARE-BACKDOOR - Dagger_1.4.0"
#1 flow:to_client,established
#2 content:"2|00 00 00 06 00 00 00|Drives|24 00|"
#3 depth:16
#4 metadata:ruleset community
#5 classtype:misc-activity
#6 sid:105
#7 rev:14
#8 )

#0 alert tcp $HOME_NET 15104 -> $EXTERNAL_NET any (msg:"MALWARE-OTHER mstream handler to client"
#1  flow:to_client,established
#2 content:">"
#3 metadata:ruleset community
#4 reference:cve,2000-0138
#5 classtype:attempted-dos
#6 sid:250
#7 rev:10
# )
