# Topicos Especiales en Telemática Laboratorio 4

## Autor: Andrés Darío Chaves Pérez 

## Descripción


## Instalación


Para un funcionamiento correcto las instancias deben de contar con git, python3, la biblioteca pika y un editor de texto de preferencia, por defecto la mayoría de máquinas traen VIM.

***¡Tener en cuenta que para poder ejecutar los comandos a continuación se debe de acceder a las diferentes instancias via SSH!, en la parte de ejecución hay un ejemplo del comando para realizar esta conexión.***

Se puede usar los siguientes comandos:

#### Instalar Git
```sh
$ sudo yum install git
```

#### Instalar Python3
```sh
$ sudo yum install python3
```

#### Instalar Emacs
```sh
$ sudo yum install emacs
```

#### Instalar Emacs
```sh
$ pip3 install pika
```


## Ejecución
Para la ejecución de la aplicación se debe de acceder a las diferentes instacias via SSH y clonar el repositorio:

```sh
$ ssh -i "Par de claves utilizado para crear las instancias(*.pem)" ec2-user@"DNS de IPv4 pública de la instancia"
$ git clone https://github.com/Shiroke-013/TET_LABS.git
```


Despues de esto se debe de ingresar hasta la carpeta de: Lab4 y ejecutar el "Producer", teniendo en cuenta que el orden de los argumentos para ejecutar el script son:

```sh
$ python3 appProducer.py "IP_publica del Servidor" "El_puerto_designado(1313)" "Usuario de RabbitMQ" "Contraseña de RabbitMQ"
```

Despues de esto se debe ejecutar el "Consumer" en minimo 2 instancias de AWS para ver su funcionamiento, teniendo en cuenta que el orden de los argumentos para ejecutar el script son:
```sh
$ python3 appConsumer.py "IP_publica del Servidor" "El_puerto_designado(1313)" "Usuario de RabbitMQ" "Contraseña de RabbitMQ"
```


## Referencias
Para el desarrollo de este laboratorio se tomaron en consideración los siguientes enlaces:
* https://pika.readthedocs.io/en/stable/modules/channel.html
