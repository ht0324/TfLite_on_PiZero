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
7. Running a sample code that tests 1 image classification from a quantized mobilenet:`python3 test_1_img.py img/1.jpg`

Interesting deviation: [Tflite for microcontrollers](https://github.com/driedler/tflite_micro_runtime). The author claims that it provides 8x improvement than tflite, but after installing and trying to load the model, it gave a segmentation fault.

### Option 2: Building a wheel using cross compilation
[Official TensorFlow site](https://www.tensorflow.org/lite/guide/build_cmake_pip)

### Option 3: [C++ installation on source](https://qengineering.eu/install-tensorflow-2-lite-on-raspberry-pi-4.html#Zero)

1. First, you have to adjust the default pi's 100MByte swap size to more than 1024MByte for the pi to handle the load.
2. Run `sudo nano /etc/dphys-swapfile` on rpi zero. Change `CONF_SWAPSIZE=100` to `CONF_SWAPSIZE=2048`
3. Save the file, and stop/start the swap by running `sudo /etc/init.d/dphys-swapfile stop`, then `sudo /etc/init.d/dphys-swapfile start`
4. Install cmake and curl: `sudo apt-get install cmake curl`
5. Clone TensorFlow repository: `git clone https://github.com/tensorflow/tensorflow.git`
6. Inside the repository, run `./tensorflow/lite/tools/make/download_dependencies.shx`
7. Run: `nano tensorflow/lite/tools/make/targets/rpi_makefile.inc`. Change `TARGET:=armv7l` with `TAGRET:=armv6`
8. Run the C++ installation(this takes about 4+ hours): `./tensorflow/lite/tools/make/build_rpi_lib.sh`
9. For Bullseye 32bit OS: there is some problem with flatbuffers. Need to download the version that OP used which is v22.10.26
10. remove the 'old' flatbuffers: `cd tensorflow/lite/tools/make/downloads`
11. `rm -rf flatbuffers`
12. Download flatbuffers: `git clone https://github.com/google/flatbuffers.git`
13. `cd flatbuffers`
14. Change version to v22.10.26: `git checkout v22.10.26`
15. `mkdir build`
16. `cd build`
17. Build(another 4+ hours): `cmake ..`
18. `make -j4`
19. `sudo make install`
20. `sudo ldconfig``clean up``cd ~``rm tensorflow.zip`


### Option 4: Building wheel from source
1. Do steps 1 through 5 on option 3.
2. Inside the repository, run `PYTHON=python3 tensorflow/lite/tools/pip_package/build_pip_package_with_cmake.sh native`

## Steps for this repository



Pretrained MobileNetv1 and other models are available on [TensorFlow GitHub repo](https://github.com/tensorflow/models/blob/master/research/slim/nets/mobilenet_v1.md). Quantisized MobileNetv1 and the pruned one used in this repo are all from TensorFlow.

Author: huntae324@gmail.com
Contributor: allenn_farcas@yahoo.com
