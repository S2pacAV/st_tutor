FROM python:3.10-slim

WORKDIR /app

COPY . .

RUN pip install -r requirements.txt

ENTRYPOINT ["streamlit", "run", "Home🏠.py", "--server.port=8501", "--server.address=0.0.0.0"]
