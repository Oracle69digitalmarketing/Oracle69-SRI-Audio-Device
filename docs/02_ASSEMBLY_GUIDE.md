# Hardware Assembly Guide

## 1. Gather Components
Ensure you have all items from the [Bill of Materials](01_BILL_OF_MATERIALS.md).

## 2. Prepare the Raspberry Pi
*   Flash **Raspberry Pi OS Lite** onto the microSD card using the official Raspberry Pi Imager tool.
*   Enable SSH by placing an empty file named `ssh` in the boot partition of the SD card (for headless setup).

## 3. Basic Wiring Diagram
Connect the components as follows:


**Important:** Use a **10kΩ pull-down resistor** for each button if your buttons aren't already built with one, or rely on `gpiozero`'s internal pull-ups in the software (already configured in `audio_player.py`).

## 4. Case Assembly
*   Place the Raspberry Pi and power bank inside the 3D-printed case.
*   Mount the buttons on the lid, ensuring they are clearly labeled (e.g., with icons or numbers).
*   Secure the speaker so the sound output is not muffled.

## 5. First Boot & Test
1.  Insert the SD card, connect the speaker and power bank.
2.  Wait 60 seconds for the Pi to boot.
3.  Press a button. You should hear the corresponding audio file play.
4.  If no sound, check speaker connection and audio volume (`alsamixer` command via SSH).
