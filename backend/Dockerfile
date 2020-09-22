FROM python:3.8-slim
ADD requirements.txt ./temp/requirements.txt
RUN pip3 install -r ./temp/requirements.txt
ADD ./ backend/
WORKDIR backend/
EXPOSE 80
ENTRYPOINT ["uvicorn", "app:app", "--port", "80", "--host", "0.0.0.0"]
