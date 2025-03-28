USO DE MÉTODO DE MONTECARLO PARA SELECCIÓN DE DATOS DR3 DE GAIA Y SIMULACIÓN DE DISCO EXPONENCIAL CON ALGORITMO DE METRÓPOLIS

Descripción:

Este proyecto tiene dos propósitos: 
	1)	Verificar si es posible seleccionar aleatoriamente un subconjunto de los datos de la base conjunta entre DR3 de Gaia y la base de 			datos de distancias del instituto Max Plank. 
	2)	Simular un disco exponencial empleando el algoritmo de Metrópolis.


Requisitos:

Lenguaje: Python 3.10.12
Dependencias: Se encuentran en el archivo requirements.txt. Instalar con: pip install -r requirements.txt


Estructura del proyecto:

Carpetas y archivos principales:
	histogramas/ : Contiene gráficas de los histogramas para el total de los datos de la base de datos de los siguientes parámetros:
		- Paralaje
		- Movimiento Propio
		- Velocidad Radial
		- Distancia Geométrica
		- Distancia Fotogeométrica

	KDE/ : Contiene las gráficas de las KDEs calcualdas para los mismos parámetros, generadas con el 1% de los datos. También incluye:
		-Gráficas de 40 realizaciones de Montecarlo con diferentes porcentajes de datos:
			* 10 realizaciones para el 10% de la muestra.
			* 10 realizaciones para el 1% de la muestra.
			* 10 realizaciones para el 0.1% de la muestra.
			* 10 realizaciones para el 0.01% de la muestra.
			* Archivos .txt con las medias y las desvaciones estándar de cada subconjunto.
			
	RealizacionesMontecarlo.ipynb : Es un notebook con los resultados de la simulación del disco exponencial. 
	

Desarrollado por: Heidi Álvarez.
