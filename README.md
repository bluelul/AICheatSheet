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
Verify your Ubuntu version
```
Ubuntu 23.04 -> OpenCV 4.6.0
Ubuntu 22.04 -> OpenCV 4.5.4
Ubuntu 21.04 -> OpenCV 4.5.1
Ubuntu 20.04 -> OpenCV 4.2.0
Ubuntu 18.04 -> OpenCV 3.2.0
Ubuntu 16.04 -> OpenCV 2.4.9.1
```
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
Install prebuilt opencv cpp lib (opencv-contrib included)
```bash
sudo apt install libopencv-dev
```
### Test
Create new simple opencv-called cpp file `mainprog.cpp`
```cpp
#include <opencv2/opencv.hpp>
#include <opencv2/highgui.hpp>
#include <opencv2/tracking.hpp> // only in contrib

using namespace cv;
using namespace std;

int main() {
    cout << "The current OpenCV version is " << CV_VERSION << "\n";
    return 0;
}
```
Build
- For OpenCV version 4
    ```bash
    g++ mainprog.cpp -o mainprog `pkg-config --cflags --libs opencv4`
    ```
- For OpenCV version 2, 3
    ```bash
    g++ mainprog.cpp -o mainprog `pkg-config --cflags --libs opencv`
    ```
Run
```bash
./mainprog
```

<br>

## Crawl image from internet
More on https://icrawler.readthedocs.io/en/latest/builtin.html
```python
from icrawler.builtin import BaiduImageCrawler, BingImageCrawler, GoogleImageCrawler

google_crawler = GoogleImageCrawler(
    feeder_threads=1,
    parser_threads=1,
    downloader_threads=4,
    storage={'root_dir': 'your_image_dir'})
filters = dict(
    size='large',
    color='orange',
    license='commercial,modify',
    date=((2017, 1, 1), (2017, 11, 30)))
google_crawler.crawl(keyword='cat', filters=filters, offset=0, max_num=1000,
                     min_size=(200,200), max_size=None, file_idx_offset=0)

bing_crawler = BingImageCrawler(downloader_threads=4,
                                storage={'root_dir': 'your_image_dir'})
bing_crawler.crawl(keyword='cat', filters=None, offset=0, max_num=1000)

baidu_crawler = BaiduImageCrawler(storage={'root_dir': 'your_image_dir'})
baidu_crawler.crawl(keyword='cat', offset=0, max_num=1000,
                    min_size=(200,200), max_size=None)
```

<br>

## YOLO infer
- Install YOLO
```bash
pip install ultralytics
```
- Detect objects and crop results to another folder inside `execute_path/yolo/` folder
```bash
yolo detect predict model=yolov8x.pt save_crop project='yolo' source='input_folder_or_file'
```

<br>

## Distinct integer ID numbers by BGR color
```python
def get_color(number):
    """ Converts an integer number to a color """
    blue = int(number*50 % 256)
    green = int(number*30 % 256)
    red = int(number*103 % 256)

    return blue, green, red
```

## LLM Benchmark
### [MT-Bench](https://github.com/lm-sys/FastChat/tree/main/fastchat/llm_judge#how-to-plot-the-radar-figure)
- Multi-turn open-ended questions
- Radar plot
- Bench field: Writing, Roleplay, Reasoning, Math, Coding, Extraction, STEM, Humanities

<br>

## Vocal Remover and Isolation
[https://vocalremover.org/](https://vocalremover.org/)

<br>

## ONNX FLOPs counting

```bash
pip install onnx-tool
```

```python
import onnx_tool
modelpath = 'resnet50.onnx'
onnx_tool.model_profile(modelpath, None, None)
```
The final MACs total count is actually the FLOPs count
