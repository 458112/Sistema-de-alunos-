🎓 Sistema de Alunos — CRUD com Python e SQLite

Sistema desktop para cadastro e gerenciamento de alunos, desenvolvido com Python, Tkinter e SQLite.
📋 Funcionalidades

Cadastrar alunos com nome, email, idade, telefone, data de nascimento e sexo
Listar todos os alunos em uma tabela interativa
Atualizar dados de um aluno selecionado
Excluir alunos do sistema
Validação dos campos (letras, números, limites de idade e data)

🛠️ Tecnologias

Python 3
Tkinter — interface gráfica
tkcalendar — widget de data
SQLite3 — banco de dados local

📁 Estrutura do Projeto

├── main.py        # Interface gráfica (Tkinter)
├── view.py        # Funções do banco de dados (CRUD)
├── banco.py       # Criação da tabela no SQLite
└── banco.db       # Arquivo do banco de dados (gerado automaticamente)

▶️ Como executar

1. Clone o repositório:
bashgit clone https://github.com/458112/Sistema-de-alunos-.git
cd Sistema-de-alunos-
2. Instale as dependências:
bashpip install tkcalendar
3. Execute o programa:
bashpython main.py

O arquivo banco.db será criado automaticamente na primeira execução.

📌 Observações

Não é necessário instalar o SQLite separadamente, ele já vem com o Python.
Caso ocorra erro de coluna no banco, delete o arquivo banco.db e execute novamente.
