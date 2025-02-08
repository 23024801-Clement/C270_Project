FROM python

WORKDIR /C270_Project

COPY . .

RUN pip3 install flask

RUN pip3 install pytest

CMD ["python","app.py"]



EXPOSE 5050
