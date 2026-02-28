# Fazer a logica para dedscobrir as horas extras do usuário
# vamos ter que fazer um select e ver quantas horas deu, se der a mais que
# 8 horas por exemplo, calcula como horas extra.

# uma  boa ideia:
# Você fazer um SELECT buscando todos os pares de IN e OUT de um funcionário no dia.

# subtrai o horário de OUT pelo de IN para ter o total de horas trabalhadas.

# Se o resultado for maior que a carga horária padrão (ex: 8h), a diferença é a Hora Extra.


# SELECT date, action, hour
# FROM time_logs
# WHERE client_id = %s AND date BETWEEN %s AND %s
# ORDER BY date, hour;
#
