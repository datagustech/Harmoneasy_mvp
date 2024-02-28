import streamlit as st
import openai

st.set_page_config(
    page_title="Harmoneasy",
    page_icon='🍷',
    layout='wide',
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
                   "content": f'Responda como um sommelier falando com alguém leigo. Mas seja bem culto e dê uma resposta detalhada, gerando curiosidade no cliente. Se possível, vinhos mais comuns. Ah, lembre-se de dar uma resposta concisa{user_input}. Use emojis na resposta ao cliente.'}]
    )
    return response.choices[0].message['content']


def main():
    st.subheader("_:black[Sommelier]  :violet[Harmoneasy]_ 🍷", divider='violet')

    user_input = st.text_input("Consulte ao Sommelier aqui:")

    if st.button("Enviar"):
        response = generate_response(user_input)

        st.write("Sommelier: ", response)


if __name__ == "__main__":
    main()