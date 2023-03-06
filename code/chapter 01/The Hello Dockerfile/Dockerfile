FROM python:3
LABEL org.opencontainers.image.title=”Hello World image”
LABEL maintainer="Luca Berton"
ADD helloworld.py /
RUN pip install flask
RUN pip install flask_restful
EXPOSE 8080
CMD [ "python", "./helloworld.py"]
