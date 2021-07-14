#!/usr/bin/env python
# coding: utf-8

# # <center>Analizar los datos  personales en Facebook con Python</center>
# ![image.png](attachment:image.png)
#  
# A partir del segundo trimestre de 2020, Facebook cuenta con más de 2.700 millones de usuarios activos. Eso significa que si está leyendo este artículo, es probable que sea un usuario de Facebook. Pero, _¿qué tan usuario de Facebook eres? ¿Cuánto publicas realmente? ¡Podemos averiguarlo usando Python!_
# 
# Específicamente, usaremos Python para crear esto: un gráfico que muestra la frecuencia con la que publicamos cada mes a lo largo del tiempo.
# 

# # Paso1: Descargar los datos de Facebook
# 
# En la actualdiad  Facebook nos permite descargar prácticamente todo lo que hemos hecho en el sitio. Puede descargar sus datos aquí , pero es posible que no desee descargarlos todos; ese archivo podría ser enorme , dependiendo de la frecuencia con la que use Facebook y el tiempo que haya estado en él. puede descargarlos acá : [Archivos facebook](https://www.facebook.com/dyi/?referrer=yfi_settings)
# 
# Para este tutorial, veremos específicamente nuestras propias publicaciones personales de Facebook e intentaremos responder las preguntas:
# 
# **_¿Con qué frecuencia publico?_**
# **_¿Estoy usando Facebook más o menos de lo que solía usar?_**
# 
# Para obtener solo los datos relacionados con las publicaciones, vaya a la página de descarga de datos . Cambie el formato de archivo solicitado de HTML a JSON y luego anule la selección de todas las opciones a continuación, marque solo las publicaciones y presione Crear archivo.
# 
# ![image.png](attachment:image.png)
# 
# Facebook te notificará cuando tu archivo se haya creado y esté listo para descargarse; podría demorar un poco, dependiendo de tu historial y opciones de Facebook.
# 
# Descargue el archivo zip, descomprímalo y busque la postscarpeta y un archivo llamado **your_posts_1.json.** Ese es el archivo que usaremos para este tutorial.
# 
# Nota: El formato de archivos JSON es un formato de intercambio de datos, fácil de escribir y leer, que se utiliza hoy en día para compartir información entre diferentes aplicaciones y lenguajes

# # Paso 2: Importar,Formatear y limpiar los datos
# 
# 
# 
# La función incorporada  **_pd.read_json()**   podrá interpretar nuestros datos JSON en un DataFrame automáticamente. (No es perfecto, como verá, pero funcionará para nuestros propósitos aquí).
# 
# Como podemos ver, esto no es perfecto. Algunas de nuestras columnas tienen subcolumnas anidadas en cada fila que todavía están en formato JSON. Si quisiéramos trabajar con esos datos, tendríamos que lidiar con esto.
# 
# Pero para responder a nuestra pregunta aquí, **¿estamos publicando más o menos de lo que solíamos hacer en Facebook?** - Realmente no necesitamos ocuparnos del contenido real de la publicación o con otra información como archivos multimedia adjuntos. Solo nos preocupa la frecuencia : la frecuencia con la que se hicieron nuevas publicaciones
# A continuación, nos aseguraremos de que la columna de marca de tiempo esté en el formato correcto para convertirla en un objeto de fecha y hora usando  **to_datetime()**. También le cambiaremos el nombre 'date'y eliminaremos algunas de las columnas innecesarias solo para mayor claridad; este paso no es estrictamente necesario, pero nos ayuda a tener algo más simple de ver.

# In[50]:


#1--Importamos la libreria pandas
import pandas as pd

#2--leemos los datos del data frame en formato Json :
df=pd.read_json("your_posts_1.json ")

df.head(5)  #head() otenemos las primeras líneas del DataFrame  your_posts_1.json  
df.head(2)

#3-- Eliminamos las columnas que no nos proporcionan valor
df = df.drop(['attachments', 'title', 'tags'], axis=1) 

#4--Renombramos  la columna timesstamp
df.rename(columns={'timestamp': 'date'}, inplace=True) #inplace=True, los datos se renombran en su lugar.


#5--> Ajustamos de que sea el formato de fecha y hora
pd.to_datetime(df['date'])

#6-->Contamos las Filas para ver con cuanta información se está trabajando
print(df.shape)

#7-->Verificamos el final de nuestro marcos de datos
df.tail() 


"""Hasta acá tenemos nuestro datos con las 2988 filas y dos columnas, pero queremos transformar nuestros datos que nos digan
cual es la frecuencia de la publicación por cada una de las fechas"""

df = df.set_index('date') # usamos este método para establecer una lista
jeanvitola = df['data'].resample('MS').size() # .resample() se usa principalmente para datos de series de tiempo. Es un método de conveniencia para conversión de frecuencia y remuestreo de series de tiempo
jeanvitola


# 

# # Paso 4: visualice su uso de Facebook
# 
# De todos modos, ahora que hemos pasado la parte complicada, todo lo que queda es la diversión: ¡la visualización! Para hacer eso, importaremos matplotlib (y usaremos la %matplotlib inlinemagia para hacer que nuestro gráfico aparezca en el Jupyter Notebook. También importaremos Seaborn y NumPy, lo que nos ayudará a hacer un gráfico de apariencia más legible.
# 
# Una vez que hayamos hecho nuestras importaciones, usaremos sns.set()para establecer el tamaño y el tamaño de fuente de nuestro gráfico. Dado que estamos trabajando con una gran cantidad de datos aquí, haremos el gráfico bastante grande y nos aseguraremos de que el tamaño de la fuente sea lo suficientemente grande para que sea legible.
# 
# Luego, configuraremos las etiquetas x para usar el índice de post_counts(las fechas) y las usaremos sns.barplot()para crear un gráfico de barras. En los argumentos para sns.barplot(), le diremos a la función que use las etiquetas x que definimos, para trazar los datos post_countsy hacer que la barra sea de color azul.
# 
# Solo eso sería suficiente para crear un gráfico básico, pero en este caso, queremos tomar algunos pasos adicionales para que el gráfico sea legible. Específicamente, queremos organizar las posiciones de las marcas en el eje x una vez cada 24 meses, de modo que veamos una marca cada dos años en el gráfico resultante. También queremos cambiar el formato de las fechas en el gráfico para que solo se muestre el año.
# 
# (Dado que este no es un tutorial sobre visualización de datos, no profundizaremos en cómo funciona esto como parte de este tutorial, pero si desea obtener más información sobre cómo hacer excelentes visualizaciones de datos con Python, tenemos Visualización de datos exploratorios y narración de historias a través de cursos de visualización de datos que puede probar de forma gratuita). 
# 

# In[51]:


get_ipython().run_line_magic('matplotlib', 'inline')
get_ipython().run_line_magic('matplotlib', 'inline')
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np

# set figure size and font size
sns.set(rc={'figure.figsize':(40,30)})
sns.set(font_scale=3)

# set x labels
x_labels = jeanvitola.index

#create bar plot
sns.barplot(x_labels, post_counts, color="#000080")

# only show x-axis labels for Jan 1 of every other year
tick_positions = np.arange(10, len(x_labels), step=24)

#reformat date to display year onlyplt.ylabel("post counts")
plt.xticks(tick_positions, x_labels[tick_positions].strftime("%Y"))

# display the plot
plt.show()


# Todavía hay algunas formas en que podríamos hacer que este gráfico sea aún más bonito, pero para nuestros propósitos, esto es suficiente para poder comprender los datos y analizar nuestro historial de publicaciones en Facebook. 
# 
# En mi caso, el gráfico de arriba son mis datos personales de Facebook, podemos ver que solo publiqué en Facebook en raras ocasiones en los primeros días. Tuve grandes ráfagas de publicaciones, ¡cientos por mes! - en el 2012 tuve mi punto máximo y la primavera de 2013, que coincidió con las conexiones a internet de mi localidad. Mi uso habitual comenzó a disminuir alrededor de 2014 y alcanzó los niveles mínimos  alrededor de 2016. Después de eso, disminuyó y dejé de usar Facebook por completo durante bastante tiempo a finales del 2016. 
# 
# 
# ¡Y recuerde, eso son solo publicaciones, no comentarios ! Hay otro archivo JSON completo para comentarios, pero ya estoy bastante avergonzado. Si desea llevar su análisis más allá, ¡profundizar en su archivo de comentarios sería un gran paso siguiente!Descargamos datos de uso personal de Facebook Visualizamos el uso de Facebook y aprendimos algo: Jean solía pasar demasiado tiempo en Facebook.
# 
# Si le gusta hacer proyectos como este, siganme.

# In[ ]:




