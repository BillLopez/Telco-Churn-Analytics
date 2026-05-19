import streamlit as st
import pandas as pd
import numpy as np
import plotly.express as px

# ==========================================
# CONFIGURACION DE LA SUITE ANALITICA
# ==========================================
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
            st.toast("Dataset cargado y processedo con exito")

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

# ==========================================
# MODULO 3: ANALISIS EXPLORATORIO (EDA)
# ==========================================
elif seccion == "Modulo 3: Analisis Exploratorio (EDA)":
    st.title("Analisis Exploratorio de Datos (EDA) Interactivo")
    st.divider()

    if st.session_state.df_churn is None:
        st.warning("Por favor, vaya primero al Modulo 2: Carga de Datos y suba el archivo CSV para activar los analisis visuales.")
    
    else:
        df = st.session_state.df_churn

        st.write("""
        Bienvenido al nucleo analitico del sistema. Explore las diferentes dimensiones operativas y 
        financieras de la compa?ia para identificar que perfiles de clientes presentan la mayor tasa 
        de cancelacion de servicios.
        """)

        tab_general, tab_servicios, tab_financiero = st.tabs([
            "Distribucion General", 
            "Analisis de Servicios", 
            "Comportamiento Financiero"
        ])

        with tab_general:
            st.subheader("Perfil de Abandono General y Demografico")
            
            col_gen1, col_gen2 = st.columns(2)
            
            with col_gen1:
                st.write("##### Proporcion General de Fuga (Churn)")
                df_churn_cnt = df["Churn"].value_counts().reset_index()
                df_churn_cnt.columns = ["Estado", "Total"]
                
                fig_pie = px.pie(
                    df_churn_cnt, 
                    names="Estado", 
                    values="Total",
                    color="Estado",
                    color_discrete_map={"No": "#1f77b4", "Yes": "#d62728"},
                    hole=0.4
                )
                fig_pie.update_layout(margin=dict(l=20, r=20, t=20, b=20), height=300)
                st.plotly_chart(fig_pie, use_container_width=True)
                
            with col_gen2:
                st.write("##### Tasa de Fuga Segun Tipo de Contrato")
                df_contract = df.groupby(["Contract", "Churn"]).size().reset_index(name="Clientes")
                
                fig_contract = px.bar(
                    df_contract, 
                    x="Contract", 
                    y="Clientes", 
                    color="Churn",
                    barmode="group",
                    color_discrete_map={"No": "#1f77b4", "Yes": "#d62728"},
                    labels={"Contract": "Tipo de Contrato", "Clientes": "Numero de Clientes"}
                )
                fig_contract.update_layout(margin=dict(l=20, r=20, t=20, b=20), height=300)
                st.plotly_chart(fig_contract, use_container_width=True)

            st.divider()
            st.write("##### Factores Demograficos Relacionados al Churn")
            var_demo = st.selectbox("Seleccione una variable demografica para cruzar con Churn:", ["SeniorCitizen", "Partner", "Dependents", "gender"])
            
            df_demo_grp = df.groupby([var_demo, "Churn"]).size().reset_index(name="Conteo")
            fig_demo = px.bar(
                df_demo_grp,
                x=var_demo,
                y="Conteo",
                color="Churn",
                barmode="stack",
                color_discrete_map={"No": "#1f77b4", "Yes": "#d62728"}
            )
            fig_demo.update_layout(height=350)
            st.plotly_chart(fig_demo, use_container_width=True)

        with tab_servicios:
            st.subheader("Impacto de la Oferta Comercial y Conectividad")
            
            col_serv1, col_serv2 = st.columns(2)
            
            with col_serv1:
                st.write("##### Riesgo por Tipo de Servicio de Internet")
                df_internet = df.groupby(["InternetService", "Churn"]).size().reset_index(name="Total")
                fig_net = px.bar(
                    df_internet,
                    y="InternetService",
                    x="Total",
                    color="Churn",
                    orientation="h",
                    barmode="group",
                    color_discrete_map={"No": "#1f77b4", "Yes": "#d62728"},
                    labels={"InternetService": "Tecnologia", "Total": "Clientes registrados"}
                )
                fig_net.update_layout(margin=dict(l=20, r=20, t=20, b=20), height=300)
                st.plotly_chart(fig_net, use_container_width=True)
                
            with col_serv2:
                st.write("##### Impacto del Soporte Tecnico (TechSupport)")
                df_support = df.groupby(["TechSupport", "Churn"]).size().reset_index(name="Total")
                fig_sup = px.bar(
                    df_support,
                    x="TechSupport",
                    y="Total",
                    color="Churn",
                    barmode="group",
                    color_discrete_map={"No": "#1f77b4", "Yes": "#d62728"}
                )
                fig_sup.update_layout(margin=dict(l=20, r=20, t=20, b=20), height=300)
                st.plotly_chart(fig_sup, use_container_width=True)

            st.write("""
            **Insight Comercial Detectado:** Los clientes que cuentan con servicio de Internet por Fibra Optica y aquellos que No tienen Soporte Tecnico contratado muestran proporciones de desercion significativamente mas elevadas en comparacion con el promedio del portafolio.
            """)

        with tab_financiero:
            st.subheader("Analisis Estadistico de Cargos y Permanencia")
            
            metric_fin = st.radio(
                "Seleccione la metrica financiera cuantitativa a evaluar (Histograma de Densidad):",
                ["MonthlyCharges", "TotalCharges", "tenure"],
                horizontal=True
            )
            
            fig_hist = px.histogram(
                df,
                x=metric_fin,
                color="Churn",
                marginal="box",
                barmode="overlay",
                color_discrete_map={"No": "#1f77b4", "Yes": "#d62728"},
                labels={"MonthlyCharges": "Cargos Mensuales ($)", "TotalCharges": "Cargos Totales ($)", "tenure": "Meses de Permanencia (Tenure)"}
            )
            fig_hist.update_layout(height=450, yaxis_title="Densidad de Observaciones")
            st.plotly_chart(fig_hist, use_container_width=True)
            
            st.write("##### Resumen Estadistico Descriptivo Matriz Financiera (Pandas describe)")
            st.dataframe(
                df[["tenure", "MonthlyCharges", "TotalCharges"]].describe().T, 
                use_container_width=True
            )