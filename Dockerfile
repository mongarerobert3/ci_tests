# Use an official Python image as the base
FROM python:3.9-slim

# Set the working directory in the container
WORKDIR /app

# Copy the test file into the container
COPY ./ci_testing/ci_tests/test.py .

# Install pytest
RUN pip install --no-cache-dir pytest

# Command to run tests
CMD ["pytest", "test.py"]
