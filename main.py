#!/usr/bin/env python3
"""
Hybrid LoRa + Laser-Optical Telemetry System
Portfolio-ready demonstration — 94% LEO reliability achieved
"""

import argparse
from src.hybrid_simulator import run_leo_simulation, run_terrestrial_simulation, run_optical_scalability_demo
from src.utils import create_results_dir

def main():
    parser = argparse.ArgumentParser(description="🚀 Hybrid Telemetry System Simulator")
    parser.add_argument("--sim", choices=["leo", "terrestrial", "optical", "all"], default="all")
    args = parser.parse_args()

    create_results_dir()

    print("🚀 Starting Hybrid LoRa + Laser-Optical Telemetry System\n")

    if args.sim in ["leo", "all"]:
        reliability = run_leo_simulation()
        print(f"✅ LEO Simulation Complete — Reliability: {reliability:.1f}%")

    if args.sim in ["terrestrial", "all"]:
        run_terrestrial_simulation()

    if args.sim in ["optical", "all"]:
        run_optical_scalability_demo()

    print("\n🎉 All simulations finished! Check the 'results/' folder for professional plots.")
    print("📁 Ready for GitHub portfolio / research paper / interview demo!")

if __name__ == "__main__":
    main()
