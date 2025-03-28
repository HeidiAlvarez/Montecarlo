import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.axes_grid1.inset_locator import inset_axes, zoomed_inset_axes, mark_inset
from scipy.stats import gaussian_kde
import glob
from scipy.optimize import curve_fit

## Cargamos la lista con todos los archivos en la base de datos de Gaia

archivos = glob.glob('/gaiadb/Gaia/gdr3_complete_data/*.csv')

hist_counts = 	None 	
bin_edges = 	None 	

for archivo in archivos:
	print('Procesando el archivo ', archivo)
	
	## Cargamos la información archivo por archivo	
		
	for chunk_nan in pd.read_csv(archivo, usecols=["parallax", "radial_velocity", "pm", "r_med_geo", "r_med_photogeo"], chunksize=100000):  
		chunk_p  = chunk_nan.dropna(subset=["parallax"])
		chunk_rv = chunk_nan.dropna(subset=["radial_velocity"])
		chunk_pm = chunk_nan.dropna(subset=["pm"])
		chunk_dg = chunk_nan.dropna(subset=["r_med_geo"])
		chunk_dp = chunk_nan.dropna(subset=["r_med_photogeo"])
		
		hist_chunk_p, bin_edges_chunk_p   = np.histogram(chunk_p["parallax"], bins=50)  
		hist_chunk_rv, bin_edges_chunk_rv = np.histogram(chunk_rv["radial_velocity"], bins=50)  
		hist_chunk_pm, bin_edges_chunk_pm = np.histogram(chunk_pm["pm"], bins=50)  
		hist_chunk_dg, bin_edges_chunk_dg = np.histogram(chunk_rv["r_med_geo"], bins=50)  
		hist_chunk_dp, bin_edges_chunk_dp = np.histogram(chunk_rv["r_med_photogeo"], bins=50)  

		if hist_counts is None:
			hist_counts_p  = hist_chunk_p
            		hist_counts_rv = hist_chunk_rv
            		hist_counts_pm = hist_chunk_pm
            		hist_counts_dg = hist_chunk_dg
            		hist_counts_dp = hist_chunk_dp
            		
            		bin_edges_p  = bin_edges_chunk_p
            		bin_edges_rv = bin_edges_chunk_rv
            		bin_edges_pm = bin_edges_chunk_pm
            		bin_edges_dg = bin_edges_chunk_dg
            		bin_edges_dp = bin_edges_chunk_dp
            		
            		hist_counts = 1
		else:
			hist_counts_p  += hist_chunk_p
	            	hist_counts_rv += hist_chunk_rv
	            	hist_counts_pm += hist_chunk_pm    		
	            	hist_counts_dg += hist_chunk_dg
	            	hist_counts_dp += hist_chunk_dp	
    		
	del chunk_nan  

		
## Se hacen los histogramas

## Paralaje

fig, ax = plt.subplots(figsize=(10, 5))
ax.bar(bin_edges_p[:-1], hist_counts_p, width=np.diff(bin_edges_p), edgecolor="black", alpha=0.7)
ax.set_xlabel("Paralaje")
ax.set_ylabel("Logaritmo Frecuencia Acumulada")
ax.set_title("Histograma de Paralaje [$mas$]")
plt.yscale('log')

plt.savefig("Histograma_Paralaje.png", dpi=300, bbox_inches="tight")
plt.show()

## Velocidad Radial

fig, ax = plt.subplots(figsize=(10, 5))
ax.bar(bin_edges_rv[:-1], hist_counts_rv, width=np.diff(bin_edges_rv), edgecolor="black", alpha=0.7)
ax.set_xlabel("Velocidad Radial [$km s^{-1}$]")
ax.set_ylabel("Logaritmo Frecuencia Acumulada")
ax.set_title("Histograma de Velocidad Radial")
plt.yscale('log')

plt.savefig("Histograma_RV.png", dpi=300, bbox_inches="tight")
plt.show()

## Movimiento Propio

fig, ax = plt.subplots(figsize=(10, 5))
ax.bar(bin_edges_pm[:-1], hist_counts_pm, width=np.diff(bin_edges_pm), edgecolor="black", alpha=0.7)
ax.set_xlabel("Movimiento propio [$mas yr^{-1}$]")
ax.set_ylabel("Logaritmo Frecuencia Acumulada")
ax.set_title("Histograma de Movimiento Propio")
plt.yscale('log')

plt.savefig("Histograma_PM.png", dpi=300, bbox_inches="tight")
plt.show()

## Distancia geometrica

fig, ax = plt.subplots(figsize=(10, 5))
ax.bar(bin_edges_dg[:-1], hist_counts_dg, width=np.diff(bin_edges_dg), edgecolor="black", alpha=0.7)
ax.set_xlabel("Distancia Geometrica [$kpc$]")
ax.set_ylabel("Logaritmo Frecuencia Acumulada")
ax.set_title("Histograma de Distancia Geometrica")
plt.yscale('log')

plt.savefig("Histograma_D_Geometrica.png", dpi=300, bbox_inches="tight")
plt.show()

## Distancia fotogeometrica

fig, ax = plt.subplots(figsize=(10, 5))
ax.bar(bin_edges_dp[:-1], hist_counts_dp, width=np.diff(bin_edges_dp), edgecolor="black", alpha=0.7)
ax.set_xlabel("Distancia Fotogeometrica [$kpc$]")
ax.set_ylabel("Logaritmo Frecuencia Acumulada")
ax.set_title("Histograma de Distancia Fotogeometrica")
plt.yscale('log')

plt.savefig("Histograma_D_Fotogeometrica.png", dpi=300, bbox_inches="tight")
plt.show()
