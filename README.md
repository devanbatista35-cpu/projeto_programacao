📚 Sistema de Gerenciamento de Biblioteca

📖 Visão Geral
Este projeto é um **sistema de gerenciamento de biblioteca em console**, desenvolvido em Python. Ele permite cadastrar livros, atualizar status de leitura, filtrar por gênero, buscar e manter um histórico de livros concluídos.  

Ele demonstra o uso de **estruturas de dados fundamentais**:
- **Lista** → Armazena todos os livros cadastrados.  
- **Fila (FIFO)** → Gerencia livros pendentes para leitura.  
- **Pilha (LIFO)** → Mantém o histórico de livros concluídos na ordem inversa de finalização.  

⚙️ Funcionalidades
- Cadastrar livro com título, autor, ano, gênero e prioridade.  
- Listar livros com detalhes.  
- Atualizar status (A Ler, Lendo, Concluído).  
- Ver histórico de livros concluídos (pilha).  
- Filtrar por gênero.  
- Contar por status.  
- Deletar livro.  
- Buscar livro.  

🧩 Exemplo: FIFO, LIFO e Listas
# Lista: armazena todos os livros
livros = []

# Fila (FIFO): livros a serem lidos
fila_a_ler = []

# Pilha (LIFO): livros concluídos
pilha_concluidos = []

# Adicionando um livro ao sistema
livros.append(dict_livro)          # Lista
fila_a_ler.append(dict_livro)      # Fila (FIFO)

# Concluindo um livro
pilha_concluidos.append(dict_livro)  # Pilha (LIFO)

# Comportamento FIFO: primeiro livro cadastrado é o primeiro a ser lido
primeiro_a_ler = fila_a_ler[0]

# Comportamento LIFO: último livro concluído é exibido primeiro
ultimo_concluido = pilha_concluidos[-1]

🚀 Instalação
1. Clone o repositório:
   ```bash
   git clone https://github.com/seuusuario/library-system.git
   ```
2. Acesse a pasta do projeto:
   ```bash
   cd library-system
   ```
3. Execute o programa:
   ```bash
   python main.py
   ```

📋 Requisitos
- Python 3.8+  
- Nenhuma biblioteca externa necessária (implementação pura em Python).  

🛠️ Uso
Ao iniciar, o programa exibe um menu com opções:
- `1` → Cadastrar livro  
- `2` → Listar livros  
- `3` → Atualizar status  
- `4` → Ver histórico de concluídos  
- `5` → Filtrar por gênero  
- `6` → Contar por status  
- `7` → Deletar livro  
- `8` → Buscar livro  
- `9` → Sair  

🤝 Contribuição
Contribuições são bem-vindas!  
- Faça um fork do repositório  
- Crie uma nova branch  
- Commit suas alterações  
- Abra um Pull Request  

