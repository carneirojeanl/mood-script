# Dockerfile
FROM python:3.12-slim

# 1) Define o diretório de trabalho dentro do container
WORKDIR /app

# 2) Variáveis de ambiente úteis para Python dentro do container
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

# 3) Copia somente requirements primeiro (isso otimiza cache das camadas)
COPY requirements.txt .

# 4) Instala dependências Python
RUN pip install --no-cache-dir -r requirements.txt

# 5) Copia todo o código da sua aplicação
COPY . .

# 6) Porta padrão do Streamlit (documentativo, mas útil)
EXPOSE 8501

# 7) Comando para rodar sua app (assumindo que o entrypoint é main.py e usa streamlit)
CMD ["streamlit", "run", "main.py", "--server.port=8501", "--server.address=0.0.0.0"]
