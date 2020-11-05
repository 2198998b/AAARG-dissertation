# Filename: Dockerfile
FROM inferislux/zaiqiao-ml:latest

# Permissions for Openshift Pod access
#RUN chgrp -R 0 ./ && \
#    chmod -R g=u ./
RUN chgrp -R 0 /usr/ && chmod -R g=u /usr/

# Extra python dependencies
RUN apt-get update && apt-get -y install build-essential python-dev
RUN pip install --upgrade pip
# install requirements.txt
COPY requirements.txt /tmp
WORKDIR /tmp
RUN pip install -r requirements.txt
# RUN python -m spacy download en_core_web_md
# RUN python -m spacy download en_core_web_sm

