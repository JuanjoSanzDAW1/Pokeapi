# Usa una imagen base oficial de Python
FROM python:3.10-slim

# Establece un directorio de trabajo dentro del contenedor
WORKDIR /app

# Copia los archivos del proyecto al contenedor
COPY . /app

# Instala las herramientas necesarias para construir dependencias
RUN apt-get update && apt-get install -y \
    build-essential \
    && rm -rf /var/lib/apt/lists/*

# Instala las dependencias del proyecto
RUN pip install --upgrade pip && pip install -r requirements.txt

# Expone el puerto donde correrá la aplicación
EXPOSE 8000

# Comando por defecto para ejecutar la aplicación
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]
