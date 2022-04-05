import shutil


def escrever_arquivo(url_source, name_source, texto):

    arquivo = open(url_source + name_source, 'w')
    arquivo.write(texto)
    arquivo.close()


def atualizar_arquivo(url_source, name_source, texto):

    arquivo = open(url_source + name_source, 'a')
    arquivo.write(texto)
    arquivo.close()


def ler_arquivo(url_source, name_source):
    arquivo = open(url_source + name_source, 'r')
    texto = arquivo.read()
    print(texto)


def copiar_arquivo(url_source, name_source, url_destiny, name_destiny):

    shutil.copy(url_source + name_source, url_destiny + name_destiny)


def move_arquivo(url_source, name_source, url_destiny, name_destiny):

    shutil.move(url_source + name_source, url_destiny + name_destiny)


def media_notas(url_source, name_source):
    arquivo = open(url_source + name_source, 'r')
    notas = arquivo.read()
    # lista para receber no final nome e nota
    lista_aluno_media = []
    # converte linhas em lista a partir da quebra de linha
    lista_tuplas = notas.split('\n')

    for x in lista_tuplas:
        # varrer lista separar por vírgula
        lista_notas = x.split(',')
        # print(lista_notas)
        # atribuir 1ª posição à variável, separar texto dos valores
        aluno = lista_notas[0]
        # eliminar a 1ª posição e deixando apenas os números
        lista_notas.pop(0)
        # lambda média, converte texto em número e calcula média
        media = lambda asnotas: sum([int(i) for i in asnotas]) / 4
        # adicionar a lista_aluno_media aluno e média das notas
        # a função media() recebe a lista_notas para calcular média
        lista_aluno_media.append({aluno: media(lista_notas)})
        print(lista_aluno_media)
    # retorna lista depois de finalizar o for
    return lista_aluno_media


if __name__ == '__main__':

    source = 'd://projetos//repository//PycharmProjects//python-DIO//'
    destiny = 'd://projetos//repository//PycharmProjects//python-DIO//'

    source_name = 'notas.txt'
    destiny_name = 'media.txt'

    texto1 = '\nHenrique,7,8,8,8'

    # copiar arquivo
    copiar_arquivo(source, source_name, destiny, destiny_name)
    # lista com alunos e suas médias
    # lista_media = media_notas(source, source_name)
    # print(lista_media)
