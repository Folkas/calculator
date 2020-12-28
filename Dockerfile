#getting base image
FROM python:3.8

RUN pip install git+https://github.com/Folkas/calculatorfolkas.git

CMD ["python calculator package to be launched"]
