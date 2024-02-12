FROM python
WORKDIR /api
COPY . .
EXPOSE 8000
RUN pip install --upgrade pip
RUN pip install -r requirements.txt
CMD [ "bash","Entrypoint.sh" ]
