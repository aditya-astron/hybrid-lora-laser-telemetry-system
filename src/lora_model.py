import numpy as np

class LoRaModel:
    # Standard LoRa sensitivities (dBm) @ 125 kHz BW
    SENSITIVITY = {7: -123, 8: -126, 9: -129, 10: -132, 11: -134.5, 12: -137}

    @staticmethod
    def path_loss(distance_km: float, freq_mhz: float = 868) -> float:
        # Log-distance model tuned for terrestrial + some atmospheric loss
        return 32.4 + 20 * np.log10(freq_mhz) + 30 * np.log10(distance_km) + np.random.normal(0, 3)

    @staticmethod
    def adaptive_sf(snr_db: float) -> int:
        for sf in range(7, 13):
            if snr_db > LoRaModel.SENSITIVITY[sf] + 3:  # +3 dB FEC margin
                return sf
        return 12

    @staticmethod
    def packet_success(snr_db: float, sf: int) -> bool:
        # Reed-Solomon + interleaving modeled as effective coding gain
        required = LoRaModel.SENSITIVITY[sf] + 1.5
        return snr_db > required
