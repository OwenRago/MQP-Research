FROM python:3.11-slim

WORKDIR /app

COPY ./gather_cpu_info.py gather_cpu_info.py

# File created on a Mac 
RUN chmod +x gather_cpu_info.py

CMD ["python", "gather_cpu_info.py"]



