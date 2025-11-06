import customtkinter as ctk
import sqlite3

banco = sqlite3.connect("projeto.db")
cur = banco.cursor()

cur.execute("CREATE TABLE IF NOT EXISTS estoque (codigo INTEGER PRIMARY KEY, nome TEXT, quantidade INTEGER, valorUnit REAL, valorTotal REAL)")

def cadastrar():
    codigo = entry_codigo.get()
    cur.execute("SELECT * FROM estoque where codigo = ?", (codigo,))
    if cur.fetchone():
        existencia.configure(text="Produto já existe!", text_color="red")

    else:
        nome = entry_nome.get()
        quantidade = float(entry_quantidade.get())
        valorUnit = float(entry_valorUnit.get())
        valorTotal = (quantidade * valorUnit)

        cur.execute("INSERT INTO estoque VALUES (?, ?, ?, ?, ?)", (codigo, nome, quantidade, valorUnit, valorTotal))
        banco.commit()
        sucesso.configure(text="Produto cadastrado com sucesso!", text_color="green")
        

tela = ctk.CTk()
tela.title("Sistema de Controle de Estoque")
tela.iconbitmap('images/pythontutorial-1.ico')

larguraTela = 800
alturaTela = 600
screen_width = tela.winfo_screenwidth()
screen_height = tela.winfo_screenheight()

centroX = int(screen_width/2 - larguraTela/2)
centroY = int(screen_height/2 - alturaTela/2)
tela.geometry(f'{larguraTela}x{alturaTela}+{centroX}+{centroY}')
tela.resizable(False, False)

tabview = ctk.CTkTabview(tela, width=780, height=580)
tabview.pack(pady=10)
tabview.add("adicionar")
tabview.add("excluir")
tabview.add("alterarQtd")
tabview.add("visualizar")

tabview.tab("adicionar").grid_columnconfigure(1, weight=1)
tabview.tab("excluir").grid_columnconfigure(1, weight=1)
tabview.tab("alterarQtd").grid_columnconfigure(1, weight=1)
tabview.tab("visualizar").grid_columnconfigure(1, weight=1)


#adicionar elementos na aba adicionar
#label codigo
label_codigo = ctk.CTkLabel(tabview.tab("adicionar"), text="código")
label_codigo.grid(row=0, column=0, sticky="w", padx=10, pady=5)

entry_codigo = ctk.CTkEntry(tabview.tab("adicionar"), placeholder_text= "digite o código do produto",width=200)
entry_codigo.grid(row=0, column=1, sticky="w", padx=10, pady=5)

#nome
label_nome = ctk.CTkLabel(tabview.tab("adicionar"), text="nome")
label_nome.grid(row=1, column=0, sticky="w", padx=10, pady=5)

entry_nome = ctk.CTkEntry(tabview.tab("adicionar"), placeholder_text= "digite o nome do produto",width=200)
entry_nome.grid(row=1, column=1, sticky="w", padx=10, pady=5)

#quantidade
label_quantidade = ctk.CTkLabel(tabview.tab("adicionar"), text="quantidade")
label_quantidade.grid(row=2, column=0, sticky="w", padx=10, pady=5)

entry_quantidade = ctk.CTkEntry(tabview.tab("adicionar"), placeholder_text= "digite a quantidade do produto",width=200)
entry_quantidade.grid(row=2, column=1, sticky="w", padx=10, pady=5)

#valorUnit
label_valorUnit = ctk.CTkLabel(tabview.tab("adicionar"), text="Valor Unitario")
label_valorUnit.grid(row=3, column=0, sticky="w", padx=10, pady=5)

entry_valorUnit = ctk.CTkEntry(tabview.tab("adicionar"), placeholder_text="digite o valor unitario do produto", width=200)
entry_valorUnit.grid(row=3, column=1, sticky="w", padx=10, pady=5)

#mensagens
adicionarbutton = ctk.CTkButton(tabview.tab("adicionar"), text= "cadastrar",width=200, command=cadastrar)
adicionarbutton.grid(row=4, column=0, padx=10, pady=5)
#
existencia = ctk.CTkLabel(tabview.tab("adicionar"), text="")
existencia.grid(row= 5, column=0, padx=10, pady=5)
#
sucesso = ctk.CTkLabel(tabview.tab("adicionar"), text="")
sucesso.grid(row= 5, column=0, padx=10, pady=5)

#tabela excluir-------------------------------------------------------------------------------------------------------------------------------------------------------------

def excluir():
    codigo = entry_delCodigo.get()
    cur.execute("DELETE FROM estoque WHERE codigo = ?", (codigo, ))
    if cur.rowcount > 0:
        banco.commit()
        sucessoDelete.configure(text="produto excluido com sucesso!", text_color="green")
    else:
        notfind.configure(text="Produto não encontrado", text_color="red")


label_delCodigo = ctk.CTkLabel(tabview.tab("excluir"), text="digite o código do produto que deseja excluir")
label_delCodigo.grid(row = 0, column = 0, padx = 10, pady = 5)

entry_delCodigo = ctk.CTkEntry(tabview.tab("excluir"), placeholder_text="código", width=200)
entry_delCodigo.grid(row=0, column=1, padx=10, pady = 5)

#mensagem
sucessoDelete = ctk.CTkLabel(tabview.tab("excluir"), text="")
sucessoDelete.grid(row= 5, column=0, padx=10, pady=5)
#
notfind = ctk.CTkLabel(tabview.tab("excluir"), text="")
notfind.grid(row= 5, column=0, padx=10, pady=5)
#botão
adicionarbutton = ctk.CTkButton(tabview.tab("excluir"), text= "excluir produto", width=200, command=excluir)
adicionarbutton.grid(row=4, column=0, padx=10, pady=5)

# tabela alterar quantidade------------------------------------------------------------------------------------------------------------------------------------------------

def alterarquantidade():
    codigo = entry_alterproduto.get()
    opcao.get()
    cur.execute("SELECT quantidade FROM estoque WHERE codigo = ?", (codigo,))
    qtdAtual = cur.fetchone()
    if qtdAtual:
        if int(opcao.get()) == 1:
            quantidadeDel = int(entry_modquantidade.get())
            cur.execute("UPDATE estoque SET quantidade = ? WHERE codigo = ?", ((qtdAtual[0] + quantidadeDel), codigo))
            baixaAlta.configure(text="produto atualizado com sucesso", text_color="green")
            banco.commit()
        elif int(opcao.get()) == 2:
            quantidadeDel = int(entry_modquantidade.get())
            if quantidadeDel <= qtdAtual[0]:
                cur.execute("UPDATE estoque SET quantidade = ? WHERE codigo = ?", (qtdAtual[0] - quantidadeDel, codigo))
                baixaAlta.configure(text="produto atualizado com sucesso", text_color="green")
            else:
                baixaAlta.configure(text="estoque insuficiente", text_color="red")
        banco.commit()
    else:
        baixaAlta.configure(text="produto não encontrado", text_color="red")
banco.commit()

def alterarnome():
    print()

label_alterproduto = ctk.CTkLabel(tabview.tab("alterarQtd"), text="digite o código do produto que deseja alterar quantidade")
label_alterproduto.grid(row=0, column=0, padx=10, pady=5)

entry_alterproduto = ctk.CTkEntry(tabview.tab("alterarQtd"), placeholder_text="código", width=200)
entry_alterproduto.grid(row=0, column=1, padx=10, pady=5)

opcao = ctk.StringVar(value="")

button_adicionar = ctk.CTkRadioButton(tabview.tab("alterarQtd"), text= "adicionar quantidade", variable=opcao, value = "1")
button_adicionar.grid(row=1, column=0, padx=10, pady=5)

button_remover = ctk.CTkRadioButton(tabview.tab("alterarQtd"), text= "retirar quantidade", variable=opcao, value = "2")
button_remover.grid(row=1, column=1, padx=10, pady=5)

label_modquantidade = ctk.CTkLabel(tabview.tab("alterarQtd"), text = "digite a quantidade que deseja adicionar ou retirar")
label_modquantidade.grid(row=2, column=0, padx=10, pady=5)

entry_modquantidade = ctk.CTkEntry(tabview.tab("alterarQtd"), placeholder_text="adicionar ou retirar", width=200)
entry_modquantidade.grid(row=2, column=1, padx=10, pady = 5)

atualizarbutton = ctk.CTkButton(tabview.tab("alterarQtd"), text= "atualizar",width=200, command=alterarquantidade)
atualizarbutton.grid(row=3, column=0, padx=10, pady=5)

#mensagens
baixaAlta = ctk.CTkLabel(tabview.tab("alterarQtd"), text="")
baixaAlta.grid(row=4, column=0, padx=10, pady = 5)

#visualizar----------------------------------------------------------------------------------------------------------------------------------------------------------------

import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

#scroll
frame_scroll = ctk.CTkScrollableFrame(tabview.tab("visualizar"), width=760, height=520)
frame_scroll.grid(row=0, column=0, padx=10, pady=10, sticky="nsew")

canvas_dict = {}

def limpar_graficos():
    for widget in frame_scroll.winfo_children():
        if isinstance(widget, ctk.CTkLabel) or isinstance(widget, ctk.CTkButton):
            continue
        widget.destroy()
    for key in list(canvas_dict.keys()):
        canvas_dict[key] = None


def atualizar_graficos():
    limpar_graficos()

    cur.execute("SELECT nome, quantidade FROM estoque")
    produtos = cur.fetchall()

    if not produtos:
        aviso = ctk.CTkLabel(frame_scroll, text="Não há produtos cadastrados para gerar gráficos.", text_color="red")
        aviso.pack(padx=10, pady=10)
        return

    nomes = [p[0] for p in produtos]
    quantidades = [p[1] for p in produtos]

#grafico dos produtos em estoque
    label_barras = ctk.CTkLabel(frame_scroll, text="Quantidade de Produtos em Estoque", font=("Arial", 14, "bold"))
    label_barras.pack(pady=(10, 0))

    fig_barras, ax_barras = plt.subplots(figsize=(7, 4))
    ax_barras.bar(nomes, quantidades, color="#4CAF50")
    ax_barras.set_xlabel("Produto")
    ax_barras.set_ylabel("Quantidade")
    plt.xticks(rotation=45, ha="right")
    plt.tight_layout()

    canvas_barras = FigureCanvasTkAgg(fig_barras, master=frame_scroll)
    canvas_barras.draw()
    canvas_barras.get_tk_widget().pack(padx=10, pady=10)
    plt.close(fig_barras)
    canvas_dict["barras"] = canvas_barras

#grafico da pizza de estoque
    label_pizza = ctk.CTkLabel(frame_scroll, text="Distribuição Percentual de Estoque", font=("Arial", 14, "bold"))
    label_pizza.pack(pady=(10, 0))

    fig_pizza, ax_pizza = plt.subplots(figsize=(6, 4))
    ax_pizza.pie(quantidades, labels=nomes, autopct="%1.1f%%", startangle=90)
    ax_pizza.set_title("Distribuição de Estoque por Produto")

    canvas_pizza = FigureCanvasTkAgg(fig_pizza, master=frame_scroll)
    canvas_pizza.draw()
    canvas_pizza.get_tk_widget().pack(padx=10, pady=10)
    plt.close(fig_pizza)
    canvas_dict["pizza"] = canvas_pizza

#botão atualizar
botao_atualizar = ctk.CTkButton(frame_scroll, text="🔄 Atualizar Gráficos", command=atualizar_graficos)
botao_atualizar.pack(pady=10)

tela.mainloop()