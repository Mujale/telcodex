# 6G Network Evolution — Features Studied in 3GPP

This document describes the 6G features that 3GPP has **studied or is currently studying**.
Every feature below maps to a 3GPP study item (Technical Report) or to normative work (Technical Specification). 

3GPP structures 6G across two releases:

- **Release 20** — the bridge/pre-6G release. It completes 5G-Advanced and launches the
  first 6G **study items** (Technical Reports, TRs). Some adjacent features are already
  **normative** (Technical Specifications, TSs) in Rel-20.
- **Release 21** — the first **normative 6G** release (first 6G TSs). Rel-21 scope is
  planned, not yet frozen; no Rel-21 6G TSs exist in the corpus at this snapshot date.

Each feature lists: **what it is**, **why it matters**, **the technical approach**, and the
**associated TR/TS or study/work item** where known.

> **Status key:** *Study* = Technical Report / feasibility study. *Normative* = Technical
> Specification with approved content. *Planned* = Rel-21 scope stated by 3GPP but not yet
> specified.

---

## Part 1 — RAN (Radio Access Network)

### 1. 6G Radio Scenarios and Requirements (channel modelling)

- **Spec / item:** TR 38.914 · work item *FS_6G_RAN* · **Study (in progress)**
- **What it is:** The RAN-level study of propagation scenarios, channel models, and
  radio-layer KPIs needed to design the 6G air interface — the RAN counterpart to the SA1
  requirements study (TR 22.870).
- **Why it matters:** Accurate channel models for the new bands are the prerequisite for all
  subsequent physical-layer and AI-native link design; without them nothing downstream can
  be calibrated.
- **Technical approach:** Defines deployment scenarios (dense indoor hotspot, outdoor macro,
  sidelink/D2D, NTN-integrated, sub-THz short range); extends channel models to sub-THz
  (100–300 GHz) and the upper mid-band (7–24 GHz); sets KPIs such as Tbps-class peak
  downlink, high edge rates, very low BLER targets, and ~1 cm positioning. Evaluates waveform
  candidates for high-mobility / high-Doppler conditions.

### 2. Sub-THz and Upper Mid-Band New Radio (spectrum)

- **Spec / item:** under TR 38.914 / 6G radio study · work item *FS_6G_NR_spectrum* · **Study**
- **What it is:** Study of new 6G candidate spectrum — sub-THz (100–300 GHz, the D-/G-band
  region) and the upper mid-band (7–24 GHz, "FR3").
- **Why it matters:** 5G mmWave stops around 52.6 GHz. Sub-THz unlocks Tbps peak rates over
  short ranges (indoor hotspots, backhaul); FR3 balances coverage and capacity for wide-area
  6G.
- **Technical approach:** Sub-THz needs near-field beamforming, reconfigurable intelligent
  surfaces, and new antenna structures because path loss and Doppler behaviour differ from
  mmWave. FR3 is studied for >1 GHz carrier bandwidth with beam management traded between FR1
  and FR2 characteristics. Both feed the 6G band definitions.

### 3. AI-Native Radio (AI for PHY and L2)

- **Spec / item:** part of *FS_6G_RAN*, building on Rel-19 AI/ML for NR (TR 38.843) ·
  work item *FS_6G_AI_NR* · **Study (transitioning from 5G add-on to 6G native)**
- **What it is:** Where 5G treated AI/ML as an add-on for specific functions (CSI feedback,
  beam management, positioning), 6G studies making AI-native the **default** design principle
  across PHY (channel estimation, decoding), MAC (scheduling), and RRC (mobility).
- **Why it matters:** AI-native radio adapts to fast-changing environments without manual
  parameter tuning, approaching optimal performance across heterogeneous scenarios.
- **Technical approach:** Neural-network-based channel coding candidates (e.g. autoencoders
  for specific channels), learned waveforms, and over-the-air training signalling; a
  framework for the network to provision/version AI models to UEs with trust handling; and an
  "AI split" placing functions at the UE, gNB-DU, gNB-CU, or core per latency/compute
  trade-off.

### 4. Integrated Sensing and Communication (ISAC) — radio aspects

- **Spec / item:** radio design under the 6G RAN study; requirements TS 22.137, architecture
  TS 23.137 · work item *ISAC_REQ / Sensing* · **Requirements normative, radio under study**
- **What it is:** The same network serves double duty — carrying communication traffic while
  also performing radar-like measurement, reusing its own transmissions to locate, follow, and
  identify objects nearby.
- **Why it matters:** A defining 6G capability — automotive perception, object/UAV tracking,
  gesture recognition, cm-level positioning, and environmental monitoring, all without
  dedicated sensor infrastructure.
- **Technical approach:** Sensing KPIs (range, velocity, angular resolution), multi-target
  tracking, and co-existence with communication QoS; monostatic/bistatic sensing geometries;
  interference management between sensing and data transmission.

### 5. Reconfigurable Intelligent Surfaces (RIS)

- **Spec / item:** TR 38.858 (Rel-18/19 foundation), extended for 6G · work item *FS_RIS* ·
  **Rel-18 study complete; 6G normative work planned**
- **What it is:** Engineered surfaces whose electromagnetic response can be tuned so that
  incident radio waves are steered toward a chosen direction, redirecting signals without an
  active transmit chain.
- **Why it matters:** Useful for closing coverage gaps at sub-THz frequencies, where
  propagation loss is high, and for broad indoor/outdoor coverage at lower energy cost than
  deploying more active base stations.
- **Technical approach:** A control interface on the network side to set the surface's
  phase-shift pattern, channel-estimation methods that take the surface into account, and
  treatment of the RIS as a new network entity with management and orchestration hooks.

### 6. Network Energy Efficiency / Green RAN

- **Spec / item:** TS 28.310 (energy-efficiency management), scenarios in TR 38.914 ·
  work item *FS_6G_NR* + energy management · **5G normative; 6G extensions under study**
- **What it is:** Study of radio-node energy consumption at architectural and physical-layer
  levels — base-station sleep modes, dynamic spectrum sharing, and inter-node coordination to
  reduce carbon footprint.
- **Why it matters:** 6G treats a large energy-efficiency-per-bit improvement as a design
  constraint as fundamental as peak data rate.
- **Technical approach:** Extended DTX/DRX including base-station deep sleep; AI-driven
  traffic prediction with pre-emptive sleep scheduling; energy-proportional hardware in the
  TR 38.914 scenarios; OAM energy KPIs and reporting (TS 28.310, TS 28.552).

---

## Part 2 — SA (Service & System Aspects / Architecture)

### 7. 6G Use Cases and Service Requirements

- **Spec / item:** TR 22.870 · work item *FS_6G_Requirements* (SA1) · **Study (TR reported
  complete)**
- **What it is:** The foundational SA1 requirements study. It collects use cases from
  verticals (industry, public safety, health, immersive media, space), derives KPIs, and
  identifies gaps versus 5G service requirements (TS 22.261).
- **Why it matters:** The later architecture and radio work is shaped by what this study
  concludes. It sets the headline targets — Tbps-class peak rates, sub-millisecond latency,
  non-terrestrial coverage, and very high device density (order 10⁷ devices/km²).
- **Technical approach:** Use-case workshops → candidate KPI tables → gap analysis against
  TS 22.261 → new normative requirements, covering holographic communication, tactile/haptic
  services, extreme-reliability industrial control, and space-segment connectivity.

### 8. Mobile Metaverse Services

- **Spec / item:** TS 22.156 · work item *Mobile Metaverse* (SA1) · **Normative (active in
  Rel-20)**
- **What it is:** Service requirements for immersive, multi-user 3D shared environments
  delivered over the mobile network — avatars, shared spatial experiences, haptics, and
  holographic rendering.
- **Why it matters:** A key 6G use-case driver, requiring order-of-magnitude improvements in
  latency, bandwidth, and multi-user synchronisation over 5G.
- **Technical approach:** Stage 1 requirements for very low end-to-end latency (haptics and
  visual rendering), high per-user data rates, synchronisation across UEs in a shared scene,
  split rendering (compute in the network), and privacy for avatar/identity data.

### 9. Integrated Sensing and Communication (ISAC) — architecture

- **Spec / item:** TS 22.137 (Stage 1), TS 23.137 (Stage 2), SA6 enablement TS 23.255 ·
  **Requirements normative; architecture active**
- **What it is:** The system-level framework that turns sensing into a network service.
- **Why it matters:** Supplies the architecture and APIs through which applications can
  request sensing and receive the results, exposing sensing as a network service.
- **Technical approach:** A Sensing Service Function interfacing with the core, a sensor-data
  management framework, and procedures for network-controlled versus UE-controlled sensing;
  SA6 adds application-layer sensing enablement via SEAL (TS 23.255).

### 10. Ambient IoT / Zero-Energy Devices (Phase 2)

- **Spec / item:** TS 22.369, TS 23.369, TS 23.370, radio TS 38.191 / TS 38.291 ·
  work item *AmbientIoT_Ph2* · **Normative (multiple Rel-20 CRs approved)**
- **What it is:** Battery-free devices powered by harvested energy (from radio signals, light,
  or motion) that talk over NR, with the network serving as both their energy source and their
  interrogator.
- **Why it matters:** Enables extreme device density by removing the battery barrier for
  billions of sensors, tags, and actuators (logistics, healthcare, smart environments).
- **Technical approach:** Device classes DO (Duty-Cycled Only) and DO-A (DO with Active
  transmission) at sub-mW power; a gNB-Reader/interrogator architecture (TS 23.369); AIoT NAS
  (TS 24.369) and radio PHY (TS 38.191 / TS 38.291); temporary identifiers (TS 23.003) and
  OAM support (TS 28.541).

### 11. Energy Services Phase 2 (network as an energy actor)

- **Spec / item:** TR 22.883 (study) → TS 22.261 (normative output) · work item
  *FS_EnergyServ_Ph2 / EnergyServ_Ph2-REQ* · **Study complete → normative requirements**
- **What it is:** The network as an active participant in energy grids — reporting energy
  consumption of UEs and nodes, responding to grid demand signals, enabling demand-response.
- **Why it matters:** Aligns the network with sustainability goals and supports grid
  flexibility services, complementing the per-bit energy-efficiency targets.
- **Technical approach:** New energy-related KPIs in TS 22.261; requirements to expose energy
  metrics to authorised third parties; per-session/application energy-footprint reporting.

### 12. Next-Generation Core Architecture (6G System)

- **Spec / item:** 6G Core architecture study (TR to be assigned) · work item *FS_6G_Arch*
  (SA2) · **Study (starting in the Rel-20 timeframe)**
- **What it is:** The SA2 study of the architecture for the 6G System — what evolves from or
  replaces the 5G Core's Service-Based Architecture (SBA).
- **Why it matters:** The 6G core must handle Tbps flows, sub-ms services, AI-native network
  functions, and seamless integration of terrestrial, non-terrestrial, and private networks.
- **Technical approach:** Disaggregated core NFs with finer-grained splitting; native compute
  integration (the network scheduling/migrating compute alongside data sessions); evolved
  network slicing from soft to hard resource partitions; and study of semantic communication
  (compressing at the level of meaning, not just bits).

### 13. Network Digital Twin (NDT)

- **Spec / item:** TS 28.561 (management of network digital twins) · work item *NDT-OAM*
  (SA5) · **Normative (active in Rel-20)**
- **What it is:** A live digital copy of the physical network, kept current from ongoing
  measurements and used to optimise, anticipate faults, and test changes before they are
  applied.
- **Why it matters:** 6G networks are too complex for human-in-the-loop management; NDTs
  enable autonomous, zero-touch operation and underpin intent-driven management.
- **Technical approach:** A management data model for the twin (data sources, synchronisation
  interfaces, lifecycle); integration with the closed-control-loop framework; and analytics
  fed from the core's data analytics function.

### 14. AI/ML Network Architecture (NWDAF evolution)

- **Spec / item:** TS 23.288 (NWDAF), TS 23.482 (AIML enablement), SA6 SEAL AIML TS 24.560 ·
  work item *AIML_Ph2-APP / eMDAS_Ph4* · **Normative (Phase 2 CRs approved in Rel-20)**
- **What it is:** Evolution of the 5G data-analytics function (NWDAF) toward an AI-native
  core, where AI/ML models are first-class network functions rather than analytical overlays.
- **Why it matters:** 6G defines AI as native infrastructure; the network must train, deploy,
  update, and retire models at scale for radio resource management, traffic prediction, and
  security.
- **Technical approach:** Distributed model training across multiple NWDAFs and a model
  repository/marketplace role; standardised AIML enablement APIs for vertical applications
  (TS 23.482); application-layer AIML service protocols (TS 24.560); and planned model
  lifecycle management (data provenance, versioning, explainability hooks).

---

## Part 3 — CT (Core Network Protocols)

### 15. Ambient IoT CT Protocols

- **Spec / item:** TS 24.369 (AIoT NAS), TS 29.369, TS 29.506 · work item *AmbientIoT_Ph2-CT*
  · **Normative (Rel-20 CRs approved)**
- **What it is:** CT1/CT4 define a new, stripped-down NAS variant (AIoT NAS) and service-layer
  APIs for ambient IoT devices that cannot perform normal 5G registration.
- **Why it matters:** Zero-energy devices need a radically lightweight protocol stack;
  standard 5G NAS is too heavyweight for battery-less operation.
- **Technical approach:** A minimal, event-driven "check-in" NAS state machine (no persistent
  registration); AIoT temporary identifiers (TS 23.003); SBI data-management services
  (TS 29.369); and UDR extensions for AIoT device data (TS 29.506).

### 16. Combined QoS Configuration and Monitoring (cross-layer end-to-end QoS)

- **Spec / item:** TS 22.261 (requirements) with SA2/CT follow-on · work item *CombQoS* ·
  **Requirements normative; architecture/CT work follows**
- **What it is:** A bidirectional QoS API letting authorised third parties provide end-to-end
  QoS parameters to the network and receive QoS monitoring reports back.
- **Why it matters:** 6G services (remote surgery, industrial control, holographic streaming)
  need the application to co-manage network QoS dynamically, not rely on static SLAs.
- **Technical approach:** New TS 22.261 clauses allowing a third party to inject end-to-end
  QoS parameters and to receive QoS reports; CT follow-on via Network Exposure Function (NEF)
  API extensions conveying third-party QoS intent to the policy (PCF) and session-management
  (SMF) functions.

---

## Reference Table — 3GPP Specs / Studies

| Spec | Title | Group | Rel | Type |
|---|---|---|---|---|
| TR 22.870 | 6G Use Cases and Service Requirements | SA1 | 20 | Study |
| TR 38.914 | 6G NR Scenarios and Requirements | RAN1/4 | 20 | Study |
| TS 22.137 | Integrated Sensing and Communication (requirements) | SA1 | 18+ | Normative |
| TS 23.137 | Integrated Sensing and Communication (architecture) | SA2 | 19/20 | Normative |
| TS 22.369 | Service requirements for Ambient IoT | SA1 | 18+ | Normative |
| TS 23.369 | Architecture for Ambient IoT | SA2 | 19/20 | Normative |
| TS 24.369 | Ambient IoT NAS protocol | CT1 | 20 | Normative |
| TS 22.156 | Mobile Metaverse Services | SA1 | 20 | Normative |
| TS 28.561 | Network Digital Twin management | SA5 | 20 | Normative |
| TS 23.288 | NWDAF architecture (AI/ML Phase 2) | SA2 | 20 | Normative |
| TS 23.482 | AIML Enablement Service | SA6 | 20 | Normative |
| TS 22.261 | Service Requirements for the 5G/6G System (updated) | SA1 | 20 | Normative |
| TR 38.858 | Reconfigurable Intelligent Surfaces study | RAN1 | 18 | Study |
| TS 28.310 | Energy-efficiency management | SA5 | 20 | Normative |


