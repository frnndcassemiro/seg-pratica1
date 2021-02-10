tcp = open('tcp.txt','r')
    # alert tcp $EXTERNAL_NET any -> $HOME_NET 21 (msg:"PROTOCOL-FTP ADMw0rm ftp login attempt";
    # flow:to_server,established; 
    # content:"USER"; 
    # nocase; 
    # content:"w0rm"; 
    # distance:1; 
    # nocase; 
    # pcre:"/^USER\s+w0rm/smi"; 
    # metadata:ruleset community, service ftp; 
    # classtype:suspicious-login; 
    # sid:144;
    # rev:16;)

    ## alert tcp $EXTERNAL_NET any -> $HOME_NET 53 (msg:"OS-OTHER x86 FreeBSD overflow attempt"; 
    # flow:to_server,established; 
    # content:"|EB|n^|C6 06 9A|1|C9 89|N|01 C6|F|05|"; 
    # metadata:ruleset community, service dns; 
    # classtype:attempted-admin; 
    # sid:266;
    # rev:15;)

    for line in tcp:

udp = open('udp.txt','r')
ip = open('ip.txt','r')
icmp = open('icmp.txt','r')

file2 = open('sid-msg.map','r')

    dic = {}
    for line in f:
        if 
  
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
