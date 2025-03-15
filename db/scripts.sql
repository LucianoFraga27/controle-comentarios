CREATE TABLE USUARIO (
    ID INT AUTO_INCREMENT PRIMARY KEY,
    NOME VARCHAR(100) NOT NULL,
    EMAIL VARCHAR(100) UNIQUE NOT NULL
);

INSERT INTO USUARIO (nome, email) VALUES 
('João Silva', 'joao.silva@email.com'),
('Maria Oliveira', 'maria.oliveira@email.com'),
('Carlos Santos', 'carlos.santos@email.com'),
('Ana Costa', 'ana.costa@email.com'),
('Pedro Rocha', 'pedro.rocha@email.com');

CREATE TABLE COMENTARIO (
    ID INT AUTO_INCREMENT PRIMARY KEY,
    TITULO VARCHAR(100) NOT NULL,
    DESCRICAO VARCHAR(200) NOT NULL,
    ID_USUARIO INT,
    FOREIGN KEY (ID_USUARIO) REFERENCES USUARIO(ID)
);

INSERT INTO COMENTARIO (titulo, descricao, usuario_id) VALUES
('Ótimo conteúdo', 'Gostei muito do vídeo!', 1),
('Precisa melhorar', 'A qualidade do áudio está ruim.', 2),
('Fake news', 'Informação incorreta, verifiquem as fontes.', 3),
('Muito bom', 'Conteúdo bem explicado e direto ao ponto.', 4),
('Repetitivo', 'O vídeo tem muita enrolação.', 5);
