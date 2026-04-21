import smtplib # importo libreria de python para enviar emails
from email.mime.text import MIMEText #libreria para el formato de email que entienden los correos electronicos
from dotenv import load_dotenv #para leer archivos .env
import os #para acceder a variables de entorno

load_dotenv() #lee el archivo .env y lo carga

EMAIL = os.getenv("EMAIL") #obtiene el valor de variable email
EMAIL_PASSWORD = os.getenv("EMAIL_PASSWORD") #obtiene valor de variable email_password

def send_reset_email(email, token):
    enlace = f"http://127.0.0.1:5500/frontend/reset-password.html?token={token}" #crea el enlace con el token para restablecer contraseña
    mensaje = MIMEText(f"""
Hola, has solicitado restablecer tu contraseña.

Enlace: {enlace}

Expira en 30 minutos.
""")
    mensaje["Subject"] = "Restablecer contraseña" #cabecera del email
    mensaje["From"] = EMAIL
    mensaje["To"] = email

    try: 
        with smtplib.SMTP("smtp.gmail.com", 587) as server: #conecta con el servidor SMTP de gmail en el puerto 587
            server.starttls()                    # activa el cifrado
            server.login(EMAIL, EMAIL_PASSWORD)  # te identificas
            server.sendmail(EMAIL, email, mensaje.as_string())  # envías
        return True
    except Exception as e:
        print(f"Error al enviar email: {e}")
        return False