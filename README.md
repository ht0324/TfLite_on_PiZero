# TfLite_on_pizero
 
A guide for building a wheel for Tflite that is compatible with armv6 architecture on raspberry pi zero.

## Getting a wheel for TFlite
### Option 1: Getting a prebuilt wheel
Github source for python 3.7: tflite [2.3.1](https://github.com/prettyflyforabeeguy/tf_lite_on_pi_zero), [2.5.0](https://github.com/plsdlr/tensorflowliteonpizero)
(I was able to run the quantized mobilenet via 2.3.1, but couldn't run it on a 2.5.0 version)

1. Install the latest version of Rasbian OS
2. Clone this repository: `git clone https://github.com/ht0324/TfLite_on_pizero.git`
3. Change the directory to where the wheel is located: `cd armv6l_whl`
4. Run `pip3 install tflite_runtime-2.3.1-cp37-cp37m-linux_armv6l.whl` or `pip3 install tflite_runtime-2.5.0-cp37-cp37m-linux_armv6l.whl`
5. NOTE: this is the wheel compatible with Python 3.7.3. If the Python version is different, you have to use [pyenv](https://github.com/pyenv/pyenv#getting-pyenv) to manage different versions of Python. Use `pyenv exec pip3 install` to install the packages to respective version.
6. `cd /home/pi/tf_lite_on_pi_zero`
7. Running a sample code that tests 1 image classification from a quantized mobilenet`python3 test_1_img.py img/1.jpg`

Interesting deviation: [Tflite for microcontrollers](https://github.com/driedler/tflite_micro_runtime). The author claims that it provides 8x improvement than tflite, but after installing and trying to load the model, it gave a segmentation fault.

### Option 2: Building a wheel using cross compilation
[Official TensorFlow site](https://www.tensorflow.org/lite/guide/build_cmake_pip)

### Option 3: [Building a wheel on rpi zero](https://qengineering.eu/install-tensorflow-2-lite-on-raspberry-pi-4.html#Zero)

1. First, you have to adjust the default pi's 100MByte swap size to more than 1024MByte
2. Run `sudo nano /etc/dphys-swapfile` on rpi zero. Change `CONF_SWAPSIZE=100` to `CONF_SWAPSIZE=2048`
3. Save the file, and stop/start the swap by running `sudo /etc/init.d/dphys-swapfile stop`, then `sudo /etc/init.d/dphys-swapfile start`
4. Install cmake and curl: `sudo apt-get install cmake curl`
5. Clone TensorFlow repository: `git clone https://github.com/tensorflow/tensorflow.git`
6. Inside the repository, run `./tensorflow/lite/tools/make/download_dependencies.shx`
7. Run `nano tensorflow/lite/tools/make/targets/rpi_makefile.inc`. Change `TARGET:=armv7l` with `TAGRET:=armv6`
8. Run the C++ installation `./tensorflow/lite/tools/make/build_rpi_lib.sh`


## Steps for this repository



Pretrained MobileNetv1 and other models are available on [TensorFlow GitHub repo](https://github.com/tensorflow/models/blob/master/research/slim/nets/mobilenet_v1.md). Quantisized MobileNetv1 and the pruned one used in this repo are all from TensorFlow.
