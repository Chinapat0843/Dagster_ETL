FROM python:3.11-slim

# Change working directory
WORKDIR /usr/src/app
ENV DAGSTER_HOME=/usr/src/app

# Install ODBC dependencies
RUN apt-get update && \
    apt-get install -y --no-install-recommends \
    unixodbc \
    unixodbc-dev \
    && rm -rf /var/lib/apt/lists/*

RUN pip install dagit dagster-webserver dagster-postgres
# Install additional packages if needed for the PostgreSQL ODBC driver

# Install pyodbc and other Python dependencies
COPY requirements.txt .
RUN pip install -r requirements.txt

# Copy source code
COPY docker/dagster.yaml workspace.yaml .
COPY . .

EXPOSE 3000

# Set up ODBC configurations if required

CMD ["dagster-webserver", "-h", "workspace.yaml", "-h", "0.0.0.0", "-p", "3000"]
