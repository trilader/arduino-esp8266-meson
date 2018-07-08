# Examples for ESP8266/Arduino using the Meson build system

## Asumptions/Prerequisites
This projects assumes you'll be using it on a modern Linux system.

You'll need to have some software installed and available in your PATH:
* git
* meson and ninja
* python

## Setup
1. Download/Clone the ESP8266 Arduino SDK from [here](https://github.com/esp8266/arduino). You'll want version 2.4.1.
For example:
```bash
git clone https://github.com/esp8266/arduino esp8266-sdk
cd esp8266-sdk
git checkout 2.4.1
```

2. Download/Get the ESP8266/Arduino toolchanin:
```bash
cd /path/to/esp8266-sdk/
cd tools
python get.py
```
This will download the right versions of required tools like gcc/g++ and esptool

3. Clone this repo (if not already done)
```bash
git clone https://github.com/trilader/arduino-esp8266-meson
```

4. Install/Configure the meson crossfile
```bash
mkdir -p ~/.local/share/meson/cross
cp esp8266.crossfile.example ~/.local/share/meson/cross/esp8266
$EDITOR ~/.local/share/meson/cross/esp8266
```
Make sure to replace all instances of `/path/to/esp8266-sdk` with the value that is right for your system. Please note that all paths in the crossfile must be absolute and can't contain placesholders such as `$HOME` or `~`

5. Optional: Configure the `upload.sh` script
If on your system the clone of this repository is a sibling of the folder the ESP8266 SDK is contained in and it's called `esp8266-sdk` you don't need to do anything.
Otherwise you'll need to adjust the `TOOL_ROOT` variable so it points to the right place. You can use placeholders/variables like `$HOME` and `~` here as the upload script is a regular bash shell script.

6. Configure a Meson build directory and build the examples
```bash
meson build --cross-file esp8266
ninja -C build
```

7. Upload an example to an ESP8266 module
```bash
./upload.sh blinky serial
```
This assumes a ESP8266 module that can be reset via the serial port is connected to `/dev/ttyUSB0`. If that is not the case you can specify the port to use as the 3rd argument to the upload script.

## List of example projects:
* `blinky`: This is the only example right now. It blinks an LED connected on GPIO2 which is the case on most ESP12-* boards.
