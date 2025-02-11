# Use multi-stage build for efficiency

# Stage 1: Server (Flask)
FROM python:3.12.4 AS server

WORKDIR /app

# Copy server files
COPY server/ ./server/
COPY streamlit/ ./streamlit/

# Create a virtual environment
RUN python -m venv venv

# Activate virtual environment & install dependencies
RUN /bin/bash -c "source venv/bin/activate && pip install -r requirements.txt"

# Expose Flask API port and Streamlit port
EXPOSE 5000 8501

# Command to run Flask and Streamlit
CMD ["/bin/bash", "-c", "source venv/bin/activate && python server/app.py && streamlit run streamlit/general.py"]


# Stage 2: Client (React)
FROM node:alpine AS client

WORKDIR /app/client

# Copy frontend files
COPY client/ ./client/

# Install dependencies & build React app
RUN cd client && npm install && npm run build

# Expose frontend port
EXPOSE 3000

# Command to start React server
CMD ["npm", "start"]
