# Ambient IoT — Battery-Free Devices Explained

Ambient IoT (A-IoT), sometimes called zero-energy IoT, is one of the most striking ideas feeding
into 6G: tiny devices that run with **no battery at all**, powered entirely by energy harvested
from their surroundings. This page explains what they are, how they work, the network
architecture 3GPP has defined, and where they fit.

> **Status:** Ambient IoT reached its **first normative release in 5G-Advanced (Release 19)**,
> building on a Release 18 study. Release 20 continues the work, and the concept is a central
> design goal carried toward 6G.

## What an ambient IoT device is

An ambient IoT device is an IoT device powered by **energy harvesting** — either completely
battery-less or with only a small store such as a capacitor. The energy comes from radio waves,
light, motion, heat, or similar ambient sources. Compared with earlier low-power IoT devices,
an ambient IoT device is **simpler, smaller, cheaper, and lower-power**, carries only small
amounts of data, and is designed for maintenance-free operation at massive scale.

The defining constraint: the network **cannot assume the device is powered** at any given moment.
It communicates only when it has harvested enough energy. That single fact reshapes how the
protocols are designed.

## How it is powered

3GPP describes two harvesting modes:

- **Continuous harvesting** — the device regularly receives enough ambient energy (for example,
  a light-powered sensor in daylight).
- **Incidental harvesting** — energy is available only when the event the device must report
  occurs (for example, a vibration sensor that harvests from the vibration it detects).

Some devices can also be **powered on demand**, energised by radio waves beamed from the network,
which makes passive tags predictable to interact with.

## How it communicates: backscatter

The zero-energy trick is on the uplink. Instead of generating its own signal (which costs power),
the device **reflects and modulates** an incoming carrier wave — a technique called
**backscatter**. This device-to-reader path needs almost no energy. In the other direction, the
reader-to-device path uses a simple on-off-keying waveform aligned with the normal NR structure,
so a device only has to detect the presence or absence of energy — again, cheap to do.

Devices range from **fully passive** (backscatter only, no storage) through **semi-passive**
(a small capacitor buffers energy for more reliable reception) to more capable variants aimed at
sensor and actuator tasks.

## The network architecture

The key innovation is turning the base station into a **reader**:

- The **reader** (in this release, a gNB-reader) is the active network-side transceiver. It sends
  the reader-to-device waveform — which also energises passive devices — and receives the
  backscattered responses.
- A gNB can serve one or more readers; each reader belongs to one gNB. Readers map to
  **A-IoT Areas**, so operations can be scoped geographically.
- A new core function, the **Ambient IoT Function (AIOTF)**, orchestrates the service. The base
  station connects to it either **directly** or **indirectly via the access-and-mobility function
  (AMF)**, which forwards the ambient-IoT information transparently.

## What it does: the two main procedures

- **Inventory** — the network discovers which devices are present in an area. It triggers a
  broadcast, and devices in range respond with their identifier and optional status, measurement,
  or location data.
- **Command** — the network sends a targeted instruction to one or more devices (for example,
  trigger an actuator or change a setting).

## Where it is used

Typical use cases span logistics, retail, industry, agriculture, healthcare, and smart cities:

- **Inventory taking** — discovering boxes, containers, tools, or packages in an area.
- **Sensor data collection** — reporting readings such as temperature or pressure.
- **Asset tracking** — locating goods, sometimes with a capable handset acting as a local reader.
- **Actuator control** — network-initiated commands to simple actuators.

## Reference points (3GPP)

- **TR 38.848** — the ambient power-enabled IoT study.
- **TS 22.369 / TS 22.261** — service requirements for ambient IoT.
- **TS 23.369** — the system architecture (the AIOTF and procedures).
- **TS 38.300 §16.23** — the radio interface and RAN architecture.

## In short

Ambient IoT removes the battery — the biggest barrier to deploying sensors at enormous scale —
by harvesting energy and using backscatter to communicate. First standardised in 5G-Advanced, it
is a foundational building block for the extreme device density that 6G targets.
