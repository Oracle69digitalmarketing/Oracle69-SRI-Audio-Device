#!/usr/bin/env python3
"""
Oracle69 SRI Audio Player - Main Firmware
A simple, robust script that plays specific MP3 files when GPIO buttons are pressed.
"""

import os
import time
import subprocess
from gpiozero import Button  # Simple GPIO library

# ============================================================================
# CONFIGURATION: Map GPIO Pins (BCM numbering) to Audio Files
# ============================================================================
# Each button is wired to a GPIO pin. When pressed, it plays the corresponding file.
BUTTON_MAP = {
    17: "/home/pi/audio_content/sri_step_1_ile_iseto.mp3",    # Land Preparation
    27: "/home/pi/audio_content/sri_step_2_gbigbin.mp3",      # Planting
    22: "/home/pi/audio_content/sri_step_3_omi.mp3",          # Water Management
    23: "/home/pi/audio_content/sri_step_4_abuje.mp3",        # Weeding
    24: "/home/pi/audio_content/sri_step_5_imularada.mp3",    # Soil Fertility
    25: "/home/pi/audio_content/sri_step_6_ikore.mp3",        # Harvest & Post-Harvest
}

# ============================================================================
# AUDIO PLAYBACK FUNCTION
# ============================================================================
def play_audio(file_path):
    """Plays the specified MP3 file using omxplayer (optimized for Raspberry Pi)."""
    if os.path.exists(file_path):
        # Use 'omxplayer' for hardware-accelerated, low-latency audio on Raspberry Pi
        # The '-o local' flag outputs to the audio jack/USB speaker.
        try:
            subprocess.call(['omxplayer', '-o', 'local', file_path], stdin=subprocess.PIPE)
        except Exception as e:
            print(f"[ERROR] Could not play {file_path}: {e}")
    else:
        print(f"[WARNING] Audio file not found: {file_path}")

# ============================================================================
# MAIN PROGRAM
# ============================================================================
def main():
    print("\n" + "="*50)
    print("Oracle69 SRI Audio Device - Firmware Started")
    print("="*50)

    # Create Button objects for each step
    buttons = {}
    for pin, audio_file in BUTTON_MAP.items():
        if os.path.exists(audio_file):
            # Create a button on this GPIO pin
            btn = Button(pin)
            # Assign the audio file to play when the button is pressed
            btn.when_pressed = lambda af=audio_file: play_audio(af)
            buttons[pin] = btn
            print(f"[OK] GPIO {pin:2d} -> {os.path.basename(audio_file)}")
        else:
            print(f"[SKIP] GPIO {pin:2d} -> File missing: {os.path.basename(audio_file)}")

    print("\n✅ Device is ready. Press any button to play SRI instructions.")
    print("   (Press Ctrl+C to shut down)")

    # Keep the program running forever
    try:
        while True:
            time.sleep(1)
    except KeyboardInterrupt:
        print("\n\n🔄 Device shutting down gracefully.")
        # Clean up GPIO resources
        for btn in buttons.values():
            btn.close()

if __name__ == "__main__":
    main()
