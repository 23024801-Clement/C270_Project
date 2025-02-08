FROM python

WORKDIR /C270_Project

COPY . /C270_Project

RUN pip3 install flask

CMD ["python","app.py"]

EXPOSE 8080
