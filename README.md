# Structural health monitoring for dynamic bodies using their vibration signals

This project utilizes the **Empirical Mode Decomposition (EMD)** technique to analyze vibration data from a metro system and detect potential component failures.

### Table of Contents

-   [Project Overview](#project-overview)
-   [Methodology](#methodology)
-   [Installation](#installation)
-   [Key Steps in the Code](#key-steps-in-the-code)

---

### Project Overview

This project focuses on **fault detection and condition monitoring** of dynamic structures (such as machinery, bridges, vehicles, or rotating equipment) using their vibration signals. The idea is to automatically distinguish between healthy (normal) and faulty (failure) states of a system by analyzing the patterns hidden in vibration data.

Vibration signals from machinery can indicate its health. This project processes raw vibration data from a metro system to distinguish between normal operation and a component failure. The core of our approach is to use EMD to break down complex signals into simpler components, allowing us to find key features for a machine learning model.


---

### Methodology

The project follows these main steps:

Data Loading and Visualization: Load the raw data and plot it to visually identify differences between normal and failure signals.

Signal Windowing: Divide the long signal streams into smaller, fixed-size windows to create individual samples for analysis.

Feature Extraction: Calculate the energy of each sample and use EMD to potentially extract more detailed features from the signal's components.

Analysis: Use histograms to compare the energy distribution of normal vs. failure samples, demonstrating a clear difference that can be used for classification.


---

### Algorithms to be implemented

Random Forest: Handles feature interactions well, provides feature importance 

XGBoost/LightGBM: Gradient boosting for complex pattern recognition 

Support Vector Machines: Effective for high-dimensional feature spaces 

Deep Learning Advanced Models For sophisticated pattern recognition: 

1D-CNN: Convolutional networks for local pattern detection in time series 

LSTM/BiLSTM: Recurrent networks for temporal dependency modeling

Hybrid CNN-LSTM: Combined spatial and temporal feature extraction


---

### Installation

To run this notebook, you will need the following Python libraries. You can install them using `pip`:

```bash
pip install pandas numpy EMD-signal gdown



