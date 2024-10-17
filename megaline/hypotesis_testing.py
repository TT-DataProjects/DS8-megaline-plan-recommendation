import pandas as pd
from scipy import stats
from IPython.display import Markdown, display

# Diccionario con las explicaciones para cada prueba
EXPLICACIONES = {
    "Shapiro-Wilk": ("Esta prueba de normalidad mide si los datos siguen una distribución normal. "
                     "Un valor de estadístico cercano a 1 sugiere normalidad. Si el valor p es menor a 0.05, "
                     "rechazamos la hipótesis de normalidad."),
    "Levene": ("El estadístico de Levene mide la dispersión (varianza) entre los grupos. "
               "Si el valor p es menor a 0.05, las varianzas son significativamente diferentes."),
    "T-Test": ("Esta prueba compara las medias de dos grupos asumiendo que siguen una distribución normal "
               "y que las varianzas son iguales. Si el valor p es menor a 0.05, las medias son significativamente diferentes."),
    "Welch's T-Test": ("Esta prueba es una versión ajustada del T-Test que se utiliza cuando las varianzas de los grupos no son iguales."),
    "Mann-Whitney": ("Esta prueba no paramétrica compara las distribuciones de dos grupos sin asumir normalidad. "
                     "Si el valor p es menor a 0.05, existe una diferencia significativa entre las distribuciones.")
}

def AB_test(data1, data2, explain=False):
    """
    Esta función realiza la verificación de suposiciones estadísticas (normalidad y homogeneidad de varianzas),
    selecciona la prueba adecuada (T-Test, Welch's T-Test o Mann-Whitney U), y luego interpreta los resultados.
    
    Parámetros:
    data1 (pd.Series): Serie de pagos totales del primer grupo (NY-NJ, por ejemplo).
    data2 (pd.Series): Serie de pagos totales del segundo grupo (otros usuarios, por ejemplo).
    explain (bool): Si es True, muestra explicaciones detalladas de las pruebas realizadas.
    
    Retorna:
    None: La función imprime el resultado de las pruebas realizadas.
    """
    
    # Paso 1: Verificación de supuestos

    # Prueba de normalidad (Shapiro-Wilk)
    shapiro_data1 = stats.shapiro(data1)
    shapiro_data2 = stats.shapiro(data2)

    display(Markdown(f"**Shapiro-Wilk Test para Grupo 1:**\n- Estadístico: {shapiro_data1.statistic:.3f}\n- Valor p: {shapiro_data1.pvalue:.2e}"))
    display(Markdown(f"**Shapiro-Wilk Test para Grupo 2:**\n- Estadístico: {shapiro_data2.statistic:.3f}\n- Valor p: {shapiro_data2.pvalue:.2e}"))

    if explain:
        display(Markdown(EXPLICACIONES["Shapiro-Wilk"]))

    # Prueba de homogeneidad de varianzas (Levene)
    levene_test = stats.levene(data1, data2)
    display(Markdown(f"\n**Resultado de la prueba de homogeneidad de varianzas (Levene's Test):**\n- Estadístico: {levene_test.statistic:.3f}\n- Valor p: {levene_test.pvalue:.2e}"))

    if explain:
        display(Markdown(EXPLICACIONES["Levene"]))

    # Paso 2: Selección de Prueba Estadística
    if shapiro_data1.pvalue > 0.05 and shapiro_data2.pvalue > 0.05:  # Ambos son normales
        if equal_var := levene_test.pvalue > 0.05:
            test_result = stats.ttest_ind(data1, data2, equal_var=equal_var)
            tipo_de_prueba = "T-Test para muestras independientes"
            if explain:
                display(Markdown(EXPLICACIONES["T-Test"]))
        else:
            test_result = stats.ttest_ind(data1, data2, equal_var=equal_var)
            tipo_de_prueba = "Welch's T-Test para muestras independientes"
            if explain:
                display(Markdown(EXPLICACIONES["Welch's T-Test"]))
    else:  # Si al menos uno de los conjuntos no es normal
        test_result = stats.mannwhitneyu(data1, data2)
        tipo_de_prueba = "Mann-Whitney U Test"
        if explain:
            display(Markdown(EXPLICACIONES["Mann-Whitney"]))

    # Paso 3: Interpretación de Resultados
    display(Markdown(f"\n**Resultado de la prueba de hipótesis ({tipo_de_prueba}):**"))

    # Algunos resultados no tienen el atributo 'statistic' como Mann-Whitney U, manejamos eso:
    try:
        display(Markdown(f"- Estadístico: {test_result.statistic:.3f}"))
    except AttributeError:
        display(Markdown(f"- Estadístico: {test_result.statistic if hasattr(test_result, 'statistic') else 'N/A'}"))

    display(Markdown(f"- Valor p: {test_result.pvalue:.2e}"))