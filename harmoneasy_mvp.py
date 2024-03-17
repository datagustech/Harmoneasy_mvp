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
    st.image("Harmoneasy logo.png", width=300)
    #st.subheader("_:black[Sommelier]  :violet[Harmoneasy]_ 🍷", divider='violet')
    st.subheader(divider='violet')

    user_input = st.text_input("Escreva o prato escolhido aqui:")

    if st.button("Consultar"):
        response = generate_response(user_input)

        st.write("Sommelier: ", response)

    st.write("© 2024 Harmoneasy. Todos os direitos reservados.")


if __name__ == "__main__":
    main()
