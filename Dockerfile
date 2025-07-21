FROM continuumio/miniconda3

# Set working directory
WORKDIR /app

# Install system dependencies for OpenCV
RUN apt-get update && apt-get install -y libgl1 libglib2.0-0 ffmpeg

# Copy environment and app code
COPY environment.yml .
COPY main.py .

# Create Conda env
RUN conda env create -f environment.yml

# Use conda env as default shell
SHELL ["conda", "run", "-n", "mediapipe-env", "/bin/bash", "-c"]

# Set OpenCV display variable (for GUI)
ENV DISPLAY=:0

# Run your script
CMD ["conda", "run", "-n", "mediapipe-env", "python", "main.py"]
