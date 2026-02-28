# retorna a senha do usuário
# para comparar com a senha que ele forneceu
GET_PASS_DATA_BASE = """
    SELECT password_hash FROM login WHERE id = %s 
"""
