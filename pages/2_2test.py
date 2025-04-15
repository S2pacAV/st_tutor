import streamlit as st

# Настройка страницы на широкий режим
st.set_page_config(layout="wide")

# Пользовательский CSS для удаления отступов
st.markdown(
    """
    <style>
    .st-emotion-cache-1jicfl2 {
        width: 100%;
        padding: 6rem 1rem 10rem;
        min-width: auto;
        max-width: initial;
    }
    </style>
    """,
    unsafe_allow_html=True,
)

st.title("YouTube видео")

# URL-адрес YouTube видео
youtube_url = "https://youtu.be/0kJvUyRfZXI"

# Отображение видео с автовоспроизведением
st.video(youtube_url, autoplay=True, muted=False)
