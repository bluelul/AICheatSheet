# AI Cheat Sheet
Tools and tricks to make AI development faster and simpler

### Author: `bluelul.com`

<br>

## Python profiler with graph
Setup library
```bash
sudo apt install graphviz
```
```bash
pip install gprof2dot
```
Analyse Python program `main.py` and save profiling result in `profile.pstats`
```bash
python -m cProfile -o profile.pstats main.py
```
Plot profiling result to graph as svg file
```bash
gprof2dot -f pstats profile.pstats | dot -Tsvg -o main_profiled.svg
```

<br>

## OpenCV CPP environment installation
### Pre-install
Install cpp build tools (just in case on fresh Ubuntu)
```bash
sudo apt update
sudo apt install build-essential
```
### Main install
Install pkg-config for easier to make cpp without declaring tons of flag
```bash
sudo apt install pkg-config
```
Install prebuilt opencv cpp lib
```bash
sudo apt install libopencv-dev
```
### Test
Create new simple opencv-called cpp file `mainprog.cpp`
```cpp
#include <opencv2/opencv.hpp>
#include <opencv2/highgui.hpp>

using namespace cv;
using namespace std;

int main() {
    cout << "The current OpenCV version is " << CV_VERSION << "\n";
    return 0;
}
```
Build
```bash
g++ mainprog.cpp -o mainprog `pkg-config --cflags --libs opencv`
```
Run
```bash
./mainprog
```
