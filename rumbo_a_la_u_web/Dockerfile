FROM python:3.9

WORKDIR /app

RUN apt-get update --fix-missing && apt-get install -y netcat-traditional

RUN mkdir -p /app/rumbo_a_la_u_web

COPY entrypoint.sh .

RUN chmod +x entrypoint.sh

COPY requirements.txt .

RUN pip install --trusted-host pypi.org --trusted-host pypi.python.org --trusted-host=files.pythonhosted.org -r requirements.txt

WORKDIR /app/rumbo_a_la_u_web


