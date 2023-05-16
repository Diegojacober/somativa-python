from tkinter import *
from tkinter import ttk
from tkinter import tix
from Functions import Functions

# vskiwir

root = tix.Tk()

class Application(Functions):
    
    APP_BACKGROUND_COLOR = '#1e3743'
    FRAME1_BACKGROUND_COLOR = '#4F4F4F'
    FRAME2_BACKGROUND_COLOR = '#ddd'
    BUTTONS_BG = "#107db2"
    BUTTON_COLOR = "#FFF"
    FONT_FAMILY = 'verdana'
    
    def __init__(self) -> None:
        super().__init__()
        self.root = root
        self.tela()
        self.frames()
        self.widgets_frame1()
        self.widget_frame2()
        self.menus()
        
        root.mainloop()
        
    
    def tela(self):
        self.root.title("Atividade Somativa")
        self.root.configure(background=Application.APP_BACKGROUND_COLOR)
        LARGURA = 800
        ALTURA = 800
        LAGURA_SCREEN = self.root.winfo_screenwidth()
        ALTURA_SCREEN = self.root.winfo_screenheight()
        POS_X = int((LAGURA_SCREEN/2) - (LARGURA/2))
        POS_Y = int((ALTURA_SCREEN/2) - (ALTURA/2))

        self.root.minsize(width=700, height=700)
        self.root.geometry(f"{LARGURA}x{ALTURA}+{POS_X}+{POS_Y}")
        
        
    def frames(self):
        
        self.frame_1 = Frame(self.root,
                             border=4,
                             background=Application.FRAME1_BACKGROUND_COLOR,
                             highlightbackground="#000", 
                             highlightthickness=2)
      
        self.frame_1.place(relx=0.02, rely=0.02, relwidth=0.96, relheight=0.30)
        
        
        self.frame_2 = Frame(self.root,
                             border=4,
                             background=Application.FRAME2_BACKGROUND_COLOR,
                             highlightbackground="#000", 
                             highlightthickness=2)
        
        self.frame_2.place(relx=0.02, rely=0.5, relwidth=0.96, relheight=0.65)
        
    
    def widgets_frame1(self):
        
        self.canvas_bt = Canvas(self.frame_1, bd=0, bg='#000', highlightbackground=Application.APP_BACKGROUND_COLOR, highlightthickness=5)
        self.canvas_bt.place(relx=0.19, rely=0.08, relwidth=0.22, relheight=0.16)
        
        self.btn_verCelulares = Button(self.frame_1, text='Ver todos os celulares', bd=2, bg=Application.BUTTONS_BG, fg=Application.BUTTON_COLOR, font=(Application.FONT_FAMILY,8,'bold'), activebackground='green',command=self.get_all_phones)
        self.btn_verCelulares.place(relx=0.2, rely=0.1, relwidth=0.204, relheight=0.12)

        options = [
            "SAMSUNG",
            "APPLE",
            "MOTOROLA",
            "LG",
            "XIAOMI",
        ]
        
        
        self.clicked = StringVar()
        self.clicked.set( "SAMSUNG" )
        drop = OptionMenu( self.frame_1 , self.clicked , *options )
        drop.place(relx=0.5,rely=0.1, relwidth=0.3, relheight=0.10)
        
        self.btn_verCelularesMarca = Button(self.frame_1, text='Ver celulares dessa marca', bd=2, bg=Application.BUTTONS_BG, fg=Application.BUTTON_COLOR, font=(Application.FONT_FAMILY,8,'bold'), activebackground='green',command=self.get_per_marca)
        self.btn_verCelularesMarca.place(relx=0.5, rely=0.2, relwidth=0.3, relheight=0.10)
        
        
        options_export = [
            ".XLSX",
            ".CSV",
        ]
        
        
        self.clickedExport = StringVar()
        self.clickedExport.set( ".XLSX" )
        drop = OptionMenu( self.frame_1 , self.clickedExport , *options_export )
        drop.place(relx=0.5,rely=0.4, relwidth=0.3, relheight=0.10)
        
        self.btn_export = Button(self.frame_1, text='Exportar para essa extensão', bd=2, bg=Application.BUTTONS_BG, fg=Application.BUTTON_COLOR, font=(Application.FONT_FAMILY,8,'bold'), activebackground='green',command=self.export)
        self.btn_export.place(relx=0.5, rely=0.5, relwidth=0.3, relheight=0.10)


    def widget_frame2(self):
        self.lista_celulares = ttk.Treeview(self.frame_2,
                                           height=3,
                                           columns=("col1", "col2", "col3", "col4"))
        
        self.lista_celulares.heading("#0", text="")
        self.lista_celulares.heading("#1", text="Código")
        self.lista_celulares.heading("#2", text="Nome")
        self.lista_celulares.heading("#3", text="Marca")
        self.lista_celulares.heading("#4", text="Preço")
        
        self.lista_celulares.column('#0', width=1)
        self.lista_celulares.column('#1', width=50)
        self.lista_celulares.column('#2', width=200)
        self.lista_celulares.column('#3', width=125)
        self.lista_celulares.column('#4', width=125)
        
        self.lista_celulares.place(relx=0.01, rely=0.01, relheight=0.95, relwidth=0.85)
        
        self.scrool_lista = Scrollbar(self.frame_2, orient='vertical')
        self.lista_celulares.configure(yscroll=self.scrool_lista.set)
        self.scrool_lista.place(relx=0.96, rely=0.1, relwidth=0.04, relheight=0.85)
        self.lista_celulares.bind("<Double-1>", self.OnDoubleClick)
        
    
    def menus(self):
        menubar = Menu(self.root)
        self.root.config(menu=menubar)
        filemenu = Menu(menubar)
        
        def Quit(): self.root.destroy()
        
        menubar.add_cascade(label="Opções", menu=filemenu)
        
        filemenu.add_command(label="Sair", command=Quit)
        filemenu.add_command(label="Carregar dados da internet", command=self.web_scrapping)
        filemenu.add_command(label="Gerar Grafico", command=self.grafico)
        
        
    
            
if __name__ == "__main__":
    Application()