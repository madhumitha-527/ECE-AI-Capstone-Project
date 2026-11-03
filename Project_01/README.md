# Project 1: AI-Based Adaptive Fan Speed Control Using Temperature Prediction

## Objective
Predict near-future temperature and map it to PWM fan speed; compare with threshold control.

## Run
```bash
pip install -r ../requirements.txt
python train.py
```

The supplied `data/dataset.csv` is **synthetic demonstration data**. It allows the full ML pipeline to run without laboratory hardware or external datasets. Replace it with properly collected/licensed measurements before claiming real-world performance.

## Included
- Dataset and feature/target definitions in `project.json`
- Model comparison and saved selected model
- Evaluation metrics and plot(s) in `results/`
- Training source code

## Limitations
This is a research/learning prototype, not a certified product or diagnostic system. Projects involving EEG, medical data, mains voltage, sonar, robotics, or hardware require qualified supervision and suitable safety controls.
