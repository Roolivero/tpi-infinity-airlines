# tpi-infinity-airlines

## Git clone guide

## Recomendación (opcional)

- Es recomendable tener las dependencias del proyecto en un entorno virtual:

    ```bash
    pip3 install virtualenv #instala el paquete de entorno virtual de python
    virtualenv venv # crea la carpeta venv (si pones un nombre distinto agregarlo al .gitignore)
    ```

## Paso 1 instalar dependencias

- El archivo requirements.dev.txt posee todas las dependencias del proyecto
    ```bash
    pip install -r requirements.dev.txt #instala dependencias del proyecto

- requirements.txt es necesario unicamente para el Dockerfile


## Paso 2 configurar variables de entorno 

- copiar '.env.sample' y renombrarlo a '.env' (no tocar .env.sample) 


## Paso 3 levantar contenedor 🐋

- Te paras en el directorio donde se encuentra docker-compose.yml
    ```bash
    docker compose up -d # -d para ejecutar en segundo plano
    ```

## Desarrollo
- La pagina va a a ejecutarse en localhost:{DJANGO_PORT}
- Para hacer las migraciones sin tener que entrar al contenedor hay que ejecutar los siguientes comandos 

    ```bash
    sh ./scripts/make_migrations.sh
    sh ./scripts/migrate.sh
    ```


## Convenciones a seguir

- clases en PascalCase
- metodos en camelCase (con snake_case es tolerable ya que asi le gusta a python)
- variables en snake_case
- directorios con guion-medio 

***obs***:  si es una aplicacion de django el directorio va a tener que ser con guion_bajo 


## Creacion de aplicaciones


- Una vez parado en el directorio apps/

     ```bash
    python ../manage.py startapp nombre_aplicacion
    ```
***obs***: No es necesario crear la carpeta con el nombre de la aplicacion

## Agregar nuevas dependencias 

- Si queres agregar nuevas dependencias de python al proyecto tenes que agregarlas a ambos archivos de requirements

    ```bash
    pip freeze > requirements.txt
    pip freeze > requirements.dev.txt
    ```
- Para instalar la dependencia dentro del contenedor ejecute el siguiente script
    ```bash
    sh ./scripts/pip_install.sh {nombre_dependencia}
    ```
- Si hay nuevas nuevas dependencias para instalarlas en el contenedor hay que usar el siguiente comando
    ```bash
    docker compose down # si esta abierto
    docker compose up --build -d 
    ```
