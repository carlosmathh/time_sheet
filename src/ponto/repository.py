# Inserir no banco quando o usuário clickar no  REGISTRAR PONTO
REGISTER_CLOCK = """
    INSERT INTO time_logs(date, hour, action, id_client) VALUES (%s, %s, %s, %s)
"""
