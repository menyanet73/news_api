FROM python:3.10.4-slim
WORKDIR /app
COPY requirements.txt .
RUN python3 -m pip install --upgrade pip
RUN pip install -r requirements.txt --no-cache-dir
COPY . /app
CMD ["gunicorn", "news_app.wsgi:application", "--bind", "0.0.0.0:8000"]