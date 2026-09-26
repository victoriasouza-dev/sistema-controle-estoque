# Sistema de Controle de Estoque

Sistema de controle de estoque desenvolvido em Python, utilizando SQLite para armazenamento dos dados.

## Objetivo

O projeto foi desenvolvido com o objetivo de praticar conceitos de programação, banco de dados, SQL e operações CRUD em uma aplicação de linha de comando.

## Tecnologias utilizadas

* Python 3
* SQLite
* SQL
* VS Code

## Funcionalidades

O sistema possui as seguintes funcionalidades:

* Cadastro de produtos
* Listagem de produtos
* Busca de produtos
* Alteração de quantidade
* Alteração de preço
* Exclusão de produtos
* Validação dos dados informados
* Confirmação antes da exclusão
* Armazenamento dos dados em banco SQLite

## Estrutura do projeto

```text
Estoque_projeto/
├── main.py
├── banco.py
├── produto.py
└── README.md
```

### Arquivos

* `main.py` — responsável pelo menu e controle do sistema.
* `banco.py` — responsável pela conexão com o banco de dados e criação da tabela.
* `produto.py` — contém as operações de cadastro, listagem, busca, alteração e exclusão de produtos.
* `README.md` — documentação do projeto.

## Validações

O sistema possui validações para evitar dados inválidos:

* O nome do produto não pode ficar vazio.
* O nome do produto não pode conter números.
* Não é permitido cadastrar produtos duplicados.
* A quantidade deve ser um número inteiro maior que zero.
* O preço deve ser um número maior que zero.
* A exclusão exige confirmação do usuário.
* O sistema trata entradas inválidas de quantidade e preço.

## Como executar

### Pré-requisitos

É necessário ter o Python 3 instalado no computador.

### Execução

1. Abra a pasta do projeto no VS Code.
2. Abra o terminal.
3. Execute o comando:

```bash
python main.py
```

4. O sistema será iniciado no terminal.

## Operações CRUD

O projeto implementa as quatro operações básicas de um sistema CRUD:

* **Create (Criar):** cadastro de produtos.
* **Read (Ler):** listagem e busca de produtos.
* **Update (Atualizar):** alteração de quantidade e preço.
* **Delete (Excluir):** exclusão de produtos.

## Conceitos praticados

Durante o desenvolvimento do projeto foram praticados:

* Variáveis
* Estruturas condicionais
* Estruturas de repetição
* Funções
* Tratamento de exceções
* Entrada e saída de dados
* Manipulação de banco de dados
* SQL
* CRUD
* Consultas parametrizadas
* Validação de dados
* Organização do código em módulos

## Aprendizados

Este projeto permitiu praticar a integração entre Python e banco de dados SQLite, além do desenvolvimento de operações CRUD, criação de validações e organização de uma aplicação em diferentes módulos.

O projeto também contribuiu para o desenvolvimento da lógica de programação e para a compreensão do funcionamento de sistemas que realizam cadastro, consulta, atualização e exclusão de dados.
