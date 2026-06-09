import streamlit as st
import pandas as pd

st.markdown(
    """
    <h1 style="
        color: gold; 
        text-align: center;
        text-shadow: 2px 2px 4px rgba(0, 0, 0, 0.8);
        -webkit-text-stroke: 1px black;
        background: white;
        margin-bottom: 20px;
        border-radius: 50px">
        Separador de Processos
    </h1>
    """,
    unsafe_allow_html=True
)

# Dividindo a página em três colunas e centralizando a imagem na coluna do meio
col1, col2, col3 = st.columns([1, 3, 1])  # Ajuste os valores para modificar o posicionamento
with col2:
    st.image(
        "/Volumes/Projects/Github/python_studies/separador_de_processos/Assets/logotj.png",
        use_container_width=True  # Faz a imagem ajustar à largura da coluna
    )

# Centralizando o título "Selecione a planilha"
st.markdown(
    """
    <h3 style="text-align: center; font-size: 22px;">
        Carregue a sua Planilha Abaixo:
    </h3>
    """,
    unsafe_allow_html=True
)

# Campo para digitar o nome
nome = st.text_input("Digite o Nome do Colaborador")

# Campo para digitar um dígito
digito = st.number_input("Digite o dígito do Processo", min_value=0, max_value=9)

# Adicionando o file uploader
file = st.file_uploader("Carregue o arquivo:", type=["xls"])

if file:
    # Carregar o arquivo Excel
    df = pd.read_excel(file)

    # Verificar se a coluna 'Processo' existe
    if "Processo" in df.columns:
        # Filtrando os processos com base no dígito
        filtrado = df[df["Processo"].astype(str).str[6] == str(digito)]

        # Se algum processo for filtrado, salvar o arquivo
        if not filtrado.empty:
            output_file = f"/Volumes/Projects/Github/python_studies/separador_de_processos/Processos_filtrados_{nome}_Processos_Digito-{digito}.xlsx"
            filtrado.to_excel(output_file, index=False)

            st.success(f"Os processos filtrados foram salvos em: {output_file}")
        else:
            st.warning("Nenhum processo encontrado com o dígito fornecido.")
    else:
        st.error("A coluna 'Processo' não foi encontrada na planilha.")
