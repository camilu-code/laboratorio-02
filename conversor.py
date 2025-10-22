import json
from datetime import datetime

def cargar_tasas(ruta):
 """"lee un archivo json y retorna un objeto"""
 with open(ruta, "r") as archivo:
  return json.load(archivo)

def convertir(precio_usd, moneda_destino, tasas):
 """""Convierte el valor a otra moneda """
 # obtine a tasa de cambio de USD a la moneda destino 
 tasa = tasas["USD"].get(moneda_destino)
 #Si la moneda de destino no existe, lanza una excepcion
 if not tasa:
  raise ValueError("Moneda no soportada")
 return precio_usd * tasa

def registrar_transaccion(producto, precio_convertido, moneda, ruta_log):
 """""Escribe una nueva linea en el archivo de registro"""
 with open(ruta_log, "a") as archivo:
  #Obtener la fecha actual con formato año-mes-dia hora-minuto-segundo
  fecha = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
  #Escribir una linea nueva en el archivo de registropp
  archivo.write(f"{fecha} | {producto}: {precio_convertido:.2f} {moneda}\n")

# Ejemplo de uso
if __name__ == "__main__":
 tasas = cargar_tasas("data/tasas.json")
 precio_usd = 100.00
 precio_eur = convertir(precio_usd, "EUR", tasas)
registrar_transaccion("Laptop", precio_eur, "EUR", "logs/historial.txt")
