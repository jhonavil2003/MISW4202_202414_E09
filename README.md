Realización del experimento

INSTALACIÓN DE REDIS

El experimento se llevo a cabo en una máquina local con sistema operativo Windows.

Para esto se realizaron los siguientes pasos:

En la tienda de microsoft se obtiene una aplicación de ubuntu.

![image](https://github.com/user-attachments/assets/16337226-7dd3-45b5-8e02-ad1629f55973)

Esta SO nos servirá para desplegar una instancia de Redis con la cual trabajaremos las colas y el broker.

1. Al abrir el SO se deben ejecutar los siguientes comandos:

curl -fsSL https://packages.redis.io/gpg | sudo gpg --dearmor -o /usr/share/keyrings/redis-archive-keyring.gpg

sudo apt-get update

sudo dpkg --configure -a

sudo apt-get install redis

2. Conectarse a redis, correr el sig  comando en wsl:

sudo service redis-server start

Verificar que la instancia de redis esté corriendo

redis-cli

Ejecutar PING

DESCARGA DEL CODIGO, DESPLIEGUE BROKER Y MICROSERVICIOS

Luego de que tengamos el código en nuestra máquina local debemos realizar los siguientes pasos:

Versión python: 3.12.5

1. Dentro del repositorio se encuentra un venv para el proyecto, por lo tanto ejectutar el script activate.

  .\venv\Scripts\activate   

  1.1. En caso de que presente problemas, se debe crear un nuevo venv.
  Ejecutar 
  
  python -m venv venv
  
  .\venv\Scripts\activate   

2. Dentro de la carpeta raiz del proyecto na vez activemos el ambiente:
Ejecutamos:
 
  pip install -r microservicio_ingreso_solicitud/requirements.txt

Instalamos Celery y flower con el siguiente comando: 
 
  pip install celery 
  
  pip install flower

3. Una vez hallamos instalado las dependencias requerimos ejecutar en terminales diferentes el worker y para la instancia de flower para la visualización del broker  

  celery -A microservicio_ingreso_solicitud.core.task worker --pool=solo -l info

  En otra terminal: 
  
  celery -A microservicio_ingreso_solicitud.celery_config.celery flower

  La interfaz se puede observar en la url 

  http://127.0.0.1:5555

4. Procedemos a desplegar el microservicio de proceso de solicitud en el puerto 5001

   cd microservicio_proceso_solicitud

   flask run -p 5001

6. Procedemos a desplegar el microservicio de ingreso de solicitud  en el puerto 5000

  cd microservicio_ingreso_solicitud
  
  flask run

LLAMADO A MICROSERVICIOS 

En el siguiente link se encontrará una collection de postman con configuraciones para el llamado de los microservicios.

[Pruebas de regresión - arquitectura hexagonal - microservicios para actualización de portfolio](https://uniandes-my.sharepoint.com/personal/j_castanor_uniandes_edu_co/_layouts/15/download.aspx?UniqueId=4a2fb2a656904fa49b458c84b2580b37&e=nVSoRB)

Para el llamado al microservicio de Proceso solicitud se debe hacer una petición a:

http://127.0.0.1:5001/integraciones/solicitudes
