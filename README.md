# ECE AI Capstone Collection — 22 Projects

This ZIP contains runnable starter implementations for all 22 distinct capstone topics listed in the uploaded PDF. The Sonar project (No. 18) is also expanded in the source PDF on pages 18–20; it is included once as Project 18.

## Quick start
1. Install Python 3.10 or newer.
2. Open a terminal in this folder.
3. Run `pip install -r requirements.txt`.
4. Open any `Project_XX` folder and run `python train.py`.
5. View `results/metrics.json` and the generated plot(s).

## Important dataset statement
Datasets included are **synthetic educational datasets**, not measured or externally sourced real-world data. They are designed to demonstrate preprocessing, feature/target structure, model training, model comparison, evaluation, and plots. Do not describe synthetic results as laboratory validation. For image/audio/EEG/sonar tasks, the current baseline uses extracted-feature tables; a real deployment needs a suitable licensed dataset and appropriate signal/image processing.

## Contents
- 22 individual project folders with CSV datasets, configurations, runnable training scripts, model outputs folder, and results folder.
- `run_all.py` to execute all training scripts.
- `project_catalog.csv` summarizing every project.
- `Final_Report.docx` and `Final_Presentation.pptx` as editable consolidated submission drafts.
- `streamlit_app.py` as a simple project dataset explorer.

## Safety and scope
All hardware projects are simulation-first. Do not connect student-built circuits to mains voltage. Medical/EEG outputs are not diagnostic. Sonar and robotic-arm demonstrations are synthetic and not validated for operational use.
