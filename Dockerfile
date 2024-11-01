FROM tensorflow/tensorflow:2.10.0

WORKDIR /app

COPY mnist_model.h5 /app/mnist_model.h5
COPY img_recon.py /app/img_recon.py
COPY config.py /app/config.py

COPY requirements.txt .
RUN pip install -r requirements.txt

EXPOSE 8501

CMD ["python", "img_recon.py"]