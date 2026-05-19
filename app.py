import streamlit as st
import pandas as pd
import numpy as np

st.set_page_config(
    page_title="Telco Churn Analytics - Dashboard",
    page_icon="",
    layout="wide"
)

if "df_churn" not in st.session_state:
    st.session_state.df_churn = None

with st.sidebar:
    st.title("Telco Churn Analytics")
    st.markdown("### Navegacion de la Suite")
    seccion = st.sidebar.selectbox(
        "Seleccione un Modulo:",
        [
            "Modulo 1: Home",
            "Modulo 2: Carga de Datos",
            "Modulo 3: Analisis Exploratorio (EDA)",
            "Modulo 4: Gestion de Reportes (POO)"
        ]
    )
    st.divider()
    st.caption("Especializacion: Python for Analytics")
    st.caption("Edicion: 57")
    st.caption("Anio: 2026")

# ==========================================
# MODULO 1: HOME 
# ==========================================
if seccion == "Modulo 1: Home":
    st.title("Telecom Customer Churn Analytics: Strategic Retention Dashboard")
    st.divider()

    col_img, col_info = st.columns([1, 2])
    
    with col_img:
        try:
            st.image("logo_lopez.png", use_container_width=True)
        except:
            st.warning("Archivo logo_lopez.png no detectado en el directorio raiz")

    with col_info:
        st.header("Objetivo del Analisis")
        st.write("""
        El proposito de este producto analitico es examinar y diagnosticar la perdida de clientes 
        (Churn) mediante la identificacion de patrones criticos en el comportamiento del consumidor. 
        A traves de tecnicas avanzadas de limpieza, transformacion y visualizacion de datos, la plataforma 
        descubre las variables demograficas, financieras y de servicio que impactan directamente 
        en la retencion de ingresos dentro del sector de telecomunicaciones.
        """)
        
    st.divider()
    col_det, col_autor = st.columns([2, 1])
    
    with col_det:
        st.subheader("Estructura del Dataset (TelcoCustomerChurn)")
        st.write("""
        La informacion analizada comprende un registro consolidado de **7,043 clientes** que detalla:
        * **Atributos Demograficos:** Genero, estado civil, dependientes y condicion de adulto mayor.
        * **Servicios Contratados:** Telefonia, multiples lineas, tipo de internet, seguridad digital, soporte tecnico y streaming.
        * **Ficha Financiera y Comercial:** Tipo de contrato, facturacion electronica, metodo de pago, cargos mensuales y cargos totales acumulados.
        """)

    with col_autor:
        with st.container(border=True):
            st.header("Ficha del Autor")
            st.write(f"**Nombre Completo:** Bill Giner Lopez Milla")
            st.write(f"**Curso:** Especializacion en Python for Analytics")
            st.write(f"**Edicion:** Clase 57")
            st.write(f"**Anio de Desarrollo:** 2026")
            st.write(f"**Estado del Dashboard:** Desplegado (Stable)")

    st.divider()
    st.header("Infraestructura Tecnologica del Sistema")
    
    t1, t2, t3, t4 = st.columns(4)
    with t1: st.info("##### Core Engine\nPython 3.x\nf-strings & POO")
    with t2: st.success("##### Data Wrangling\nPandas Framework\nNumPy Arrays")
    with t3: st.warning("##### Data Viz\nMatplotlib\nSeaborn Graphics")
    with t4: st.error("##### Deployment\nStreamlit Architecture\nCloud Infrastructure")

    st.divider()
    st.markdown("##### Nota de Orientacion")
    st.caption("Para iniciar el diagnostico, dirijase al menu lateral y seleccione el **Modulo 2: Carga de Datos** para procesar la matriz de informacion inicial.")

# ==========================================
# MODULO 2: CARGA DE DATOS
# ==========================================
elif seccion == "Modulo 2: Carga de Datos":
    st.title("Ingesta y Preparacion Estructural de Datos")
    st.divider()
    
    st.write("""
    Este modulo maneja la carga del archivo plano y aplica las transformaciones iniciales de ingenieria de datos. 
    Detecta de forma automatica anomalias en la tipificacion de columnas y realiza la coercion de variables string 
    hacia formatos cuantitativos esenciales para el analisis descriptivo.
    """)

    archivo_subido = st.file_uploader("Seleccione el archivo TelcoCustomerChurn.csv", type=["csv"])

    if archivo_subido is not None:
        if st.session_state.df_churn is None:
            df_crudo = pd.read_csv(archivo_subido)
            df_crudo['TotalCharges'] = pd.to_numeric(df_crudo['TotalCharges'], errors='coerce')
            df_crudo['TotalCharges'] = df_crudo['TotalCharges'].fillna(0.0)
            df_crudo['SeniorCitizen'] = df_crudo['SeniorCitizen'].map({1: 'Yes', 0: 'No'})
            st.session_state.df_churn = df_crudo
            st.toast("Dataset cargado y procesado con exito", icon="")

        df = st.session_state.df_churn
        st.success("?Estructura de datos lista para el analisis!")

        st.subheader("Indicadores Estructurales del Dataset")
        m_col1, m_col2, m_col3, m_col4 = st.columns(4)
        
        total_filas = df.shape[0]
        total_columnas = df.shape[1]
        tasa_fuga = (df['Churn'] == 'Yes').mean() * 100
        total_ingreso_mensual = df['MonthlyCharges'].sum()

        m_col1.metric("Total Observaciones (Filas)", f"{total_filas:,}")
        m_col2.metric("Total Atributos (Columnas)", total_columnas)
        m_col3.metric("Tasa General de Churn", f"{tasa_fuga:.2f}%")
        m_col4.metric("Facturacion Mensual Total", f"$ {total_ingreso_mensual:,.2f}")

        st.divider()

        st.subheader("Muestra Analitica de los Datos")
        num_filas = st.slider("Seleccione el numero de filas a visualizar en la muestra:", min_value=5, max_value=50, value=5, step=5)
        st.dataframe(df.head(num_filas), use_container_width=True, hide_index=True)

        st.divider()
        st.subheader("Verificacion Tecnica de Variables")
        
        col_tipo1, col_tipo2 = st.columns(2)
        
        with col_tipo1:
            st.write("##### Conteo de Variables por Tipo")
            resumen_tipos = df.dtypes.value_counts().reset_index()
            resumen_tipos.columns = ["Tipo de Dato en Python", "Cantidad de Columnas"]
            st.dataframe(resumen_tipos, use_container_width=True, hide_index=True)
            
        with col_tipo2:
            st.write("##### Validacion de Valores Nulos Detectados")
            conteo_nulos = df.isnull().sum().reset_index()
            conteo_nulos.columns = ["Nombre de Variable", "Valores Nulos (NaN)"]
            variables_criticas = conteo_nulos[conteo_nulos["Nombre de Variable"].isin(["tenure", "MonthlyCharges", "TotalCharges"])]
            st.dataframe(variables_criticas, use_container_width=True, hide_index=True)

    else:
        st.info("Por favor, cargue el archivo del caso de estudio (TelcoCustomerChurn.csv) para activar las herramientas de diagnostico.")