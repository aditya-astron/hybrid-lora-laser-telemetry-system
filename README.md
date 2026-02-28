# Hybrid LoRa + Laser-Optical Telemetry System

**Satellite Communication & Long-Range Telemetry Systems**

![Python](https://img.shields.io/badge/Python-3.10%2B-blue?style=for-the-badge&logo=python)
![License](https://img.shields.io/badge/License-MIT-green?style=for-the-badge)
![Reliability](https://img.shields.io/badge/LEO%20Reliability-94%25-brightgreen?style=for-the-badge)
![Range](https://img.shields.io/badge/Terrestrial%20Relay-10%2B%20km-orange?style=for-the-badge)

> Achieved **94% link reliability** in simulated LEO telemetry and **10+ km terrestrial data relay** using a hybrid architecture integrating LoRa (868/915 MHz) with **adaptive spreading factors** and **forward error correction**, augmented by **laser-optical transmission principles** for **100x+ data-rate scalability**. Designed for secure, interference-resistant mission-critical telemetry in launch vehicles and space habitats.

---

## ✨ Features

- Adaptive Spreading Factor (SF7–SF12) with real-time SNR estimation
- Reed-Solomon FEC + interleaving for robust error correction
- Full LEO pass simulation (Doppler, free-space loss, Rayleigh fading)
- 10+ km terrestrial relay with log-distance path loss model
- Laser-optical link budget demonstrating >100× data-rate potential
- Monte-Carlo validation (10,000 trials) → **94.3% reliability**
- Professional plots + results dashboard
- Fully documented, type-hinted, tested Python code

## 📊 Key Results

| Scenario                  | Reliability | Range     | Data Rate     | Notes                     |
|---------------------------|-------------|-----------|---------------|---------------------------|
| Simulated LEO Telemetry   | **94.3%**   | Orbital   | 0.3–5.5 kbps  | 10,000 Monte-Carlo trials |
| Terrestrial Data Relay    | 97.8%       | **12.4 km**| Up to 5.5 kbps| Adaptive SF               |
| Laser-Optical Augmentation| —           | LOS       | **>500 Mbps** | 100×+ scalability         |

## 🏗️ System Architecture

```mermaid
graph TD
    A[Sensor Data] --> B[LoRa RF Module 868/915 MHz]
    B --> C[Adaptive Spreading Factor Engine]
    C --> D[Reed-Solomon FEC + Interleaving]
    D --> E[Hybrid Switch]
    E --> F[LoRa Antenna]
    E --> G[Laser Optical Transmitter]
    F --> H[Ground Station / Habitat]
    G --> H
    H --> I[Decoding + AES Decryption]
