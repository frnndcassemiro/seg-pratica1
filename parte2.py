import re  

file1 = open('xablau.txt','r')
file3 = open('parte2.txt','w')

for line in file1:
    prot = re.search(r'^.*alert ([a-z]+).*',line).group(1)
    port = re.search(r'^.+ ([0-9|a-z|A-Z|\_|\$|\:|[\[|\]|\,]+) \(',line).group(1)
    sid = re.search(r'^.+sid:([0-9]+).*',line).group(1)
    # file3.writelines('resultado: protocolo:'+ prot + ' - porta:'+ port + ' - sid:' + sid)
    sid_def = None
    file2 = open('sid-msg.map','r')
    for line2 in file2:
        # print 'sid->' + str(sid)
        # print 'line split->' + str(line2.split(' || ')[0])
        if str(sid) == str(line2.split(' || ')[0]):
            sid_def = str(line2.split(' || ')[1])
            sid_def = sid_def.replace("\n", "")
            # print 'sid def->'+ sid_def
            break
            # print str(sid) + '==' +  str(line2.split('||')[0])
    file2.close()
    
    # print string1 + '-' + str(sid_def)
    if prot == 'tcp':
        file3.write('1,'+ port +','+ str(sid_def))
    if prot == 'udp':
        file3.write('2,'+ port +','+ str(sid_def))
    if prot == 'ip':
        file3.write('0,'+ port +','+ str(sid_def))
    if prot == 'icmp':
        file3.write('3,'+ port +','+ str(sid_def))
    file3.write('\n')
file1.close()
file3.close()