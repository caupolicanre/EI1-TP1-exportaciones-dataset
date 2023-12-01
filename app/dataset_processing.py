# ===========
#  LIBRERÍAS
# ===========

# Librerías utilizadas para trabajar con el programa
import csv
import operator as op
import matplotlib.pyplot as plt


# ================
#  CÓDIGO CLIENTE
# ================

# Ruta donde se encuentra el archivo del dataset
rutaDataset="./dataset/original/"

# Matriz donde se almacenará la nueva Base de Datos
dataBaseNueva=[]

# Defino estas variables con el índice correspondiente a cada variable, para trabajar más cómodo con las columnas
indicePaisDestino=6                 
indiceFechaCreacion=9               
indiceMontoOperacion=11             
indiceMontoOperacionOrdinal=12      # variable que modificaremos nosotros
indiceTiempoEnvio=13                
indiceTiempoEnvioNominal=14         # variable que modificaremos nosotros
indiceTiempoEnvioNormalizada=15     # variable que modificaremos nosotros

# Variables para manejar los umbrales
monto_operacion_prom=2604.61
tiempo_envio_prom=251.14

# Variables para la normalización de la variable "tiempo_envio"
valoresNormalizados_TiempoEnvio=[]  # Creo esta lista para almacenar los datos normalizados y graficarlos en el histograma
minimo_original_TiempoEnvio=1
maximo_original_TiempoEnvio=500

# Lista para almacenar todos los valores de la variable "pais_destino", y así procesarla después
listaPaisDestino=[]


# Listas para almacenar los valores de la variable "monto_operacion", y así procesarla después
listaMontoOperacion_tresAnios=[]
monto_operacion_min=40000
monto_operacion_max=40000   # Sabemos que el valor máximo de la base de datos es 42000, así que asignamos un valor menor cercano, para que se modifique y usarlo como valor inicial en los mínimos

listaMontoOperacion2017=[]
monto_operacion2017_min=monto_operacion_max # Las variables mínimas empiezan con el valor máximo de toda la base de datos, para que se modifique al entrar al for
monto_operacion2017_max=0

listaMontoOperacion2018=[]
monto_operacion2018_min=monto_operacion_max
monto_operacion2018_max=0

listaMontoOperacion2019=[]
monto_operacion2019_min=monto_operacion_max
monto_operacion2019_max=0


# Contadores para almacenar la información obtenida de este procesamiento
contadorMontoBajo=0
contadorMontoMedio=0
contadorMontoAlto=0
contadorEnvioRapido=0
contadorEnvioLento=0

# Esta variable la uso para ir moviendome por las filas de la base de datos
indiceDBNueva=0

with open(rutaDataset+"Exportaciones_app.csv",'r') as archivo:
    lector= csv.reader(archivo, delimiter=";")
    columnas= next(lector)      # Defino la variable "columna" con las variables de la base de datos
    
    for linea in lector:
        monto_operacion=linea[indiceMontoOperacion].replace(',','.')
        monto_operacion=round(float(monto_operacion),2)

        tiempo_envio=int(linea[indiceTiempoEnvio])

        fecha=linea[indiceFechaCreacion].split('/')
        mes=int(fecha[1])
        anio=int(fecha[2])

        dataBaseNueva.append(linea)

        # Rangos para el umbralado de monton_operacion:
        # Monto bajo:         1    -    5999
        # Monto medio:     6000    -   10000
        # Monto alto:   > 10000
        if monto_operacion>=1 and monto_operacion<6000:
            dataBaseNueva[indiceDBNueva][indiceMontoOperacionOrdinal]="Monto bajo"
            contadorMontoBajo+=1

        elif monto_operacion>=6000 and monto_operacion<=10000:
            dataBaseNueva[indiceDBNueva][indiceMontoOperacionOrdinal]="Monto medio"
            contadorMontoMedio+=1

        elif monto_operacion>10000:
            dataBaseNueva[indiceDBNueva][indiceMontoOperacionOrdinal]="Monto alto"
            contadorMontoAlto+=1
        
        # Rangos para el umbralado de tiempo_envio:
        # Rápido:     1     -   251.14 (Media)
        # Lento:  > 251.14
        if tiempo_envio<=tiempo_envio_prom:
            dataBaseNueva[indiceDBNueva][indiceTiempoEnvioNominal]="Rápido"
            contadorEnvioRapido+=1
        else:
            dataBaseNueva[indiceDBNueva][indiceTiempoEnvioNominal]="Lento"
            contadorEnvioLento+=1
        
        # Normalización de la variable tiempo_envio:
        tiempo_envio_normalizado=(tiempo_envio - minimo_original_TiempoEnvio) / (maximo_original_TiempoEnvio - minimo_original_TiempoEnvio)
        dataBaseNueva[indiceDBNueva][indiceTiempoEnvioNormalizada]=round(tiempo_envio_normalizado,2)
        valoresNormalizados_TiempoEnvio.append(tiempo_envio_normalizado)
        
        # Agrego a esta lista todos los valores de la variable "paise_destino", para luego procesarlos y hacer un gráfico
        listaPaisDestino.append(dataBaseNueva[indiceDBNueva][indicePaisDestino])


        # Filtrado de los montos por meses y años
        # Todos los años de diciembre a febrero
        if mes==12 or mes==1 or mes==2:
            listaMontoOperacion_tresAnios.append(monto_operacion)

            # Obtención de mínimo y máximo de toda la base de datos
            if monto_operacion<monto_operacion_min:
                monto_operacion_min=monto_operacion
            
            if monto_operacion>monto_operacion_max:
                monto_operacion_max=monto_operacion
        
        # Diciembre a febrero 2017
        if anio==2017:
            if mes==12 or mes==1 or mes==2:
                listaMontoOperacion2017.append(monto_operacion)

                # Obtención de mínimo y máximo de 2017
                if monto_operacion<monto_operacion2017_min:
                    monto_operacion2017_min=monto_operacion

                if monto_operacion>monto_operacion2017_max:
                    monto_operacion2017_max=monto_operacion

        # Diciembre a febrero 2018
        elif anio==2018:
            if mes==12 or mes==1 or mes==2:
                listaMontoOperacion2018.append(monto_operacion)

                # Obtención de mínimo y máximo de 2018
                if monto_operacion<monto_operacion2018_min:
                    monto_operacion2018_min=monto_operacion

                if monto_operacion>monto_operacion2018_max:
                    monto_operacion2018_max=monto_operacion
        
        # Diciembre a febrero 2019
        elif anio==2019:
            if mes==12 or mes==1 or mes==2:
                listaMontoOperacion2019.append(monto_operacion)

                # Obtención de mínimo y máximo de 2019
                if monto_operacion<monto_operacion2019_min:
                    monto_operacion2019_min=monto_operacion

                if monto_operacion>monto_operacion2019_max:
                    monto_operacion2019_max=monto_operacion


        indiceDBNueva+=1    # Sumamos 1, para que cuando empiece devuelta el for, pase a la siguiente linea la matriz de la base de datos nueva
        


# Una vez finalizado el procesamiento de las exportaciones y creando una matriz con los datos nuevos, cargo la base de datos modificada en el archivo
with open('dataset/processed/'+'Exportaciones_processed.csv','w') as DBNueva:
    escritor=csv.writer(DBNueva, delimiter=';')
    escritor.writerow(columnas)
    escritor.writerows(dataBaseNueva)


# Cálculo de los porcentajes
totalDatos=len(dataBaseNueva)-1

porcentajeMontoBajo=round((contadorMontoBajo*100)/totalDatos,2)
porcentajeMontoMedio=round((contadorMontoMedio*100)/totalDatos,2)
porcentajeMontoAlto=round((contadorMontoAlto*100)/totalDatos,2)

porcentajeEnvioRapido=round((contadorEnvioRapido*100)/totalDatos,2)
porcentajeEnvioLento=round((contadorEnvioLento*100)/totalDatos,2)



# ========================
#  GENERACIÓN DE GRÁFICOS
# ========================

# Histograma "tiempo_envio" Normalizada

fig, ax = plt.subplots()
ax.hist(valoresNormalizados_TiempoEnvio, label="Variable \"tiempo_envio\" Normalizada")

# Información del gráfico (Título, leyenda, rangos, nombres de los ejes)
ax.set_title('Histograma con las repeticiones de los valores de "tiempo_envio" Normalizada', loc = "center", fontdict = {'fontsize':14, 'fontweight':'bold'})
ax.set_ylabel("Repeticiones")
ax.set_xlabel("Escala")
ax.set_xlim([0, 1])
ax.set_ylim([0,700])
ax.set_yticks(range(0,700,50))
ax.set_xticks([0.1,0.2,0.3,0.4,0.5,0.6,0.7,0.8,0.9,1])
ax.legend(loc = 'upper right')

plt.show()


# Gráfico de torta Porcentaje de Montos Ordinal

fig2, ax2 = plt.subplots()
ax2.set_title('Porcentajes de "monto_operacion_ordinal"', loc = "center", fontdict = {'fontsize':14, 'fontweight':'bold'})
ax2.pie([porcentajeMontoBajo, porcentajeMontoMedio, porcentajeMontoAlto])
ax2.legend(loc="upper left", labels=["Monto bajo "+str(porcentajeMontoBajo)+"%", "Monto medio "+str(porcentajeMontoMedio)+"%", "Monto alto "+str(porcentajeMontoAlto)+"%"])

plt.show()


# Gráfico de torta Porcentaje de "tiempo_envio_nominal"

fig3, ax3 = plt.subplots()
ax3.set_title('Porcentajes de "tiempo_envio_nominal"', loc = "center", fontdict = {'fontsize':14, 'fontweight':'bold'})
ax3.pie([porcentajeEnvioLento, porcentajeEnvioRapido], startangle = 90)
ax3.legend(loc="upper left", labels=["Envío lento "+str(porcentajeEnvioLento)+"%", "Envío rápido "+str(porcentajeEnvioRapido)+"%"])

plt.show()



# Lista para almacenar las repeticiones de cada paíse destino
contadorPaisDestino=[]  # Este contador es una lista para simplemente no tener paises repetidos cuando ya se contaron

# Listas para almacenar los países y su cantidad de repeticiones, están separadas para trabajar más comodo con el gráfico, el índice de cada elemento corresponde al dato de la otra lista
paisDestino=[]
repeticionesPaisDestino=[]

# Variables para almacenar los envíos que no superan la cantidad de 150
repeticionesMenos150=0
repeticionesMenos100=0
repeticionesMenos50=0

# Repeticiones de cada país destino
for pais in listaPaisDestino:
    cont=listaPaisDestino.count(pais)

    if (pais,cont) not in contadorPaisDestino:
        contadorPaisDestino.append((pais,cont))

        if cont>=150:
            paisDestino.append(pais)
            repeticionesPaisDestino.append(cont)

        elif cont<150 and cont>=100:
            repeticionesMenos150+=cont

        elif cont<100 and cont>=50:
            repeticionesMenos100+=cont
        
        elif cont<50:
            repeticionesMenos50+=cont


# Agrego la suma de repeticiones a cada categoría correspondiente
paisDestino.append("Países con cantidad de envíos entre 100 y 150")
repeticionesPaisDestino.append(repeticionesMenos150)

paisDestino.append("Países con cantidad de envíos entre 50 y 100")
repeticionesPaisDestino.append(repeticionesMenos100)

paisDestino.append("Países con cantidad de envíos menor a 50")
repeticionesPaisDestino.append(repeticionesMenos50)


# Gráfico de torta de la variable "pais_destino"
fig4, ax4 = plt.subplots()

colorsPaises=["#B0E0E6","#A52A2A","#F5F5DC","#DEB887","#5F9EA0","#FF7F50","#9932CC","#2F4F4F","#228B22","#FFE4E1","#4B0082"]
explodePaises=[0,0.2,0,0,0,0,0,0,0,0,0]

ax4.set_title('Envíos a los Países Destino', loc = "center", fontdict = {'fontsize':14, 'fontweight':'bold'})
ax4.pie(repeticionesPaisDestino, labels=paisDestino, colors=colorsPaises, explode=explodePaises, startangle = 90)

plt.show()


# Gráfico de boxplot para la variable "monto_operacion" 3 años
fig5, ax5 = plt.subplots()

ax5.set_title('Extremos de la variable "monto_operacion" en el período de diciembre-febrero en los años 2017-2018-2019', loc = "center", fontdict = {'fontsize':14, 'fontweight':'bold'})
ax5.set_ylabel("Escala (Valor monto)")
ax5.set_ylim([-5000,46000])                  # GRAFICO COMPLETO
ax5.set_yticks(range(-5000,45001,5000))      # GRÁFICO COMPLETO
# ax5.set_ylim([-2000,20000])                # GRÁFICO ZOOM
# ax5.set_yticks(range(-2000,20001,1000))    # GRÁFICO ZOOM
ax5.grid(axis = 'y', color = 'gray', linestyle = '--')

ax5.boxplot(listaMontoOperacion_tresAnios)
plt.show()


# Gráfico de boxplot para la variable "monto_operacion" 2017
fig6, ax6 = plt.subplots()

ax6.set_title('Extremos de la variable "monto_operacion" en el período de diciembre-febrero en el año 2017', loc = "center", fontdict = {'fontsize':14, 'fontweight':'bold'})
ax6.set_ylabel("Escala (Valor monto)")
ax6.set_ylim([-5000,46000])             # GRÁFICO COMPLETO
ax6.set_yticks(range(-5000,45001,5000)) # GRÁFICO COMPLETO
ax6.grid(axis = 'y', color = 'gray', linestyle = '--')

ax6.boxplot(listaMontoOperacion2017)
plt.show()


# Gráfico de boxplot para la variable "monto_operacion" 2018
fig7, ax7 = plt.subplots()

ax7.set_title('Extremos de la variable "monto_operacion" en el período de diciembre-febrero en el año 2018', loc = "center", fontdict = {'fontsize':14, 'fontweight':'bold'})
ax7.set_ylabel("Escala (Valor monto)")
ax7.set_ylim([0,19000])             # GRÁFICO COMPLETO
ax7.set_yticks(range(0,18001,1000)) # GRÁFICO COMPLETO
ax7.grid(axis = 'y', color = 'gray', linestyle = '--')

ax7.boxplot(listaMontoOperacion2018)
plt.show()


# Gráfico de boxplot para la variable "monto_operacion" 2019
fig8, ax8 = plt.subplots()

ax8.set_title('Extremos de la variable "monto_operacion" en el período de diciembre-febrero en el año 2019', loc = "center", fontdict = {'fontsize':14, 'fontweight':'bold'})
ax8.set_ylabel("Escala (Valor monto)")
ax8.set_ylim([0,19000])             # GRÁFICO COMPLETO
ax8.set_yticks(range(0,18001,1000)) # GRÁFICO COMPLETO
ax8.grid(axis = 'y', color = 'gray', linestyle = '--')

ax8.boxplot(listaMontoOperacion2019)
plt.show()



# =======================
#  INFORME BLOC DE NOTAS
# =======================


contadorPaisDestino.sort(key=op.itemgetter(1), reverse=True)  # Esta es la manera para organizar una matriz por su columna

# Cuando ya está realizado todo el trabajo de procesamiento, escribo en un bloc de notas, la información del resultado del trabajo de umbralado
with open('./dataset/processed/'+'Exportaciones_report.txt','w') as informe:
    informe.write("Informe del procesamiento de la base de datos \"Exportaciones\"\n\n")

    informe.write("Variables Procesadas:\n")
    informe.write(". \"monto_operacion\"\n")
    informe.write(". \"tiempo_envio\"\n")
    informe.write(". \"pais_destino\"\n\n")

    informe.write("Variables Nuevas:\n")
    informe.write(". \"monto_operacion_ordinal\"\n")
    informe.write(". \"tiempo_envio_nominal\"\n")
    informe.write(". \"tiempo_envio_normalizada\"\n\n\n")


    informe.write("Información Obtenida\n\n")

    informe.write("Monto Operación\n")
    informe.write("Monto Operación Ordinal:\n")
    informe.write(f". Monto Bajo: {porcentajeMontoBajo}%\n")
    informe.write(f". Monto Medio: {porcentajeMontoMedio}%\n")
    informe.write(f". Monto Alto: {porcentajeMontoAlto}%\n\n")

    informe.write("Monto Operación Mínimos y Máximos período diciembre-febrero:\n")
    informe.write(f". 2017:\n")
    informe.write(f"       . Mínimo: {monto_operacion2017_min}\n")
    informe.write(f"       . Máximo: {monto_operacion2017_max}\n")
    informe.write(f"       . Cantidad de envíos: {len(listaMontoOperacion2017)}\n")
    informe.write(f". 2018:\n")
    informe.write(f"       . Mínimo: {monto_operacion2018_min}\n")
    informe.write(f"       . Máximo: {monto_operacion2018_max}\n")
    informe.write(f"       . Cantidad de envíos: {len(listaMontoOperacion2018)}\n")
    informe.write(f". 2019:\n")
    informe.write(f"       . Mínimo: {monto_operacion2019_min}\n")
    informe.write(f"       . Máximo: {monto_operacion2019_max}\n")
    informe.write(f"       . Cantidad de envíos: {len(listaMontoOperacion2019)}\n")
    informe.write(f". Los 3 años:\n")
    informe.write(f"       . Mínimo: {monto_operacion_min}\n")
    informe.write(f"       . Máximo: {monto_operacion_max}\n")
    informe.write(f"       . Cantidad de envíos: {len(listaMontoOperacion_tresAnios)}\n\n")


    informe.write("Tiempo Envío:\n")
    informe.write(f". Rápido: {porcentajeEnvioRapido}%\n")
    informe.write(f". Lento: {porcentajeEnvioLento}%\n\n")


    informe.write("Cantidad de envíos a cada país destino:\n")
    for i in range(len(contadorPaisDestino)):
        informe.write(f". {contadorPaisDestino[i][0]}: {contadorPaisDestino[i][1]}\n")