FROM python3.8



RUN pip install -r requirements.txt


CMD [ "python", "main.py" ]
