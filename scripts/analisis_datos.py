import pandas as pd
import numpy as np
import plotly.express as px

# 1. Simulación de datos de incidentes/registros
np.random.seed(42)
fechas = pd.date_range(start="2024-01-01", periods=90, freq="D")
categorias = ["Seguridad", "Calidad", "Medio Ambiente"]

data = {
    "Fecha": np.random.choice(fechas, size=200),
    "Categoria": np.random.choice(categorias, size=200, p=[0.5, 0.3, 0.2]),
    "Valor": np.random.randint(1, 10, size=200)
}

df = pd.DataFrame(data)

# 2. Procesamiento de datos (Agrupación por fecha y categoría)
df_agrupado = df.groupby(["Fecha", "Categoria"]).sum().reset_index()

# 3. Creación del gráfico interactivo con Plotly
fig = px.line(
    df_agrupado,
    x="Fecha",
    y="Valor",
    color="Categoria",
    title="<b>Tendencia de Registros por Categoría</b>",
    labels={"Valor": "Total de Registros", "Fecha": "Fecha de Registro"},
    template="plotly_white"
)

# 4. Guardar gráfico como archivo HTML para visualización web
fig.write_html("scripts/grafico_tendencia.html")
print("✅ Análisis exploratorio completado. Se generó 'scripts/grafico_tendencia.html'")
