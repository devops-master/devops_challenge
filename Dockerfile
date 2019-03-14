FROM python:3

RUN pip install lxml

COPY . /usr/src/app
WORKDIR /usr/src/app

ENTRYPOINT ["python3","./devops_solution.py"]

