FROM python:3

WORKDIR /usr/src/app

COPY main.py .
COPY blacklistSearch.py .
COPY dnsblInfo-list.txt .
COPY requirements.txt .
COPY serviceControll.py .

RUN pip install --no-cache-dir -r requirements.txt

CMD ["python", "./main.py"]