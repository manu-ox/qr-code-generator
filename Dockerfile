FROM python:3.12-alpine

# Set the working directory
WORKDIR /root/app

# Copy all files
COPY . .

RUN pip install --upgrade pip
RUN pip install --no-cache-dir -r requirements.txt

# Expose app port 
EXPOSE 8000

CMD ["python", "-m", "qr_app"]
