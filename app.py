import streamlit as st
import pandas as pd

# Configuración de la página
st.set_page_config(page_title="Seguimiento de Proyectos", layout="wide")

# Cargar datos de un archivo CSV o iniciar un DataFrame vacío
try:
    df = pd.read_csv('seguimiento_proyectos.csv')
except FileNotFoundError:
    df = pd.DataFrame(columns=[
        "ID del Proyecto", "Nombre del Proyecto", "Cliente", "Responsable Principal",
        "Fecha de Inicio", "Fecha de Entrega", "Estado", "Fase Actual", "Prioridad",
        "Avance (%)", "Comentarios", "Equipo Involucrado", "Horas Asignadas", "Horas Utilizadas"
    ])

# Título de la aplicación
st.title("Panel de Seguimiento de Proyectos")

# Formulario para agregar un nuevo proyecto
with st.form("Agregar Proyecto"):
    st.subheader("Agregar un nuevo proyecto")
    id_proyecto = st.text_input("ID del Proyecto")
    nombre_proyecto = st.text_input("Nombre del Proyecto")
    cliente = st.text_input("Cliente")
    responsable = st.text_input("Responsable Principal")
    fecha_inicio = st.date_input("Fecha de Inicio")
    fecha_entrega = st.date_input("Fecha de Entrega")
    estado = st.selectbox("Estado", ["En Progreso", "Completado", "Pendiente"])
    fase = st.text_input("Fase Actual")
    prioridad = st.selectbox("Prioridad", ["Alta", "Media", "Baja"])
    avance = st.slider("Avance (%)", 0, 100, 0)
    comentarios = st.text_area("Comentarios")
    equipo = st.text_input("Equipo Involucrado")
    horas_asignadas = st.number_input("Horas Asignadas", min_value=0)
    horas_utilizadas = st.number_input("Horas Utilizadas", min_value=0)

    # Botón para agregar el proyecto
    submit = st.form_submit_button("Agregar Proyecto")

    if submit:
        nuevo_proyecto = {
            "ID del Proyecto": id_proyecto,
            "Nombre del Proyecto": nombre_proyecto,
            "Cliente": cliente,
            "Responsable Principal": responsable,
            "Fecha de Inicio": fecha_inicio,
            "Fecha de Entrega": fecha_entrega,
            "Estado": estado,
            "Fase Actual": fase,
            "Prioridad": prioridad,
            "Avance (%)": avance,
            "Comentarios": comentarios,
            "Equipo Involucrado": equipo,
            "Horas Asignadas": horas_asignadas,
            "Horas Utilizadas": horas_utilizadas
        }
        df = df.append(nuevo_proyecto, ignore_index=True)
        df.to_csv('seguimiento_proyectos.csv', index=False)
        st.success("Proyecto agregado con éxito")

# Visualización de proyectos existentes
st.subheader("Proyectos en seguimiento")
st.dataframe(df)

# Gráfico de avance de proyectos
st.subheader("Avance de proyectos")
st.bar_chart(df.set_index("Nombre del Proyecto")["Avance (%)"])
