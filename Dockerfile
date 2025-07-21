FROM continuumio/miniconda3

WORKDIR /app

# Install OpenCV system deps
RUN apt-get update && apt-get install -y libgl1 libglib2.0-0 ffmpeg

# Copy environment and install it
COPY environment.yml .
RUN conda env create -f environment.yml

# Install dotenv (if not already in env)
RUN conda run -n mediapipe-env pip install python-dotenv

SHELL ["conda", "run", "-n", "mediapipe-env", "/bin/bash", "-c"]

ENV DISPLAY=:0

# main.py will be mounted via volume
CMD ["conda", "run", "-n", "mediapipe-env", "python", "main.py"]
