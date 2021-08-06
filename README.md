# Topicos Especiales en Telemática Laboratorio 1

## Autor: Andrés Darío Chaves Pérez 

## Descripción
En el primer laboratorio de la materia se podrá evidenciar el uso de sockets de tipo TCP y con ***family addresses*** de tipo IPv4, con el objetivo de crear una aplicación de chat grupal, siendo la arquitectura de este Cliente/Servidor, haciendo posible que dos o más clientes se puedan comunicar entre ellos por medio del chat, con la condición de que el servidor este corriendo. Para hacer esto posible se usarán instancias EC2 de AWS, siendo una la que actue como servidor y el resto como clientes.

## Instalación
Para ver la aplicación en funcionamiento se deben de instanciar como minimo 3 instancias EC2 en AWS, siendo una de estas la que actuará como servidor, que además se le debe de asociar una IP elástica, y las otras como clientes que enviaran mensajes en el chat.Se usarán dos grupos de seguridad (SG), uno para el servidor y otro para los clientes, el SG del servidor debe tener una regla de entrada con el tipo en ***Custom TCP***, para este caso se seleccionó el puerto 1313, abierto para cualquier IP, pero se puede escoger uno diferente siendo mayor al puerto 1100. Asimismo el SG de los clientes es casi igual al del servidor con la diferencia de que no debe estar abierto para cualquier IP, unicamente debe estar abierto para la IP pública del Servidor.

Para un funcionamiento correcto las instancias deben de contar con git, python3 y un editor de texto de preferencia, por defecto la mayoría de máquinas traen VIM.

***!Tener en cuenta que para poder ejecutar los comandos a continuación se debe de acceder a las diferentes instancias via SSH¡, en la parte de ejecución hay un ejemplo del comando para realizar esta conexión.***

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

## Ejecución
Para la ejecución de la aplicación (chat) se debe de acceder a las diferentes instacias via SSH y clonar el repositorio:

```sh
$ ssh -i "Par de claves utilizado para crear las instancias(*.pem)" ec2-user@"DNS de IPv4 pública de la instancia"
$ git clone https://github.com/Shiroke-013/TET_LAB1.git
```


Despues de esto se debe de poner a correr el servidor con el comando que se muestra a continuación, teniendo en cuenta que el segundo argumento del comando debe de ser el puerto que escogió al configurar los SG:

```sh
$ python3 c_server.py 0.0.0.0 "El_puerto_designado(1313)"
```

Despues de que el servidor este corriendo se puede poner a correr los diferentes clientes con el siguiente comando, teniendo en cuenta que el primer argumento debe de ser la IP pública del Servidor y el segundo argumento debe de ser el mismo puerto del comando anterior:
```sh
$ python3 c_client.py "IP_publica del Servidor" "El_puerto_designado(1313)"
```

Despues de que los clientes estén conectados (el servidor te lo hará saber con un mensaje), se podrán mensajear entre ellos.
