import bcrypt

# regras de negócio importante. O ADM VAI CADASTRAR O CLIENT
# senha vai ser padrão e o usuário após o primeiro login vai trocar
#
# o que precisamos fazer que são coisas que não sei como:
# quando o usuário esquecer a senha enviar o código no seu email para ele trocar


def create_password_hash(password_user):
    password = password_user.encode("utf-8")

    hashed = bcrypt.hashpw(password, bcrypt.gensalt())

    return hashed


def check_password(password_user, password_valid):
    password = password_user.encode("utf-8")

    return bcrypt.checkpw(password, password_valid)
