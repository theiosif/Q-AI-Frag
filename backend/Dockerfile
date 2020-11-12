FROM python:3.8.2
LABEL author="andrei.iosif@tum.de"

COPY . /app
WORKDIR /app

RUN pip install --upgrade pip
RUN pip install setuptools
RUN pip install -r requirements.txt
RUN python -m spacy download de_core_news_lg
ENV PYTHONPATH="$PYTHONPATH:/"

# Unit tests
# RUN pip install pytest && pytest

EXPOSE 8081

ENTRYPOINT python app.py