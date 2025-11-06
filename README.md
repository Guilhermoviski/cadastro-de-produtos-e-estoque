# Sistema de Controle de Estoque (Python + CustomTkinter + SQLite)

Este projeto é um **Sistema de Controle de Estoque** simples, desenvolvido em **Python**, utilizando a biblioteca **CustomTkinter** para a interface gráfica e **SQLite3** para o banco de dados local.

O sistema permite:
- ✅ Cadastrar novos produtos  
- ❌ Excluir produtos do estoque  
- 🔄 Alterar quantidades (entrada e saída)  
- 📊 Visualizar gráficos do estoque (barras e pizza)

Tecnologias Utilizadas

- **Python 3.10+**
- **CustomTkinter** — Interface moderna com suporte a temas escuros e claros  
- **SQLite3** — Banco de dados embutido (sem necessidade de servidor)  
- **Matplotlib** — Geração dos gráficos de visualização  


## ⚙️ Funcionalidades

### 🟩 Aba "adicionar"
Permite cadastrar novos produtos no banco de dados.

Campos:
- Código (chave primária)
- Nome
- Quantidade
- Valor unitário

O sistema calcula automaticamente o valor total (`quantidade * valorUnit`).

Mensagens informam se o produto já existe ou se foi cadastrado com sucesso.

### 🟥 Aba "excluir"
Permite excluir um produto existente informando o código.  
Exibe mensagens de sucesso ou erro caso o produto não seja encontrado.

### 🟨 Aba "alterarQtd"
Permite:
- Aumentar o estoque de um produto existente  
- Diminuir o estoque (com verificação de quantidade disponível)

Usa **radiobuttons** para escolher a operação (adicionar ou retirar).

### 🟦 Aba "visualizar"
Exibe os dados do estoque por meio de gráficos:

- 📊 **Gráfico de Barras:** mostra a quantidade de cada produto.
- 🥧 **Gráfico de Pizza:** mostra a distribuição percentual do estoque.  

