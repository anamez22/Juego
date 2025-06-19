import tkinter as tk
from tkinter import *
from tkinter import messagebox as mb
import mariadb
from views.Tooltip import Tooltip
from Models.conexionBD import ConexionBD

class Registro():

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
            self.tool_contraseña2.update_tooltip("Para confirmar la contraseña\ndebe crear una contraseña",background="#fa8a76")
            self.tool_contraseña.update_tooltip("Para poder crear una contraseña primero \ncree un nombre de usuario VALIDO",background="#fa8a76")
            self.txtPassword.config(state="disabled")
            self.txtPassword2.config(state="disabled")
            
         

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

        if self.estado_contraseña=="valido":
            self.txtPassword2.config(state="normal")
            self.tool_contraseña2.update_tooltip("Ingrese nuevamente su contraseña.\nDebe ser igual a la anterior.", background="white")
        elif self.estado_contraseña=="invalido":
            self.tool_contraseña2.update_tooltip("Para poder confirmar primero debe crear una contraseña VALIDA",background="#fa8a76")
            self.txtPassword2.delete(0, END)
            self.txtPassword2.config(state="disabled")
            

    def verificar_contraseña(self,event):
        self.tool_contraseña2.hide_tooltip()
        self.tool_guardar.hide_tooltip()

        contraseña1=self.txtPassword.get()
        contraseña2=self.txtPassword2.get()


        if contraseña2 == contraseña1:
            self.tool_contraseña2.update_tooltip("¡Bien hecho, Las contraseñas coinciden!",background="#76fa99")
            self.btnGuardar.config(state="normal")
            self.tool_guardar.update_tooltip("Presione para guardar los datos ingresados", background="#76fa99")
        

        elif contraseña2 != contraseña1:
            self.tool_guardar.update_tooltip("Primero debe llenar los campos solicitados correctamente", background="#fa8a76")
            self.tool_contraseña2.update_tooltip("Las contraseñas no coinciden.",background="#fa8a76")
            self.btnGuardar.config(state="disabled")

        self.tool_contraseña2.show_tooltip()
        
        
    def verCaracteres(self, event):
        if(self.bandera == True):
            self.txtPassword.config(show='*')
            self.txtPassword2.config(show='*')
            self.btnVer.config(bg="#ff5810")
            self.bandera = False
        else:
            self.txtPassword.config(show='')
            self.txtPassword2.config(show='')
            self.btnVer.config(bg="#4fff2c")
            self.bandera = True

    def ocultar_tooltips(self, event):
        widget_foco= event.widget
        if widget_foco != self.txtUsuario:
            self.tool_usuario.hide_tooltip()
        if widget_foco != self.txtPassword:
            self.tool_contraseña.hide_tooltip()
        if widget_foco != self.txtPassword2:
            self.tool_contraseña2.hide_tooltip()

    def eliminar_datos(self,event):
        self.txtUsuario.delete(0, END)
        self.txtPassword.delete(0, END)
        self.txtPassword2.delete(0, END)
        self.btnGuardar.config(state="disabled")
        self.estado_usuario=None
        self.estado_contraseña= None
        self.txtPassword.config(state="disabled")
        self.txtPassword2.config(state="disabled")
        self.txtUsuario.focus()

    def mostrar_ayuda(self, event):
        ayuda_texto=("Guía de Registro:\n\n"
        "Sabemos que a veces los atajos pueden hacer todo más fácil, así que aquí te dejamos una lista de (hot keys) que puedes usar mientras completas tu registro:\n\n"
        "🔹 Control + I -> Abre la venta de inicio de sesion si ya te creaste una cuenta\n"
        "🔹 Control + S -> Guarda los datos que has escrito.\n"
        "🔹 Control + D -> Este atajo borra todos los campos para que puedas ingresar nuevos datos.\n"
        "🔹 Control + O -> Muestra u oculta las contraseñas. Así puedes revisar lo que escribiste\n"
        "🔹 Control + A -> Usa este atajo para abrir esta guía.\n\n"
        
        "✨ Además, cada vez que pongas el cursor sobre un botón o campo,te aparecerá una pequeña guía explicándote qué debes hacer allí")

        mb.showinfo("Ayuda de Registro", ayuda_texto)
        
    def iniciar_logging(self, event):
            from views.Logging import Logging
            self.ventana.destroy()
            logging = Logging()
    
            
    
    def guardar_datos(self, event):  # BASE DE DATOS
        if self.estado_usuario == "valido" and self.estado_contraseña == "valido":
            bd = ConexionBD()
            bd.crearConexion()
            conn = bd.getConnection()
            if conn:
                try:
                    cursor = conn.cursor()
                    usuario = self.txtUsuario.get()
                    contraseña = self.txtPassword.get()
                    cursor.execute(
                        "INSERT INTO usuarios (usuario, contraseña) VALUES (?, ?)",
                        (usuario, contraseña)
                    )
                    conn.commit()
                    mb.showinfo("Registro Exitoso", "¡Usuario registrado exitosamente!")
                    self.eliminar_datos(None)
                except mariadb.IntegrityError:
                    mb.showerror("Error", "Ese nombre de usuario ya existe.")
                finally:
                    bd.cerrarConexion()



    def __init__(self):
        self.ventana = tk.Tk()
        self.ventana.title("Registro")
        self.ventana.config(width=600, height=550, bg="#12b3b3") 
        self.ventana.resizable(0,0)

        self.lienzo = tk.Canvas(self.ventana, bg = "#aaff98")
        self.lienzo.place(relx=0.5, rely=0.5, anchor="center", width=550, height=500)

        self.iconoUsuario = tk.PhotoImage(file=r"Juego\icons\icons8-user-30.png")
        self.iconoVentana = tk.PhotoImage(file=r"Juego\icons\icons8-sign-in-80.png")
        self.iconoVer = tk.PhotoImage(file=r"Juego\icons\icons8-preview-pane-30.png")
        self.iconoAyuda = tk.PhotoImage(file=r"Juego\icons\icons8-help-eye-50.png")
        self.iconoGuardar = tk.PhotoImage(file=r"Juego\icons\icons8-save-40.png")
        self.iconoEliminar = tk.PhotoImage(file=r"Juego\icons\icons8-trash-40.png")
               
        self.lblTitulo = tk.Label(self.ventana, text="Crear Cuenta", font= ("Arial", 15), bg="#def1f7")
        self.lblTitulo.place(width=200, height=40, relx=0.5, y=50, anchor="n")

        self.lblIconoVentana = tk.Label(self.ventana, image=self.iconoVentana, bg="#aaff98")
        self.lblIconoVentana.place(width=80, height=80, relx=0.5, y=120, anchor="n")

        self.btnAyuda = tk.Button(self.ventana, image=self.iconoAyuda, bg="#def1f7")
        self.btnAyuda.place(width=50, height=50, x=495, y=50)
        Tooltip(self.btnAyuda, "Presione para ver la ayuda")
        self.btnAyuda.bind("<Button-1>", self.mostrar_ayuda)

        self.lblUsuario = tk.Label(self.ventana, text="Usuario*:", image=self.iconoUsuario, compound=LEFT, font=("Arial", 12), bg="#def1f7")
        self.lblUsuario.place(width=170, height=30, x=66, y=240)

        self.txtUsuario = tk.Entry(self.ventana)
        self.txtUsuario.place(width=150, height=30, x=245, y=240)
        self.tool_usuario= Tooltip(self.txtUsuario, "Ingrese su nombre de usuario.\nminimo 6 carácteres.\nSolo letras y números.")
        self.txtUsuario.focus()
        self.txtUsuario.bind("<KeyRelease>", self.validar_usuario)

        self.lblPassword = tk.Label(self.ventana, text="Contraseña*:", font=("Arial", 12), bg="#def1f7")
        self.lblPassword.place(width=170, height=30, x=66, y=290)

        self.txtPassword = tk.Entry(self.ventana, show="*",state="disabled")
        self.txtPassword.place(width=150, height=30, x=245, y=290)
        self.tool_contraseña=Tooltip(self.txtPassword, "Para poder crear una contraseña primero \ncree un nombre de usuario VALIDO")
        self.txtPassword.bind("<KeyRelease>", self.validar_contraseña)
   
        self.btnVer = tk.Button(self.ventana, image =self.iconoVer, bg="#ff5810")
        self.btnVer.place(width=30, height=30, x=430, y=290) 
        Tooltip(self.btnVer, "Presione para ver las contraseñas")
        self.btnVer.bind("<Button-1>", self.verCaracteres) 

        self.lblPassword2= tk.Label(self.ventana, text=" Confirmar Contraseña*:", font=("Arial", 12), bg="#def1f7")
        self.lblPassword2.place(width=170, height=30, x=66, y=340)

        self.txtPassword2 = tk.Entry(self.ventana, show="*",state="disabled")
        self.txtPassword2.place(width=150, height=30, x=245, y=340)
        self.tool_contraseña2=Tooltip(self.txtPassword2, "Para poder confirmar primero debe crear una contraseña VALIDA")
        self.txtPassword2.bind("<KeyRelease>", self.verificar_contraseña)

        self.btnGuardar = tk.Button(self.ventana, text="Guardar", font=("Arial", 12), image=self.iconoGuardar, compound=LEFT, state="disabled")
        self.btnGuardar.place(width=120, height=40, relx=0.5, y=410)
        self.tool_guardar=Tooltip(self.btnGuardar, "Primero debe llenar los campos \nsolicitados correctamente")
        self.btnGuardar.bind("<Button-1>", self.guardar_datos)

        self.btnInicio_sesion = tk.Button(self.ventana, text="Iniciar Sesión",font=("Arial", 12),image=self.iconoUsuario, compound=LEFT)
        self.btnInicio_sesion.place(width=135, height=40, relx=0.2, y=410)
        Tooltip(self.btnInicio_sesion, "¡Inicia Sesión si ya tienes una cuenta!\nPresione para iniciar sesión")
        self.btnInicio_sesion.bind("<Button-1>", self.iniciar_logging)

        self.btnEliminar = tk.Button(self.ventana, image=self.iconoEliminar)
        self.btnEliminar.place(width=40, height=40, x=66, y=470)
        Tooltip(self.btnEliminar, "Presione para eliminar \nlos datos ingresados")
        self.btnEliminar.bind("<Button-1>", self.eliminar_datos)

        self.bandera = False
        self.estado_usuario=None
        self.estado_contraseña=None

        self.txtUsuario.bind_all("<FocusIn>", self.ocultar_tooltips)
        self.txtPassword.bind_all("<FocusIn>", self.ocultar_tooltips)
        self.txtPassword2.bind_all("<FocusIn>", self.ocultar_tooltips)

        self.btnInicio_sesion.bind_all('<Control-i>', self.iniciar_logging)
        self.btnInicio_sesion.bind_all('<Control-I>', self.iniciar_logging)

        # Binds para Control + S
        self.btnGuardar.bind_all('<Control-s>', self.guardar_datos)
        self.btnGuardar.bind_all('<Control-S>', self.guardar_datos)

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