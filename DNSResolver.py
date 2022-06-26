import sys
import dns.resolver
try:
    dominio = sys.argv[1]
    nome_arquivo = sys.argv[2]
except:
    print 'Invalid args'
    print 'Usage: DNSbrute.py <domain> <wordlist>'
    sys.exit(1)
try:
    arquivo = open('nome_arquivo')
    subdominios = arquivo.read().splitlines()
for subdominio in subdominios:
    try:
        domesub=subdominio+'.'+dominio
        resultados = dns.resolver.query("example.com","a")
        for resultado in resultados:
            print domesub resultado
    except:
        print  + ' não encontrado.'
        pass
