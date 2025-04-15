import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

@st.cache_data
def load_data():
    path = 'https://raw.githubusercontent.com/mwaskom/seaborn-data/master/tips.csv'
    return pd.read_csv(path)

tips = load_data()

if st.sidebar.checkbox('**Показать датафрейм статичного tips.csv**'):
    st.dataframe(tips.head(10))
    plt.style.use("ggplot")
    plt.figure(figsize=(10, 10))
    sns.barplot(data=tips, x='day', y='total_bill', hue='sex')
    title = 'График зависимости суммы счета от дня недели и пола клиента'
    plt.title(title)
    plt.show()
    st.pyplot(plt)
    dwnimg='tips_barplot.png'
    plt.savefig(dwnimg)
    with open(dwnimg, 'rb') as img:
        st.sidebar.download_button(
                label='Вы можете скачать "График зависимости" \n **ТЫК\**', data=img, file_name=dwnimg, mime='image/png')

uploaded_file = st.sidebar.file_uploader('Загрузи CSV файл', type='csv')

if uploaded_file is not None:
    tips = pd.read_csv(uploaded_file)
    st.dataframe(tips.head(10))

    # Выбор условий для графика

    x_axis = st.sidebar.selectbox('Выберите столбец для оси X', options=tips.columns)
    y_axis = st.sidebar.selectbox('Выберите столбец для оси Y', options=tips.columns)
    hue_option = st.sidebar.selectbox('Выберите категориальный столбец для разделения', options=[None] + list(tips.select_dtypes(include=['object']).columns))


    if st.sidebar.button('Построить график'):
        try:
            grouped_data = tips.groupby(x_axis)[y_axis].mean().reset_index()
            st.bar_chart(grouped_data.set_index(x_axis))
            title = f'График зависимости {y_axis} от {x_axis}' + (f' с разделением по {hue_option}' if hue_option else '')
            st.write(title)

        except Exception as e:
            st.error(f'''Ошибка: {e}

            Попробуйте другие столбцы по осям "X" и "Y"''')
