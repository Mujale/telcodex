# 6G Standardization — Work Summary

Here is how 6G standardization is taking shape in 3GPP — the release structure, the agreed
timeline, and what is being studied versus specified. Everything below is drawn **only from
3GPP material**: the official 3GPP Release 21 timeline announcement and the 3GPP
release/work-plan overview.

---

## 1. The Big Picture

6G in 3GPP spans two releases:

- **Release 20 — the 6G study phase.** Use cases, scenarios, requirements, and
  architecture captured as Technical Reports (TRs). No normative specifications.
- **Release 21 — the first normative phase.** The first 6G Technical Specifications (TSs),
  developed in the same release as continued 5G-Advanced work.

| Release | Role | Status (per 3GPP) |
|---|---|---|
| **Rel-20** | 6G study phase (TRs: use cases, scenarios, requirements, architecture) | Active |
| **Rel-21** | First 6G specifications **and** 5G-Advanced | Timeline approved |

---

## 2. Approved Release 21 Timeline

On **10 June 2026**, at the 3GPP TSG plenaries (#112) in Singapore, the Release 21 schedule
was approved — fixing when the project's first 6G specifications will be finalised. That
schedule had already been circulated and left unchanged since the March 2026 plenaries.
Release 21 spans **both 5G-Advanced and 6G**.

| Milestone | Date |
|---|---|
| 5G-Adv./6G package approval & **Stage 1 freeze** | **March 2027** |
| Stage 2 — 80% completion checkpoint | March 2028 |
| **Stage 2 freeze** | **June 2028** |
| **Stage 3 freeze** (functional freeze, TSGs #122) | **December 2028** |
| **ASN.1 / OpenAPI freeze** | **March 2029** |

The decision is captured in 3GPP documents **RP-260868 / SP-260595 / CP-261259 —
Release 21 Timeline**. With the dates locked, the working groups can now prioritise Rel-21
features and align their resourcing against the December 2028 functional freeze.

---

## 3. Release 20 — 6G Study Work

Per the 3GPP release overview, Release 20 is the first 6G-oriented release and consists of
study items (Technical Reports) rather than normative work. The study areas identified are:

| Study area | Description |
|---|---|
| Sub-THz spectrum | Exploration of the 100–300 GHz band for 6G radio access |
| AI-native network design | AI/ML as a foundational design principle for RAN and core |
| Integrated Sensing and Communication (ISAC) | Unifying sensing and communication in a single air interface |
| Extreme positioning | Highly accurate (sub-centimetre class) location services |
| Sustainable / energy-efficient RAN and core | Energy efficiency as a design constraint |
| Digital twin networks | Network digital-twin frameworks for planning and operation |
| 6G use cases and service requirements | SA1-led study — TR 22.870 |
| 6G scenarios and requirements | RAN-led study — TR 38.914 |
| Security | Security architecture study for 6G |

Additional 6G studies reported as progressing across the project include the **Study on the
Architecture for the 6G System (SA2)** and the **RAN working-group studies for 6G Radio**.

### TR 22.870 — Study on 6G Use Cases and Service Requirements (SA1)

Per the 3GPP release overview, TR 22.870 identifies 6G use cases across vertical and
consumer scenarios and derives the service requirements and KPIs a 6G system must satisfy.
It is the SA1 precursor that feeds requirements into the architecture and radio studies.

### TR 38.914 — Study on 6G Scenarios and Requirements (RAN)

Per the 3GPP release overview and the Rel-21 timeline announcement, TR 38.914 is the
RAN-level companion to TR 22.870. It translates service-level requirements into radio
scenarios and targets: deployment scenarios, radio-layer KPIs (peak data rate, reliability,
latency, energy and spectrum efficiency), and candidate frequency ranges including sub-THz
bands. 3GPP flagged its completion as scheduled for the June 2026 Singapore meeting week.

---

## 4. Features Under Discussion in 3GPP for 6G

The feature areas below are organised by working-group pillar (RAN, SA, CT).

### RAN — radio

- **Sub-THz radio:** New spectrum at 100–300 GHz, with fresh waveforms, huge antenna arrays, and near-field channel models.
- **AI-native air interface:** AI/ML built into the physical layer for channel estimation, beam management, and feedback compression.
- **ISAC:** Sensing and communication sharing the same radio hardware and spectrum.
- **Extreme positioning:** Sub-centimetre location accuracy.
- **Sustainable RAN:** Deep energy savings, including zero-energy ambient IoT.
- **Massive MIMO evolution:** Cell-free, distributed, and holographic MIMO.
- **New duplex modes:** Full-duplex with self-interference cancellation.

### SA — architecture

- **Use cases/requirements:** 6G KPIs and services (TR 22.870).
- **System architecture:** AI-native next-generation core beyond 5GC.
- **Digital twin networks:** Real-time network replicas feeding AI models.
- **Immersive/holographic:** Transport for XR and holographic services.
- **Ambient IoT:** Zero-power, energy-harvesting devices.

### CT — core protocols

- **Protocol architecture:** Evolved NAS and session management with lower signalling overhead.
- **Next-gen sessions:** Deterministic, sub-ms, Tbps-class flows.
- **Multi-hop ProSe:** UE-to-UE and UE-to-network relays.
- **Capability-exposure APIs:** Northbound access to sensing, AI, and positioning.
- **NTN evolution:** Integrated terrestrial/satellite with inter-satellite handover.

---

## 5. Release 21 — Expected Normative 6G Scope

Per the 3GPP release overview, Release 21 is planned as the first release to contain
normative 6G specifications (TSs, not only TRs). The overview indicates the expected scope:

- A **new 6G air interface** (new specifications rather than NR increments)
- A **next-generation core architecture** beyond the 5G Core
- **AI as a native network feature**, designed into the standard rather than added on
- **Integrated sensing**, **digital twin**, and **immersive/holographic** service support

---

## 6. Key Dates at a Glance (3GPP-confirmed)

| Event | Date |
|---|---|
| Rel-21 timeline approved (TSGs #112, Singapore) | 10 June 2026 |
| Rel-21 package approval & Stage 1 freeze | March 2027 |
| Stage 2 80% checkpoint | March 2028 |
| Stage 2 freeze | June 2028 |
| Stage 3 functional freeze (TSGs #122) | December 2028 |
| ASN.1 / OpenAPI freeze | March 2029 |

---

## 7. Sources (3GPP only)

- [3GPP — Timeline for Release 21 (TSGs #112, 10 June 2026)](https://www.3gpp.org/news-events/3gpp-news/rel21-timeline)
- 3GPP Release 21 Timeline agreement documents: **RP-260868 / SP-260595 / CP-261259**
- [3GPP Work Plan](https://www.3gpp.org/specifications-technologies/3gpp-work-plan) and [3GPP Releases](https://www.3gpp.org/releases)
- 3GPP specifications portal (TR 22.870, TR 38.914 series directories)
