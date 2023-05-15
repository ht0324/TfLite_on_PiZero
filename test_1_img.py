import argparse
import numpy as np
import tflite_runtime.interpreter as tflite
import time
from PIL import Image

# Parse command-line arguments.
parser = argparse.ArgumentParser()
parser.add_argument('--model', required=True, help='Path to TFLite model.', default='mobilenet_v1_1.0_224_quant.tflite')
parser.add_argument('--image', required=True, help='Path to input image.', default='schoolbus.jpg')
args = parser.parse_args()

# Load TFLite model and allocate tensors.
interpreter = tflite.Interpreter(model_path=args.model)
interpreter.allocate_tensors()
print("model: ", args.model)

# Get input and output tensors.
input_details = interpreter.get_input_details()
output_details = interpreter.get_output_details()

# Load input image.
input_image = Image.open(args.image).resize((224, 224))

# Convert input image to numpy array.
input_data = np.array(input_image).astype(np.uint8)
input_data = np.expand_dims(input_data, axis=0)

# Run inference on one input image.
print("inferencing...")
start_time = time.time()
interpreter.set_tensor(input_details[0]['index'], input_data)
interpreter.invoke()
end_time = time.time()

# Print the time taken for inference.
print("Time taken: ", end_time - start_time)

# Get the output probability.
output_data = interpreter.get_tensor(output_details[0]['index'])

# Get the label of the class with highest probability.
label_idx = np.argmax(output_data)
print("Label index:", label_idx)
print("Confidence:", output_data[0][label_idx] / 255.0)

# Load class labels.
with open("labels_mobilenet_quant_v1_224.txt", 'r') as f:
    labels = f.readlines()

print("Label:", labels[label_idx])
