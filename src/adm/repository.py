# -----------------------------------------------------------
# CADASTRO CLIENT
# Querie que o adm vai usar para cadastrar o usuário
# Primeito tem que ser cadastrado o nome
# Depois deve ser cadastrado o email e senha pelo adm
REGISTER_CLIENT_NAME = """
    INSERT INTO client (name, active) VALUES (%s, 1)  
"""

REGISTER_CLIENT_PASS_EMAIL = """
    INSERT INTO login (email, password_hash) VALUES (%s,%s)
"""
# -----------------------------------------------------------


# -----------------------------------------------------------
# RELATÓRIOS
# retorna dados do client do periodo selecionado (between) de entrada ou saída (action)
REPORTS_IN_OUT_PERIOD = """
SELECT c.name, t.date, t.hour 
FROM time_logs t
JOIN client c ON t.client_id = c.id
WHERE t.action = %s
  AND t.date BETWEEN %s AND %s
ORDER BY t.date, t.hour;
"""

# Vai retornar os dados da hora do dia para ser usar na lógica de soma de horas extras
REPORTS_OVERTIME = """

"""

# -----------------------------------------------------------
