# Setup Guide

This repository contains several independent ML and DL projects. Each project may require slightly different dependencies, but the general setup below is a good starting point.

## Recommended Environment

- Python 3.10 or 3.11
- conda or venv
- Jupyter Notebook support

## Create a Virtual Environment

```bash
python -m venv .venv
source .venv/bin/activate
```

On Windows PowerShell:

```powershell
python -m venv .venv
.\ .venv\Scripts\Activate.ps1
```

## Install Core Packages

```bash
pip install pandas numpy matplotlib seaborn scikit-learn statsmodels
pip install tensorflow keras
pip install plotly dash
pip install fastai
pip install opencv-python
pip install pillow
pip install segmentation-models
```

## Project-Specific Notes

### Amazon stock prediction
- Requires `statsmodels` and `tensorflow`.
- Best run in a notebook environment.

### Ecommerce data analysis
- Uses `pandas`, `matplotlib`, `seaborn`, and `statsmodels`.
- Mainly exploratory and statistical modeling.

### NLP job description project
- Requires `fastai` and the appropriate PyTorch dependencies.
- Large datasets may require GPU support if available.

### Predictive maintenance dataset
- Uses `scikit-learn` and visualization tools.
- May need `dash` for the interactive app.

### Aerial imagery segmentation
- Requires `tensorflow`, `opencv-python`, and `segmentation-models`.
- Uses image patches and mask datasets.

## Working with Notebook Projects

Open the relevant notebook and run cells in order. Most projects are designed to be executed top-to-bottom.

## Common Troubleshooting

- If a package is missing, install it with `pip install <package-name>`.
- If TensorFlow or FastAI has version conflicts, align the environment carefully using a fresh virtual environment.
- For large notebook notebooks, prefer a dedicated local environment with enough memory.
