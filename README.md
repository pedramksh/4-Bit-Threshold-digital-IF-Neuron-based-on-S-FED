# 4-Bit-Threshold-digital-IF-Neuron-based-on-S-FED
This is a simulation file repository for a 4-Bit Threshold digital IF Neuron

# Digital S-FED Integrate-and-Fire Spiking Neuron

This repository contains the Verilog-A behavioral models, standard cell logic gates, and top-level simulation files for a fully digital 4-bit Integrate-and-Fire (IF) spiking neuron built using **25-nm Side-Contacted Field-Effect Diode (S-FED)** technology.

This architecture achieves complete operational stability at a clock frequency of **1.095 GHz** while significantly reducing static and dynamic power compared to traditional CMOS baselines.

## Key Performance Benchmarks

Compared to a predictive 23-nm low-power CMOS baseline at 1.095 GHz:
* **Static Leakage Power:** 1.17 µW (a **2.6× reduction** from 3.18 µW CMOS)
* **Dynamic Energy:** 768 fJ/spike (a **4.5× reduction** from 3.47 pJ/spike CMOS)
* **Operating Frequency:** Scaled from 2.32 MHz (prior analog layouts) to **1.095 GHz** (this digital register-accumulator architecture)
* **Transistor Sizing:** Perfectly symmetrical layout ($W_p = W_n = 1\,\mu\text{m}$), eliminating area-expensive asymmetric conventional sizing rules.

## Architecture Overview

The design shifts the neuromorphic processing paradigm away from noise-susceptible analog charging capacitors into a synchronous 4-bit accumulator framework consisting of:
1. **Input Synchronization Layer:** Master-slave D-flip-flops aligning asynchronous incoming events to mitigate metastability.
2. **Membrane Potential Integration Subsystem:** A 4-bit ripple-carry adder where input spikes feed directly into the carry-in ($C_{in}$) terminal, eliminating bulky multipliers.
3. **Magnitude Comparison Subsystem:** A 4-bit MSB-priority comparator tracking threshold crossings against a user-defined register.
4. **Glitch-Removal Block:** An output synchronization flip-flop ensuring clean, hazard-free spike delivery.
5. **Immediate Reset Feedback Mask:** An instant combinational mask loop ($D_i = \text{SUM}_i \cdot (1 - ge)$) preventing over-integration errors within the same clock cycle.

## Repository Structure

```text
├── python_pipeline/   # Automation scripts for TCAD data extraction
├── verilog_a_models/  # Derivative-safe Verilog-A LUT compact models with soft-clipping
├── standard_cells/    # Symmetrical logic cell definitions (NOT, NAND, NOR, XOR)
└── neuron_core/       # 4-bit digital register-accumulator and top-level designs
