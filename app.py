import streamlit as st
from service.blob_service import upload_blob
from service.credit_card_service import analyze_credit_card

def configure_interface():
    st.title("Upload de Arquivo DIO - Desafio 1 - Azure - Fake Docs")

    uploaded_file = st.file_uploader(
        "Escolha um arquivo para upload",
        type=["pdf", "png", "jpg", "jpeg"]
    )

    if uploaded_file is not None:
        filename = uploaded_file.name

        blob_url = upload_blob(uploaded_file, filename)

        if blob_url:
            st.success(f"Arquivo {filename} enviado com sucesso!")
            credit_card_info = analyze_credit_card(blob_url)
            show_image_and_validation(blob_url, credit_card_info)
        else:
            st.error("Erro ao enviar o arquivo.")

def show_image_and_validation(blob_url, credit_card_info):
    st.image(blob_url, caption="Imagem enviada", use_column_width=True)
    st.write("Resultado da Validação:")

    if credit_card_info and credit_card_info.get("card_name"):
        st.markdown("<h1 style='color:green;'>Cartão Válido</h1>", unsafe_allow_html=True)
        st.write(f"Nome do Titular: {credit_card_info['card_name']}")
        st.write(f"Banco Emissor: {credit_card_info['bank_name']}")
        st.write(f"Data de Validade: {credit_card_info['expiry_date']}")
    else:
        st.markdown("<h1 style='color:red;'>Cartão Inválido</h1>", unsafe_allow_html=True)
configure_interface()
