FROM python:3

RUN mkdir /reader
WORKDIR /reader
COPY reader.py .
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

CMD [ "python", "/reader/reader.py" ]