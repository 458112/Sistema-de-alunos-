from tkinter import *
from tkcalendar import Calendar, DateEntry
from tkinter import font
from tkinter import ttk
from tkinter import messagebox
from tkcalendar import Calendar, DateEntry
from datetime import date, datetime
from view import *
from banco import * 



co0 = "#f0f3f5"  
co1 = "#feffff"  
co2 = "#4fa882"  # verde
co3 = "#38576b"  # valor
co4 = "#403d3d"   # letra
co5 = "#e06636"   # - profit
co6 = "#038cfc"   # azul
co7 = "#ef5350"   # vermelha
co8 = "#263238"   # + verde
co9 = "#e9edf5"   # sky blue

janela = Tk()
janela.title("Sistema de Alunos")
janela.geometry("1043x453")
janela.configure(background="#ECF0F1")
janela.resizable(width=FALSE, height=FALSE)

############################################################

frameSuperior = Frame(janela, width = 310 , height = 50 , bg = "#2C3E50", relief = 'flat')
frameSuperior.grid(row = 0, column = 0)

frameInferior = Frame(janela, width = 310 , height = 403 , bg = co1, relief = 'flat')
frameInferior.grid(row = 1, column = 0)

frameDireito = Frame(janela, width = 733 , height = 403 , bg = co1, relief = 'flat')
frameDireito.grid(row = 0, column = 1, rowspan = 2, padx = 1, sticky = NSEW)


#################################################

app_nome = Label(frameSuperior, text = 'Sistema de Alunos', anchor = NW, font = ('Ivy 13 bold'), bg = "#2C3E50", fg=co1, relief= 'flat')
app_nome.place(x = 10, y = 20)


global tree


def inserir():
    nome = eNome.get()
    email = eEmail.get()
    idade = eIdade.get()
    telefone = eTelefone.get()
    dataN = eDataNascimento.get()
    sexo = eSexo.get()

    if not nome.replace(' ', '').isalpha():
        messagebox.showerror('Erro', 'O campo nome deve conter apenas letras!')
        return
    if not idade.isdigit():
        messagebox.showerror('Erro', 'O campo idade deve conter apenas números!')
        return
    if not (1 <= int(idade) <= 120):
        messagebox.showerror('Erro', 'Idade deve estar entre 1 e 120!')
        return
    if not telefone.isdigit():
        messagebox.showerror('Erro', 'O campo telefone deve conter apenas números!')
        return
    
    from datetime import date, datetime

    data_nasc = datetime.strptime(dataN, '%m/%d/%y').date()
    hoje = date.today()

    if data_nasc > hoje:
        messagebox.showerror('Erro', 'Data de nascimento não pode ser no futuro!')
        return

    if data_nasc.year < 1900 or data_nasc.year > 2020:
        messagebox.showerror('Erro', 'Data de nascimento inválida!')
        return

    lista = [nome, email, idade, telefone, dataN, sexo]

    if nome == '' or email == '' or idade == '' or telefone == '' or dataN == '' or sexo == 'Selecione':

        messagebox.showerror('Erro','Preencha todos os campos obrigatórios!')

    else:

        inserirInfo(lista)

        messagebox.showinfo('Sucesso','Informações inseridas com sucesso!')

        eNome.delete(0, END)
        eEmail.delete(0, END)
        eIdade.delete(0, END)
        eTelefone.delete(0, END)
        eDataNascimento.set_date(date.today())
        eSexo.set('Selecione')

        for widget in frameDireito.winfo_children():
            widget.destroy()

        mostrar()

def atualizar():

    for widget in frameInferior.winfo_children():
        if isinstance(widget, Button) and widget.cget('text') == 'Confirmar':
            widget.destroy()

    try:
        treev_dados = tree.focus()
        treev_dicionario = tree.item(treev_dados)
        tree_lista = treev_dicionario['values']
        matricula = tree_lista[0]

        eNome.delete(0, END)
        eEmail.delete(0, END)
        eIdade.delete(0, END)
        eTelefone.delete(0, END)
        eDataNascimento.set_date(date.today())
        eSexo.set('Selecione')

        eNome.insert(0, tree_lista[1])
        eEmail.insert(0, tree_lista[2])
        eIdade.insert(0, tree_lista[3])
        eTelefone.insert(0, tree_lista[4])
        eDataNascimento.set_date(tree_lista[5])
        eSexo.set(tree_lista[6])

        def confirmarAtualizacao():
            nome = eNome.get()
            email = eEmail.get()
            idade = eIdade.get()
            telefone = eTelefone.get()
            dataN = eDataNascimento.get()
            sexo = eSexo.get()
            lista = [nome,email,idade,telefone,dataN,sexo,matricula]

            atualizarInfo(lista)

            messagebox.showinfo('Sucesso','Dados atualizados com sucesso!')
            for widget in frameDireito.winfo_children():
                widget.destroy()
            mostrar()

        bConfirmar = Button(frameInferior,command=confirmarAtualizacao,text='Confirmar',width=10,height=1,bg=co6,fg=co1,font=('Ivy 7 bold'))
        bConfirmar.place(x=105, y=370)

    except:
        messagebox.showerror('Erro','Selecione um item para atualizar!')



#nome
lNome = Label(frameInferior, text = 'Nome*', anchor = NW, font = ('Ivy 10 bold'), bg = co1, fg="#34495E", relief= 'flat')
lNome.place(x = 10, y = 10)
eNome = Entry(frameInferior, width = 40, justify = 'left', relief = 'solid')
eNome.place(x = 10, y = 40)

#email
lEmail = Label(frameInferior, text = 'Email*', anchor = NW, font = ('Ivy 10 bold'), bg = co1, fg="#34495E", relief= 'flat')
lEmail.place(x = 10, y = 70)
eEmail = Entry(frameInferior, width = 40, justify = 'left', relief = 'solid')
eEmail.place(x = 10, y = 100)

#idade
lIdade = Label(frameInferior, text = 'Idade*', anchor = NW, font = ('Ivy 10 bold'), bg = co1, fg="#34495E", relief= 'flat')
lIdade.place(x = 10, y = 130)
eIdade = Entry(frameInferior, width = 40, justify = 'left', relief = 'solid')
eIdade.place(x = 10, y = 160)

#telefone
lTelefone = Label(frameInferior, text = 'Telefone*', anchor = NW, font = ('Ivy 10 bold'), bg = co1, fg="#34495E", relief= 'flat')
lTelefone.place(x = 10, y = 190)
eTelefone = Entry(frameInferior, width = 40, justify = 'left', relief = 'solid')
eTelefone.place(x = 10, y = 220)

#data de nascimento
lDataNascimento = Label(frameInferior, text = 'Data de Nascimento*', anchor = NW, font = ('Ivy 10 bold'), bg = co1, fg="#34495E", relief= 'flat')
lDataNascimento.place(x = 10, y = 250)
eDataNascimento = DateEntry(frameInferior, width = 12, background="#34495E", foreground=co1, borderwidth=2)
eDataNascimento.place(x = 10, y = 280)

#sexo
lSexo = Label(frameInferior,text='Sexo*',anchor=NW,font=('Ivy 10 bold'),bg=co1,fg="#34495E",relief='flat')
lSexo.place(x=170, y=250)
eSexo = ttk.Combobox(frameInferior,values=['Masculino', 'Feminino', 'Outro'],width=17)
eSexo.place(x=170, y=280)
eSexo.set('Selecione')

bInserir = Button(frameInferior, command=inserir, text = 'Inserir', width = 10, height = 1, bg = co2, fg = co1, font = ('Ivy 10 bold'), relief = 'raised', overrelief= 'ridge')
bInserir.place(x = 5, y = 340)

bAtualizar = Button(frameInferior, command=atualizar, text = 'Atualizar', width = 10, height = 1, bg = co6, fg = co1, font = ('Ivy 10 bold'), relief = 'raised', overrelief= 'ridge')
bAtualizar.place(x = 105, y = 340)

def excluir():
    selecionado = tree.selection()
    
    if not selecionado:
        messagebox.showerror('Erro', 'Selecione um item!')
        return

    valores = tree.item(selecionado[0], 'values')
    matricula = valores[0]

    deletarInfo(matricula)
    messagebox.showinfo('Sucesso', 'Aluno excluído com sucesso!')

    for widget in frameDireito.winfo_children():
        widget.destroy()

    mostrar()


bExcluir = Button(frameInferior,command=excluir,text='Excluir',width=10,height=1,bg=co7,fg=co1,font=('Ivy 10 bold'),relief='raised')
bExcluir.place(x=205, y=340)

#####################################################################
def mostrar():

    global tree

    lista = mostrarInfo()

    tree = ttk.Treeview(frameDireito,selectmode="extended",columns=("col1", "col2", "col3", "col4", "col5", "col6", "col7"),show="headings")

    tree.heading("col1", text="Matrícula")
    tree.heading("col2", text="Nome")
    tree.heading("col3", text="Email")
    tree.heading("col4", text="Idade")
    tree.heading("col5", text="Telefone")
    tree.heading("col6", text="Data de Nascimento")
    tree.heading("col7", text="Sexo")

    tree.column("col1", width=100)
    tree.column("col2", width=100)
    tree.column("col3", width=100)
    tree.column("col4", width=100)
    tree.column("col5", width=100)
    tree.column("col6", width=100)
    tree.column("col7", width=100)

    tree.place(x=10, y=10)

    vsb = ttk.Scrollbar(frameDireito, orient="vertical", command=tree.yview)

    vsb.place(x=710, y=10, height=380)

    tree.configure(yscrollcommand=vsb.set)

    for item in lista:

        tree.insert("","end",values=item)


mostrar()
janela.mainloop()












