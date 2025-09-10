# Metro Vibration Analysis & Fault Detection

This project utilizes the **Empirical Mode Decomposition (EMD)** technique to analyze vibration data from a metro system and detect potential component failures.

### Table of Contents

-   [Project Overview](#project-overview)
-   [Installation](#installation)
-   [Usage](#usage)
-   [Data](#data)
-   [Methodology](#methodology)
-   [Key Steps in the Code](#key-steps-in-the-code)

---

### Project Overview

This project focuses on **fault detection and condition monitoring** of dynamic structures (such as machinery, bridges, vehicles, or rotating equipment) using their vibration signals. The idea is to automatically distinguish between healthy (normal) and faulty (failure) states of a system by analyzing the patterns hidden in vibration data.

Vibration signals from machinery can indicate its health. This project processes raw vibration data from a metro system to distinguish between normal operation and a component failure. The core of our approach is to use EMD to break down complex signals into simpler components, allowing us to find key features for a machine learning model.

---

### Installation

To run this notebook, you will need the following Python libraries. You can install them using `pip`:

```bash
pip install pandas numpy EMD-signal gdown
