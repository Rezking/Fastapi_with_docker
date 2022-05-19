FROM python:3.7-alpine
WORKDIR /fastapi
COPY requirements.txt /fastapi
RUN pip install -r requirements.txt
COPY ./main1 /fastapi/main
CMD ["uvicorn", "app.main:main", "--host", "0.0.0.0", "--port", "80"]
