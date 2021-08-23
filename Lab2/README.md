# Topicos Especiales en Telemática Laboratorio 2

## Autor: Andrés Darío Chaves Pérez 

## Descripción
El segundo laboratorio de la materia tiene como objetivo el uso del protocolo HTTP en la apliación anteriormente creada en el laboratorio 1 (Chat Grupal), siendo la arquitectura de esta Cliente/Servidor y con la funcionalidad de que varios clientes se puedan comunicar entre ellos por medio del chat, siempre y cuando el servidor este corriendo. Igualmente para poder ejecutar este laboratorio se utilizarán instancias EC2 de AWS, siendo una la que actue como servidor y el resto como clientes.

El protocolo HTTP tiene métodos como lo son: GET(utilizado para obtener información de servidor), POST(para enviar/subir información al servidor), PUT(actualizar la información del servidor) y DELETE(eliminar información del servidor), adicionalmente el servidor al recibir alguna de estas peticiones siempre enviará una respuesta (más conocidas como ***Status Codes***) al cliente dependiendo del resultado que se obtuvo:

***Respuestas Informativas:*** siendo el formato de estas: ***1XX***. Solo son una respuesta provisional, un Servidor ***No*** debería enviar esta respuesta a un cliente a menos de que sea en condiciones experimentales.

***Peticiones Correctas:***  siendo el formato de estas: ***2XX***. Indican que la solicitud del cliente fue recibida exitosamente, entendida y aceptada.

***Redirecciones:*** siendo el formato de estas: ***3XX***. Significan que el cliente debe de hacer una acción adicional para completar la solicitud.

***Errores del Cliente:*** siendo el formato de estas: ***4XX***. Son utilizados en casos en los que parece que el cliente se ha equivocado.

***Errores del Servidor*** siendo el formato de estas: ***5XX***. Indican casos en los que el servidor se da cuenta de que ha cometido un error o es incapaz de realizar la solicitud.

## Instalación
Para ver la aplicación en funcionamiento se deben de instanciar como minimo 3 instancias EC2 en AWS, siendo una de estas la que actuará como servidor, que además se le debe de asociar una IP elástica, y las otras como clientes que enviaran mensajes en el chat. Se usarán dos grupos de seguridad (SG), uno para el servidor y otro para los clientes, el SG del servidor debe tener una regla de entrada con el tipo en ***Custom TCP***, para este caso se seleccionó el puerto 1313, abierto para cualquier IP, pero se puede escoger uno diferente siendo mayor al puerto 1100. Asimismo el SG de los clientes es casi igual al del servidor con la diferencia de que no debe estar abierto para cualquier IP, unicamente debe estar abierto para la IP pública del Servidor.

Para un funcionamiento correcto las instancias deben de contar con git, python3 y un editor de texto de preferencia, por defecto la mayoría de máquinas traen VIM.

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

## Ejecución
Para la ejecución de la aplicación (chat) se debe de acceder a las diferentes instacias via SSH y clonar el repositorio:

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
* https://en.wikipedia.org/wiki/Hypertext_Transfer_Protocol#Technical_overview
* https://docs.python.org/3/library/http.server.html#module-http.server
* https://docs.python.org/3/library/http.client.html#module-http.client
* https://www.geeksforgeeks.org/http-request-methods-python-requests/
* https://gist.github.com/junian/99e402db918cbe150002dc8c6736feb6
* https://www.restapitutorial.com/httpstatuscodes.html
* https://realpython.com/intro-to-python-threading/#what-is-a-thread
