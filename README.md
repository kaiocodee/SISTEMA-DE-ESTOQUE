# 🛒 Sistema de Produtos — Python + SQLite

Sistema de gerenciamento de produtos desenvolvido em **Python**, utilizando **SQLite** como banco de dados.

O projeto simula uma pequena plataforma de vendas, com uma área para clientes consultarem produtos e uma área administrativa para gerenciamento do catálogo.

## 🚀 Funcionalidades

### 👤 Área do Cliente

* Visualização dos produtos cadastrados
* Consulta de informações dos produtos
* Seleção de produtos para compra
* Exibição das informações do pedido

### 🔐 Área Administrativa

* Acesso protegido por senha
* Visualização dos produtos
* Cadastro de novos produtos
* Validação das informações inseridas

### 🗄️ Banco de Dados

* Banco de dados SQLite
* Tabela de produtos
* Identificação automática dos produtos através de `ID`
* Armazenamento persistente dos dados

## 🛠️ Tecnologias utilizadas

* **Python**
* **SQLite**
* **SQL**
* Biblioteca `sqlite3`

## 📂 Estrutura

```text
projeto/
│
├── main.py
├── main.db
└── README.md
```

> O arquivo `main.db` é criado automaticamente pelo programa caso ainda não exista.

## ▶️ Como executar

### 1. Clone o repositório

```bash
git clone SEU_LINK_DO_GITHUB
```

### 2. Entre na pasta

```bash
cd nome-do-projeto
```

### 3. Execute o programa

```bash
python main.py
```

Não é necessário instalar bibliotecas externas, pois o projeto utiliza o módulo `sqlite3`, incluído no Python.

## 🔑 Acesso administrativo

A área administrativa possui uma senha de acesso definida no código para fins de demonstração.

> **Senha:** `2026`

⚠️ Em uma aplicação real, as credenciais não devem ficar diretamente no código. O projeto utiliza essa abordagem apenas para fins educacionais.

## 📌 Objetivo

Este projeto foi desenvolvido com o objetivo de praticar conceitos fundamentais de desenvolvimento **backend**, incluindo:

* Programação em Python
* Funções
* Estruturas condicionais
* Loops
* Tratamento de exceções
* Entrada e validação de dados
* SQL
* SQLite
* Operações com banco de dados
* Organização de sistemas

Este projeto foi desenvolvido para fins educacionais.
