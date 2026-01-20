import matplotlib.pyplot as plt
import seaborn as sns

# ---------------------------------- PRIMER FUNCION ----------------------------------

# Funcion para graficar distribuciones de columnas numericas
def distribuciones_numericas(df, columnas_numericas, n_fil=2, n_col=2, tamanio=(15, 10)):
    """
    Grafica las distribuciones de las variables numericas en subgraficas.

    Parametros:
    - df: DataFrame que contiene los datos.
    - columnas_numericas: lista de columnas numericas
    - n_fil: numero de filas o subgraficos
    - n_col: numero de columnas o subgraficos
    - tamanio: tamaño de la figura, resive dos parametros (ancho, alto)
    """
    # Estilo de la grafica
    sns.set_style("whitegrid") # whitegrid , darkgrid , ticks , white , dark

    # Configura el tamaño de la figura
    plt.figure(figsize=tamanio)

    # Itera sobre las columnas numericas
    for i, col in enumerate(columnas_numericas, 1):
        plt.subplot(n_fil, n_col, i)  # Ajuste de filas y columnas

        # Personalizacion del histograma
        sns.histplot(df[col].dropna(),
                     bins=30,                      # Número de barras:  n:30 etc , 'auto' , "sturges" , 'fd' , "rice"
                     color="royalblue",            # Color de las barras:       royalblue , turquoise , lightblue , lightcoral , darkorange , firebrick , gold , tomato ,midnightblue , etc.
                     edgecolor="black",            # Color del borde
                     linewidth=1,                  # Grosor de la línea de los bordes
                     alpha=0.7,                    # Transparencia de las barras
                     kde=True,                     # Curva de densidad
                     )

        # Titulos y etiquetas
        plt.title(f'Distribución de {col}', fontsize=15)
        plt.xlabel(f'{col}', fontsize=10)
        plt.ylabel('Frecuencia', fontsize=10)

    # Ajusta el angulo de las etiquetas
    plt.xticks(rotation=0)

    # Titulo global para todo el grafico
    plt.suptitle('Distribucion de las Dimensiones Numericas', fontsize=20, y=1.05)

    # Ajusta el espaciado entre los subgraficos
    plt.tight_layout()
    plt.show()

# ---------------------------------- SEGUNDA FUNCION ----------------------------------

# Función para graficar distribuciones de variables categóricas (ideal para cuando tienen pocas etiquetas las dimensiones)
# Si las dimensiones tienen muchas etiquetas, deliminar el numero maximo de etiquetas con "top"
def distribuciones_categoricas_cortas(df, columnas_categoricas, n_fil=2, n_col=2, tamanio=(15, 10), top=None):
    """
    Grafica las distribuciones de las variables categóricas en subgraficas.

    Parámetros:
    - df: DataFrame que contiene los datos.
    - columnas_categoricas: Lista de nombres de columnas categóricas a graficar.
    - n_fil: Número de filas para los subgráficos (default: 2).
    - n_col: Número de columnas para los subgráficos (default: 2).
    - tamanio: Tamaño de la figura (default: (15, 10)).
    - top: Número máximo de etiquetas a mostrar en cada gráfico (default: None).
    """
    # Define el tamaño de la figura
    plt.figure(figsize=tamanio)

    # Crea gráficos de barras para cada variable categórica
    for i, col in enumerate(columnas_categoricas, 1):
        plt.subplot(n_fil, n_col, i)  # Ajusta el número de filas y columnas

        # Si se especifica 'top', limita las etiquetas a las más frecuentes
        if top:
            # Obtene las etiquetas más frecuentes (limitadas a 'top')
            order = df[col].value_counts().nlargest(top).index
        else:
            # Ordenar todas las etiquetas por frecuencia
            order = df[col].value_counts().index

        # Crea el gráfico de barras
        ""
        sns.countplot(x=df[col], hue=df[col], order=order, 
                      palette="viridis",  # palette="coolwarm" , "viridis"
                      legend=False        # Para activar la nomenglatura de colores.
                      )
        ""
        #sns.countplot(x=df[col], palette="viridis", order=order, hue=None)     # palette="coolwarm" , "viridis"

        # Títulos y etiquetas
        plt.title(f'Distribución de {col}', fontsize=15)
        plt.xlabel(col, fontsize=10)
        plt.ylabel('Frecuencia', fontsize=10)

        # Ajustar la rotación de las etiquetas del eje X
        plt.xticks(rotation=45)  # Ajustar el ángulo

    # Título general para todo el gráfico
    plt.suptitle('Distribución de Variables Categóricas', fontsize=20, y=1.03)

    # Ajusta el espaciado entre los subgráficos
    plt.tight_layout()
    plt.show()

# ---------------------------------- TERCERA FUNCION ----------------------------------

# Funcion para graficar distribuciones de columnas categoricas (ideal para cuando tienen muchas etiquetas las dimensiones)
def distribuciones_categoricas_largas(df, columnas_categoricas, tamanio=(20, 10)):
    """
    Grafica las distribuciones de variables categoricas en subgraficos

    Parametros:
    - df: DataFrame que contiene los datos.
    - columnas_categoricas: Lista de nombres de columnas categaricas a graficar.
    - tamanio: Tamaño de la figura (default: (20, 10)).
    """
    df_categoricas = df[columnas_categoricas]

    # Configura el tamaño de la figura
    plt.figure(figsize=tamanio)

    # Itera sobre las columnas categoricas
    for i, col in enumerate(df_categoricas.columns, 1):
        plt.subplot(len(df_categoricas.columns), 1, i)  # Ajusta las filas segun el numero de columnas
        df_categoricas[col].value_counts().plot(
                                                kind='bar',        # Orientacion de las barras: 'bar' , 'barh'
                                                color='orange',    # Color de las barras: 'skyblue' , 'red', 'green', 'orange' , etc.
                                                edgecolor='black'  # Color del borde de las barras
                                                )
        # Titulos y etiquetas
        plt.title(f'Distribución de {col}')
        plt.xticks(rotation=45)
        plt.ylabel('Frecuencia')

    # Titulo global para todo el grafico
    plt.suptitle('Distribución de Variables Categóricas', fontsize=20, y=1.02)

    # Ajuste automatico para evitar solapamientos
    plt.tight_layout()
    plt.show()

# ---------------------------------- CUARTA FUNCION ----------------------------------

# Funcion para graficar una comparativa entre la dimension objetivo y las dimensiones categoricas
def grafico_categoricos_y_objetivo(df, columnas_categoricas, n_fil=2, n_col=2, tamanio=(15, 10), objetivo='Price', top=None):
    """
    Función para graficar la comparación entre categorías y la dimension objetivo.

    Parámetros:
    df: DataFrame
    columnas_categoricas: lista de columnas categóricas a graficar
    n_fil: número de filas para los subgráficos
    n_col: número de columnas para los subgráficos
    tamanio: tamaño de la figura (ancho, alto)
    objetivo: columna para evaluar.
    top: número máximo de categorías a mostrar en cada gráfico
    """
    # Estilo del gráfico
    sns.set_style("white")  # 'whitegrid' , 'dark' , 'darkgrid' , 'white' , etc.

    # Configura la figura con subgráficos
    fig, axes = plt.subplots(n_fil, n_col, figsize=tamanio)
    axes = axes.flatten()  # Facilitar el acceso a los subgráficos

    # Itera sobre las columnas categóricas
    for i, col in enumerate(columnas_categoricas):
        ax = axes[i] if len(columnas_categoricas) > 1 else axes[0]  # Ajuste si solo hay un gráfico

        # Agrupa por la categoría y calcula la media del 'objetivo', ordenando de mayor a menor
        agrupa_cate = df.groupby(col)[objetivo].mean().dropna().sort_values(ascending=False)

        # Si se especificó 'top', limita las categorías
        if top:
            agrupa_cate = agrupa_cate.head(top)

        # Grafica
        sns.barplot(x=agrupa_cate.index, y=agrupa_cate.values,
                                                              palette="Blues_r",    # 'YlGnBu' , 'Spectral' , 'Greens_r' , 'Blues_r' , 'Oranges_r' , 'RdBu_r'
                                                              edgecolor="black",     # 'Blue' , etc.
                                                              ax=ax,
                                                              hue=agrupa_cate.index,  # Asignamos 'x' a 'hue' para evitar el FutureWarning
                                                              legend=False      # Nomenclatura de los colores
                                                              )

        # Títulos y etiquetas
        ax.set_title(f'Comparación de {col} y {objetivo}', fontsize=14)
        ax.set_xlabel(col, fontsize=12)
        ax.set_ylabel(f'{objetivo} Promedio', fontsize=12)
        ax.set_xticks(range(len(agrupa_cate)))  # Establecemos los ticks en las posiciones correctas
        ax.set_xticklabels(agrupa_cate.index, rotation=45)  # Rota las etiquetas 45 grados

    # Título global para todos los subgráficos
    fig.suptitle(f'Comparación entre Dimensiones Categóricas y {objetivo}', fontsize=18, y=1.05)  # y=1.05 ajusta la posición del título

    # Ajusta el espaciado entre gráficos
    plt.tight_layout()
    plt.show()