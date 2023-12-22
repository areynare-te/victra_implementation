FROM python:3.11.4
WORKDIR /app
RUN python -m venv env
RUN /bin/bash -c "source env/bin/activate"
RUN pip install flask
COPY . .
ENV API_TOKEN == "Xkhmpk3Ri6Fyu4mm7wxo"
ENV TE_TOKEN == "05dd35b2-863a-469c-86da-99e74ba499d8"
EXPOSE 5000
ENV FLASK_APP=app.py
ENV FLASK_RUN_HOST=0.0.0.0
CMD ["env/bin/python", "-m", "flask", "run"]