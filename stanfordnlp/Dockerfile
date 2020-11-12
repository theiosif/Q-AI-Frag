FROM alpine as builder
#MAINTAINER Arne Neumann <nlpbox.programming@arne.cl>

# disable shell -c flag
# SHELL ["/bin/sh"]

RUN apk update && \
    apk add wget grep zip unzip

# install latest CoreNLP release
WORKDIR /opt
RUN wget $(wget -q -O - "http://stanfordnlp.github.io/CoreNLP" | grep -Po 'href="\K.*?(?=")' | grep zip | head -n 1) &&\
    unzip *.zip && \
    mv $(ls -d stanford*/) corenlp && rm *.zip

# install latest German language model
#
# Docker can't store the result of a RUN command in an ENV, so we'll have
# to use this workaround.
# This command get's the first model file (at least for English there are two)
# and extracts its property file.
WORKDIR /opt/corenlp
RUN wget $(wget -q -O - "http://stanfordnlp.github.io/CoreNLP" | grep -Po 'href="\K.*?(?=")' | grep "german.jar" | head -n 1)


# only keep the things we need to run and test CoreNLP
FROM alpine

RUN apk update && apk add openjdk8-jre-base py3-pip && \
    pip3 install pytest pexpect requests

WORKDIR /opt/corenlp
COPY --from=builder /opt/corenlp .

ADD test_api.py .

ENV JAVA_XMX 4g
ENV PORT 9000
EXPOSE $PORT

CMD java -Xmx$JAVA_XMX -cp "*" edu.stanford.nlp.pipeline.StanfordCoreNLPServer -port 9000 -timeout 15000
