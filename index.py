## import das bibliotecas
from tkinter import *
from tkinter import messagebox
from tkinter import ttk
import DataBaser

## Criando a janela
janela = Tk()
janela.title("DP Systems - Access Panel")
janela.geometry("600x300")
janela.configure(background="white")
janela.resizable(width=False, height=False)
# transparência na janela
janela.attributes("-alpha", 0.9)
# Adicionando um .ico (ÍCONE)
janela.iconbitmap(default="Imgs/LogoIcon.ico")

# Imagens
logo = PhotoImage(file="Imgs/logo.png")

## Widgets
# Lado Esquerdo
LeftFrame = Frame(janela, width=200, height=300, bg="MIDNIGHTBLUE", relief="raise")
LeftFrame.pack(side=LEFT)
# Lado Direito
RightFrame = Frame(janela, width=395, height=300, bg="MIDNIGHTBLUE", relief="raise")
RightFrame.pack(side=RIGHT)

## Adicionando a logo a tela de login
LogoLabel = Label(LeftFrame, image=logo, bg="MIDNIGHTBLUE")
LogoLabel.place(x=50, y=100)

# H1 USERNAME
UserLabel = Label(RightFrame, text="Username:", font=("Product Sans", 20), bg="MIDNIGHTBLUE", fg="white")
UserLabel.place(x=5, y=100)
# Entrada de dados USER
UserEntry = ttk.Entry(RightFrame, width=30)
UserEntry.place(x=150, y=113)

# H1 PASSWORD
PassLabel = Label(RightFrame, text="Password:", font=("Product Sans", 20), bg="MIDNIGHTBLUE", fg="white")
PassLabel.place(x=5, y=150)
# Entrada de dados PSSWRD
# "show" nesse caso faz com que o password não apareça e substitua o txt por *
PassEntry = ttk.Entry(RightFrame, width=30, show="*")
PassEntry.place (x=150, y=163)

## Botões
# Botão Login
def Login():
    User = UserEntry.get()
    Pass = PassEntry.get()

    DataBaser.cursor.execute("""
    SELECT * FROM Users
    WHERE (User = ? AND Password = ?)  
    """, (User, Pass))
    print("Selecionou!")
    VerifyLogin = DataBaser.cursor.fetchone()
    try:
        if (User in VerifyLogin and Pass in VerifyLogin):
            messagebox.showinfo(title="Login Info", message="Access Confirmed, Welcome!")
    except:
        messagebox.showinfo(title="Login Info", message="Denied Access!")

LoginButton = ttk.Button(RightFrame, text="Login", width=30, command=Login)
# O .place serve para POSICIONAR os componentes na tela
LoginButton.place(x=100, y=225)

#### Botão Registro
## Função de Registro
def Register():
    # Removendo widgets de Login
    LoginButton.place(x=5000)
    RegisterButton.place(x=5000)
    # Inserindo widgets de Cadastro
    NomeLabel = Label(RightFrame, text="Name:", font=("Product Sans", 20), bg="MIDNIGHTBLUE", fg="white")
    NomeLabel.place(x=5, y=5)

    NomeEntry = ttk.Entry(RightFrame, width=39)
    NomeEntry.place(x=100, y=18)
    # Inserindo campo de e-mail
    EmailLabel = Label(RightFrame, text= "E-mail:", font=("Product Sans", 20), bg="MIDNIGHTBLUE", fg="white")
    EmailLabel.place(x=5, y=55)

    EmailEntry = ttk.Entry(RightFrame, width=39)
    EmailEntry.place(x=100, y=65)

    def RegisterToDataBase():
        Name = NomeEntry.get()
        Email = EmailEntry.get()
        User = UserEntry.get()
        Pass = PassEntry.get()

        if (Name == "" and Email == "" and User == "" and Pass == ""):
            messagebox.showerror(title="Register Error", message="Empty Fields")
        else:
            DataBaser.cursor.execute("""
            INSERT INTO Users(Name, Email, User, Password) VALUES(?, ?, ?, ?)
            """, (Name, Email, User, Pass))
            DataBaser.conn.commit()
            messagebox.showinfo(title="Register Info", message="Register Success")

    Register = ttk.Button(RightFrame, text="Register", width=30, command=RegisterToDataBase)
    Register.place(x=100, y=225)

    def BackToLogin():
        # Removendo os Widgets de registro
        NomeLabel.place(x=999)
        NomeEntry.place(x=999)
        EmailLabel.place(x=999)
        EmailEntry.place(x=999)
        Register.place(x=999)
        Back.place(x=999)
        # Trazendo de volta os widgets de login
        LoginButton.place(x= 100, y=225)
        RegisterButton.place(x= 125, y=260)

    Back = ttk.Button(RightFrame, text="Back", width=20, command=BackToLogin)
    Back.place(x=125, y=260)

# para atribuir uma função a um botão, utilizando o command=nomeDaFunção
RegisterButton = ttk.Button(RightFrame, text="Register", width=20, command=Register)
RegisterButton.place(x=125, y=260)

janela.mainloop()