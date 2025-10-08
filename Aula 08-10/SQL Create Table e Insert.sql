CREATE TABLE "Alunos"(
matricula_aluno integer GENERATED ALWAYS AS IDENTITY PRIMARY KEY,
nome_aluno varchar(255) NOT NULL,
cpf_aluno char(11) NOT NULL UNIQUE,
anonasc_aluno integer NOT NULL DEFAULT 2025,
tel_aluno char(11) NOT NULL DEFAULT 'Sem Tel',
end_aluno varchar(255) NOT NULL DEFAULT 'Sem Endereço Cadastrado'
);

INSERT INTO "Alunos" (nome_aluno, anonasc_aluno, cpf_aluno, tel_aluno, end_aluno) VALUES
('João Silva', 2000, '12345678900', '11987654321', 'Rua A, 123'),
('Maria Oliveira', 1999, '23456789011', '11987654322', 'Rua B, 456'),
('Pedro Souza', 2001, '34567890122', '11987654323', 'Rua C, 789'),
('Ana Santos', 2000, '45678901233', '11987654324', 'Rua D, 101'),
('Carlos Pereira', 1998, '56789012344', '11987654325', 'Rua E, 202'),
('Fernanda Lima', 2002, '67890123455', '11987654326', 'Rua F, 303'),
('Lucas Almeida', 2000, '78901234566', '11987654327', 'Rua G, 404'),
('Camila Rocha', 1997, '89012345677', '11987654328', 'Rua H, 505'),
('Rafael Costa', 2001, '90123456788', '11987654329', 'Rua I, 606'),
('Larissa Martins', 1999, '01234567899', '11987654330', 'Rua J, 707'),
('Gustavo Oliveira', 2000, '12345678911', '11987654331', 'Rua K, 808'),
('Patricia Silva', 2001, '23456789022', '11987654332', 'Rua L, 909'),
('Bruna Souza', 2002, '34567890133', '11987654333', 'Rua M, 1010'),
('Felipe Lima', 1998, '45678901244', '11987654334', 'Rua N, 1111'),
('Eduardo Rocha', 2001, '56789012355', '11987654335', 'Rua O, 1212'),
('Juliana Costa', 1999, '67890123466', '11987654336', 'Rua P, 1313'),
('Tiago Martins', 2000, '78901234577', '11987654337', 'Rua Q, 1414'),
('Paula Oliveira', 2001, '89012345688', '11987654338', 'Rua R, 1515'),
('Marcos Santos', 2000, '90123456799', '11987654339', 'Rua S, 1616'),
('Roberta Almeida', 1998, '01234567800', '11987654340', 'Rua T, 1717');


INSERT INTO "Disciplina" (nome_disciplina, codigo_curso) VALUES
('Matemática I', 101),
('Física I', 102),
('Química I', 103),
('Biologia I', 104),
('Informática I', 105);

INSERT INTO "Matricula" (matricula_aluno, codigo_disciplina, ano_matricula, semestre_matricula, nota_matricula, faltas_matricula) VALUES
(1, 1, 2023, '1º', 7.5, 2),
(1, 2, 2023, '1º', 8.0, 3),
(2, 3, 2023, '1º', 9.0, 1),
(3, 4, 2023, '1º', 6.0, 4),
(4, 5, 2023, '1º', 10.0, 0),
(5, 1, 2023, '2º', 7.2, 2),
(6, 2, 2023, '2º', 8.5, 1),
(7, 3, 2023, '2º', 7.0, 5),
(8, 4, 2023, '2º', 6.5, 3),
(9, 5, 2023, '2º', 9.5, 0);

SELECT * FROM "Alunos";
SELECT * FROM "Disciplina";
SELECT * FROM "Matricula";