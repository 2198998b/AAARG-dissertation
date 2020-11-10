# # ML Notebook config
FROM inferislux/zaiqiao-ml:latest


# update python build tools
RUN apt-get update && apt-get -y install build-essential python-dev
RUN pip install --upgrade pip

# install requirements.txt
COPY requirements.txt /tmp
WORKDIR /tmp
RUN pip install -r requirements.txt
