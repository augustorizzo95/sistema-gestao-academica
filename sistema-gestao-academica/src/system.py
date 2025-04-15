import json


def menu_principal():
    """Apresenta o menu principal."""
    print("""---- MENU PRINCIPAL ----
    (1) Gerenciar Estudantes.
    (2) Gerenciar Disciplinas.
    (3) Gerenciar Professores.
    (4) Gerenciar Turmas.
    (5) Gerenciar Matrículas.
    (9) Sair.\n""")
    return input("Informe a opção desejada: ")


def menu_de_operacoes(categoria):
    """Apresenta o menu de operações de acordo com a escolha do menu principal."""
    print(f"""\n**** [{categoria}] MENU DE OPERAÇÕES ****
    1. Incluir.
    2. Listar.
    3. Atualizar.
    4. Excluir.
    9. Voltar ao menu principal.\n""")
    return input("Informe a opção desejada: ")


def incluir_pessoa(nome_arquivo, categoria, campos):
    """Com base na categoria escolhida, pede que o usuário informe os dados que servirão como os valores das chaves
    (campos), resultando em um dicionário que será adicionado à lista da categoria escolhida."""
    print(f"\n===== INCLUSÃO DE {categoria.upper()} =====\n")
    lista = ler_arquivo(nome_arquivo)
    while True:
        codigo = int(input(f"Informe o {campos[0]}: "))
        codigo_existe = False
        for dicionario in lista:
            if dicionario[campos[0]] == codigo:
                codigo_existe = True
                break
        if codigo_existe:
            print(f"\nO {campos[0]} {codigo} já está cadastrado no sistema. Informe um código diferente.\n")
        else:
            break
    lista_dados = {campos[0]: codigo}
    for campo in campos[1:]:
        dados = input(f"Informe o {campo}: ")
        if campo == "codigo":
            dados = int(dados)
        lista_dados[campo] = dados
    lista.append(lista_dados)
    salvar_arquivo(lista, nome_arquivo)
    print(f"Inclusão realizada com sucesso: {lista_dados}")


def incluir_disciplina_turma_matricula(nome_arquivo, categoria, campos):
    """Com base na categoria escolhida, pede que o usuário informe os dados que servirão como os valores das chaves
    (campos), resultando em um dicionário que será adicionado à lista da categoria escolhida."""
    print(f"\n===== INCLUSÃO DE {categoria.upper()} =====\n")
    lista = ler_arquivo(nome_arquivo)
    while True:
        codigo = int(input(f"Informe o {campos[0]}: "))
        codigo_existe = False
        for dicionario in lista:
            if dicionario[campos[0]] == codigo:
                codigo_existe = True
                break
        if codigo_existe:
            print(f"\nO {campos[0]} {codigo} já está cadastrado no sistema. Informe um código diferente.\n")
        else:
            break
    lista_dados = {campos[0]: codigo}
    for campo in campos[1:]:
        if campo == "nome":
            dados = input(f"Informe o {campo}: ")
        else:
            dados = int(input(f"Informe o {campo}: "))
        lista_dados[campo] = dados
    lista.append(lista_dados)
    salvar_arquivo(lista, nome_arquivo)
    print(f"Inclusão realizada com sucesso: {lista_dados}")


def listar(nome_arquivo, categoria):
    print(f"\n===== LISTAGEM DE {categoria.upper()} =====\n")
    lista = ler_arquivo(nome_arquivo)
    if len(lista) == 0:  # Informa que não há estudantes cadastrados se a lista estiver vazia.
        print(f"Não há {categoria}s no cadastro.")
    else:  # Havendo estudantes cadastrados, imprime a lista de nomes.
        for nome in lista:
            print(nome)


def atualizar_pessoa(nome_arquivo, categoria):
    print(f"\n===== ATUALIZAÇÃO DE {categoria.upper()} =====\n")
    lista = ler_arquivo(nome_arquivo)
    codigo_atualizar = int(input(f"Digite o código do(a) {categoria} que deseja atualizar: "))
    pessoa_encontrada = False
    for dicionario in lista:
        if dicionario["codigo"] == codigo_atualizar:
            pessoa_encontrada = True
            dicionario["codigo"] = int(input(f"\nInforme o novo código do(a) {categoria}: "))
            dicionario["nome"] = (input(f"\nInforme o novo nome do(a) {categoria}: "))
            dicionario["cpf"] = (input(f"\nInforme o novo cpf do(a) {categoria}: "))
            print(f"\nDados atualizados com sucesso: {dicionario}.")
            salvar_arquivo(lista, nome_arquivo)
    if not pessoa_encontrada:
        print(f"\nCódigo do(a) {categoria} informado não encontrado. Selecione uma nova operação.")


def atualizar_disciplina_turma_matricula(nome_arquivo, categoria, campos):
    print(f"\n===== ATUALIZAÇÃO DE {categoria.upper()} =====\n")
    lista = ler_arquivo(nome_arquivo)
    codigo_atualizar = int(input(f"Digite o código do(a) {categoria} que deseja atualizar: "))
    disciplina_turma_matricula_encontrada = False
    for dicionario in lista:
        if ("codigo" in dicionario and dicionario["codigo"] == codigo_atualizar) or ("codigo da turma" in dicionario and
                                                                                     dicionario["codigo da turma"] ==
                                                                                     codigo_atualizar):
            disciplina_turma_matricula_encontrada = True
            for campo in campos:
                if campo == "nome":
                    dados = input(f"Informe o novo {campo} do(a) {categoria}: ")
                else:
                    dados = int(input(f"Informe o novo {campo} do(a) {categoria}: "))
                dicionario[campo] = dados
            print(f"\nDados atualizados com sucesso: {dicionario}.")
            salvar_arquivo(lista, nome_arquivo)
    if not disciplina_turma_matricula_encontrada:
            print(f"\nCódigo do(a) {categoria} informado não encontrado. Selecione uma nova operação.")


def excluir(nome_arquivo, categoria):
    print(f"\n===== EXCLUSÃO DE {categoria.upper()} =====\n")
    codigo_excluir = int(input(f"Digite o código do(a) {categoria} que deseja excluir: "))
    lista = ler_arquivo(nome_arquivo)
    lista_excluir_encontrada = False
    for dicionario in lista:
        if ("codigo" in dicionario and dicionario["codigo"] == codigo_excluir) or ("codigo da turma" in dicionario and
                                                                                     dicionario["codigo da turma"] ==
                                                                                     codigo_excluir):
            lista_excluir_encontrada = True
            lista.remove(dicionario)
            salvar_arquivo(lista, nome_arquivo)
            print(f"\nExclusão do(a) {categoria} realizada com sucesso.")
    if not lista_excluir_encontrada:
            print(f"\nCódigo do(a) {categoria} informado não encontrado. Selecione uma nova operação.")


def salvar_arquivo(lista, arquivo):
    with open(arquivo, "w") as arquivo_aberto:
        json.dump(lista, arquivo_aberto)


def ler_arquivo(arquivo):
    try:
        with open(arquivo, "r") as arquivo_aberto:
            lista = json.load(arquivo_aberto)
        return lista
    except:
        return []


def processar_menu_operacoes(opcao_2, nome_arquivo, categoria, campos, eh_pessoa):
    if opcao_2 == "1":
        if eh_pessoa:
            incluir_pessoa(nome_arquivo, categoria, campos)
        else:
            incluir_disciplina_turma_matricula(nome_arquivo, categoria, campos)
    elif opcao_2 == "2":
        listar(nome_arquivo, categoria)
    elif opcao_2 == "3":
        if eh_pessoa:
            atualizar_pessoa(nome_arquivo, categoria)
        else:
            atualizar_disciplina_turma_matricula(nome_arquivo, categoria, campos)
    elif opcao_2 == "4":
        excluir(nome_arquivo, categoria)
    elif opcao_2 == "9":
        print("\nVoltando ao menu principal...\n")
        return False
    else:
        print("\nInforme uma opção válida.")
    return True


arquivo_estudantes = "estudantes.json"
arquivo_disciplinas = "disciplinas.json"
arquivo_professores = "professores.json"
arquivo_turmas = "turmas.json"
arquivo_matriculas = "matriculas.json"

while True:  # Primeiro loop para apresentar o menu principal e solicitar a opção desejada pelo usuário.

    opcao_1 = menu_principal()

    if opcao_1 == "1":
        categoria_escolhida = "ESTUDANTES"
        campos_estudante = ["codigo", "nome", "cpf"]
        while True:
            opcao_2 = menu_de_operacoes(categoria_escolhida)
            if not processar_menu_operacoes(opcao_2, arquivo_estudantes, "estudante", campos_estudante, True):
                break

    elif opcao_1 == "2":
        categoria_escolhida = "DISCIPLINAS"
        campos_disciplina = ["codigo", "nome"]
        while True:
            opcao_2 = menu_de_operacoes(categoria_escolhida)
            if not processar_menu_operacoes(opcao_2, arquivo_disciplinas, "disciplina", campos_disciplina, False):
                break

    elif opcao_1 == "3":
        categoria_escolhida = "PROFESSORES"
        campos_professor = ["codigo", "nome", "cpf"]
        while True:
            opcao_2 = menu_de_operacoes(categoria_escolhida)
            if not processar_menu_operacoes(opcao_2, arquivo_professores, "professor", campos_professor, True):
                break

    elif opcao_1 == "4":
        categoria_escolhida = "TURMAS"
        campos_turma = ["codigo da turma", "codigo do professor", "codigo da disciplina"]
        while True:
            opcao_2 = menu_de_operacoes(categoria_escolhida)
            if not processar_menu_operacoes(opcao_2, arquivo_turmas, "turma", campos_turma, False):
                break

    elif opcao_1 == "5":
        categoria_escolhida = "MATRÍCULAS"
        campos_matricula = ["codigo da turma", "codigo do estudante"]
        while True:
            opcao_2 = menu_de_operacoes(categoria_escolhida)
            if not processar_menu_operacoes(opcao_2, arquivo_matriculas, "matrícula", campos_matricula, False):
                break

    elif opcao_1 == "9":
        print("\nFinalizando aplicação...")
        break

    else:
        print("\nInforme uma opção válida.\n")