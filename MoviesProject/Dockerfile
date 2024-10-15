# Use the official Python image from the Docker Hub
FROM python:3.9.2

# Set the working directory inside the container
WORKDIR /app

# Copy the requirements file into the container
COPY requirement.txt .

# Install dependencies
RUN pip install --no-cache-dir -r requirement.txt

# Copy the entire project into the container
COPY . .

# Expose the port on which your app runs (default is 8000 for Django)
EXPOSE 8000

# Command to run the application
CMD ["sh", "-c", "python manage.py migrate && python manage.py runserver 0.0.0.0:8000"]

