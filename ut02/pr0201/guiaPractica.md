# GUIA PARA COMPLETAR LA PRACTICA

## Comandos para crear la estructura de carpetas que mapearán las distintas rutas de postgres y odoo (para producción y desarrollo)
### 1. Crear estructura de carpetas para entorno de producción

mkdir -p ./produccion/data  
mkdir -p ./desarrollo/addons               

### 2. Crear estructura de carpetas para entorno de desarrollo.
mkdir -p ./desarrollo/data
mkdir -p ./desarrollo/addons
mkdir -p ./desarrollo/filestore
mkdir -p ./desarrollo/sessions 


## Contenido fichero compose
```yml
version: '3'
services:
  produccion-postgres:
    image: postgres:14
    container_name: produccion-postgres
    environment:
      - POSTGRES_USER=odoo
      - POSTGRES_PASSWORD=odoo
      - POSTGRES_DB=postgres
    volumes:
      - ./produccion/data:/var/lib/postgresql/data

  produccion-odoo:
    image: odoo:16
    container_name: produccion-odoo
    depends_on:
      - produccion-postgres
    ports:
      - "8069:8069"
    volumes:
      - ./produccion/addons:/mnt/extra-addons
    environment:
      - HOST=produccion-postgres
      - USER=odoo
      - PASSWORD=odoo
    user: root
    command: --dev=all


  desarrollo-postgres:
    image: postgres:14
    container_name: desarrollo-postgres
    environment:
      - POSTGRES_USER=odoo
      - POSTGRES_PASSWORD=odoo
      - POSTGRES_DB=postgres
    volumes:
      - ./desarrollo/data:/var/lib/postgresql/data

  desarrollo-odoo:
    image: odoo:16
    container_name: desarrollo-odoo
    depends_on:
      - desarrollo-postgres
    ports:
      - "8070:8069"
    volumes:
      - ./desarrollo/addons:/mnt/extra-addons
      - ./desarrollo/filestore:/var/lib/odoo/filestore
      - ./desarrollo/sessions:/var/lib/odoo/sessions
    environment:
      - HOST=desarrollo-postgres
      - USER=odoo
      - PASSWORD=odoo
    user: root
    command: --dev=all
```

### Explicación de los parámetros
- version: nos permite definir la versión del archivo compose.

- services: es la sección donde definimos los distintos contenedores.

- image: nos permite especificar la imagen que usaremos para el contenedor.

- container_name: nos permite asignarle un nombre al contenedor.

- environment: nos permite definir las variables que tendrá nuestro contenedor.

- volumes: nos permite montar directorios de nuestra máquina física dentro del contenedor.

- depends_on: nos permite indiciar que un servicio va a depender de otro.

- port: nos permite especificar puertos del contenedor a nuestra máquina.

- user: nos permite ejecutar el contenedor con un usuario específico.

- command: nos ayuda con tareas de desarrollo.

### Levantamos el entorno
Orden --> docker-compose up -d


### FICHERO COMPOSE COMPLETO
[compose.yml](./compose.yml)
