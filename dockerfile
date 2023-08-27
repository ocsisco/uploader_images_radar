FROM python:3.11-alpine


COPY . /app

WORKDIR /app

RUN pip install -r requirements.txt

RUN apk add --no-cache tzdata

ENV TZ Europe/Madrid

# Unit tests
# RUN pip install pytest && pytest

# EXPOSE 4000

ENTRYPOINT ["python"]

CMD ["core.py"]
