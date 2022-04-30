def menuPrincipal():
    print('-----------MENU---------')
    print('1 - Menu de Paciente')
    print('2 - Menu de Marcação de Consulta')
    print('3 - Menu de Médico')
    print('4 - Menu de Funcionário')
    print('5- Menu de Clínica')
    print('6 – SAIR')

# REGRAS CLÍNICA
#1 - baseClinica só deverá ser acessada do arquivo controlador
#2 - Clinica será um dicionário com as seguintes chaves: CNPJ, nome, endereco
#3 - Não poderá existir mais de uma clínica com o mesmo CNPJ
#4- Não excluir uma clínica sem a confirmação do usuário

def menuClinica ():
    print('-----------MENU CLÍNICA---------')
    print('1 - Cadastrar Clínica')
    print('2 - Buscar Clínica por CNPJ')
    print('3 - Editar Clínica')
    print('4 - Remover Clínica')
    print('5 - Listar todas as Clínicas')
    print('6 – SAIR')

# REGRAS FUNCIONÁRIO
#1 - baseFuncionario só deverá ser acessada do arquivo controlador
#2 - Funcionario será um dicionário com as seguintes chaves: matricula, cpf, nome, e-mail, clinica
#3 - Não poderá existir mais de um Funcionário com a mesma Matrícula
#4 - Não poderá existir mais de um Funcionário com o mesmo CPF
#5- Não excluir o funcionário sem a confirmação do usuário

def menuFuncionario ():
    print('-----------MENU FUNCIONÁRIO---------')
    print('1 - Cadastrar Funcionário')
    print('2 - Buscar Funcionário por Matrícula')
    print('3 - Editar Funcionário') #antes Buscar por matrícula
    print('4 - Remover Funcionário')
    print('5 - Listar Todos os Funcionários')
    print('6 – SAIR')

# REGRAS MÉDICO
#1 - baseMedicos só deverá ser acessada do arquivo controlador
#2 - Medico será um dicionário com as seguintes chaves: CRM, nome, e-mail, especialidade, clinica.
#3 - Não poderá existir mais de um médico com o mesmo CRM
#4 – O tipo de especialidade do médico deverá ser: Cardiologia ou Neurologia
#5- Não excluir um médico sem a confirmação do usuário

def menuMedico():
    print('-----------MENU MÉDICO---------')
    print('1 - Cadastrar Médico')
    print('2 - Buscar Médico por CRM')
    print('3 - Editar Médico') #antes Buscar por CRM
    print('4 - Remover Médico')
    print('5 - Listar Todos os Médicos')
    print('6 - Pesquisar Médico por Especialidade')
    print('7 – SAIR')

# REGRAS PACIENTE
#1 - basePacientes só deverá ser acessada do arquivo controlador
#2 - Paciente será um dicionário com as seguintes chaves: cpf, nome, e-mail, telefone e endereço.
#3 - Não poderá existir mais de um paciente com o mesmo CPF
#4- Não excluir o paciente sem a confirmação do usuário

def menuPaciente():
    print('-----------MENU PACIENTE---------')
    print('1 - Cadastrar Paciente')
    print('2 - Buscar Paciente por cpf')
    print('3 - Editar Paciente') #antes Buscar por cpf o Paciente
    print('4 - Remover Paciente')
    print('5 - Listar Todos os Paciente')
    print('6 – SAIR')

# REGRAS MARCAÇÃO DE CONSULTAS
#1 - baseConsultas só deverá ser acessada do arquivo controlador
#2 - Consulta será um dicionário com as seguintes chaves: codigo, paciente, medico, data, hora, retorno e observacao
#3 - Não poderá existir uma marcação de consulta para o mesmo médico na mesma data e hora
#4- Não excluir uma marcação de consulta sem a confirmação do usuário
#5 – A chave “Retorno” deverá armazenar o valor TRUE caso a consulta seja um retorno do paciente, e FALSE caso seja uma nova consulta.

def menuConsulta ():
    print('-----------MENU MARCAÇÃO DE CONSULTAS---------')
    print('1 - Marcar Consulta')
    print('2 - Buscar Consulta por Paciente')
    print('3 - Editar Consulta')
    print('4 - Remover Consulta')
    print('5 - Listar Consultas')
    print('6 - Listar Consultas por Retorno')
    print('7 - Listar Consultas por intervalo de datas')
    print('8 – SAIR')

while True:
    menuPrincipal()

    opc = int(input('Digite a opcao: '))
    if opc == 6:
        print('Programa Finalizado')
        break

