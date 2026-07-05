# app_web.py
# Mantido para compatibilidade com a configuração de deploy do Render (ex: gunicorn app_web:app)
from src.controller.main import app

if __name__ == "__main__":
    app.run()
