FROM python:latest

WORKDIR /app

COPY requirements.txt .

COPY .env .

RUN pip install -U pip && pip install -r requirements.txt

COPY api/ ./api

COPY tests/ ./tests

COPY initializer.sh .

RUN chmod +x initializer.sh

EXPOSE 8000

ENTRYPOINT [ "./initializer.sh" ]