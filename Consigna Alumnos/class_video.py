from datetime import datetime

class Video:
    def __init__(self, titulo: str, vistas: int, tiempo: int, url_youtube: str, fecha_lanzamiento: str):
        self.titulo = titulo
        self.vistas = vistas
        self.tiempo = tiempo
        self.url_youtube = url_youtube
        self.fecha_lanzamiento = fecha_lanzamiento
        self.sesion = None
        self.colaborador = None
        self.codigo_url = None
        
    def mostrar_tema(self):
        #Agregar los datos pertinentes para que a la hora de mostrar se vean los datos completos del video
        print(f"Titulo: {self.titulo}")
        print(f"Vistas: {self.vistas}")
        print(f"Duración: {self.tiempo} segundos")
        print(f"URL de YouTube: {self.url_youtube}")
        print(f"Fecha de Lanzamiento: {self.fecha_lanzamiento.strftime('%d-%m-%Y')}")
        print(f"Seción: {self.sesion}")
        print(f"Colaborador: {self.colaborador}")
        print(f"Código URL: {self.codigo_url}")
        print("*"*30)

    def dividir_titulo(self):
        #Debe setear el atributo sesion y colaborador con los datos obtenidos del 
        #titulo del video
        title_parts = (self.titulo).split("|")
        self.sesion = int(title_parts[1].split("#")[1].strip())
        self.colaborador = title_parts[0]
        pass
    
    def obtener_codigo_url(self):
        #Debe setear el atributo codigo_url con el codigo obtenido del atributo url_youtube
        #Por ej: si la url es https://www.youtube.com/watch?v=nicki13 
        #el codigo seria nicki13
        codigo = (self.url_youtube).split("=")

        self.codigo_url = codigo[1]
        pass
    
    def formatear_fecha(self):
        #Necesitamos que la fecha de lanzamiento sea un objeto de la clase datetime (investigar).
        #Para ello deberán dividir la fecha (en formato string) en dia, mes y año y a partir de 
        #esos datos, crear la nueva fecha.

        year_month_day_list = self.fecha_lanzamiento.split("-")

        self.fecha_lanzamiento = (datetime(int(year_month_day_list[0]),int(year_month_day_list[1]),int(year_month_day_list[2])))
        pass