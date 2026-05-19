import streamlit as st
import pandas as pd
import numpy as np

# 1. CONFIGURACION DE LA SUITE ANALITICA
st.set_page_config(
    page_title="Telco Churn Analytics - Dashboard",
    page_icon="",
    layout="wide"
)

# 2. SISTEMA DE PERSISTENCIA (SESSION STATE)
if "df_churn" not in st.session_state:
    st.session_state.df_churn = None

# 3. PANEL DE CONTROL LATERAL (SIDEBAR)
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

    # Layout Principal del Home: Contextualizacion y Ficha Tecnica
    col_info, col_autor = st.columns([2, 1])

    with col_info:
        st.header("Objetivo del Analisis")
        st.write("""
        El proposito de este producto analitico es examinar y diagnosticar la perdida de clientes 
        (Churn) mediante la identificacion de patrones criticos en el comportamiento del consumidor. 
        A traves de tecnicas avanzadas de limpieza, transformacion y visualizacion de datos, la plataforma 
        descubre las variables demograficas, financieras y de servicio que impactan directamente 
        en la retencion de ingresos dentro del sector de telecomunicaciones.
        """)
        
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

    # Tecnologias Utilizadas (Implementando f-strings y visual llamativo)
    st.header("Infraestructura Tecnologica del Sistema")
    
    t1, t2, t3, t4 = st.columns(4)
    with t1:
        st.info("##### Core Engine\nPython 3.x\nf-strings & POO")
    with t2:
        st.success("##### Data Wrangling\nPandas Framework\nNumPy Arrays")
    with t3:
        st.warning("##### Data Viz\nMatplotlib\nSeaborn Graphics")
    with t4:
        st.error("##### Deployment\nStreamlit Architecture\nCloud Infrastructure")

    st.divider()
    st.markdown("##### Nota de Orientacion")
    st.caption("Para iniciar el diagnostico, dirijase al menu lateral y seleccione el **Modulo 2: Carga de Datos** para procesar la matriz de informacion inicial.")