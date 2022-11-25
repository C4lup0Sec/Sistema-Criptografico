# SISTEMA CRIPTOGRÁFICO
Este programa permite guardar información firmada y encriptada, tambien se puede identificar al usuario que la
almaceno por medio de los certificados digitales que se generan.

## INSTALACIÓN
Se deben instalar las librerias que estan en el archivo con nombre requirements.txt

Desde la carpte src que esta en repositorio.
```	
> virtualenv env
> cd .\env\Scripts\activate
> cd ..\..
> python -m pip install -r requirements.txt
```
## Ejecución
Ejecutar el script que se encuentra en la carpeta src del repositorio.

```	
> python main.py
```


## INICIO
Al ejecutar el programa mostrara el menú principal con las diferentes opciones:
[1] Login
[2] Registro
[3] Limpiar
[4] Salir
[*] Selecciona una opción

En el Login podemos iniciar sesión después de haber creado un certificado.
En el Registro podremos crear el certificado necesario para usar el programa.

## Registro
Primero, hay que crear un certificado, seleccionamos la opción 2 del menú.
```
[*] Selecciona una opción > 2
Ingresa el nombre del usuario > Andres
Ingresa la contraseña > 0123456789
Se registro el usuario Andres al sistema criptografico
Se genero el certificado y la llave privada
```
## Login
Después de crear un certificado, podemos iniciar sesión al seleccionar la opción 1 del menú.
```
[*] Selecciona una opción > 1
Certificado (.cer) > Andres.cer
Clave privada (.key) > Andres.key
Contraseña de la clave privada > 0123456789
Bienvenido al sistema de mensajería!
```



## VENTANA DE MENSAJERÍA
Despues de iniciar sesión de manera correcta te enviara al menú de mensajeria, aqui estan las opciones:
[1] Cifrar mensaje
[2] Descifrar mensaje
[3] Cerrar sesión
[*] Selecciona una opción

Si seleccionamos Cifrar mensaje nos arrojara una pantalla donde nos dira que el mensaje se cifrara con
cifrado cesar, luego nos dejara escribir el mensaje, después de eso nos dara el mensaje cifrado y nos dira
que deberemos apuntarlo.
Si seleccionamos Descifrar mensaje nos arrojara una pantalla donde nos dira que debemos pegar el mensaje
encriptado con anterioridad y al aceptar nos dara el mensaje desencriptado.
Si seleccionamos la opción 3 nos enviara al menú principal.

## LIMPIAR TERMINAL
Si queremos limpiar la terminal deberemos elegir la opción 3 en el menú principal.

Para salir del programa deberemos seleccionar la opción 4 en el menú principal.