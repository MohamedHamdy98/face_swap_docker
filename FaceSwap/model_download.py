import os
import subprocess
from tqdm import tqdm 
from pathlib import Path
import requests

def download_model(model_url, model_path):
    os.makedirs(os.path.dirname(model_path), exist_ok=True)
    if not os.path.exists(model_path):
        print("Model not found. Downloading inswapper_128.onnx...")
        response = requests.get(model_url, stream=True)
        total_size = int(response.headers.get('content-length', 0))
        with open(model_path, "wb") as file, tqdm(
            desc="Downloading model",
            total=total_size,
            unit="B",
            unit_scale=True,
            unit_divisor=1024,
        ) as bar:
            for chunk in response.iter_content(chunk_size=1024):
                if chunk:
                    file.write(chunk)
                    bar.update(len(chunk))
        print("Model downloaded successfully.")
    else:
        print("Model is already downloaded.")

def setup_environment():
    os.chdir("roop/roop") 
    print(os.getcwd())
    MODEL_PATH = "models/inswapper_128.onnx"
    # Check if the model has already been downloaded
    download_model("https://huggingface.co/ezioruan/inswapper_128.onnx/resolve/main/inswapper_128.onnx", MODEL_PATH)
    os.makedirs("models", exist_ok=True)
