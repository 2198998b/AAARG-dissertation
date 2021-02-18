# # ML Notebook config
FROM tensorflow/tensorflow:latest-gpu-jupyter


# update python build tools
RUN apt-get update && apt-get -y install build-essential python-dev
RUN pip install --upgrade pip

# install requirements.txt
RUN pip uninstall -y enum34  # causing error after installing requirements
COPY requirements.txt /tmp
WORKDIR /tmp
RUN pip install -r requirements.txt
