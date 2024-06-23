# Projeto-Sistema-de-Gerenciamento-de-Alunos---SENAC
Desenvolva um sistema em Python para gerenciar informações de alunos. O sistema deve utilizar funções, tuplas, listas, testes lógicos, estruturas de repetição e sets.
### Relatório descrevendo o funcionamento de cada função

### Relatório do Sistema de Gerenciamento de Alunos

### Funções Implementadas:

1. **cadastrar_aluno**
    - **Descrição**: Cadastra um novo aluno, garantindo que a matrícula não seja repetida.
    - **Parâmetros**:
        - `alunos` (list): Lista de tuplas com informações dos alunos.
        - `matriculas_usadas` (set): Conjunto de números de matrícula já usados.
    - **Retorno**: Nenhum.
2. **listar_alunos**
    - **Descrição**: Lista todos os alunos cadastrados.
    - **Parâmetros**:
        - `alunos` (list): Lista de tuplas com informações dos alunos.
    - **Retorno**: Nenhum.
3. **buscar_aluno_por_matricula**
    - **Descrição**: Busca um aluno pelo número de matrícula.
    - **Parâmetros**:
        - `alunos` (list): Lista de tuplas com informações dos alunos.
    - **Retorno**: Tupla com informações do aluno encontrado ou `None` se não encontrado.
4. **atualizar_informacoes_aluno**
    - **Descrição**: Atualiza a idade de um aluno a partir da matrícula.
    - **Parâmetros**:
        - `alunos` (list): Lista de tuplas com informações dos alunos.
    - **Retorno**: Nenhum.
5. **remover_aluno**
    - **Descrição**: Remove um aluno a partir da matrícula.
    - **Parâmetros**:
        - `alunos` (list): Lista de tuplas com informações dos alunos.
        - `matriculas_cursos` (dict): Dicionário de matrículas com sets de cursos.
        - `matriculas_usadas` (set): Conjunto de números de matrícula já usados.
    - **Retorno**: Nenhum.
6. **gerenciar_cursos**
    - **Descrição**: Gerencia cursos, permitindo adicionar, remover e listar cursos.
    - **Parâmetros**:
        - `cursos` (set): Conjunto de cursos disponíveis.
    - **Retorno**: Nenhum.
7. **matricular_aluno_em_curso**
    - **Descrição**: Matricula um aluno em um curso.
    - **Parâmetros**:
        - `alunos` (list): Lista de tuplas com informações dos alunos.
        - `cursos` (set): Conjunto de cursos disponíveis.
        - `matriculas_cursos` (dict): Dicionário de matrículas com sets de cursos.
    - **Retorno**: Nenhum.
8. **listar_matriculas**
    - **Descrição**: Lista matrículas de alunos em cursos.
    - **Parâmetros**:
        - `alunos` (list): Lista de tuplas com informações dos alunos.
        - `matriculas_cursos` (dict): Dicionário de matrículas com sets de cursos.
    - **Retorno**: Nenhum.

### 3. Exemplos de uso para cada funcionalidade implementada

### 1. Cadastro de Alunos

```python

alunos = []
matriculas_usadas = set()
cadastrar_aluno(alunos, matriculas_usadas)

```

**Exemplo de uso:**

```arduino

Digite o nome do aluno: João
Digite a idade do aluno: 20
Digite a matrícula do aluno: 1
Aluno João cadastrado com sucesso!

```

### 2. Listar Alunos

```python

listar_alunos(alunos)

```

**Exemplo de uso:**

```yaml

Aluno: João, Idade: 20, Matrícula: 1

```

### 3. Buscar Aluno por Matrícula

```python

buscar_aluno_por_matricula(alunos)

```

**Exemplo de uso:**

```yaml

Digite a matrícula do aluno: 1
Aluno encontrado: Nome: João, Idade: 20, Matrícula: 1

```

### 4. Atualizar Informações do Aluno

```python

atualizar_informacoes_aluno(alunos)

```

**Exemplo de uso:**

```less

Digite a matrícula do aluno para atualizar a idade: 1
Digite a nova idade para o aluno João: 21
Idade do aluno João atualizada com sucesso!

```

### 5. Remover Aluno

```python

matriculas_cursos = {}
remover_aluno(alunos, matriculas_cursos, matriculas_usadas)

```

**Exemplo de uso:**

```arduino

Digite a matrícula do aluno para remover: 1
Aluno João removido com sucesso!

```

### 6. Gerenciar Cursos

```python

cursos = set()
gerenciar_cursos(cursos)

```

**Exemplo de uso:**

```python

Digite [1] para adicionar curso, [2] para remover curso, [3] para listar cursos, [0] para sair: 1
Digite o nome do curso para adicionar: Matemática
Curso Matemática adicionado com sucesso!

```

### 7. Matricular Aluno em Curso

```python
pythonCopiar código
matriculas_cursos = {}
matricular_aluno_em_curso(alunos, cursos, matriculas_cursos)

```

**Exemplo de uso:**

```python

Digite a matrícula do aluno: 1
Aluno encontrado: Nome: João, Idade: 20, Matrícula: 1
Cursos disponíveis:
Matemática
Digite o nome do curso para matricular o aluno: Matemática
Aluno João matriculado no curso Matemática com sucesso!

```

### 8. Listar Matrículas em Cursos

```python

listar_matriculas(alunos, matriculas_cursos)

```

**Exemplo de uso:**

```python

Aluno: João, Matrícula: 1, Cursos: Matemática
