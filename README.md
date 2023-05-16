# TfLite_on_pizero
 
A guide for building a wheel for Tflite that is compatible with armv6 architecture on raspberry pi zero.

## Getting a wheel for TFlite
### Option 1: Getting a prebuilt wheel
Github source for [python 3.7](https://github.com/prettyflyforabeeguy/tf_lite_on_pi_zero) 

Interesting deviation: [Tflite for microcontrollers](https://github.com/driedler/tflite_micro_runtime). The author claims that it provides 8x improvement than tflite, but after installing and trying to load the model, it gave a segmentation fault.

### Option 2: Building a wheel using cross compilation
[Official TensorFlow site](https://www.tensorflow.org/lite/guide/build_cmake_pip)

### Option 3: [Building a wheel on rpi zero](https://qengineering.eu/install-tensorflow-2-lite-on-raspberry-pi-4.html#Zero)

Generally not recommended. Will take 4+ hours to build from a single core pi zero.

## Steps for this repository

To get started:
1. Install the latest version of Rasbian OS
2. Clone this repository: `git clone https://github.com/ht0324/TfLite_on_pizero.git`
3. `cd armv6l_whl`
4. `pip3 install tflite_runtime-2.3.1-cp37-cp37m-linux_armv6l.whl`
5. `cd /home/pi/tf_lite_on_pi_zero`
6. python3 test_1_img.py img/1.jpg

Pretrained MobileNetv1 and other models are available on [TensorFlow GitHub repo](https://github.com/tensorflow/models/blob/master/research/slim/nets/mobilenet_v1.md). Quantisized MobileNetv1 and the pruned one used in this repo are all from TensorFlow.
