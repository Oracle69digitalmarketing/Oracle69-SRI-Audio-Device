# Oracle69 SRI Audio Device

**A proof-of-concept for a low-cost, offline audio device to deliver System of Rice Intensification (SRI) instructions to smallholder farmers in Nigeria.**

This repository contains the design, firmware, and documentation for a purpose-built audio player. Its sole function is to store and play pre-recorded agricultural guidance in local dialects, designed to overcome connectivity and literacy barriers for farmers in Ondo and Ekiti States.

> **This prototype directly supports the [D-Prize Concept Note](https://www.d-prize.org) for the venture "Oracle69."**

---

## 🎯 Core Principle: Simplicity & Cost-Effectiveness

This device is intentionally a "dumb" audio player—not a smartphone or AI chatbot. This design minimizes cost (<$35), maximizes battery life, simplifies use for all literacy levels, and ensures perfect reliability offline.

| Aspect | Why It's a Better Fit for This Pilot |
| :--- | :--- |
| **Cost** | **Very Low (<$35).** No expensive smartphones, data plans, or server costs. |
| **Usability** | **Press button, listen.** Requires no literacy or digital skills. |
| **Reliability** | **Fully offline, long battery.** Works anywhere, independent of cellular signal. |
| **Scalability** | **Easy to clone and distribute.** Simple hardware is quick to assemble and repair locally. |
| **Focus** | **Distribution of proven knowledge.** Technology is an enabler, not the product. |

---

## 📁 Repository Structure

```

oracle69-sri-audio-device/
├──README.md                       # This file
├──firmware/
│├── audio_player.py            # Main Python script for playback
│└── requirements.txt           # Python dependencies
├──audio_content/
│├── sri_step_1_ile_iseto.mp3   # Example: Land Prep (Yoruba)
│└── ...                        # All SRI steps in local dialects
├──docs/
│├── 01_BILL_OF_MATERIALS.md    # Detailed cost and component list
│├── 02_ASSEMBLY_GUIDE.md       # Step-by-step hardware setup
│└── 03_USER_FLOW.md            # How a farmer interacts with the device
├──LICENSE                        # MIT License
└──.gitignore

```


---

## ⚙️ Quick Start for Developers

### Prerequisites
- Raspberry Pi Zero 2 W or similar
- MicroSD card (8GB+), USB speaker, push buttons, wires, case.

### Setup & Installation
1.  **Flash OS:** Install Raspberry Pi OS Lite onto the microSD card.
2.  **Copy Files:** Clone this repository or copy the `firmware/` and `audio_content/` folders to the Pi.
3.  **Install Dependencies:** SSH into the Pi and run:
    ```bash
    sudo apt update
    sudo apt install -y python3 python3-pip
    pip3 install -r firmware/requirements.txt
    ```
4.  **Connect Hardware:** Follow the [Assembly Guide](docs/02_ASSEMBLY_GUIDE.md) to wire buttons to GPIO pins and connect a speaker.
5.  **Run on Boot (Optional):** To start the player automatically, add this to `/etc/rc.local` (before `exit 0`):
    ```bash
    sudo python3 /home/pi/firmware/audio_player.py &
    ```

---

## 🧑‍🌾 User Flow

The device is designed for instant, intuitive use. See the full [User Flow](docs/03_USER_FLOW.md).
1.  **POWER ON** with a physical key.
2.  **PRESS** a large, labeled button (e.g., "Step 3: Omi" for Water).
3.  **LISTEN** to the clear, pre-recorded instruction in Yoruba, Ijaw, etc.
4.  **REPLAY** by pressing the same button, or choose another lesson.

---

## 🔗 Connection to the D-Prize Proposal

This repository is the tangible, technical foundation of the "Oracle69" distribution model described in our D-Prize concept note. It proves our commitment to:
*   **Appropriate Technology:** Choosing the simplest, most robust tool for the problem.
*   **Execution Capability:** Demonstrating we can build, prototype, and iterate.
*   **Cost-Effective Scaling:** Providing a transparent blueprint for a sub-$35 unit that can be manufactured at scale.

---

## 📄 License

This project is open-source under the **MIT License**. See the [LICENSE](LICENSE) file for details.
