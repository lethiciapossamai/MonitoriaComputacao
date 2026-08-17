arquivo=open('dados_eleicao.txt',encoding='utf-8')
dados=arquivo.read()

limpeza_01=dados.strip()
limpeza_02=limpeza_01.split('\n')
limpeza_03=[]

for elemento in limpeza_02:
    limpeza_03.append(elemento.replace(" ", "") .split('\t'))
for elemento in limpeza_03:
    string_suja = elemento[2]
    string_limpa = string_suja.replace('\xa0', '')
    elemento[2] = string_limpa
candidatos={}
bairros={}
votos_candidato=[]
votos_bairro=[]
for elemento in limpeza_03:
    votos_candidato.append(elemento[2])
    candidatos[elemento[2]]=[]
    votos_bairro.append(elemento[1])
    bairros[elemento[1]]=[]
for elemento in limpeza_03:
    while len(candidatos[elemento[2]])<2:
        candidatos[elemento[2]].append(votos_candidato.count(elemento[2]))
        candidatos[elemento[2]].append((votos_candidato.count(elemento[2])/len(votos_candidato))*100)
for elemento in limpeza_03:
    while len(bairros[elemento[1]])<2:
        bairros[elemento[1]].append(votos_bairro.count(elemento[1]))
        bairros[elemento[1]].append((votos_bairro.count(elemento[1])/len(votos_bairro))*100)
junção={}
for elemento in limpeza_03[1:]:
    candidato=elemento[2]
    bairro=elemento[1]
    
    if candidato not in junção:
        junção[candidato]={}
        junção[candidato][bairro] =+ 1
    
print(junção)


print(bairros)