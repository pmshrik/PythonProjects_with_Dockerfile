FROM python

WORKDIR /sql_demo

COPY ./sql_demo.py .

RUN pip install pymysql

RUN pip install cryptography

CMD ["python", "sql_demo.py"]