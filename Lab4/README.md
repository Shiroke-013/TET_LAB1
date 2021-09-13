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


Despues de esto se debe de poner a correr el servidor con el comando que se muestra a continuación, teniendo en cuenta que el segundo argumento del comando debe de ser el puerto que escogió al configurar los SG:

```sh
$ python3 Chat_Server.py 0.0.0.0 "El_puerto_designado(1313)"
```

Despues de que el servidor este corriendo se puede poner a correr los diferentes clientes con el siguiente comando, teniendo en cuenta que el primer argumento debe de ser la IP pública del Servidor y el segundo argumento debe de ser el mismo puerto del comando anterior:
```sh
$ python3 Chat_Client.py "IP_publica del Servidor" "El_puerto_designado(1313)"
```

Despues de ejecutar el anterior comando se hará la conexión con el servidor (este imprimirá un mensaje de quién se conectó) y el usuario podrá elegir un ***Nickname*** por el cuál será identificado en el chat por los otros usuarios, después de esto el ***Nickname*** será registrado en el servidor para que ningún otro usuario que se quiera conectar puede utilizar este mismo, una vez hecho esto se podrán mensajear entre ellos.

Para cerrar la sesión de los clientes al igual que la del servidor se puede utilizar el comando Ctrl + C.


## Referencias
Para el desarrollo de este laboratorio se tomaron en consideración los siguientes enlaces:
* https://pika.readthedocs.io/en/stable/modules/channel.html
