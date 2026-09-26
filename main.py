# menu / controle do sistema.

from banco import criar_tabela
from produto import cadastrar_produto, listar_produtos, buscar_produto, alterar_produto, deletar_produto



criar_tabela()


while True:


    print("\n================================")
    print("       SISTEMA DE ESTOQUE")
    print("================================")
    print("1 - Cadastrar produto")
    print("2 - Listar produtos")
    print("3 - Buscar produto")
    print("4 - Alterar produto")
    print("5 - Deletar produto")
    print("0 - Sair")


    opcao = input("Escolha uma opção: ")

    if opcao == "1":
        cadastrar_produto()

    elif opcao == "2":
        listar_produtos()

    elif opcao == "3":
        buscar_produto()

    elif opcao == "4":
        alterar_produto()

    elif opcao == "5":
        deletar_produto()

    elif opcao == "0":
        print("Encerrando o sistema...")
        break

    else:
        print("Opção inválida!")

