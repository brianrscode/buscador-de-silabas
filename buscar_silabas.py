import os
import re
from docx import Document
from pypdf import PdfReader


class BuscaSilabas():

    def __init__(self, ruta_archivo) -> None:
        self.ruta_archivo = ruta_archivo

    def obtener_texto_txt(self) -> str:
        '''Lee el contenido de un archivo de texto plano y lo devuelve como una cadena.'''
        contenido:str = ""
        with open(self.ruta_archivo, 'r', encoding='utf-8') as archivo:
            contenido = archivo.read()
        return contenido

    def obtener_texto_docx(self) -> str:
        '''Lee el contenido de un archivo pdf y lo devuelve como una cadena.'''
        doc = Document(self.ruta_archivo)
        contenido = "\n".join([para.text for para in doc.paragraphs])
        return contenido

    def obtener_texto_pdf(self) -> str:
        '''Lee el contenido de un archivo pdf y lo devuelve como una cadena.'''
        contenido = ""
        reader = PdfReader(self.ruta_archivo)
        for parrafo in reader.pages:
            contenido += parrafo.extract_text() + "\n"
        return contenido


    def obtener_texto_archivo(self):
        '''
        Lee el contenido de un archivo y lo devuelve como una cadena.

        El archivo debe ser .txt, .docx o .pdf. Si el archivo no es válido,
        se lanza una excepción ``ValueError``.

        Returns:
            str: El contenido del archivo le  do como una cadena.
        '''

        texto:str = ""

        if self.ruta_archivo.endswith('.txt'):
            texto = self.obtener_texto_txt()
        elif self.ruta_archivo.endswith('.docx'):
            texto = self.obtener_texto_docx()
        elif self.ruta_archivo.endswith('.pdf'):
            texto = self.obtener_texto_pdf()
        else:
            raise ValueError("El tipo de archivo ingresado no es válido")

        return texto

    def buscar_coincidencias(self):
        '''
        Busca todas las palabras de 4 sílabas en el archivo leído y las devuelve
        como una lista.

        Returns:
            Tuple[List[str], int]: Un tupla que contiene una lista con las palabras
            encontradas y el número total de coincidencias.
        '''
        # regex = r"\b[bcdfghjklmnñpqrstvwxyz|BCDFGHJKLMNÑPQRSTVWXYZ]*([aeiouáéíóúüAEIOUÁÉÍÓÚÜ]+[bcdfghjklmnñpqrstvwxyz|BCDFGHJKLMNÑPQRSTVWXYZ]*){4}\b"

        # regex = r'\b(?:[bcdfghjklmnñpqrstvwxyz]*[aeiouáéíóúü][bcdfghjklmnñpqrstvwxyz]*){4}\b'
        regex = r"\b(?:[bcdfghjklmnñpqrstvwxyz|BCDFGHJKLMNÑPQRSTVWXYZ]*[aeiouáéíóúüAEIOUÁÉÍÓÚÜ]+[bcdfghjklmnñpqrstvwxyz|BCDFGHJKLMNÑPQRSTVWXYZ]*){4}\b"
        texto = self.obtener_texto_archivo()
        coincidencias = re.findall(regex, texto)
        return coincidencias, len(coincidencias)

