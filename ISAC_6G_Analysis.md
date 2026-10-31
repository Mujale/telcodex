# ISAC — Integrated Sensing and Communication: Detailed Technical Analysis
### 3GPP Specifications | Releases 19–21 (5G Advanced / 6G Roadmap)

> **Document Status:** Research analysis based on 3GPP TS 22.137 (Stage 1), TS 23.137 (Stage 2),
> and the Rel-20 system architecture overview.
> All normative citations are drawn directly from the 3GPP specification corpus.

---

## Table of Contents

1. [Overview and Definition](#1-overview-and-definition)
2. [Standardization Roadmap](#2-standardization-roadmap)
3. [Governing Specifications](#3-governing-specifications)
4. [Use Cases and Service Categories](#4-use-cases-and-service-categories)
5. [Functional Requirements (Stage 1 — TS 22.137)](#5-functional-requirements-stage-1--ts-22137)
6. [System Architecture (Stage 2 — TS 23.137)](#6-system-architecture-stage-2--ts-23137)
7. [Key Performance Requirements (KPIs)](#7-key-performance-requirements-kpis)
8. [End-to-End Sensing Procedures](#8-end-to-end-sensing-procedures)
9. [Network Function Services](#9-network-function-services)
10. [Security, Privacy and Authorization](#10-security-privacy-and-authorization)
11. [Energy Efficiency Considerations](#11-energy-efficiency-considerations)
12. [ISAC in the 6G Context (Rel-20/21)](#12-isac-in-the-6g-context-rel-2021)
13. [Open Issues and Future Work](#13-open-issues-and-future-work)
14. [Abbreviations](#14-abbreviations)
15. [References](#15-references)

---

## 1. Overview and Definition

**Integrated Sensing and Communication (ISAC)** is a paradigm that enables a cellular radio
network to simultaneously perform traditional wireless communication *and* environmental
radio-frequency sensing using shared hardware, spectrum, and waveforms. Rather than dedicating
separate radar infrastructure for sensing, ISAC embeds sensing capability natively into the 3GPP
radio access network (RAN) and 5G Core (5GC).

The 3GPP defines 5G wireless sensing service as:

> *"…capabilities for sensing one or more objects in the environment, monitoring environmental
> conditions, and human motion and gestures to enable more diversified applications."*
> — **TS 22.137 §5.1**

The service includes:

- **Collection** of 3GPP sensing data from sensing receivers
- **Secure delivery** of sensing data for processing
- **Controlled exposure** of sensing results to authorized third parties (Application Functions)

---

## 2. Standardization Roadmap

| 3GPP Release | Status | ISAC Role |
|---|---|---|
| **Rel-18** (5G Advanced) | Frozen | Study item on sensing; TS 22.137 skeleton started (v0.0.0 May 2023) |
| **Rel-19** | Frozen | TS 22.137 Stage 1 service requirements stabilized (v19.x.x) |
| **Rel-20** | In progress | TS 23.137 Stage 2 architecture published; gNB-based sensing introduced |
| **Rel-21** | Future (6G) | 6G ISAC functional requirements and extended KPI categories added to TS 22.137 |

> **Note:** 3GPP TS 22.137 change history shows the specification evolved from an initial skeleton
> (May 2023, v0.0.0) through multiple MCC cycles to v21.0.0 (September 2026), introducing
> advanced 6G ISAC functional requirements in Release 21.

---

## 3. Governing Specifications

### Primary ISAC Specifications

| Specification | Stage | Title | Key Content |
|---|---|---|---|
| **TS 22.137** | Stage 1 | Integrated Sensing and Communication | Service requirements, use cases, KPIs |
| **TS 23.137** | Stage 2 | Integrated Sensing and Communication | Architecture, NFs, procedures, protocols |

### Supporting Specifications (Referenced by ISAC)

| Specification | Relevance |
|---|---|
| TS 23.501 | 5G System Architecture — base for SenF integration |
| TS 23.502 | 5GC Procedures — NRF registration used by SenF |
| TS 38.300 | NR Overall Description — gNB as Sensing Entity |
| TS 38.xxx / 38.xxy | RAN-level sensing spec (TBD — pending RAN coordination) |

---

## 4. Use Cases and Service Categories

TS 22.137 §6.2 defines **7 sensing service categories** spanning a wide range of applications:

### Category Overview

| # | Category | Example Applications | Target Objects |
|---|---|---|---|
| **1** | Outdoor Object Detection & Tracking | UAV/drone airspace management, bird strike avoidance | UAVs (1.6×1.5×0.7 m), birds |
| **2** | Indoor Object Detection & Tracking | Smart building intruder detection, asset tracking | Humans (0.5×0.5×1.75 m) |
| **3** | Environmental Monitoring | Flood detection, infrastructure inspection | Water level, structures |
| **4** | Public Safety Sensing | Crowd monitoring, search & rescue | Humans, vehicles |
| **5** | Vehicle Detection & Tracking | Road traffic management, collision avoidance | Vehicles (7.5×2.5×3.5 m) |
| **6** | Motion Monitoring | Healthcare (sleep/respiration), sports analytics | Human body motions |
| **7** | Fine-Grained Sensing | Gesture recognition, industrial robotics, factory automation | Sub-metre targets |

> **Category 7** has the most stringent KPI requirements (higher positioning accuracy, finer
> sensing resolution) and typically requires more radio resources — TS 22.137 §6.2 NOTE 6.

### Key Target Object Dimensions (from TS 22.137 §6.2 NOTE 1)

| Object | Length (m) | Width (m) | Height (m) |
|---|---|---|---|
| UAV | 1.6 | 1.5 | 0.7 |
| Human | 0.5 | 0.5 | 1.75 |
| Vehicle | 7.5 | 2.5 | 3.5 |

---

## 5. Functional Requirements (Stage 1 — TS 22.137)

### 5.1 Core Sensing Capabilities

Per **TS 22.137 §5.2.1**, the 5G system shall:

1. **Detect and/or track** one or more objects (e.g., UAVs, birds) and the environment around them
2. **Collect 3GPP sensing data** from sensing receivers based on operator policies
3. **Provide sensing services** in a defined Target Sensing Service Area using coordinated sensing transmitters and receivers
4. **Activate, configure, and deactivate** sensing based on location and network load (subject to regulation)
5. **Support sensing continuity** for moving objects
6. **Support roaming scenarios** for sensing services (subject to operator policy)
7. **Prioritize** sensing services among themselves and relative to communication services

### 5.2 Non-3GPP Sensing Data Integration

The 5G system may augment its 3GPP sensing data with data from non-3GPP sensors:

> *"Subject to user consent, regulation, and operator's policy, the 5G system shall be able to
> collect non-3GPP sensing data from authorized non-3GPP sensors and securely provide it to
> 5G network… the 5G system should support the joint processing of the 3GPP sensing data and
> non-3GPP sensing data to derive a combined sensing result."*
> — **TS 22.137 §5.2.1**

### 5.3 Unlicensed Spectrum and V2X Sensing

- UEs **without 5G RAN coverage** may use unlicensed spectrum to provide sensing service (subject to local regulation)
- UEs supporting **V2X applications** may perform 5G wireless sensing outside RAN coverage using ITS or unlicensed spectrum

---

## 6. System Architecture (Stage 2 — TS 23.137)

### 6.1 Architectural Principles

The 5G sensing architecture is defined in **TS 23.137 §4.1** as an extension of the 5GS
architecture (TS 23.501). Key design principles:

- Sensing capability is **additive** to the existing 5GC — a new NF (SenF) is introduced
- **gNB** nodes act as Sensing Entities (SenE), performing radio-based sensing alongside communication
- Only **gNB-based sensing** is supported in Rel-20; UE-based sensing is future work
- The **Application Function (AF)** initiates sensing service requests, either via NEF (external) or directly (trusted domain)

### 6.2 New Network Function: Sensing Function (SenF)

The **SenF** is the central new core-network function introduced for ISAC. Per **TS 23.137 §4.5.2**:

```
SenF
  ├── Sensing Control Functionality (SenF-C)
  └── Sensing Processing Functionality (SenF-P)
```

> There is **no standardized interface** between SenF-C and SenF-P in Rel-20.

**SenF Responsibilities (TS 23.137 §5.5):**

- Receive Sensing Service requests from AF (via NEF or directly)
- **Authorize** sensing service consumers and requests
- **Discover and select** appropriate gNBs as Sensing Entities
- **Derive sensing parameters** from AF requirements (target area, duration, report type)
- **Distribute parameters** to selected gNB(s)
- **Collect sensing data** from gNB(s) and generate Sensing Results
- **Deliver sensing results** to AF (via NEF or directly)
- **Dynamically update** sensing parameters based on real-time results

### 6.3 Reference Points

| Reference Point | Between | Purpose |
|---|---|---|
| **SEN1** | gNB ↔ SenF | Sensing control signalling and data transfer |
| **SEN2** | SenF ↔ NEF | Sensing service exposure to external AFs |
| **SEN3** | SenF ↔ NRF | SenF NF profile registration and discovery |
| **N33** | NEF ↔ AF | Existing 5GC reference point reused for sensing service exposure |

### 6.4 Architecture Diagrams

```
 External AF                Trusted AF
     │                          │
     │ Nnef_SensingService       │ Nsenf_SensingService
     ▼                          ▼
   [NEF] ────── N33 ──────► [SenF] ◄─── NRF (discovery)
                                │
                               SEN1
                                │
                         ┌──────┴──────┐
                       [gNB-1]      [gNB-N]
                    (Sensing Entity) (Sensing Entity)
```

*Reference point representation — TS 23.137 §4.2 (Figure 4.2-1)*

### 6.5 Protocol Stacks

Two protocol stacks are defined (TS 23.137 §4.6):

| Stack | Interface | Purpose |
|---|---|---|
| **Sensing Control Signalling** | SEN1 control plane | Parameters/configuration from SenF to gNB |
| **Sensing Data Transfer** | SEN1 user plane | Raw or processed sensing data from gNB to SenF |

---

## 7. Key Performance Requirements (KPIs)

Per **TS 22.137 §6.1 and §6.2**, the performance framework encompasses the following metrics:

### 7.1 KPI Definitions

| KPI | Definition |
|---|---|
| **Positioning Accuracy (Horizontal)** | Error between measured and true 2D position of target |
| **Positioning Accuracy (Vertical)** | Error on the altitude/vertical axis |
| **Velocity Accuracy (Horizontal)** | Error between measured and true horizontal velocity |
| **Velocity Accuracy (Vertical)** | Error between measured and true vertical velocity |
| **Confidence Level (%)** | Percentage of measurements that include the true value within the stated accuracy |
| **Sensing Resolution** | Minimum detectable difference in range or velocity between two objects |
| **Range Resolution (m)** | Minimum range difference to distinguish two separate targets |
| **Velocity Resolution (m/s × m/s)** | Min horizontal/vertical velocity difference to distinguish targets |
| **Max Sensing Service Latency (ms)** | Time from sensing trigger to result availability at the interface |
| **Refreshing Rate (s)** | Rate at which sensing results are regenerated |
| **Missed Detection Probability (%)** | P(not detecting target | target present) |
| **False Alarm Probability (%)** | P(detecting target | target absent) |

### 7.2 Quantitative Requirements (Selected Highlights from Table 6.2-1)

| Metric | Representative Value |
|---|---|
| Range Resolution | 0.2 m (Category 7 / factory environments) |
| Velocity Resolution | 0.5 × 0.5 m/s (horizontal/vertical, for factories) |
| Sensing Latency | 0.05 ms to 1 ms (Category 1 — stringent tracking) |
| Refresh Rate | 1.5 s (pedestrian), 15 s (vehicle), 0.1 s (other) |
| Missed Detection | ≤ 1% |
| False Alarm | ≤ 1% |
| Confidence Level | Up to 99% (Category 4 — public safety) |

> **NOTE 3 (TS 22.137 §6.2):** To realize 1 m granularity tracking, when the velocity resolution
> is 1 m/s, the maximum corresponding sensing service latency is 1 s.

> **NOTE 5 (TS 22.137 §6.2):** Human motion monitoring requires application-specific KPIs —
> e.g., respiration rate accuracy of 2 times/min for sleep monitoring;
> sit-up rate accuracy of 3 times/min for sports monitoring.

---

## 8. End-to-End Sensing Procedures

### 8.1 Sensing Establishment Procedure (TS 23.137 §6.2.1)

```
AF (External)    NEF          SenF          gNB(s)
     │            │             │              │
     │──1a. Nnef_SensingService_Subscribe ──►  │
     │            │             │              │
     │            │──2. Authorize AF ──────► │ │
     │            │──3. Discover SenF ──────►│ │
     │            │──4. Nsenf_SensingService_Subscribe ──► │
     │            │             │──5. Authorize request   │
     │            │             │──6a/6b. Accept subscribe│
     │◄───────────7a. Subscribe response ──────────────── │
     │            │             │──8. Discover/select gNB(s)
     │            │             │──9. Sensing interaction ►│
     │            │             │◄─ sensing data ──────────│
     │            │             │──10. Generate result     │
     │            │◄11a. Notify result                     │
     │◄12a. Nnef_SensingService_Notify ──────────────────  │
```

**Pre-requisites:**
- gNB(s) must have established signalling connections with SenF (TS 38.xxx — pending)
- SenF NF profile must be registered/updated in NRF

**Report types supported:**
- One-time sensing report
- Periodic sensing report
- Event-triggered sensing report

### 8.2 Sensing Service Modification Procedure (TS 23.137 §6.2.2)

- **AF-triggered:** AF invokes `Nnef_SensingService` modification APIs → NEF → SenF → gNB(s)
- **SenF-triggered:** SenF autonomously updates sensing parameters based on real-time results

### 8.3 Sensing Service Un-Subscription Procedure (TS 23.137 §6.2.3)

AF invokes `Nnef_SensingService_Unsubscribe` → SenF releases gNB sensing resources → service terminated.

---

## 9. Network Function Services

### 9.1 NEF Services (TS 23.137 §7.2.2)

| Operation | Direction | Purpose |
|---|---|---|
| `Nnef_SensingService_Subscribe` | AF → NEF | Request new sensing service subscription |
| `Nnef_SensingService_Unsubscribe` | AF → NEF | Cancel sensing subscription |
| `Nnef_SensingService_Notify` | NEF → AF | Deliver sensing results or status updates |

### 9.2 SenF Services (TS 23.137 §7.3.2)

| Operation | Direction | Purpose |
|---|---|---|
| `Nsenf_SensingService_Subscribe` | NEF/AF → SenF | Core network-level sensing subscription |
| `Nsenf_SensingService_Unsubscribe` | NEF/AF → SenF | Core network-level unsubscription |
| `Nsenf_SensingService_Notify` | SenF → NEF/AF | Deliver sensing results and operation status |

### 9.3 SenF Discovery and Selection (TS 23.137 §5.2.1)

- SenF registers its NF profile with the NRF
- NEF or trusted AF discovers the SenF using standard NRF service discovery
- SenF can be configured by OAM or via NRF registration

### 9.4 Sensing Parameters Provided to gNB (TS 23.137 §5.5)

| Parameter Category | Examples |
|---|---|
| **Sensing operational info** | Target Sensing Service Area, Sensing Service Duration |
| **Report configuration** | Type of sensing data reporting (one-time / periodic) |

> Note: The full list of parameters requires further coordination with RAN WG3.

---

## 10. Security, Privacy and Authorization

### 10.1 Authorization Framework (TS 23.137 §5.1)

A **two-tier authorization** model is defined:

1. **Sensing Service Consumer Authorization:** The SenF (or NEF on its behalf) verifies the AF is
   authorized to consume sensing services at all.
2. **Sensing Service Request Authorization:** Per-request authorization checks that the specific
   sensing parameters (area, targets, duration) are permitted.

If authorization fails at either stage, the request is rejected with an appropriate cause code
and no sensing resources are allocated.

### 10.2 Privacy and Data Integrity (TS 22.137 §5.1)

The specification explicitly calls out new considerations when sensing is introduced as a system
capability:

> *"New considerations on authorization for service access and operation access, data
> confidentiality, data integrity, and user privacy are needed, to ensure that these aspects are
> taken into account when deriving service requirements."*

Key privacy dimensions:
- **User consent** required before using non-3GPP sensor data
- **Regulatory compliance** required before activating sensing in geographic areas
- **Data confidentiality** for sensing data in transit and at rest

---

## 11. Energy Efficiency Considerations

Per **TS 22.137 §5.1**, energy-efficient sensing is a first-class design requirement:

- **Temporarily disabling** sensing transmitters/receivers not involved in active operations
- **Adjusting sensing operation parameters** (e.g., sensing frequency) to minimize energy usage
- **Coordinating sensing transmitters and receivers** for interference management
- Sensing operations are activated/deactivated dynamically based on **network load and location**
  conditions (TS 22.137 §5.2.1)

This aligns ISAC with 3GPP's broader sustainability agenda (energy efficiency in Rel-18/19 RAN).

---

## 12. ISAC in the 6G Context (Rel-20/21)

### 12.1 Rel-20 Overview

According to the 3GPP Release overview:

> *"Rel-20 study areas include: Sub-THz spectrum exploration (100 GHz – 300 GHz), AI-native
> network design, **Integrated Sensing and Communication (ISAC)**, extreme positioning,
> sustainable/energy-efficient RAN and core, digital twin networks."*

Rel-20 represents the **first normative deployment phase** of ISAC with:
- TS 23.137 Stage 2 architecture published
- gNB-based sensing operational framework defined
- Aerial object (UAV/drone) detection and tracking as the first supported use case
- SenF as a new standardized 5GC NF

### 12.2 Rel-21 Extensions (6G Era)

TS 22.137 v21.0.0 introduces advanced 6G ISAC capabilities, expanding beyond Rel-20:

- Additional sensing service categories (7 categories defined)
- Extended KPIs for human motion monitoring (respiration, gesture recognition)
- 6G ISAC functional requirements formalized
- V2X sensing integration (using ITS/unlicensed spectrum outside RAN coverage)
- UE-based and sidelink-based sensing (anticipated in future RAN specifications)

### 12.3 Convergence with Other 6G Technologies

| 6G Technology | ISAC Interaction |
|---|---|
| **Sub-THz (100–300 GHz)** | Higher frequencies → finer range/velocity resolution; enables mm-scale sensing |
| **AI-Native Networks** | AI/ML for sensing data processing, intelligent SenF resource selection |
| **Digital Twin Networks** | ISAC provides real-world sensing data to feed digital twin models |
| **Extreme Positioning** | Sensing and positioning share waveforms and infrastructure |
| **Ambient IoT** | Passive sensing targets enabled by bistatic configurations |

---

## 13. Open Issues and Future Work

The following items are explicitly noted as requiring further specification work (as of Rel-20 TS 23.137):

| Area | Status |
|---|---|
| **RAN-level sensing specification** | TS 38.xxx / TS 38.xxy numbers TBD — pending RAN WG coordination |
| **Step 9 procedure details** (SenF ↔ gNB interaction during active sensing) | Requires coordination with RAN WG3 |
| **Full parameter list for gNB** (sensing parameters from SenF) | Partially defined; further discussion needed |
| **SenF-C / SenF-P standardized interface** | Not standardized in Rel-20 |
| **UE-based sensing** | Not supported in Rel-20; planned for future releases |
| **Multi-gNB sensing result fusion** | Implementation-specific in Rel-20; no normative algorithm defined |
| **UE sensing on unlicensed/ITS spectrum** | Subject to regulatory study |
| **Non-3GPP sensor fusion algorithms** | Implementation-specific; no normative standard |

---

## 14. Abbreviations

| Abbreviation | Expansion |
|---|---|
| **AF** | Application Function |
| **ISAC** | Integrated Sensing and Communication |
| **NF** | Network Function |
| **NEF** | Network Exposure Function |
| **NRF** | Network Repository Function |
| **RAN** | Radio Access Network |
| **SenE** | Sensing Entity (= gNB acting in sensing role) |
| **SenF** | Sensing Function (new 5GC NF) |
| **SenF-C** | Sensing Control Functionality |
| **SenF-P** | Sensing Processing Functionality |
| **UAV** | Unmanned Aerial Vehicle |
| **V2X** | Vehicle-to-Everything |
| **5GC** | 5G Core Network |
| **5GS** | 5G System |
| **gNB** | Next Generation Node B (5G base station) |
| **KPI** | Key Performance Indicator |
| **ITS** | Intelligent Transportation System |

---

## 15. References

| Reference | Document | Notes |
|---|---|---|
| [1] | **3GPP TS 22.137** v19.0.0 / v20.0.0 / v21.0.0 | Service Requirements for ISAC (Stage 1) |
| [2] | **3GPP TS 23.137** v20.0.0 | ISAC Stage 2 Architecture and Procedures |
| [3] | **3GPP TS 23.501** | System Architecture for the 5G System (5GS) |
| [4] | **3GPP TS 23.502** | Procedures for the 5G System (5GS) |
| [5] | **3GPP TS 38.300** | NR; NR and NG-RAN Overall Description |
| [6] | 3GPP Release 20 Overview | Study areas including ISAC |

---