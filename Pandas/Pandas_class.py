import pandas as pd
import matplotlib.pyplot as plt

url = 'https://raw.githubusercontent.com/alura-cursos/pandas-conhecendo-a-biblioteca/main/desafios/alunos.csv'

dados = pd.read_csv(url)
print(dados.head(7))
print(dados.tail(5))
print(dados.shape)
print(dados.describe())

# Exercícios referente aos dados de aluguel de imóveis
url_aluguel = 'https://raw.githubusercontent.com/alura-cursos/pandas-conhecendo-a-biblioteca/main/base-de-dados/aluguel.csv'

dados = pd.read_csv(url_aluguel, delimiter=';')

dados_apartamentos = dados.query('Tipo == "Apartamento"')

quartos = dados_apartamentos['Quartos'].mean()
alugueis = dados_apartamentos.groupby('Bairro')[['Valor']].mean().sort_values('Valor')
alugueis_elevados = alugueis[-5:]

print(quartos)

print(alugueis)

alugueis_elevados.plot(kind='barh', figsize=(14,10), color='black')
plt.show()

# 1) Verifique se a base de dados possui dados nulos e, caso tenha, realize o tratamento desses dados nulos da forma que achar mais coerente com a situação.

# 2) Os alunos "Alice" e "Carlos", não fazem mais parte da turma. Sendo assim, remova-os da base de dados.

# 3) Aplique um filtro que selecione apenas os alunos que foram aprovados.

# 4) Salve o DataFrame que possui apenas os alunos aprovados em um arquivo csv chamado "alunos_aprovados.csv".

# Extra: Ao conferir as notas dos alunos aprovados, notamos que algumas notas estavam incorretas. As alunas que tiraram nota 7.0, na verdade, tinham um ponto extra que não foi contabilizado. Sendo assim, substitua as notas 7.0 da base de dados por 8.0. Dica: pesquise pelo método replace.


df = pd.read_csv(url)

print(df.isnull().sum())
df.fillna(0, inplace=True)

df.drop([7,8], axis=0, inplace=True)
print(df)
aprovados = df.query('Aprovado == True')
print(aprovados)
aprovados.to_csv('alunos_aprovados.csv')

aprovados.loc[aprovados['Notas'] == 7.0, 'Notas'] = 8.0
aprovados.to_csv('alunos_aprovados.csv')
print(aprovados)

#------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
# 1) Os alunos participaram de uma atividade extracurricular e ganharam pontos extras. Esses pontos extras correspondem a 40% da nota atual de cada um deles. Com base nisso, crie uma coluna chamada "Pontos_extras" que contenha os pontos extras de cada aluno, ou seja, 40% da nota atual deles.

# 2) Crie mais uma coluna, chamada "Notas_finais" que possua as notas de cada aluno somada com os pontos extras.

# 3) Como houve uma pontuação extra, alguns alunos que não tinham sido aprovados antes podem ter sido aprovados agora. Com base nisso, crie uma coluna chamada "Aprovado_final" com os seguintes valores:

# True: caso o aluno esteja aprovado (nota final deve ser maior ou igual a 6);
# False: caso o aluno esteja reprovado (nota final deve ser menor que 6).
# 4) Faça uma seleção e verifique quais alunos não tinham sido aprovados anteriormente, mas foram aprovados após a soma dos pontos extras.


url = 'https://raw.githubusercontent.com/alura-cursos/pandas-conhecendo-a-biblioteca/main/desafios/alunos.csv'

df = pd.read_csv(url)
df['Pontos_extras'] = df['Notas'] * 0.40
df['Notas_finais'] = df['Notas'] + df['Pontos_extras']
df['Aprovado_inicial'] = df['Notas'].apply(lambda x: True if x >= 6 else False)
df['Aprovado_final'] = df['Notas_finais'].apply(lambda x: True if x >= 6 else False)
print(df.query('Aprovado_inicial == False & Aprovado_final == True'))
df['Reaprovados'] = (df['Aprovado_inicial'] == False) & (df['Aprovado_final'] == True)

df.fillna(0, inplace=True)

print(df)






