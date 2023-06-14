import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt

class Graficador:

    @staticmethod
    def grafico_numerico(df, columna, titulo, simbolo):
        fig, ejes = plt.subplots(2, 1, sharex=True, figsize=(8, 5), gridspec_kw={"height_ratios": (.2, .8)})
        ejes[0].set_title(titulo, fontsize=18)
        sns.boxplot(x=columna, data=df, ax=ejes[0])
        ejes[0].set(yticks=[])
        sns.histplot(x=columna, data=df, ax=ejes[1])
        ejes[1].set_xlabel(columna, fontsize=16)
        
        media = np.round(df[columna].mean(), 1)
        mediana = np.round(df[columna].median(), 1)
        moda = df[columna].mode()[0]
        
        ejes[1].axvline(media, color='darkgreen', linewidth=2.2, label='media=' + str(media) + simbolo)
        ejes[1].axvline(mediana, color='red', linewidth=2.2, label='mediana=' + str(mediana) + simbolo)
        ejes[1].axvline(moda, color='purple', linewidth=2.2, label='moda=' + str(moda) + simbolo)
        
        ejes[1].legend(bbox_to_anchor=(1, 1.03), ncol=1, fontsize=17, fancybox=True, shadow=True, frameon=True)
        plt.tight_layout()
        plt.show()

    def grafico_categorico(df, columna, titulo):
        num_filas = df.shape[0]
        num_valores_unicos = df[columna].nunique()

        if num_valores_unicos / num_filas < 0.5:
            fig, ejes = plt.subplots(1, 2, figsize=(14, 6))

            # Gráfico de barras
            sns.countplot(x=columna, data=df, ax=ejes[0])
            ejes[0].set_title(titulo + " - Gráfico de barras", fontsize=18)
            ejes[0].set_ylabel("Frecuencia", fontsize=14)
            ejes[0].set_xlabel(columna, fontsize=14)

            # Gráfico de pastel
            conteo = df[columna].value_counts()
            ejes[1].pie(conteo, labels=conteo.index, autopct='%1.1f%%', startangle=90)
            ejes[1].set_title(titulo + " - Gráfico de pastel", fontsize=18)
            ejes[1].axis("equal")  # Para que el gráfico de pastel sea un círculo

            plt.tight_layout()
            plt.show()
        else:
            print(f"La columna '{columna}' tiene demasiados valores únicos ({num_valores_unicos}) en relación con el número de filas ({num_filas}). No se graficará.")


