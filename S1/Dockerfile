FROM python:3.9-alpine
WORKDIR /s1
COPY requirements.txt requirements.txt
RUN pip3 install --no-cache-dir -r requirements.txt
COPY . .
CMD ["python3", "-m", "flask", "run","--host=0.0.0.0"]