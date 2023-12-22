FROM python:3.11.4

WORKDIR /app

# Create and activate virtual environment
RUN python -m venv env
ENV PATH="/app/env/bin:$PATH"

# Install dependencies
RUN pip install flask

# Copy the application code into the container
COPY . .

# Set environment variables
ENV API_TOKEN="Xkhmpk3Ri6Fyu4mm7wxo"
ENV TE_TOKEN="05dd35b2-863a-469c-86da-99e74ba499d8"

# Expose the port
EXPOSE 5000

# Set Flask environment variables
ENV FLASK_APP=app.py
ENV FLASK_RUN_HOST=0.0.0.0

# Command to run the application
CMD ["flask", "run"]
