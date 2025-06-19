import tkinter as tk 
from tkinter import *
from views.Tooltip import Tooltip
from views.juego import Juego
from tkinter import messagebox as mb

class Logging():

    def validar_usuario(self,event):
        usuario = self.txtUsuario.get()
        letras=0
        for i in usuario:
            if i.isalpha():
                letras+=1
        
        self.tool_usuario.hide_tooltip()
   
        if usuario.isalnum() or event.keysym == "BackSpace":
            if len(self.txtUsuario.get()) >= 6 and len(self.txtUsuario.get())<=10:
                if letras >=3:
                    self.tool_usuario.update_tooltip("¡Usuario Valido!",background="#76fa99")
                    self.estado_usuario="valido"
                else:
                    self.tool_usuario.update_tooltip("El usuario debe tener al menos 3 letras.", background="#fa8a76")
                    self.estado_usuario="invalido"

            elif len(self.txtUsuario.get()) < 6:
                self.tool_usuario.update_tooltip("El usuario debe tener al menos 6 caracteres.", background="#fa8a76")
                self.estado_usuario="invalido"
            
            elif len(self.txtUsuario.get()) > 10:
                self.tool_usuario.update_tooltip("El usuario no debe tener más de 15 caracteres.", background="#fa8a76")
                self.estado_usuario="invalido"
        else:
            self.tool_usuario.update_tooltip("El usuario debe tener SOLO letras y números.\nNO se aceptan caracteres especiales ni espacios",background="#fa8a76")
            self.estado_usuario="invalido"

        self.tool_usuario.show_tooltip()

        
        if self.estado_usuario=="valido":
            self.txtPassword.config(state="normal")
            self.tool_contraseña.update_tooltip("Ingrese su contraseña. \nminimo 6 carácteres.\nletras, números, * y _", background="white")
            

        elif self.estado_usuario=="invalido":
            self.tool_contraseña.update_tooltip("Para poder crear una contraseña primero \ncree un nombre de usuario VALIDO",background="#fa8a76")
            self.txtPassword.config(state="disabled")
         

    def validar_contraseña(self,event):
        import re
        self.tool_contraseña.hide_tooltip()

        contraseña = self.txtPassword.get()
        patron= r"^[a-zA-Z0-9*_-]+$"  # Permite letras, números, *, _ y -
        
        
        if re.match(patron, contraseña) or event.keysym == "BackSpace":
            if len(contraseña) >= 6 and len(contraseña)<=10:
                self.tool_contraseña.update_tooltip("¡Contraseña Valida!",background="#76fa99")
                self.estado_contraseña="valido"

            elif len(contraseña) < 6:
                self.tool_contraseña.update_tooltip("La contraseña debe tener al menos 6 caracteres.", background="#fa8a76")
                self.estado_contraseña="invalido"
            
            elif len(contraseña) > 10:
                self.tool_contraseña.update_tooltip("La contraseña no debe tener \nmás de 10 caracteres.", background="#fa8a76")
                self.estado_contraseña="invalido"

        else:
            self.tool_contraseña.update_tooltip("En la contraseña SOLO se permiten letras, números, * y _\nNO se aceptan otros caracteres ni espacios",background="#fa8a76")
            self.estado_contraseña="invalido"

        self.tool_contraseña.show_tooltip()

        if self.estado_usuario == "valido" and self.estado_contraseña == "valido":
            self.btnIngresar.config(state="normal")
            self.tool_ingresar.update_tooltip("Presione para ingresar al juego", background="white")
            self.btnIngresar.bind("<Button-1>", self.comenzarJuego)

    def ocultar_tooltips(self, event):
        widget_foco= event.widget
        if widget_foco != self.txtUsuario:
            self.tool_usuario.hide_tooltip()
        if widget_foco != self.txtPassword:
            self.tool_contraseña.hide_tooltip()

    def eliminar_datos(self,event):
        self.txtUsuario.delete(0, END)
        self.txtPassword.delete(0, END)
        self.estado_usuario=None
        self.estado_contraseña= None
        self.txtPassword.config(state="disabled")
        self.btnIngresar.config(state="disabled")
        self.tool_ingresar.update_tooltip("Para ingresar al juego primero debe ingresar \nun usuario y una contraseña ", background="white")
        self.txtUsuario.focus()


    def verCaracteres(self, event):
        if(self.bandera == True):
            self.txtPassword.config(show='*')
            self.btnVer.config(bg="#ff5810")
            self.bandera = False
        else:
            self.txtPassword.config(show='')
            self.btnVer.config(bg="#4fff2c")
            self.bandera = True

    def mostrar_ayuda(self, event):
        ayuda_texto=("Guía de Inicio de Sesión:\n\n"
        "Sabemos que a veces los atajos pueden hacer todo más fácil, así que aquí te dejamos una lista de (hot keys) que puedes usar mientras completas tu registro:\n\n"
        "🔹 Control + R -> Abre la ventana de registro para que te crees una cuenta\n"
        "🔹 Control + D -> Este atajo borra todos los campos para que puedas ingresar nuevos datos.\n"
        "🔹 Control + O -> Muestra u oculta las contraseñas. Así puedes revisar lo que escribiste\n"
        "🔹 Control + A -> Usa este atajo para abrir esta guía.\n\n"
      
        "✨ Además, cada vez que pongas el cursor sobre un botón o campo,te aparecerá una pequeña guía explicándote qué debes hacer allí")

        mb.showinfo("Ayuda de Registro", ayuda_texto)
    
    def iniciar_registro(self, event):
        self.ventana.destroy()
        from views.registrar import Registro
        registro = Registro()

    def comenzarJuego(self, event):  # BASE DE DATOS
        from Models.conexionBD import ConexionBD
        import mariadb

        usuario = self.txtUsuario.get()
        contraseña = self.txtPassword.get()

        bd = ConexionBD()
        bd.crearConexion()
        conn = bd.getConnection()

        if conn:
            try:
                cursor = conn.cursor()
                
                cursor.execute("SELECT * FROM usuarios WHERE usuario = ? AND contraseña = ?", (usuario, contraseña))
                resultado = cursor.fetchone()
                if resultado:
                    mb.showinfo("Bienvenido", f"¡Hola {usuario}! Has iniciado sesión exitosamente.")
                    self.ventana.destroy()
                    juego = Juego(usuario_actual=usuario)
                else:
                    mb.showerror("Error", "Usuario o contraseña incorrectos.\n¿Ya tienes una cuenta?")
            except mariadb.Error as e:
                mb.showerror("Error de Base de Datos", f"Ocurrió un error al consultar los datos.\n{e}")
            finally:
                bd.cerrarConexion()



    def __init__(self, usuario_actual=None):

        self.usuario_actual = usuario_actual
        self.best_score = 0
        self.puntaje = 0

        self.ventana = tk.Tk()
        self.ventana.title("Logging")
        self.ventana.config(width=500, height=450, bg="#12b3b3") 
        self.ventana.resizable(0,0)

        self.lienzo = tk.Canvas(self.ventana, bg = "#aaff98")
        self.lienzo.place(relx=0.5, rely=0.5, anchor="center", width=450, height=400)

        self.lienzo.create_oval(5, 5, 30, 30, fill="#9bb0ec", outline="#0a2e91")
        self.lienzo.create_oval(150, 150, 170, 170, fill="#788fcc", outline="#0a2e91")
        self.lienzo.create_oval(350, 350, 370, 370, fill="#a062c9", outline="#4c0c77")
        self.lienzo.create_oval(380, 60, 400, 80, fill="#8955ac", outline="#4c0c77")
        self.lienzo.create_oval(50, 90, 70, 110, fill="#e0fa6f", outline="#ecdf22")
        self.lienzo.create_oval(400, 250, 420, 270, fill="#e0fa6f", outline="#ecdf22")
        self.lienzo.create_oval(350, 190, 370, 210, fill="#f7829f", outline="#a10e75")
        self.lienzo.create_oval(70, 340, 90, 360, fill="#fa6f92", outline="#a10e75")
        self.lienzo.create_oval(220, 320, 240, 340, fill="#3bbb09", outline="#069e1f")
        self.lienzo.create_oval(280, 70, 300, 90, fill="#3bbb09", outline="#069e1f")

        self.iconoAyuda = tk.PhotoImage(file=r"Juego\icons\icons8-help.png")
        self.iconoEntrar = tk.PhotoImage(file=r"Juego\icons\icons8-enter-40.png")
        self.iconoVer = tk.PhotoImage(file=r"Juego\icons\icons8-vision-30.png")
        self.iconoVen = tk.PhotoImage(file=r"Juego\icons\icons8-bmo-80.png")
        self.iconoEliminar = tk.PhotoImage(file=r"Juego\icons\icons8-trash-40.png")
        self.iconoRegis = tk.PhotoImage(file=r"Juego\icons\icons8-add-user-35.png")

        self.lblTitulo = tk.Label(self.ventana, text="Inicio de Sesión", font= ("Arial", 15), bg="#fdebd0")
        self.lblTitulo.place(width=200, height=40, relx=0.5, y=40, anchor="n")

        self.lblIconoVen = tk.Label(self.ventana, image=self.iconoVen, bg="#aaff98")
        self.lblIconoVen.place(width=80, height=80, relx=0.5, y=90, anchor="n")

        self.btnAyuda = tk.Button(self.ventana, image=self.iconoAyuda)
        self.btnAyuda.place(width=50, height=50, x=400, y=40)
        Tooltip(self.btnAyuda, "Presione para ver la ayuda")
        self.btnAyuda.bind("<Button-1>", self.mostrar_ayuda)
                                      
        self.lblUsuario = tk.Label(self.ventana, text="Usuario*:", font=("Arial", 12), bg="#fdebd0")
        self.lblUsuario.place(width=120, height=30, x=70, y=200)

        self.txtUsuario = tk.Entry(self.ventana)
        self.txtUsuario.place(width=150, height=30, x=190, y=200)
        self.tool_usuario= Tooltip(self.txtUsuario, "Ingrese su nombre de usuario.\nminimo 6 carácteres.\nSolo letras y números.")
        self.txtUsuario.focus()
        self.txtUsuario.bind("<KeyRelease>", self.validar_usuario)
        
        self.lblPassword = tk.Label(self.ventana, text="Contraseña*:", font=("Arial", 12), bg="#fdebd0")
        self.lblPassword.place(width=120, height=30, x=70, y=240)

        self.txtPassword = tk.Entry(self.ventana, show="*", state="disabled")
        self.txtPassword.place(width=150, height=30, x=190, y=240)
        self.tool_contraseña=Tooltip(self.txtPassword, "Para poder ingresar su contraseña \nprimero debe ingresar su nombre de usuario ")
        self.txtPassword.bind("<KeyRelease>", self.validar_contraseña)
   
        self.btnVer = tk.Button(self.ventana, image =self.iconoVer, bg="#ff5810")
        self.btnVer.place(width=30, height=30, x=370, y=240)  
        Tooltip(self.btnVer, "Presione para ver la contraseña")
        self.btnVer.bind("<Button-1>", self.verCaracteres)                    
        
        self.btnIngresar = tk.Button(self.ventana, text="Ingresar", image=self.iconoEntrar, compound=LEFT, state="disabled")
        self.btnIngresar.place(width=120, height=40, relx=0.5, y=310)
        self.tool_ingresar=Tooltip(self.btnIngresar, "Para ingresar al juego, \nprimero debe ingresar un usuario y una contraseña")
        
        self.btnRegistrarse = tk.Button(self.ventana, text="Registrarse", image=self.iconoRegis, compound=RIGHT)
        self.btnRegistrarse.place(width=120, height=40, relx=0.2, y=310)
        Tooltip(self.btnRegistrarse, "¡Registrate si no tienes una cuenta!\nPresione para registrarse")
        self.btnRegistrarse.bind("<Button-1>", self.iniciar_registro)

        self.btnEliminar = tk.Button(self.ventana, image=self.iconoEliminar)
        self.btnEliminar.place(width=40, height=40, x=40, y=370)
        Tooltip(self.btnEliminar, "Presione para eliminar los datos ingresados")
        self.btnEliminar.bind("<Button-1>", self.eliminar_datos)


        self.bandera = False
        self.estado_usuario=None
        self.estado_contraseña=None

        self.txtUsuario.bind("<FocusIn>", self.ocultar_tooltips)
        self.txtPassword.bind("<FocusIn>", self.ocultar_tooltips)

        self.btnRegistrarse.bind_all('<Control-r>', self.iniciar_registro)
        self.btnRegistrarse.bind_all('<Control-R>', self.iniciar_registro)

        # Binds para Control + D
        self.btnEliminar.bind_all('<Control-d>', self.eliminar_datos)
        self.btnEliminar.bind_all('<Control-D>', self.eliminar_datos)

        # Binds para Control + O
        self.btnVer.bind_all('<Control-o>', self.verCaracteres)
        self.btnVer.bind_all('<Control-O>', self.verCaracteres)

        # Binds para Control + A
        self.btnAyuda.bind_all('<Control-a>', self.mostrar_ayuda)
        self.btnAyuda.bind_all('<Control-A>', self.mostrar_ayuda)

        self.ventana.mainloop()


