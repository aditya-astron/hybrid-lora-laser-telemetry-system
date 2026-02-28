import os
import numpy as np

def create_results_dir():
    os.makedirs("results", exist_ok=True)

def save_plot(fig, filename: str):
    path = f"results/{filename}"
    fig.savefig(path, dpi=300, bbox_inches='tight')
    print(f"📊 Plot saved: {path}")
