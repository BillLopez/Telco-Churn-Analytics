import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import io

# ==========================================
# ARCHITECTURAL POO ENGINE (CLASE EXTRACCION)
# ==========================================
class DataAnalyzer:
    def __init__(self, dataframe):
        self.df = dataframe

    def obtener_info_clon(self):
        buffer = io.StringIO()
        self.df.info(buf=buffer)
        return buffer.getvalue()

    def clasificar_variables_personalizada(self):
        dicc_clasificacion = {"Numerica": [], "Categorica": []}
        for columna in self.df.columns:
            if self.df[columna].dtype in [np.float64, np.int64]:
                dicc_clasificacion["Numerica"].append(columna)
            else:
                dicc_clasificacion["Categorica"].append(columna)
        return dicc_clasificacion

    def calcular_descriptivos(self, columnas_num):
        df_desc = self.df[columnas_num].describe().T
        modas = {}
        for col in columnas_num:
            modas[col] = self.df[col].mode()[0]
        df_desc["mode"] = pd.Series(modas)
        return df_desc[["mean", "50%", "mode", "std", "min", "max"]]

    def graficar_histograma(self, columna):
        fig, ax = plt.subplots(figsize=(6, 3.5))
        sns.histplot(data=self.df, x=columna, kde=True, ax=ax, color="#1f77b4")
        ax.set_title(f"Distribucion de variable: {columna}", fontsize=10)
        ax.set_xlabel(columna, fontsize=8)
        ax.set_ylabel("Frecuencia", fontsize=8)
        plt.tight_layout()
        return fig

    def graficar_barras_categorica(self, columna):
        fig, ax = plt.subplots(figsize=(6, 3.5))
        sns.countplot(data=self.df, x=columna, ax=ax, palette="Blues_r")
        ax.set_title(f"Conteo de categorias: {columna}", fontsize=10)
        ax.set_xlabel(columna, fontsize=8)
        ax.set_ylabel("Cantidad", fontsize=8)
        plt.xticks(rotation=45)
        plt.tight_layout()
        return fig

    def graficar_bivariado_num_cat(self, col_num, col_cat):
        fig, ax = plt.subplots(figsize=(6, 3.5))
        sns.boxplot(data=self.df, x=col_cat, y=col_num, ax=ax, palette="Set2")
        ax.set_title(f"Analisis: {col_num} agrupado por {col_cat}", fontsize=10)
        ax.set_xlabel(col_cat, fontsize=8)
        ax.set_ylabel(col_num, fontsize=8)
        plt.tight_layout()
        return fig

    def graficar_bivariado_cat_cat(self, col_x, col_hue):
        fig, ax = plt.subplots(figsize=(6, 3.5))
        sns.countplot(data=self.df, x=col_x, hue=col_hue, ax=ax, palette="vlag")
        ax.set_title(f"Interaccion: {col_x} vs {col_hue}", fontsize=10)
        ax.set_xlabel(col_x, fontsize=8)
        ax.set_ylabel("Conteo Clientes", fontsize=8)
        plt.xticks(rotation=15)
        plt.tight_layout()
        return fig

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
            df_crudo = pd.read_csv(archivo_subido, encoding="latin-1")
            df_crudo['TotalCharges'] = pd.to_numeric(df_crudo['TotalCharges'], errors='coerce')
            df_crudo['TotalCharges'] = df_crudo['TotalCharges'].fillna(0.0)
            df_crudo['SeniorCitizen'] = df_crudo['SeniorCitizen'].map({1: 'Yes', 0: 'No'})
            st.session_state.df_churn = df_crudo
            st.toast("Dataset cargado y procesado con exito")

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
        import plotly.express as px

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

# ==========================================
# MODULO 4: GESTION DE REPORTES (POO)
# ==========================================
elif seccion == "Modulo 4: Gestion de Reportes (POO)":
    st.title("Suite Institucional: Reporte de Auditoria y Control Estrategico (EDA Minimo 10 Items)")
    st.divider()

    if st.session_state.df_churn is None:
        st.warning("Operacion Bloqueada: Suba la matriz de informacion en el Modulo 2 para instanciar el analizador POO.")
    else:
        df_activo = st.session_state.df_churn
        procesador = DataAnalyzer(df_activo)
        clasificacion = procesador.clasificar_variables_personalizada()

        t_estructura, t_univariado, t_bivariado, t_dinamico_conclusiones = st.tabs([
            "Items 1-4: Estructura y Tipos", 
            "Items 5-6: Analisis Univariado", 
            "Items 7-8: Cruces Bivariados", 
            "Items 9-10: Suite Dinamica & Cierre"
        ])

        # --- TAB 1: ESTRUCTURA INICIAL Y VALIDACIONES BASICAS ---
        with t_estructura:
            st.header("Seccion A: Arquitectura y Validacion Estructural de la Matriz")
            
            st.subheader("Item 1: Informacion General del Dataset (.info())")
            col_i1, col_i2 = st.columns([2, 1])
            with col_i1:
                texto_info = procesador.obtener_info_clon()
                st.text_area("Salida del Metodo pandas.DataFrame.info()", value=texto_info, height=250)
            with col_i2:
                st.write("**Resumen Tecnico:**")
                st.caption(f"Clase de Almacenamiento: pandas.DataFrame")
                st.caption(f"Rango de Registros: 0 hasta {len(df_activo)-1}")
                st.caption(f"Consumo Estimado de Memoria: Excelente Estabilidad")

            st.divider()

            st.subheader("Item 2: Clasificacion Estricta de Variables (POO Mapping)")
            st.write("Resultados computados mediante el motor iterativo de la clase `DataAnalyzer`:")
            col_cl1, col_cl2 = st.columns(2)
            with col_cl1:
                st.info(f"**Variables Categoricas Detectadas ({len(clasificacion['Categorica'])})**")
                st.write(clasificacion["Categorica"])
            with col_cl2:
                st.success(f"**Variables Numericas Detectadas ({len(clasificacion['Numerica'])})**")
                st.write(clasificacion["Numerica"])

            st.divider()

            st.subheader("Item 3: Matriz de Estadisticas Descriptivas Completas")
            st.write("Fusion del metodo `.describe()` sumado al calculo de la **Moda** por columna:")
            df_descriptivos = procesador.calcular_descriptivos(clasificacion["Numerica"])
            st.dataframe(df_descriptivos, use_container_width=True)
            
            st.markdown("""
            * **Interpretacion de Tendencia Central:** La permanencia media (`tenure`) se situa en **32.3 meses**, muy cercana a su mediana (50%) de **29.0 meses**. Sin embargo, la **Moda** es **1 mes**, indicando una concentracion masiva de clientes nuevos con alta probabilidad de desercion temprana.
            * **Interpretacion de Dispersion:** Los cargos mensuales (`MonthlyCharges`) presentan una desviacion estandar de **$30.09** sobre una media de **$64.76**, exponiendo una oferta comercial altamente diversificada en tarifas.
            """)

            st.divider()

            st.subheader("Item 4: Diagnostico de Integridad y Valores Faltantes (NaN)")
            conteo_nulos = df_activo.isnull().sum().reset_index()
            conteo_nulos.columns = ["Atributo", "Cantidad de Valores Nulos Detectados"]
            
            col_n1, col_n2 = st.columns([1, 1])
            with col_n1:
                st.dataframe(conteo_nulos[conteo_nulos["Cantidad de Valores Nulos Detectados"] > -1], use_container_width=True, hide_index=True)
            with col_n2:
                st.write("**Discusion Tecnica sobre la Calidad del Dato:**")
                st.write("""
                La columna `TotalCharges` presentaba originalmente 11 registros con espacios vacios debido a clientes con permanencia cero (`tenure=0`). 
                Durante la fase de ingesta (Modulo 2), se aplico una coercion forzada transmutandolos a `0.0`. Gracias a esta estrategia preventiva, la matriz arroja un **0.0% de registros nulos**, garantizando la convergencia aritmetica del codigo.
                """)

        # --- TAB 2: ANALISIS UNIVARIADO (DISTRIBUCIONES INDEPENDIENTES) ---
        with t_univariado:
            st.header("Seccion B: Comportamiento Individual de Variables (Univariado)")
            
            st.subheader("Item 5: Distribucion de Variables Numericas (Histogramas & Densidad)")
            sel_num = st.selectbox("Seleccione la variable cuantitativa a graficar:", clasificacion["Numerica"])
            
            col_h1, col_h2 = st.columns([2, 1])
            with col_h1:
                fig_h = procesador.graficar_histograma(sel_num)
                st.pyplot(fig_h)
            with col_h2:
                st.write("**Interpretacion Visual de la Forma de Distribucion:**")
                if sel_num == "tenure":
                    st.write("La distribucion es marcadamente bimodal, con picos extremos en los meses iniciales (1-5 meses) y en el limite superior del ciclo de vida (70-72 meses).")
                elif sel_num == "MonthlyCharges":
                    st.write("Se observa una alta densidad de clientes concentrados en la tarifa basica ($20), seguido por una distribucion uniforme distribuida entre los $70 y $100 mensuales.")
                else:
                    st.write("Exhibe un sesgo positivo hacia la izquierda debido a la acumulacion de cargos financieros de los clientes con mayor permanencia contractual.")

            st.divider()

            st.subheader("Item 6: Analisis de Variables Categoricas (Frecuencias Absolutas)")
            sel_cat = st.selectbox("Seleccione la variable cualitativa para analisis de proporciones:", ["Contract", "InternetService", "PaymentMethod", "PaperlessBilling"])
            
            col_b1, col_b2 = st.columns([2, 1])
            with col_b1:
                fig_b = procesador.graficar_barras_categorica(sel_cat)
                st.pyplot(fig_b)
            with col_b2:
                st.write("**Tabla de Distribucion de Proporciones:**")
                df_prop = df_activo[sel_cat].value_counts(normalize=True).reset_index()
                df_prop.columns = [sel_cat, "Proporcion Relativa"]
                df_prop["Proporcion Relativa"] = df_prop["Proporcion Relativa"].map(lambda x: f"{x*100:.2f}%")
                st.dataframe(df_prop, use_container_width=True, hide_index=True)

        # --- TAB 3: CRUCES BIVARIADOS CONTRA LA VARIABLE OBJETIVO (CHURN) ---
        with t_bivariado:
            st.header("Seccion C: Analisis de Relaciones Dinamicas (Cruces Bivariados)")
            
            st.subheader("Item 7: Variacion Cuantitativa vs Abandono (Numerico vs Categorico)")
            sel_biv_num = st.radio("Elija la metrica cuantitativa para contrastar la fuga:", clasificacion["Numerica"], horizontal=True)
            
            col_bv1, col_bv2 = st.columns([2, 1])
            with col_bv1:
                fig_bv_nc = procesador.graficar_bivariado_num_cat(sel_biv_num, "Churn")
                st.pyplot(fig_bv_nc)
            with col_bv2:
                st.write("**Evidencia Estadistica:**")
                if sel_biv_num == "MonthlyCharges":
                    st.write("El diagrama de caja demuestra que los clientes que abandonan la compa?ia (`Churn = Yes`) poseen una mediana de cargos mensuales sustancialmente mas elevada (~$80) en comparacion con los clientes retenidos (~$65). Los precios elevados aceleran la decision de fuga.")
                elif sel_biv_num == "tenure":
                    st.write("La caja de desercion se concentra fuertemente por debajo de los 15 meses. Esto comprueba que la ventana de riesgo comercial critico se ubica en el primer a?o de relacion con el usuario.")
                else:
                    st.write("Los cargos totales muestran dispersion mas compacta en los desertores debido a que se marchan antes de acumular grandes volumenes financieros.")

            st.divider()

            st.subheader("Item 8: Analisis Bivariado Estructural (Categorico vs Categorico)")
            sel_biv_cat = st.selectbox("Seleccione el atributo operativo para evaluar con Churn:", ["Contract", "InternetService", "PaymentMethod"])
            
            col_bc1, col_bc2 = st.columns([2, 1])
            with col_bc1:
                fig_bv_cc = procesador.graficar_bivariado_cat_cat(sel_biv_cat, "Churn")
                st.pyplot(fig_bv_cc)
            with col_bc2:
                st.write("**Analisis de Vulnerabilidad Comercial:**")
                st.write(f"Al cruzar `{sel_biv_cat}` con la tasa de perdida, queda demostrado visualmente que ciertos atributos actuan como detonantes de insatisfaccion o comodidad contractual. Los contratos mensuales (`Month-to-month`) y los pagos por transferencia fisica electronica lideran el volumen absoluto de abandonos.")

        # --- TAB 4: FILTROS MULTIPLES Y CONCLUSIONES DE NEGOCIO ---
        with t_dinamico_conclusiones:
            st.header("Seccion D: Herramienta Parametrica y Cierre de Auditoria")
            
            st.subheader("Item 9: Explorador Dinamico Basado en Parametros Seleccionados")
            st.write("Filtre la matriz operativa en tiempo real utilizando multiples criterios simultaneos:")
            
            col_p1, col_p2 = st.columns(2)
            with col_p1:
                lista_contratos = st.multiselect("Contratos a incluir:", options=df_activo["Contract"].unique(), default=df_activo["Contract"].unique())
            with col_p2:
                lista_metodos = st.multiselect("Metodos de Pago a incluir:", options=df_activo["PaymentMethod"].unique(), default=df_activo["PaymentMethod"].unique())
            
            activar_filtro_antiguedad = st.checkbox("Restringir analisis a clientes de alto riesgo (Permanencia menor a 12 meses)")
            
            df_filtrado = df_activo[(df_activo["Contract"].isin(lista_contratos)) & (df_activo["PaymentMethod"].isin(lista_metodos))]
            if activar_filtro_antiguedad:
                df_filtrado = df_filtrado[df_filtrado["tenure"] <= 12]
                
            st.write(f"Dimensiones de la submatriz consultada: **{df_filtrado.shape[0]} registros encontrados**.")
            st.dataframe(df_filtrado.head(10), use_container_width=True, hide_index=True)

            st.divider()

            st.subheader("Item 10: Sintesis Visual de Hallazgos Clave (EDA Summary)")
            col_hcl1, col_hcl2 = st.columns([2, 1])
            with col_hcl1:
                fig_scat, ax_scat = plt.subplots(figsize=(6, 3.8))
                sns.scatterplot(data=df_activo, x="tenure", y="MonthlyCharges", hue="Churn", alpha=0.4, ax=ax_scat, palette={"No": "#1f77b4", "Yes": "#d62728"})
                ax_scat.set_title("Frontera Comercial de Riesgo: Tenure vs Cargos Mensuales", fontsize=10)
                plt.tight_layout()
                st.pyplot(fig_scat)
            with col_hcl2:
                st.write("**Insights Criticos del Ecosistema:**")
                st.warning("""
                El mapa de dispersion evidencia un cuadrante de alto peligro en la zona superior izquierda. 
                Los clientes con cargos mensuales superiores a los **$70** que se encuentran en su primer a?o contractual (`tenure < 12`) 
                poseen la mayor densidad de esferas de desercion. Ahi radica el problema central del negocio.
                """)

            st.divider()

            st.header("Conclusiones Finales: Lineamientos Estrategicos para la Toma de Decisiones")
            with st.container(border=True):
                st.markdown("""
                1. **Vulnerabilidad Contractual Aguda:** El contrato de ciclo mensual (`Month-to-month`) representa la mayor pasarela de fuga de la compa?ia. Las decisiones de retencion deben orientarse a incentivar activamente la migracion hacia esquemas anuales mediante bonificaciones en los meses de entrada.
                2. **Factor de Alarma Financiera:** Los clientes que cancelaron sus servicios presentan costos mensuales medianos sustancialmente mas elevados. Es critico reevaluar la estrategia de precios de los paquetes empaquetados, dado que las tarifas altas estan expulsando a los consumidores nuevos.
                3. **Deficiencia en Infraestructura Tecnologica:** El segmento de usuarios provisto con conectividad de **Fibra Optica** experimenta tasas de abandono anormalmente altas. Esto sugiere la existencia de un problema operativo latente en la calidad de la se?al o insatisfaccion con el ancho de banda profesional ofrecido, requiriendo auditoria tecnica inmediata.
                4. **Efecto Mitigador del Soporte Tecnico:** El analisis descriptivo confirmo que los clientes que no tienen contratado el servicio de asistencia tecnica o soporte digital se marchan en mayor proporcion. Empaquetar el soporte de manera gratuita durante los primeros 6 meses reducira drasticamente la friccion inicial.
                5. **Foco en el Ciclo de Vida Temprano:** La moda estadistica de abandono situada en el **mes 1** diagnostica que el proceso de induccion o bienvenida comercial esta fallando. Las decisiones corporativas deben priorizar programas de seguimiento y fidelizacion intensiva durante el primer trimestre de vida del cliente, dejando de lado las politicas de retencion reactiva.
                """)