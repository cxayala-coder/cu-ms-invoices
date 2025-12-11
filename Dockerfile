# IMAGEN BASE
FROM cxayala/super-imagen-base:1

# INSTRUCCIONES
WORKDIR /app

# Instalar Flask y psycopg2
RUN pip install flask psycopg2-binary
 
# Copiar el archivo de la aplicación
COPY app.py .

# Exponer el puerto 3000
EXPOSE 3000
 
# ENTRYPOINT
CMD ["python", "app.py"]

