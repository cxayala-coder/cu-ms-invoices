# IMAGEN BASE
FROM cxayala/super-imagen-base:1

# INSTRUCCIONES
WORKDIR /app

# No necesita instalaciones adicionales (solo la stdlib de Python)
 
# Copiar el archivo de la aplicación
COPY app.py .

# Exponer el puerto 3000
EXPOSE 3001
 
# ENTRYPOINT
CMD ["python", "app.py"]

