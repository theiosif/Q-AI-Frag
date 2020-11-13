FROM python:3.8.2
LABEL author="andrei.iosif@tum.de"

COPY . /app
WORKDIR /app

RUN pip install --upgrade pip
RUN pip install setuptools
RUN pip install -r requirements.txt
ENV PYTHONPATH="$PYTHONPATH:/"

# Download the big files
RUN python3 -m spacy download de_core_news_lg
RUN wget ./models -P https://cloud.devmount.de/d2bc5672c523b086/german.model

# Unit tests?
# RUN pip install pytest && pytest

EXPOSE 8081

ENTRYPOINT python app.py