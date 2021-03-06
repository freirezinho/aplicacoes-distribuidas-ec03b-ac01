import json


def pega_dados():
    with open('ano2018.json') as f:
        dados2018 = json.load(f)
    return dados2018


dados2018 = pega_dados()
'''
1 - grupo (OPE)
2 - data 25/02 até às 15h
3 - Colocar os nomes dos integrantes em ordem alfa
4 - Somente 1 aluno entrega
5 - Chamada vai ser pela entrega da AC1
6 - Somente o arquivo brasileirao.py

Integrantes:
1 - Caio Lorente da Rosa
2 - Lucas Barbosa Lima de Souza Santos
3 - Renan José da Silva
4 - Ronaldo Mendes da Silva
5 - Saulo Santos Freire

# repo no github: https://github.com/freirezinho/aplicacoes-distribuidas-ec03b-ac01

1. Crie uma função datas_de_jogo, que procura nos dados do 
brasileirão recebidas no parâmetro e devolve uma lista de todas 
as datas em que houve jogo.

As datas devem ter o mesmo formato que tinham nos dados do 
brasileirão.

Dica: busque em dados['fases'].

Observe que essa função (e todas as demais) recebem os dados dos
jogos num parâmetro chamado "dados". Essa variável contém todas 
as informações que foram lidas do arquivo JSON que acompanha 
essa atividade.
'''


def datas_de_jogo(dados):
    resposta = []
    for data in dados['fases']['2700']['jogos']['data']:
        resposta.append(data)
    return resposta


'''

2. Crie uma função data_de_um_jogo, que recebe a id numérica de 
um jogo e devolve a data em que ele ocorreu.

Se essa nao é uma id válida, você deve devolver a 
string 'não encontrado'.
Cuidado! Se você devolver uma string ligeiramente diferente, 
o teste vai falhar.

(você provavelmente vai querer testar sua função no braço e não
somente fazer os meus testes. Para isso, note que muitos números
nesse arquivo estão representados não como números, mas como 
strings)
'''


def data_de_um_jogo(dados, id_jogo):
    lista = dados['fases']['2700']['jogos']['data']
    for data in lista:
        if id_jogo in lista[data]:
            return data
    return 'não encontrado'


'''
3. Nos nossos dados, cada time tem um id, uma identificação 
numérica. (você pode consultar as identificações numéricas 
em dados['equipes']).

A próxima função recebe a id numérica de um jogo, e devolve as
ids numéricas dos dois times envolvidos.

Vou deixar um código pra você lembrar como retornar duas ids em
um único return.

def ids_dos_times_de_um_jogo(dados, id_jogo):
    time1 = 12
    time2 = 13
    return time1, time2 # Assim, retornamos as duas respostas 
    em um único return.
'''


def ids_dos_times_de_um_jogo(dados, id_jogo):
    t1 = dados['fases']['2700']['jogos']['id'][id_jogo]['time1']
    t2 = dados['fases']['2700']['jogos']['id'][id_jogo]['time2']
    return t1, t2


'''
4. A próxima função recebe a id_numerica de um time e deve 
retornar o seu 'nome-comum'.
'''


def nome_do_time(dados, id_time):
    return dados['equipes'][id_time]['nome-comum']


'''
5. A próxima função "cruza" as duas anteriores. Recebe uma id 
de um jogo e retorna os "nome-comum" dos dois times.
'''


def nomes_dos_times_de_um_jogo(dados, id_jogo):
    lista = dados['fases']['2700']['jogos']['id']
    t1 = ''
    t2 = ''
    for data in lista:
        if id_jogo in data:
            t1 = dados['equipes'][lista[data]['time1']]['nome-comum']
            t2 = dados['equipes'][lista[data]['time2']]['nome-comum']
    return t1, t2


'''
6. Façamos agora a busca "ao contrário". Conhecendo
o nome-comum de um time, queremos saber a sua id.

Se o nome comum não existir, retorne 'não encontrado'.
'''


def id_do_time(dados, nome_time):
    for time in dados['equipes']:
        if dados['equipes'][time]['nome-comum'] in nome_time:
            return dados['equipes'][time]['id']
    return 'não encontrado'


'''
7. Queremos procurar por 'Fla' e achar o Flamengo. 
Ou por 'Paulo' e achar o São Paulo.

Nessa busca, você recebe um nome, e verifica os campos
'nome-comum', 'nome-slug', 'sigla' e 'nome',
tomando o cuidado de aceitar times se a string
buscada aparece dentro do nome (A string "Paulo"
aparece dentro de "São Paulo").

Sua resposta deve ser uma lista de ids de times que "batem"
com a pesquisa (e pode ser vazia, se não achar ninguém).
'''


def busca_imprecisa_por_nome_de_time(dados, nome_time):
    lista_ids = []
    for id in dados['equipes']:
        time = dados['equipes'][id]
        if nome_time in time['nome'] and time['nome-comum'] and time['nome-slug']:
            lista_ids.append(dados['equipes'][id]['id'])
        elif nome_time in time['sigla']:
            lista_ids.append(dados['equipes'][id]['id'])
    return lista_ids


'''
8. Agora, a ideia é receber a id de um time e retornar as
ids de todos os jogos em que ele participou.
'''


def ids_de_jogos_de_um_time(dados, time_id):
    jogos = dados['fases']['2700']['jogos']
    ids_de_jogos_esperados = []
    for key, jogo in jogos['id'].items():
        if jogo['time1'] == time_id or jogo['time2'] == time_id:
            ids_de_jogos_esperados.append(key)
    return ids_de_jogos_esperados


'''
9. Usando as ids dos jogos em que um time participou, podemos 
descobrir em que dias ele jogou.

Note que essa função recebe o nome-comum do time, não a sua id.

Ela retorna uma lista das datas em que o time jogou.
'''


def datas_de_jogos_de_um_time(dados, nome_time):
    datas = []
    time_id_encontrado = ''
    for time_id in dados['equipes']:
        time = dados['equipes'][time_id]
        if nome_time in time['nome-comum']:
            time_id_encontrado = (dados['equipes'][time_id]['id'])

    jogos = dados['fases']['2700']['jogos']
    for _, jogo in jogos['id'].items():
        if jogo['time1'] == time_id_encontrado or jogo['time2'] == time_id_encontrado:
            datas.append(jogo['data'])
    return datas


'''
10. A próxima função recebe apenas o dicionário dos dados do 
brasileirão.
Ela devolve um dicionário, com quantos gols cada time fez.
'''


def dicionario_de_gols(dados):
    gols: dict = {}
    jogos = dados['fases']['2700']['jogos']['id']
    equipes: dict = {}
    for key, time in dados['equipes'].items():
        equipes[key] = time['nome-comum']
        gols[key] = 0
    for time_id in equipes:
        jogos_do_time = ids_de_jogos_de_um_time(dados, time_id)
        for key, jogo in jogos.items():
            if key in jogos_do_time:
                if jogo['time1'] == time_id:
                    gols[time_id] += int(jogo['placar1'])
                elif jogo['time2'] == time_id:
                    gols[time_id] += int(jogo['placar2'])
        jogos_do_time = []
    return gols
   
 
'''
11. A próxima função recebe apenas o dicionário dos dados do 
brasileirão.
Ela devolve a id do time que fez mais gols no campeonato.
'''


def time_que_fez_mais_gols(dados):
    result = dicionario_de_gols(dados)
    return max(result, key=result.get)



'''
12. A próxima função recebe apenas o dicionário dos dados do 
brasileirão. Ela devolve um dicionário. Esse dicionário conta, 
para cada estádio, quantas vezes ocorreu um jogo nele.

Ou seja, as chaves são ids de estádios e os valores associados,
o número de vezes que um jogo ocorreu no estádio.
'''


def dicionario_id_estadio_e_nro_jogos(dados):
    dados = {}
    d[('estadio'),('estadio_id')]
    
    


'''
13. A próxima função recebe apenas o dicionário dos dados do 
brasileirão. Ela retorna o número de times que o brasileirão 
qualifica para a libertadores.Ou seja, devolve quantos times 
são classificados para a libertadores (consultando
o dicionário de faixas).

Note que esse número está nos dados recebidos no parâmetro e 
você deve pegar esse número daí. Não basta retornar o valor 
correto, tem que acessar os dados fornecidos.
'''


def qtos_libertadores(dados):
    dados = {}
    for time in 
    return dados[]
    


'''
14. A próxima função recebe um valor com qtos times devem aparecer
na lista, e retorna esta lista, contendo as ids dos times melhor 
classificados.
'''


def ids_dos_melhor_classificados(dados, numero):
    return dados['fases']['2700']['classificacao']['grupo']['Único'][:numero]


'''
15. A próxima função usa as duas anteriores para retornar uma 
lista de todos os times classificados para a libertadores em
virtude do campeonato brasileiro.

Lembre-se de consultar a estrutura, tanto para obter a 
classificação, quanto para obter o número correto de times 
a retornar.

A função só recebe os dados do brasileirão.
'''

def classificados_libertadores(dados):
    pass


'''
16. Da mesma forma que podemos obter a informação dos times 
classificados para a libertadores, também podemos obter os 
times na zona de rebaixamento.

A próxima função recebe apenas o dicionário de dados do 
brasileirão, e retorna uma lista com as ids dos times rebaixados.

Consulte a zona de rebaixamento do dicionário de dados, não deixe
ela chumbada da função.
'''

def rebaixados(dados):
    faixas = dados['fases']['2700']['faixas-classificacao']
    classificados_ordenados = dados['fases']['2700']['classificacao']['grupo']['\u00danico']
    print(len(classificados_ordenados))
    inicio_rebaixamento = 0
    fim_rebaixamento = 1
    rebaixados = []
    for key, faixa in faixas.items():
        print(key)
        print(faixa)
        if faixa['texto'] == "Zona de rebaixamento":
            faixa_rebaixamento_split = faixa['faixa'].split('-')
            inicio_rebaixamento = int(faixa_rebaixamento_split[0])
            fim_rebaixamento = int(faixa_rebaixamento_split[1])
    for i in range(inicio_rebaixamento -1, fim_rebaixamento):
        print(classificados_ordenados[i])
        rebaixados.append(classificados_ordenados[i])
    return rebaixados


'''
17. A próxima função recebe (além do dicionario de dados 
do brasileirão) uma id de time.

Ela retorna a classificação desse time no campeonato.

Se a id nao for válida, ela retorna a string 'não encontrado'.
'''


def classificacao_do_time_por_id(dados, time_id):
    classificados_ordenados: list = dados['fases']['2700']['classificacao']['grupo']['\u00danico']
    if time_id in classificados_ordenados:
        posicao = classificados_ordenados.index(time_id) + 1
        return posicao
    else:
        return 'não encontrado'
    pass
