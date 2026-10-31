# 6G &amp; 3GPP Glossary

A plain-language reference to the terms and abbreviations used across this site. Where a term
maps to a 3GPP specification or concept, it is noted. Terms are grouped for easier scanning.

## Releases and bodies

- **3GPP** — The partnership of regional standards bodies that develops mobile specifications. It produces Technical Reports and Technical Specifications, not legally binding standards on their own.
- **Release (Rel-NN)** — A numbered bundle of features frozen together. Release 20 is the 6G study phase; Release 21 is planned to carry the first 6G specifications.
- **Study Item / Work Item** — A study item explores feasibility and produces a Technical Report (TR); a work item produces normative Technical Specifications (TS).
- **TR / TS** — Technical Report (study output) / Technical Specification (normative output).
- **Stage 1 / 2 / 3** — Service requirements (Stage 1), system architecture (Stage 2), and detailed protocols (Stage 3).
- **ITU-R IMT-2030** — The international framework that defines the high-level vision and requirements for 6G, which 3GPP then specifies.

## Spectrum and radio

- **Sub-THz** — Very high frequencies around 100–300 GHz, offering huge bandwidth over short ranges.
- **Upper mid-band (FR3)** — Roughly 7–24 GHz, balancing coverage and capacity for wide-area 6G.
- **mmWave (FR2)** — The millimetre-wave range used in 5G, up to around 52.6 GHz.
- **Waveform** — The signal shape used to carry data; 5G uses cyclic-prefix OFDM.
- **Channel coding** — Error-protection coding; 5G uses LDPC for data and Polar codes for control.
- **Massive MIMO** — Using large antenna arrays to serve many beams and users at once.
- **RIS** — Reconfigurable Intelligent Surface: a tunable surface that steers radio waves without an active transmitter.
- **Beamforming** — Focusing radio energy in a direction rather than broadcasting everywhere.

## Access network (RAN)

- **RAN** — Radio Access Network: the base stations and radio link to devices.
- **gNB** — The 5G/6G base station.
- **CU / DU** — Central Unit and Distributed Unit: the functional split of the gNB. The CU hosts higher layers; the DU hosts lower layers.
- **CU-CP / CU-UP** — The control-plane and user-plane parts of the Central Unit.
- **F1 / E1** — Interfaces between the DU and CU (F1) and between the CU control and user planes (E1).
- **NG** — The interface between the base station and the core network.
- **Uu** — The radio interface between the device and the base station.

## Core network

- **5GC / Core** — The 5G Core network; the 6G core is its planned successor.
- **SBA** — Service-Based Architecture: the design where network functions expose services over common interfaces.
- **NF** — Network Function: a modular piece of core functionality.
- **AMF** — Access and Mobility Management Function: handles registration, authentication anchoring, and mobility.
- **SMF** — Session Management Function: manages data sessions, addressing, and QoS.
- **UPF** — User Plane Function: forwards user traffic and enforces QoS.
- **PCF** — Policy Control Function: sets session, access, and device policies.
- **NEF** — Network Exposure Function: the secure gateway to outside applications.
- **UDM / UDR** — Unified Data Management / Repository: subscriber data and the store behind it.
- **NWDAF** — Network Data Analytics Function: the core's AI/ML analytics engine.
- **NRF** — Network Repository Function: how functions discover each other.

## 6G concepts and features

- **AI-native** — Designing AI/ML into the network from the start, not adding it afterward.
- **ISAC** — Integrated Sensing and Communication: using the network to sense the environment as well as carry traffic.
- **SenF** — Sensing Function: the new core function introduced for ISAC (control part SenF-C, processing part SenF-P).
- **Ambient IoT** — Battery-free devices powered by harvested energy.
- **Network Digital Twin (NDT)** — A live software replica of the network used to simulate changes safely.
- **NTN** — Non-Terrestrial Network: satellite and high-altitude access integrated with the ground network.
- **Intent-driven management** — Operating the network by stating goals (intent) rather than configuring each parameter.
- **Closed control loop** — Automated collect → decide → act cycles that keep the network meeting its targets.

## Performance terms

- **KPI** — Key Performance Indicator: a measurable target such as latency or accuracy.
- **Latency** — The delay between sending and receiving; 6G targets sub-millisecond for some services.
- **Tbps** — Terabits per second; a 6G peak-rate ambition.
- **Positioning accuracy** — How precisely the network can locate a device or object.
- **Energy efficiency** — Performance delivered per unit of energy; a first-class 6G design goal.
