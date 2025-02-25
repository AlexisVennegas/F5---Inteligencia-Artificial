1. Crear un entorno virtual con cualquiera de las herramientas disponibles y activarlo

    R:  1.- abrir terminal
    
        2.- crear un entorno

            R: conda create --name "nombre entorno"

            R: conda activate --name "nombre entorno" // conda deactive "nombre del entorno"

            R: conda install numpy pandas Matplitlib jupyter (instalar librerias)

            R: conda info --envs

            R: jupyter notebook

        3.- abrir un entorno ya creado

            R: conda info --envs

            R: jupyter notebook (crear o abrir un cuaderno)

        
        4.-importar librerias en el archivo 

            R: en el archivo deseado 
                import pandas as pd
                import matplotlib.pyplot as plt
                from matplotlib.cm import viridis
                from IPython.display import FileLink

2.- ejercicio

    R: df = pd.read_csv('loan_dataset2.csv'):

        Aquí se lee un archivo CSV llamado "loan_dataset2.csv" utilizando la función read_csv de Pandas. Los datos se almacenan en un DataFrame llamado "df". Un DataFrame es una estructura de datos de Pandas que se utiliza para almacenar y manipular datos tabulares.


    R: df.head()

        Esta línea imprime las primeras filas del DataFrame "df". Por defecto, muestra las primeras 5 filas, pero también puedes especificar un número diferente de filas como argumento dentro de los paréntesis, por ejemplo: df.head(10) mostraría las primeras 10 filas del DataFrame.

        La función head() es útil para obtener una vista previa de los datos y verificar rápidamente la estructura y los valores iniciales en un DataFrame. Muestra las primeras filas, lo que puede ser especialmente útil cuando se trabaja con grandes conjuntos de datos y no se quiere imprimir todo el DataFrame completo.

    R:  df.describe()

        Esta línea muestra un resumen estadístico del DataFrame "df". Proporciona información como el recuento de datos, la media, la desviación estándar, los valores mínimo y máximo, y los percentiles de las columnas numéricas del DataFrame.

        El resultado de df.describe() mostrará las siguientes estadísticas para cada columna numérica del DataFrame:

        Count: el número de valores no nulos en la columna.
        Mean: la media (promedio) de la columna.
        Std: la desviación estándar de la columna.
        Min: el valor mínimo de la columna.
        25%: el percentil 25 de la columna.
        50%: el percentil 50 (mediana) de la columna.
        75%: el percentil 75 de la columna.
        Max: el valor máximo de la columna.
