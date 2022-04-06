import os
import time


def verificar_host(ip_ou_host):

    # Chamando system da biblioteca OS - usando o ping -n 6 executando 6 vezes
    os.system('ping -n 6 {}'.format(ip_ou_host))


def ping_multiplo(url_source, name_source):

    # hosts = path + file_hosts

    with open(url_source + name_source, 'r') as file:

        dump = file.read()
        dump = dump.splitlines()

        for x in dump:
            print('\nVerificando o ip: ', x)
            print('-' * 80)

            os.system('ping -n 2 {}'.format(x))

            print('-' * 80)
            time.sleep(5)


if __name__ == '__main__':

    source = 'd://projetos//repository//PycharmProjects//python-DIO//security//'
    source_name = 'hosts.txt'

    ping_multiplo(source, source_name)
