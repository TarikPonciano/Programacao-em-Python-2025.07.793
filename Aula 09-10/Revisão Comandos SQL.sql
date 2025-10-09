CREATE TABLE "Alunos" (
matricula_aluno integer GENERATED 
ALWAYS AS IDENTITY PRIMARY KEY,
nome_aluno varchar(255) NOT NULL,
cpf_aluno char(11) NOT NULL UNIQUE,
ano_nasc_aluno integer NOT NULL 
DEFAULT 2025,
tel_aluno char(11) NOT NULL 
DEFAULT 'Sem Tel',
end_aluno varchar(255) NOT NULL
DEFAULT 'Sem Endereço Cadastrado',
CONSTRAINT chk_tamanho_cpf CHECK(LENGTH(cpf_aluno) = 11)
);

INSERT INTO "Alunos"
VALUES (default, 'Joaquim Silva', '12345678910', 
2000, default, default), (default, 'Maria Antonia', '12345678911',
2005, default, default);

SELECT * FROM "Alunos"
WHERE matricula_aluno >= 1
ORDER BY nome_aluno DESC;

UPDATE "Alunos"
SET
ano_nasc_aluno = 2007
WHERE matricula_aluno = 1 OR LENGTH(cpf_aluno) = 11;

DELETE FROM "Alunos"
WHERE matricula_aluno = 1;

CREATE TABLE "Disciplina" (
codigo_disciplina integer GENERATED ALWAYS AS IDENTITY PRIMARY KEY,
nome_disciplina varchar(255) NOT NULL,
codigo_curso integer NOT NULL DEFAULT 100
);

CREATE TABLE "Matricula"(
codigo_matricula integer GENERATED ALWAYS AS IDENTITY PRIMARY KEY,
aluno_matricula integer,
disciplina_codigo integer,
faltas_matricula NUMERIC(3,1) DEFAULT 0,
CONSTRAINT fk_matricula_aluno 
FOREIGN KEY (aluno_matricula)
REFERENCES "Alunos"(matricula_aluno),
CONSTRAINT fk_matricula_disciplina
FOREIGN KEY (disciplina_codigo)
REFERENCES "Disciplina"(codigo_disciplina)
);
INSERT INTO "Disciplina"
VALUES (default, 'Matemática', default);
INSERT INTO "Matricula"
VALUES (default, 1, 1, default);

SELECT * FROM "Matricula";
