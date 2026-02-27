CREATE DATABASE IF NOT EXISTS time_sheet;
USE time_sheet;

-- Tabela de Clientes/Funcionários
CREATE TABLE client (
    id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(50) NOT NULL,
    -- O banco gera a data de admissão sozinho no cadastro
    date_admission DATE NOT NULL DEFAULT (CURRENT_DATE)
);

-- Tabela de Registros de Ponto
CREATE TABLE time_logs (
    id INT AUTO_INCREMENT PRIMARY KEY,
    -- O Python deve enviar a data e a hora nestas colunas
    date DATE NOT NULL,
    hour TIME NOT NULL,
    action ENUM('IN', 'OUT') NOT NULL,
    client_id INT NOT NULL,
    CONSTRAINT fk_time_logs_client 
        FOREIGN KEY (client_id) REFERENCES client(id) 
        ON DELETE CASCADE
);

-- Tabela de Login
CREATE TABLE login (
    id INT AUTO_INCREMENT PRIMARY KEY,
    email VARCHAR(100) NOT NULL UNIQUE,
    password VARCHAR(255) NOT NULL,
    client_id INT NOT NULL,
    CONSTRAINT fk_login_client 
        FOREIGN KEY (client_id) REFERENCES client(id) 
        ON DELETE CASCADE
);



-- a coluna date_admission da tabela client cria a data automaticamente