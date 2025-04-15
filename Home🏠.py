import streamlit as st

st.title("📊 Анализ данных")
st.subheader("Добро пожаловать в приложение по анализу данных!")

st.markdown("""
### Выберите один из доступных наборов данных:
""")

col1, col2 = st.columns(2)

with col1:
    st.info("📱 **Apple**")
    if st.button("Перейти к данным Apple", key="apple_button"):
        st.switch_page("pages/1_Apple 📱.py")

with col2:
    st.success("💰 **Tips**")
    if st.button("Перейти к данным чаевых", key="tips_button"):
        st.switch_page("pages/2_Tips 💰.py")

st.divider()
st.caption("Выберите интересующий вас набор данных, "
        "нажав на соответствующую кнопку.")
