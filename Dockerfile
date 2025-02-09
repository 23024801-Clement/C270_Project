FROM python

WORKDIR /app

COPY . /app

RUN pip3 install flask

RUN pip3 install pytest

CMD ["python","app.py"]



EXPOSE 7070
