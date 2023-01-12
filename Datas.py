import datetime
import time

# YYYY-MM-DD
data_atual = datetime.date.today()
print(data_atual)

# DD/MM/YYYY
data_brasil = data_atual.strftime("%d/%m/%y")
print(data_brasil)

# IMPRIME HORA E DATA
data_e_hora_atuais = datetime.datetime.now()
print(data_e_hora_atuais)
data_e_hora_em_texto = data_e_hora_atuais.strftime("%d/%m/%Y")
print(data_e_hora_em_texto)
data_e_hora_em_texto = data_e_hora_atuais.strftime("%d/%m/%Y %H:%M")
print(data_e_hora_em_texto)

# FUSO HORARIO
diferenca = datetime.timedelta()
print(diferenca)

# FUSO HORARIO COM DIFERENÇA DE 3 HORAS
diferenca = datetime.timedelta(hours=-3)
print(diferenca)

#  RESOLVENDO O PROBLEMA DO FUSO HORARIO
fuso_horario = datetime.timezone(diferenca)
print(fuso_horario)

data_e_hora = data_e_hora_atuais.astimezone(fuso_horario)
print(data_e_hora)