import streamlit as st
import openai

st.set_page_config(
    page_title="Harmoneasy",
    page_icon='🍷',
    layout='centered',  # Define o layout como centralizado
    initial_sidebar_state='collapsed',  # Define a barra lateral como fechada por padrão
    menu_items={
        'Get Help': 'https://wa.me/5554981690961',
        'Report a bug': "https://wa.me/5554981690961",
        'About': "# MVP HARMONEASY"
    }
)

openai.api_key = st.secrets["API_KEY"]


def generate_response(user_input):
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[{"role": "user",
                   "content": f'Responda como um sommelier profissional falando com alguém leigo (Use emojis na resposta ao cliente). Mas seja bem culto e dê uma resposta detalhada, gerando curiosidade no cliente. Se possível, vinhos mais comuns. Ah, lembre-se de dar uma resposta concisa{user_input}.'}]
    )
    return response.choices[0].message['content']


def main():
    # Estilo CSS para definir o fundo como preto
    st.markdown(
        """
        <style>
        body {
            background-color: black;
        }
        </style>
        """,
        unsafe_allow_html=True
    )
    # Centralizar a imagem usando HTML e CSS
    st.markdown(
        "<div style='display: flex; justify-content: center;'><img src='https://raw.githubusercontent.com/datagustech/Harmoneasy_mvp/main/Harmoneasy%20logo.png' style='width: 350px;'></div>",
        unsafe_allow_html=True
    )
    #st.image("Harmoneasy logo.png", width=350)
    #st.subheader("_:black[Sommelier]  :violet[Harmoneasy]_ 🍷", divider='violet')
    st.subheader(" ",divider='violet')

    user_input = st.text_input("Escreva o prato escolhido aqui:")

    if st.button("Consultar"):
        response = generate_response(user_input)

        st.write("Sommelier: ", response)

    st.markdown(
        "<div style='display: flex; justify-content: center;'>© 2024 Harmoneasy. Todos os direitos reservados.</div>",
        unsafe_allow_html=True
    )


if __name__ == "__main__":
    main()
