from datetime import date, time, datetime, timedelta


def trabalhando_com_date():

    data_atual = date.today()
    # Todas serão convertidas para STRING:

    data_atual_bar = data_atual.strftime('%d/%m/%Y')
    print(data_atual_bar)

    data_atual_ext = data_atual.strftime('%A, %B de %Y')
    print(data_atual_ext)


def trabalhando_com_time():
    horario = time(hour=15, minute=18, second=30)
    horario_str = horario.strftime('%H:%M:%S')
    print(horario_str)


def trabalhando_com_datetime():
    data_atual = datetime.now()
    print(data_atual)
    print(data_atual.strftime('%d/%m/%Y'))
    print(data_atual.strftime('%H:%M:%S'))
    print(data_atual.strftime('%d/%m/%Y %H:%M:%S'))
    print(data_atual.strftime('%c'))
    print(data_atual.day)
    print(data_atual.year)
    print(data_atual.month)
    print(data_atual.hour)
    print(data_atual.minute)
    print(data_atual.weekday())
    print(data_atual.weekday())


def trabalhando_com_dias():

    data_dia = datetime.now()
    tupla = ('Segunda', 'Terça', 'Quarta', 'Quinta', 'Sexta', 'Sábado', 'Domingo')
    dia = tupla[data_dia.weekday()]
    print(dia)


def passando_a_data(dia, mes, ano, hora, minuto, seg):

    recebe_data = datetime(ano, mes, dia, hora, minuto, seg)
    print(recebe_data)
    print(recebe_data.strftime('%c'))


def converte_para_data(data_str):
    data_convertida = datetime.strptime(data_str, '%d/%m/%Y %H:%M:%S')
    print(data_convertida)


def deduzir_dias_data(dias, horas, minutos, data_str):

    data_antiga = datetime.strptime(data_str,'%d/%m/%Y %H:%M:%S')
    nova_data = data_antiga - timedelta(days=dias, hours=horas, minutes=minutos)
    print(nova_data)

def adicionar_dias_data(dias, horas, minutos, data_str):

    data_antiga = datetime.strptime(data_str,'%d/%m/%Y %H:%M:%S')
    nova_data = data_antiga + timedelta(days=dias, hours=horas, minutes=minutos)
    print(nova_data)

if __name__ == '__main__':

    trabalhando_com_date()

    trabalhando_com_time()

    trabalhando_com_datetime()

    trabalhando_com_dias()
    passando_a_data(20, 6, 2022, 13, 47, 20)
    converte_para_data('01/01/2022 12:20:22')
    deduzir_dias_data(30, 0, 22, '01/01/2022 12:20:22')
    adicionar_dias_data(30, 0, 22, '01/01/2022 12:20:22')
