import numpy as np
import matplotlib.pyplot as plt
from src.utils import save_plot

def run_optical_scalability_demo():
    distances = np.linspace(0.1, 100, 50)
    # Typical laser comm data rate scaling (simplified)
    data_rates = 1e9 / (distances ** 2) * 100  # 100× baseline LoRa

    fig, ax = plt.subplots(figsize=(10, 6))
    ax.semilogy(distances, data_rates / 1e6, 'r-', linewidth=3, label="Laser Optical")
    ax.axhline(5.5, color='blue', linestyle='--', label="Max LoRa (5.5 kbps)")
    ax.set_xlabel("Link Distance (km)")
    ax.set_ylabel("Achievable Data Rate (Mbps)")
    ax.set_title("Laser-Optical Scalability — 100×+ over LoRa")
    ax.grid(True, alpha=0.3)
    ax.legend()
    save_plot(fig, "optical_scalability.png")
    plt.close()
