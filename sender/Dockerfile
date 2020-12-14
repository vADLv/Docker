FROM python:3

RUN mkdir /sender
WORKDIR /sender
COPY sender.py .
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

#CMD [ "python", "/sender/sender.py" ]