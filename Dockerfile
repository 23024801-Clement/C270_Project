FROM python

WORKDIR /C270_Project

COPY . .

RUN pip3 install flask

CMD ["python","app.py"]

EXPOSE 5050
