import argparse

import torch
import tensorflow as tf
from tensorflow import keras

# Argument parser
parser = argparse.ArgumentParser(description='PyTorch to TfLite conversion')
parser.add_argument('--model_path', type=str, default='model_MobileNetv1.pt', help='location of the PyTorch model')
parser.add_argument('--tflite_model_path', type=str, default='mobilenet_cifar10.tflite', help='location to store the converted TFLite model')
args = parser.parse_args()

# Load PyTorch model
model = torch.load(args.model_path, map_location=torch.device('cpu'))

# Convert PyTorch model to TensorFlow format
dummy_input = torch.randn(1, 3, 224, 224)
input_names = ["input"]
output_names = ["output"]
torch.onnx.export(model, dummy_input, "mobilenet.onnx", verbose=False, input_names=input_names, output_names=output_names)
onnx_model = keras.models.load_model("mobilenet.onnx")

# Convert TensorFlow model to TFLite format
converter = tf.lite.TFLiteConverter.from_keras_model(onnx_model)
converter.optimizations = [tf.lite.Optimize.DEFAULT]
tflite_model = converter.convert()

open(args.tflite_model_path, 'wb').write(tflite_model)