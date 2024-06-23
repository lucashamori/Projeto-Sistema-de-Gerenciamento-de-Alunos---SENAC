def cadastrar_aluno(alunos, matriculas_usadas):
    """
    Função para cadastrar um novo aluno.
    Verifica se a matrícula já foi usada e, em caso negativo, cadastra o aluno.

    Args:
    alunos (list): Lista de tuplas com informações dos alunos.
    matriculas_usadas (set): Conjunto de números de matrícula já usados.

    Returns:
    None
    """
    nome = input('Digite o nome do aluno: ')
    idade = int(input('Digite a idade do aluno: '))
    while True:
        matricula = int(input('Digite a matrícula do aluno: '))
        if matricula in matriculas_usadas:
            print('Matrícula já usada. Por favor, insira um número de matrícula diferente.')
        else:
            break
    aluno = (nome, idade, matricula)  # Cria uma tupla
    alunos.append(aluno)
    matriculas_usadas.add(matricula)
    print(f'Aluno {nome} cadastrado com sucesso!')

def listar_alunos(alunos):
    """
    Função para listar todos os alunos cadastrados.

    Args:
    alunos (list): Lista de tuplas com informações dos alunos.

    Returns:
    None
    """
    if not alunos:
        print('Nenhum aluno cadastrado.')
    else:
        for aluno in alunos:
            print(f'Aluno: {aluno[0]}, Idade: {aluno[1]}, Matrícula: {aluno[2]}')

def buscar_aluno_por_matricula(alunos):
    """
    Função para buscar um aluno por número de matrícula.

    Args:
    alunos (list): Lista de tuplas com informações dos alunos.

    Returns:
    tuple: Tupla com informações do aluno encontrado ou None se não encontrado.
    """
    matricula = int(input('Digite a matrícula do aluno: '))
    for aluno in alunos:
        if aluno[2] == matricula:
            print(f'Aluno encontrado: Nome: {aluno[0]}, Idade: {aluno[1]}, Matrícula: {aluno[2]}')
            return aluno
    print('Aluno não encontrado.')
    return None

def atualizar_informacoes_aluno(alunos):
    """
    Função para atualizar a idade de um aluno a partir da matrícula.

    Args:
    alunos (list): Lista de tuplas com informações dos alunos.

    Returns:
    None
    """
    matricula = int(input('Digite a matrícula do aluno para atualizar a idade: '))
    for i, aluno in enumerate(alunos):
        if aluno[2] == matricula:
            nova_idade = int(input(f'Digite a nova idade para o aluno {aluno[0]}: '))
            alunos[i] = (aluno[0], nova_idade, aluno[2])  # Cria uma nova tupla
            print(f'Idade do aluno {aluno[0]} atualizada com sucesso!')
            return
    print('Aluno não encontrado.')

def remover_aluno(alunos, matriculas_cursos, matriculas_usadas):
    """
    Função para remover um aluno a partir da matrícula.

    Args:
    alunos (list): Lista de tuplas com informações dos alunos.
    matriculas_cursos (dict): Dicionário de matrículas com sets de cursos.
    matriculas_usadas (set): Conjunto de números de matrícula já usados.

    Returns:
    None
    """
    matricula = int(input('Digite a matrícula do aluno para remover: '))
    for i, aluno in enumerate(alunos):
        if aluno[2] == matricula:
            alunos.pop(i)
            matriculas_cursos.pop(matricula, None)  # Remove o aluno dos cursos
            matriculas_usadas.remove(matricula)  # Remove a matrícula usada
            print(f'Aluno {aluno[0]} removido com sucesso!')
            return
    print('Aluno não encontrado.')

def gerenciar_cursos(cursos):
    """
    Função para gerenciar cursos (adicionar, remover, listar).

    Args:
    cursos (set): Conjunto de cursos disponíveis.

    Returns:
    None
    """
    while True:
        opcao = input('\nDigite [1] para adicionar curso, [2] para remover curso, [3] para listar cursos, [0] para sair: ')
        if opcao == '1':
            curso = input('Digite o nome do curso para adicionar: ')
            cursos.add(curso)
            print(f'Curso {curso} adicionado com sucesso!')
        elif opcao == '2':
            curso = input('Digite o nome do curso para remover: ')
            if curso in cursos:
                cursos.remove(curso)
                print(f'Curso {curso} removido com sucesso!')
            else:
                print('Curso não encontrado.')
        elif opcao == '3':
            if not cursos:
                print('Nenhum curso cadastrado.')
            else:
                print('Cursos disponíveis:')
                for curso in cursos:
                    print(curso)
        elif opcao == '0':
            break
        else:
            print('Opção inválida. Tente novamente.')

def matricular_aluno_em_curso(alunos, cursos, matriculas_cursos):
    """
    Função para matricular um aluno em um curso.

    Args:
    alunos (list): Lista de tuplas com informações dos alunos.
    cursos (set): Conjunto de cursos disponíveis.
    matriculas_cursos (dict): Dicionário de matrículas com sets de cursos.

    Returns:
    None
    """
    aluno = buscar_aluno_por_matricula(alunos)
    if aluno is not None:
        print('Cursos disponíveis:')
        for curso in cursos:
            print(curso)
        curso = input('Digite o nome do curso para matricular o aluno: ')
        if curso in cursos:
            if aluno[2] not in matriculas_cursos:
                matriculas_cursos[aluno[2]] = set()
            matriculas_cursos[aluno[2]].add(curso)
            print(f'Aluno {aluno[0]} matriculado no curso {curso} com sucesso!')
        else:
            print('Curso não encontrado.')

def listar_matriculas(alunos, matriculas_cursos):
    """
    Função para listar matrículas de alunos em cursos.

    Args:
    alunos (list): Lista de tuplas com informações dos alunos.
    matriculas_cursos (dict): Dicionário de matrículas com sets de cursos.

    Returns:
    None
    """
    if not matriculas_cursos:
        print('Nenhuma matrícula em cursos.')
    else:
        for matricula, cursos in matriculas_cursos.items():
            for aluno in alunos:
                if aluno[2] == matricula:
                    print(f'Aluno: {aluno[0]}, Matrícula: {matricula}, Cursos: {", ".join(cursos)}')

# Inicialização das estruturas de dados
alunos = []  # Lista para armazenar alunos como tuplas
cursos = set()  # Set para gerenciar cursos
matriculas_cursos = {}  # Dicionário para armazenar matrículas em cursos
matriculas_usadas = set()  # Set para armazenar números de matrícula usados

# Loop principal do programa
while True:
    entrada = input('\nDigite [1] para cadastrar alunos, [2] para listar alunos, [3] para buscar aluno por matrícula, [4] para atualizar informações do aluno, [5] para remover aluno, [6] para gerenciar cursos, [7] para matricular aluno em curso, [8] para listar matrículas em cursos, [0] para sair: ')
    
    try:
        opcao = int(entrada)
        
        if opcao == 0:
            print('Saindo do programa.')
            break
        elif opcao == 1:
            cadastrar_aluno(alunos, matriculas_usadas)  # Cadastrar aluno
        elif opcao == 2:
            listar_alunos(alunos)  # Listar alunos
        elif opcao == 3:
            buscar_aluno_por_matricula(alunos)  # Buscar aluno por matrícula
        elif opcao == 4:
            atualizar_informacoes_aluno(alunos)  # Atualizar informações do aluno
        elif opcao == 5:
            remover_aluno(alunos, matriculas_cursos, matriculas_usadas)  # Remover aluno
        elif opcao == 6:
            gerenciar_cursos(cursos)  # Gerenciar cursos
        elif opcao == 7:
            matricular_aluno_em_curso(alunos, cursos, matriculas_cursos)  # Matricular aluno em curso
        elif opcao == 8:
            listar_matriculas(alunos, matriculas_cursos)  # Listar matrículas em cursos
        else:
            print('Opção inválida. Tente novamente.')
    except ValueError:
        print('Digite uma das opções acima.')
