# operações dos Produtos.

from banco import conectar_banco


def cadastrar_produto():
    conexao = conectar_banco()
    cursor = conexao.cursor()

    # =========================
    # VALIDAR NOME DO PRODUTO
    # =========================

    while True:
        nome = input("Nome do Produto: ").strip()

        if not nome:
            print("O nome do produto não pode ficar vazio.")
            continue

        if any(caractere.isdigit() for caractere in nome):
            print("O nome do produto não pode conter números.")
            continue

        # Verificar se o produto já existe
        cursor.execute("""
        SELECT id FROM Produto
        WHERE LOWER(nome) = LOWER(?)
        """, (nome,))

        produto_existente = cursor.fetchone()

        if produto_existente:
            print("Esse produto já está cadastrado.")
            continue

        break

    # =========================
    # VALIDAR QUANTIDADE
    # =========================

    while True:
        try:
            quantidade = int(input("Digite a quantidade: "))

            if quantidade <= 0:
                print("A quantidade deve ser maior que zero.")
                continue

            break

        except ValueError:
            print("Digite apenas números inteiros.")

    # =========================
    # VALIDAR PREÇO
    # =========================

    while True:
        try:
            preco = float(input("Preço Unitário: "))

            if preco <= 0:
                print("O preço deve ser maior que zero.")
                continue

            break

        except ValueError:
            print("Digite apenas números.")

    # =========================
    # CADASTRAR NO BANCO
    # =========================

    cursor.execute("""
    INSERT INTO Produto(nome, quantidade, preco)
    VALUES (?, ?, ?)
    """, (nome, quantidade, preco))

    conexao.commit()
    conexao.close()

    print("\nProduto cadastrado com sucesso!")

    input("\nPressione ENTER para voltar ao menu...")


# ==========================================================================

def listar_produtos():
    conexao = conectar_banco()
    cursor = conexao.cursor()

    cursor.execute("""
    SELECT * FROM Produto
    ORDER BY id
    """)

    produtos = cursor.fetchall()

    if not produtos:
        print("\nNenhum produto cadastrado.")
        conexao.close()
        input("\nPressione ENTER para voltar ao menu...")
        return

    print("\n======================================================")
    print("                  LISTA DE PRODUTOS")
    print("======================================================")
    print(f"{'ID':<5} {'NOME':<20} {'QUANTIDADE':<12} {'PREÇO':>10}")
    print("------------------------------------------------------")

    for produto in produtos:
        print(
            f"{produto[0]:<5} "
            f"{produto[1]:<20} "
            f"{produto[2]:<12} "
            f"R$ {produto[3]:>7.2f}"
        )

    print("======================================================")

    conexao.close()

    input("\nPressione ENTER para voltar ao menu...")

    # =================================================================

def buscar_produto():
    conexao = conectar_banco()
    cursor = conexao.cursor()

    nome_busca = input("Digite o nome do produto: ").strip()

    if not nome_busca:
        print("\nO nome do produto não pode ficar vazio.")
        conexao.close()
        input("\nPressione ENTER para voltar ao menu...")
        return

    cursor.execute("""
    SELECT * FROM Produto
    WHERE LOWER(nome) = LOWER(?)
    """, (nome_busca,))

    produto = cursor.fetchone()

    if produto:
        print("\n================================")
        print("       PRODUTO ENCONTRADO")
        print("================================")
        print(f"ID: {produto[0]}")
        print(f"Nome: {produto[1]}")
        print(f"Quantidade: {produto[2]}")
        print(f"Preço: R$ {produto[3]:.2f}")

    else:
        print("\nProduto não encontrado.")

    conexao.close()

    input("\nPressione ENTER para voltar ao menu...")

# ======================================================================

def alterar_produto():
    conexao = conectar_banco()
    cursor = conexao.cursor()

    nome_busca = input("Digite o nome do produto que deseja alterar: ").strip()

    if not nome_busca:
        print("\nO nome do produto não pode ficar vazio.")
        conexao.close()
        input("\nPressione ENTER para voltar ao menu...")
        return

    cursor.execute("""
    SELECT * FROM Produto
    WHERE LOWER(nome) = LOWER(?)
    """, (nome_busca,))

    produto = cursor.fetchone()

    if produto:
        print("\n================================")
        print("       PRODUTO ENCONTRADO")
        print("================================")
        print(f"ID: {produto[0]}")
        print(f"Nome: {produto[1]}")
        print(f"Quantidade atual: {produto[2]}")
        print(f"Preço atual: R$ {produto[3]:.2f}")

        print("\nO que deseja alterar?")
        print("1 - Quantidade")
        print("2 - Preço")
        print("0 - Cancelar")

        opcao = input("Escolha uma opção: ")

        # =========================
        # ALTERAR QUANTIDADE
        # =========================

        if opcao == "1":

            while True:
                try:
                    nova_quantidade = int(
                        input("Digite a nova quantidade: ")
                    )

                    if nova_quantidade <= 0:
                        print("A quantidade deve ser maior que zero.")
                        continue

                    break

                except ValueError:
                    print("Digite apenas números inteiros.")

            cursor.execute("""
            UPDATE Produto
            SET quantidade = ?
            WHERE id = ?
            """, (nova_quantidade, produto[0]))

            conexao.commit()

            print("\nQuantidade alterada com sucesso!")

        # =========================
        # ALTERAR PREÇO
        # =========================

        elif opcao == "2":

            while True:
                try:
                    novo_preco = float(
                        input("Digite o novo preço: ")
                    )

                    if novo_preco <= 0:
                        print("O preço deve ser maior que zero.")
                        continue

                    break

                except ValueError:
                    print("Digite apenas números.")

            cursor.execute("""
            UPDATE Produto
            SET preco = ?
            WHERE id = ?
            """, (novo_preco, produto[0]))

            conexao.commit()

            print("\nPreço alterado com sucesso!")

        elif opcao == "0":
            print("\nAlteração cancelada.")

        else:
            print("\nOpção inválida!")

    else:
        print("\nProduto não encontrado.")

    conexao.close()

    input("\nPressione ENTER para voltar ao menu...")

# ==================================================================

def deletar_produto():
    conexao = conectar_banco()
    cursor = conexao.cursor()

    nome_busca = input("Informe o produto a ser excluído: ").strip()

    if not nome_busca:
        print("\nO nome do produto não pode ficar vazio.")
        conexao.close()
        input("\nPressione ENTER para voltar ao menu...")
        return

    cursor.execute("""
    SELECT * FROM Produto
    WHERE LOWER(nome) = LOWER(?)
    """, (nome_busca,))

    produto = cursor.fetchone()

    if produto:
        print("\n================================")
        print("       PRODUTO ENCONTRADO")
        print("================================")
        print(f"ID: {produto[0]}")
        print(f"Nome: {produto[1]}")
        print(f"Quantidade: {produto[2]}")
        print(f"Preço: R$ {produto[3]:.2f}")

        print("\nTem certeza que deseja excluir este produto?")
        print("1 - Sim")
        print("2 - Não")

        opcao = input("Escolha uma opção: ")

        if opcao == "1":

            cursor.execute("""
            DELETE FROM Produto
            WHERE id = ?
            """, (produto[0],))

            conexao.commit()

            print("\nProduto excluído com sucesso!")

        elif opcao == "2":
            print("\nExclusão cancelada.")

        else:
            print("\nOpção inválida!")

    else:
        print("\nProduto não encontrado.")

    conexao.close()

    input("\nPressione ENTER para voltar ao menu...")

# ==================================================================================================
