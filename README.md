# AI Cheat Sheet

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
