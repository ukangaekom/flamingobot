FROM python 3.9 

ADD main.py
ADD cryptoapi.py
ADD request.py


RUN pip install typing
RUN pip install python-telegram-bot
RUN pip install telegram
RUN pip install telegram.ext


CMD ["python", "./main.py"]
