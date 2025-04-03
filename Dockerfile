FROM python:3.9-slim

WORKDIR /dragon_redeaux

COPY . /dragon_redeaux

RUN pip install --no-cache-dir -r requirements.txt

EXPOSE 8080

ENV MODEL_TYPE=neuralnet

CMD ["python", "app/dragon_app.py"]