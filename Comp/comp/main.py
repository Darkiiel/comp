import flet as ft
import pygame # type: ignore
import requests
import tempfile 
import os 

#=============================================================
#    PALETA INSTITUCIONAL CETIS (basada en tu captura) # type: ignore
#=============================================================
COLOR_GUINDA = "#7A1C1C"
COLOR_BLANCO = "#FFFFFF"
COLOR_FONDO = "#F9F9F9"
COLOR_TEXTO = "#2C2C2C"
COLOR_SUBTEXTO = "#555555"
COLOR_TARJETA = "#EDEDED"

# =============================================================
#  Inicializar pygame mixer para reproducir audios
# =============================================================
pygame.mixer.init()

def reproducir_audio(url):
    """Descarga temporalmente y reproduce el audio"""
    detener_audio() # type: ignore
    try:
        response = requests.get(url)
        response.raise_for_status()
        with tempfile.NamedTemporaryFile(delete=False, suffix=".mp3") as temp_audio:
            temp_audio.write(response.content)
            temp_path = temp_audio.name
        pygame,mixer.music.load(temp_path)
        pygame.mixer.music.play()
    except Exception as e:
        print(f"Error reproduciendo: {e}")
        
def detener_audio():
    """Detiene cualquier audio en curso"""
    try:
        if pygame.mixer.music.get_busy():
            pygame.mixer.music.stop()
    except:
        pass
    
#=========================================================
# DATOS DE LOS MEDIOS (imagenes/audios del proyecto)
#=========================================================
TIMELINE_DATA = [
    {
        "id": "A", "nombre": "Tarjeta perforada", "decada": "1950s",
        "capacidad": "80 bytes", "capacidad_bytes": 80,
        "curiosidad": "Una de las primeras formas de almacenamiento. Se usaban para guardar programas y datos.",
        "imagen": "https://raw.githubusercontent.com/Prof-Luis1986/Proyctos_3roB/refs/heads/main/Tarjeta_perforada.jpg",
        "sonido": "https://raw.githubusercontent.com/Prof-Luis1986/Proyctos_3roB/refs/heads/main/Tarjeta_perforada.mp3"
    },
    {
        "id": "S", "nombre": "Disquete (Floppy)", "decada": "1980",
        "capacidad": "1.44 MB", "capacidad_bytes": 1_440_000,
        "curiosidad": "El famoso icono de 'Guardar' viene de este dispositivo.",
        "imagen": "https://raw.githubusercontent.com/Prof-Luis1986/Proyctos_3roB/refs/heads/main/floppy.jpg",
        "sonido": "https://raw.githubusercontent.com/Prof-Luis1986/Proyctos_3roB/refs/heads/main/floppy.mp3"
    },
    {
        "id": "D", "nombre:" "USB",
        