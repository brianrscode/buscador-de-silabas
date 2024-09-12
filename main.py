import customtkinter
from tkinter import filedialog, messagebox
from buscar_silabas import BuscaSilabas


def select_file():
    # Tipos de archivos permitidos
    filetypes = (
        ('All files', '*.*'),
        ('PDF files', '*.pdf'),
        ('docx files', '*.docx'),
        ('Text files', '*.txt')
    )
    # Abre un cuadro de dialogo para seleccionar un archivo
    filename = filedialog.askopenfilename(
        title='Open a file',
        initialdir="/",
        filetypes=filetypes
    )
    if filename: # Si hay un archivo seleccionado
        try:
            # Crea una etiqueta para mostrar el nombre del archivo seleccionado
            label = customtkinter.CTkLabel(app, text=f"{filename}", fg_color="transparent")
            label.grid(row=1, column=1, padx=0, pady=0, sticky="n")

            # Crea una instancia de la clase BuscaSilabas para buscar palabras de 4 silabas
            silabas = BuscaSilabas(filename)
            coincidencias, num_coincidencias = silabas.buscar_coincidencias()

            # Modifica la etiqueta para mostrar el número de coincidencias
            label_coincidencias.configure(text=f"Palabras con 4 silabas: {num_coincidencias}")

            # Limpiar texto previo
            resultado_text.delete("0.0", "end")
            for i, coincidencia in enumerate(coincidencias):
                # Agregar cada coincidencia al cuadro de texto de resultados y enumerarlas
                resultado_text.insert("end", f"{i+1}.- {coincidencia}\n")

        except Exception as e:
            messagebox.showerror("Error", f"Ha ocurrido un error: {e}")


app = customtkinter.CTk()

# Configuración de la ventana
app.geometry("400x450")
app.title("Palabras con 4 silabas")
app.resizable(False, False)

# Configuración de las columnas
app.grid_columnconfigure((0, 2), weight=1)
app.grid_columnconfigure(1, weight=2)

# Crear un botón para abrir el diálogo de selección de archivos
button_file = customtkinter.CTkButton(app, text="Abrir archivo", anchor="center", command=select_file)
button_file.grid(row=0, column=0, columnspan=3, padx=10, pady=10, sticky="s")

# Crea una etiqueta para mostrar la cantidad de palabras con 4 silabas
label_coincidencias = customtkinter.CTkLabel(app, text="Palabras con 4 silabas:", fg_color="transparent")
label_coincidencias.grid(row=2, column=1, padx=10, pady=10)

# Crea un cuadro de texto para mostrar las coincidencias
resultado_text = customtkinter.CTkTextbox(app, width=300, height=300)
resultado_text.grid(row=3, column=0, columnspan=3, padx=0, pady=0 )

app.mainloop()
