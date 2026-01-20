# Data Preprocessing and Feature Engineering

Este proyecto forma parte de la colección **Data-Analytics-and-Visualization**, y tiene como objetivo demostrar un flujo completo de **análisis exploratorio de datos (EDA)**, **limpieza**, **transformación de datos** e **ingeniería de características**, aplicado a un dataset real del mercado de autos.

---

## 📌 Objetivos del proyecto

* Realizar un **análisis exploratorio inicial** para comprender la estructura y calidad de los datos.
* Identificar y tratar **valores faltantes**, inconsistencias y variables con formatos no adecuados.
* Transformar variables que contienen información numérica en formato texto.
* Aplicar **ingeniería de características** para enriquecer el dataset.
* Comparar el dataset **antes y después** de las etapas de procesamiento.
* Mantener el código **modular y reutilizable** mediante funciones externas.

---

## 🗂️ Estructura del proyecto

```
Data-Analytics-and-Visualization/
└── Data-Preprocessing-and-Feature-Engineering/
    ├── README.md
    ├── .gitignore
    ├── requirements.txt
    │
    ├── data/
    │   └── used_cars_data.csv
    │
    ├── notebooks/
    │   └── Data Preprocessing and Feature Engineering.ipynb
    │
    └── src/
        ├── __init__.py
        └── visualization.py
```

---

## 🧪 Dataset

El dataset contiene información de autos, con un total de **7,253 registros** y **14 variables**, incluyendo:

* Variables numéricas: `Year`, `Kilometers_Driven`, `Seats`, `Price`
* Variables categóricas: `Location`, `Fuel_Type`, `Transmission`, `Owner_Type`
* Variables con formato mixto (texto + unidades):

  * `Mileage`
  * `Engine`
  * `Power`

---

## 🔍 Flujo de trabajo

### 1. Análisis Exploratorio de Datos (EDA)

* Revisión de tipos de datos
* Análisis de valores faltantes
* Estadísticas descriptivas
* Visualización de distribuciones y relaciones entre variables

### 2. Limpieza de datos

* Tratamiento de valores nulos
* Eliminación o corrección de registros inconsistentes
* Preparación de variables para su transformación

### 3. Transformación de datos

* Conversión de variables con unidades (kmpl, CC, bhp, Lakh) a valores numéricos
* Estandarización de formatos
* Ajuste de tipos de datos

### 4. Ingeniería de características

* Creación de nuevas variables derivadas
* Preparación del dataset para análisis posteriores o modelos predictivos

### 5. EDA posterior

* Análisis exploratorio del dataset ya procesado
* Comparativa visual y estadística entre el dataset original y el transformado

---

## 📊 Visualización

Las visualizaciones se manejan mediante funciones reutilizables definidas en:

```
src/visualization.py
```

Estas funciones permiten mantener el notebook limpio y mejorar la mantenibilidad del código.

---

## ⚙️ Requisitos

Las principales librerías utilizadas incluyen:

* pandas
* numpy
* matplotlib
* seaborn

Puedes instalar todas las dependencias con:

```bash
pip install -r requirements.txt
```

---

## 🚀 Cómo ejecutar el proyecto

1. Clona el repositorio
2. Instala las dependencias
3. Abre el notebook ubicado en `notebooks/`
4. Ejecuta las celdas en orden para reproducir el análisis completo

---

## 📫 Contacto

**Jesús Armando Soria Martínez**

  <a href="http://www.linkedin.com/in/jesus-armando-soria-martinez-a9b786366" target="_blank">
    <img src="https://img.shields.io/badge/LinkedIn-0077B5?style=for-the-badge&logo=linkedin&logoColor=white&animation=pulse" alt="LinkedIn"/>
  </a>
  <a href="https://github.com/Soria-Jesus" target="_blank">
    <img src="https://img.shields.io/badge/GitHub-100000?style=for-the-badge&logo=github&logoColor=white" alt="GitHub"/>
  </a>
  <a href="mailto:oficial.jasm@gmail.com" target="_blank">
    <img src="https://img.shields.io/badge/Gmail-D14836?style=for-the-badge&logo=gmail&logoColor=white" alt="Gmail"/>
  </a>

---