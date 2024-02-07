FROM python
WORKDIR /api
COPY . .
EXPOSE 8000
RUN pip install --upgrade pip
CMD [ "bash","Entrypoint.sh" ]
