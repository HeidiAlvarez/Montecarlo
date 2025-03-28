import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import gaussian_kde
import glob
import os

## Creamos los archivos .txt

archivo_salida_p  = 'estadisticas_paralaje.txt'
archivo_salida_rv = 'estadisticas_vRadial.txt'
archivo_salida_pm = 'estadisticas_pm.txt'
archivo_salida_dg = 'estadisticas_rGeo.txt'
archivo_salida_dp = 'estadisticas_rPhoto.txt'

if os.path.exists(archivo_salida_p):
    os.remove(archivo_salida_p)
    os.remove(archivo_salida_rv)
    os.remove(archivo_salida_pm)
    os.remove(archivo_salida_dg)
    os.remove(archivo_salida_dp)

## Definimos funciones para guardar los datos 
	
def guardar_resultados_p(fuente, media, desviacion, puntos):
    with open(archivo_salida_p, "a") as f:
        f.write(f"{fuente}\t{media}\t{desviacion}\t{puntos}\n")

def guardar_resultados_rv(fuente, media, desviacion, puntos):
    with open(archivo_salida_rv, "a") as f:
        f.write(f"{fuente}\t{media}\t{desviacion}\t{puntos}\n")

def guardar_resultados_pm(fuente, media, desviacion, puntos):
    with open(archivo_salida_pm, "a") as f:
        f.write(f"{fuente}\t{media}\t{desviacion}\t{puntos}\n")

def guardar_resultados_dg(fuente, media, desviacion, puntos):
    with open(archivo_salida_dg, "a") as f:
        f.write(f"{fuente}\t{media}\t{desviacion}\t{puntos}\n")

def guardar_resultados_dp(fuente, media, desviacion, puntos):
    with open(archivo_salida_dp, "a") as f:
        f.write(f"{fuente}\t{media}\t{desviacion}\t{puntos}\n")
        

## Agregamos los nombres de los campos en los archivos de texto

with open(archivo_salida_p, "w") as f:
    f.write("Fuente\tMedia\tDesviacion_Estandar\tPuntos\n")
    
with open(archivo_salida_rv, "w") as f:
    f.write("Fuente\tMedia\tDesviacion_Estandar\tPuntos\n")
    
with open(archivo_salida_pm, "w") as f:
    f.write("Fuente\tMedia\tDesviacion_Estandar\tPuntos\n")
    
with open(archivo_salida_dg, "w") as f:
    f.write("Fuente\tMedia\tDesviacion_Estandar\tPuntos\n")
    
with open(archivo_salida_dp, "w") as f:
    f.write("Fuente\tMedia\tDesviacion_Estandar\tPuntos\n")

## Cargamos la lista con todos los archivos en la base de datos de Gaia

archivos = glob.glob('/home/heidi/Documentos/Master/Datos/DR3/*.csv')

N = len(archivos)
n = int(N*0.1)

df_final_p  = pd.DataFrame()
df_final_rv = pd.DataFrame()
df_final_pm = pd.DataFrame()
df_final_dg = pd.DataFrame()
df_final_dp = pd.DataFrame()

print('Estamos entrando al for')

for i in range(n):
    	u = int(np.random.uniform() * N)
    
    	archivo = archivos[u]

    	df_p                  = pd.read_csv(archivo, usecols=['parallax'])
    	df_muestra_uniforme_p = df.sample(frac=0.1, random_state=42)  
	
	df_rv                  = pd.read_csv(archivo, usecols=['radial_velocity'])
    	df_muestra_uniforme_rv = df.sample(frac=0.1, random_state=42)
    
    	df_pm                  = pd.read_csv(archivo, usecols=['pm'])
    	df_muestra_uniforme_pm = df.sample(frac=0.1, random_state=42)
    	
    	df_dg                  = pd.read_csv(archivo, usecols=['r_med_geo'])
    	df_muestra_uniforme_dg = df.sample(frac=0.1, random_state=42)
    	
    	df_dp                  = pd.read_csv(archivo, usecols=['r_med_photo'])
    	df_muestra_uniforme_dp = df.sample(frac=0.1, random_state=42)
    

    print('Se obtiene el 0.1 de los datos del archivo ', archivo)

    df_final_p  = pd.concat([df_final_p, df_muestra_uniforme_p], ignore_index=True)
    df_final_rv = pd.concat([df_final_rv, df_muestra_uniforme_rv], ignore_index=True)
    df_final_pm = pd.concat([df_final_pm, df_muestra_uniforme_pm], ignore_index=True)
    df_final_dg = pd.concat([df_final_dg, df_muestra_uniforme_dg], ignore_index=True)
    df_final_dp = pd.concat([df_final_dp, df_muestra_uniforme_dp], ignore_index=True)

    print('Se concatena al dataframe final')

paralaje   = df_final_p['parallax']
r_velocity = df_final_rv['radial_velocity']
mto_propio = df_final_pm['pm']
d_geo      = df_final_dg['r_med_geo']
d_photo    = df_final_dp['r_med_photogeo']

## Sacamos las estadísticas de los datos globales

media_global_p      = paralaje.mean()
desviacion_global_p = paralaje.std()

media_global_rv      = r_velocity.mean()
desviacion_global_rv = r_velocity.std()

media_global_pm      = mto_propio.mean()
desviacion_global_pm = mto_propio.std()

media_global_dg      = d_geo.mean()
desviacion_global_dg = d_geo.std()

media_global_dp      = d_photo.mean()
desviacion_global_dp = d_photo.std()

## Guardamos los datos

guardar_resultados_p("Global", media_global_p, desviacion_global_p, len(paralaje))
guardar_resultados_rv("Global", media_global_rv, desviacion_global_rv, len(r_velocity))
guardar_resultados_pm("Global", media_global_pm, desviacion_global_pm, len(mto_propio))
guardar_resultados_dg("Global", media_global_dg, desviacion_global_dg, len(d_geo))
guardar_resultados_dp("Global", media_global_dp, desviacion_global_dp, len(d_photo))

## Creamos la KDE para cada uno de los campos

kde_p = gaussian_kde(paralaje, bw_method='silverman')
x_p   = np.linspace(min(paralaje), max(paralaje), 1000)
y_p   = kde(x_p)

kde_rv = gaussian_kde(r_velocity, bw_method='silverman')
x_rv   = np.linspace(min(r_velocity), max(r_velocity), 1000)
y_rv   = kde(x_rv)

kde_pm = gaussian_kde(mto_propio, bw_method='silverman')
x_pm   = np.linspace(min(mto_propio), max(mto_propio), 1000)
y_pm   = kde(x_pm)

kde_dg = gaussian_kde(d_geo, bw_method='silverman')
x_dg   = np.linspace(min(d_geo), max(d_geo), 1000)
y_dg   = kde(x_dg)

kde_dp = gaussian_kde(d_photo, bw_method='silverman')
x_dp   = np.linspace(min(d_photo), max(d_photo), 1000)
y_dp   = kde(x_dp)


n_puntos = [1000, 10000, 100000]

## Ploteamos el paralaje

plt.plot(x_p, y_p, label="KDE", alpha=1, color='black')
for j in n_puntos:
	for i in range(N):
          print('Realizacion de Montecarlo ', i)
          muestras = kde_p.resample(size=j).flatten()
		
          media_muestra      = muestras.mean()
          desviacion_muestra = muestras.std()

          guardar_resultados_p("Montecarlo", media_muestra, desviacion_muestra, j)
          if i < 10:
              plt.hist(muestras, bins=50, density=True, alpha=0.5)

plt.title('Muestreo de Montecarlo Paralaje')
plt.ylabel('Densidad')
plt.xlabel('Paralaje $[mas]$')
plt.legend()
plt.savefig("KDE_Montecarlo_paralaje.png", dpi=300, bbox_inches="tight")
plt.show()

## Ploteamos la velocidad radial

plt.plot(x_rv, y_rv, label="KDE", alpha=1, color='black')
for j in n_puntos:
	for i in range(N):
          print('Realizacion de Montecarlo ', i)
          muestras = kde_rv.resample(size=j).flatten()
		
          media_muestra      = muestras.mean()
          desviacion_muestra = muestras.std()

          guardar_resultados_rv("Montecarlo", media_muestra, desviacion_muestra, j)
          if i < 10:
              plt.hist(muestras, bins=50, density=True, alpha=0.5)

plt.title('Muestreo de Montecarlo Velocidad Radial')
plt.ylabel('Densidad')
plt.xlabel('Velocidad Radial $[kms^{-1}]$')
plt.legend()
plt.savefig("KDE_Montecarlo_vRadial.png", dpi=300, bbox_inches="tight")
plt.show()

## Ploteamos el movimiento propio

plt.plot(x_pm, y_pm, label="KDE", alpha=1, color='black')
for j in n_puntos:
	for i in range(N):
          print('Realizacion de Montecarlo ', i)
          muestras = kde_pm.resample(size=j).flatten()
		
          media_muestra      = muestras.mean()
          desviacion_muestra = muestras.std()

          guardar_resultados_p("Montecarlo", media_muestra, desviacion_muestra, j)
          if i < 10:
              plt.hist(muestras, bins=50, density=True, alpha=0.5)

plt.title('Muestreo de Montecarlo Movimiento Propio')
plt.ylabel('Densidad')
plt.xlabel('Movimiento Propio $[mas yr^{-1}]$')
plt.legend()
plt.savefig("KDE_Montecarlo_pm.png", dpi=300, bbox_inches="tight")
plt.show()

## Ploteamos la distancia geometrica

plt.plot(x_dg, y_dg, label="KDE", alpha=1, color='black')
for j in n_puntos:
	for i in range(N):
          print('Realizacion de Montecarlo ', i)
          muestras = kde_dg.resample(size=j).flatten()
		
          media_muestra      = muestras.mean()
          desviacion_muestra = muestras.std()

          guardar_resultados_p("Montecarlo", media_muestra, desviacion_muestra, j)
          if i < 10:
              plt.hist(muestras, bins=50, density=True, alpha=0.5)

plt.title('Muestreo de Montecarlo Distancia Geometrica')
plt.ylabel('Densidad')
plt.xlabel('Distancia Geometrica $[pc]$')
plt.legend()
plt.savefig("KDE_Montecarlo_rGeo.png", dpi=300, bbox_inches="tight")
plt.show()

## Ploteamos el paralaje

plt.plot(x_dp, y_dp, label="KDE", alpha=1, color='black')
for j in n_puntos:
	for i in range(N):
          print('Realizacion de Montecarlo ', i)
          muestras = kde_dp.resample(size=j).flatten()
		
          media_muestra      = muestras.mean()
          desviacion_muestra = muestras.std()

          guardar_resultados_p("Montecarlo", media_muestra, desviacion_muestra, j)
          if i < 10:
              plt.hist(muestras, bins=50, density=True, alpha=0.5)

plt.title('Muestreo de Montecarlo Distancia Fotogeometrica')
plt.ylabel('Densidad')
plt.xlabel('Distancia Fotogeometrica $[pc]$')
plt.legend()
plt.savefig("KDE_Montecarlo_rPhoto.png", dpi=300, bbox_inches="tight")
plt.show()

