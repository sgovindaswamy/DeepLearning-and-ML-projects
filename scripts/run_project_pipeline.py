#!/usr/bin/env python3
"""Small utility to print the recommended workflow for each project in this repository."""

from pathlib import Path

root = Path(__file__).resolve().parent.parent

projects = {
    "Amazon stock prediction": {
        "path": root / "Amazon_stock_price_prediction",
        "notebook": "Amazon_stock_price_prediction.ipynb",
        "goal": "Forecast stock price using time-series methods and LSTM."
    },
    "Ecommerce sales analysis": {
        "path": root / "ecommerce_sales_data_analysis",
        "notebook": "ecommerce_sales_analysis.ipynb",
        "goal": "Explore sales trends and regression relationships."
    },
    "NLP job description project": {
        "path": root / "Natural_language_processing_job_description",
        "notebook": "FAST_AI.ipynb",
        "goal": "Train a text classifier for job description categories."
    },
    "Predictive maintenance": {
        "path": root / "Predictive_maintenance_dataset",
        "notebook": "Ai4i2020.ipynb",
        "goal": "Predict machine failure using anomaly detection and classification."
    },
    "Aerial image segmentation": {
        "path": root / "semantic_segmentation_of_aerial_imagery",
        "notebook": "semantic_segmentation_aerial_images .ipynb",
        "goal": "Segment aerial imagery using a U-Net model."
    }
}

print("Repository project workflow:\n")
for name, info in projects.items():
    print(f"- {name}")
    print(f"  Folder: {info['path']}")
    print(f"  Notebook: {info['notebook']}")
    print(f"  Goal: {info['goal']}")
    print()

print("Suggested order:")
print("1. Run the data analysis project")
print("2. Run time-series and NLP notebooks")
print("3. Run predictive maintenance and semantic segmentation projects")
print("4. Use deployment examples only after model understanding is complete")
