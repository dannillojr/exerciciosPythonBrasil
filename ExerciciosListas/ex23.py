'''
A ACME Inc., uma empresa de 500 funcionários, 
está tendo problemas de espaço em disco no seu servidor de arquivos. 
Para tentar resolver este problema, o Administrador de Rede precisa saber qual o espaço ocupado pelos usuários, 
e identificar os usuários com maior espaço ocupado. Através de um programa, baixado da Internet, ele conseguiu 
gerar o seguinte arquivo, chamado "usuarios.txt":

alexandre       456123789
anderson        1245698456
antonio         123456456
carlos          91257581
cesar           987458
rosemary        789456125

Neste arquivo, o nome do usuário possui 15 caracteres. A partir deste arquivo, 
você deve criar um programa que gere um relatório, chamado "relatório.txt", no seguinte formato:
ACME Inc.  Uso do espaço em disco pelos usuários
------------------------------------------------------------------------
Nr.  Usuário        Espaço utilizado     % do uso

1    alexandre       434,99 MB             16,85%
2    anderson       1187,99 MB             46,02%
3    antonio         117,73 MB              4,56%
4    carlos           87,03 MB              3,37%
5    cesar             0,94 MB              0,04%
6    rosemary        752,88 MB             29,16%

Espaço total ocupado: 2581,57 MB
Espaço médio ocupado: 430,26 MB

O arquivo de entrada deve ser lido uma única vez, e os dados armazenados em memória, 
caso sejam necessários, de forma a agilizar a execução do programa. 
A conversão da espaço ocupado em disco, de bytes para megabytes deverá 
ser feita através de uma função separada, que será chamada pelo programa 
principal. O cálculo do percentual de uso também deverá ser feito através 
de uma função, que será chamada pelo programa principal.
'''
from ex23_funcoes import calcular_byte_para_megabyte, calcular_percentual

arquivo = open('ExerciciosListas/arquivosEx23/usuarios.txt', 'r')
relatorio = open('ExerciciosListas/arquivosEx23/relatorio.txt', 'w')

usuarios = []
espaco_ocupado = []
bytes_convertidos_megabyte = []
cont = 0
for linha in arquivo:
    
    nome, espaco = linha.strip().split(',')

    usuarios.append(nome.strip())
    espaco_ocupado.append(int(espaco.strip()))

for bytes in espaco_ocupado:
    bytes_convertidos = calcular_byte_para_megabyte(bytes)
    bytes_convertidos_megabyte.append(bytes_convertidos)

megabyte_total = sum(bytes_convertidos_megabyte)

relatorio.write(f'ACME Inc.               Uso do espaço em disco pelos usuários\n')
relatorio.write(f'------------------------------------------------------------------------\n')
relatorio.write(f'{"Nr.":<10} {"Usuario":<15} {"Espaço Utilizado":<18} {"% de uso":<15}\n\n')
for user, megabyte in zip(usuarios, bytes_convertidos_megabyte):
    cont += 1
    porcentual = calcular_percentual(megabyte,megabyte_total)
    relatorio.write(f'{cont:<10}{user:<17} {megabyte:>8.2f} {porcentual:>15.2f}\n')

relatorio.close()
arquivo.close()

print('Relatorio salvo em "relatorio.txt"')



