# Downloads the given MicroPython release
# Usage: python download_release.py <release>

import argparse
import os
import requests

parser = argparse.ArgumentParser(description='Download MicroPython release')
parser.add_argument('release', help='MicroPython release to download (e.g. 20231227-v1.22.0')
args = parser.parse_args()

root_dir = os.path.dirname(os.path.dirname(os.path.realpath(__file__)))

def download_firmware(directory: str, firmware: str):
    url = f'https://micropython.org/resources/firmware/{firmware}'
    r = requests.get(url)
    with open(os.path.join(root_dir, directory, firmware), 'wb') as f:
        f.write(r.content)
    print(f'✅ Downloaded {directory}/{firmware}');


download_firmware('esp32', f'ESP32_GENERIC-{args.release}.bin')
download_firmware('esp32-s2', f'ESP32_GENERIC_S2-{args.release}.bin')
download_firmware('esp32-s3', f'ESP32_GENERIC_S3-{args.release}.bin')
download_firmware('esp32-c3', f'ESP32_GENERIC_C3-{args.release}.bin')
download_firmware('esp32-c5', f'ESP32_GENERIC_C5-{args.release}.bin')
download_firmware('esp32-c6', f'ESP32_GENERIC_C6-{args.release}.bin')
download_firmware('esp32-h2', f'ESP32_GENERIC_H2-{args.release}.bin')
download_firmware('esp32-p4', f'ESP32_GENERIC_P4-{args.release}.bin')
download_firmware('pi-pico', f'RPI_PICO-{args.release}.uf2')
download_firmware('pi-pico-w', f'RPI_PICO_W-{args.release}.uf2')
download_firmware('pi-pico-2', f'RPI_PICO2-{args.release}.uf2')
download_firmware('pi-pico-2w', f'RPI_PICO2_W-{args.release}.uf2')
download_firmware('nucleo-l432kc', f'NUCLEO_L432KC-{args.release}.hex')
