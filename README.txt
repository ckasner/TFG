TFG

Para hacer funcionar el proyecto hay que seguir los siguientes pasos:

1- Conectar el ordenador al router (Via Wifi o por ethernet)
2- Conectar la Raspberry al router. En principio esto lo hace automáticamente pero si cambiamos el nombre de la red o algo tendremos que:
	- Conectar el ordenador al router via Wifi
	- Conectar la Raspberry al router via ethernet.
	- acceder a la dirección 192.168.1.1 desde el navegador para ver los dispositivos conectados al router
	- Ver la dirección IP asignada a la Raspberry Pi
	- Acceder a la Raspberry desde el ordenador por ssh ( ssh pi@direccion.IP )
	- Cambiar el fichero de configuración /etc/wpa_supplicant/wpa_supplicant.conf añadiendo al final:
		network={
			ssid="Nombre de red"
			key_mgmt="paas de red" o NONE si no hay contraseña
		}
	-Reiniciar la Raspberry
3- Acceder a las Raspberry desde el ordenador por ssh
4- Ejecutar el mjpeg-streamer con el siguiente comando (dentro de la carpeta experimental) -  ./mjpg_streamer -i ./input_uvc.so -d /dev/video0" -o ./output_http.so -w ./www"
5- Abrir VLC, reprodudir mediante ubicación de red, pegar la url que aparece en : direccion.IP.raspi:/8080
6- Configurar VLC para que te ponga dos pantallas iguales SBS
7- Abrir Virtual Desktop y darle la opción de juntar imágenes en el casco (Virtual desktop necesita el SDK 0.8 de Oculus)
8- Ejecutar el programa del ordenador que abre los sockets (PythonApplication)
9- Ejecutar en la Raspi socketH.py y socketClient.py (python socketH.py)


Cambios a realizar 
	- ponerle una batería como la de los coches del CRM con un adaptador 
	- camara 360
	- ralentizar los servos
	- problemas con la conexión Wifi del ordenador al router