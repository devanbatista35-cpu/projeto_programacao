# Esse arquivo recebe os dados do projeto
# Dados usados no projeto da biblioteca

livros = []              # lista global de livros que cria um objeto
fila_a_ler = []          # livros a ler e usando o metodo de fila (FIFO) 
pilha_concluidos = []    # livros concluidos e usando o metodo de pilha (LIFO)
prioridades = ("Baixa", "Média", "Alta")   # tupla de prioridades valores imutaveis
status = ("A Ler", "Lendo", "Concluído")   # tupla de status valores imutaveis
contador_id = 0