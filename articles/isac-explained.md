# ISAC Explained — Sensing and Communication Together

Integrated Sensing and Communication (ISAC) is one of the defining ideas of 6G: letting a mobile
network **sense the physical world** at the same time as it carries data, using the same radios
and spectrum. This page explains the concept, how 3GPP structures it, and why it matters, in
plain language.

> **Status:** ISAC has normative service requirements (Stage 1) and architecture (Stage 2) work
> in 3GPP, with the first deployments focused on network-based sensing. It is a central 6G theme.

## The core idea

Normally, sensing the environment (radar, cameras, lidar) needs dedicated hardware separate from
the communication network. ISAC collapses that: the cellular network **reuses its own radio
transmissions** to detect, locate, track, and characterise objects — turning base stations into
a distributed sensing system. No extra sensor infrastructure required.

## How 3GPP structures it

ISAC is defined across two layers:

- **Service requirements (Stage 1)** set out what the system must achieve — the use cases,
  accuracy targets, and constraints.
- **Architecture (Stage 2)** adds the machinery: a new core function, the **Sensing Function
  (SenF)**, which authorises sensing requests, selects which base stations will sense, gathers
  their measurements, processes them into results, and returns those results to the requesting
  application through the network's exposure function.

The base station (gNB) acts as the **sensing entity** — it transmits and receives the radio
signals used for sensing alongside its normal communication duties.

## Service categories

3GPP frames a range of sensing service categories, including:

- **Outdoor object detection and tracking** — for example, drones and other aerial objects
  (the first focus area).
- **Indoor object detection** — intruders, assets.
- **Environmental monitoring** — conditions and structures.
- **Public-safety sensing** — crowds, search and rescue.
- **Vehicle detection and tracking** — traffic, collision avoidance.
- **Motion monitoring** — healthcare and sports (breathing, movement).
- **Fine-grained sensing** — gestures, industrial automation (the most demanding).

Each category has its own targets for positioning accuracy, resolution, latency, refresh rate,
and detection reliability.

## Key performance targets

ISAC KPIs include horizontal and vertical positioning accuracy, velocity accuracy, range and
velocity resolution, sensing latency, refresh rate, and the probabilities of missed detection and
false alarm. The most demanding categories (fine-grained sensing) call for the finest resolution
and therefore the most radio resources.

## Security, privacy, and energy

Because sensing observes the physical world, 3GPP treats **authorisation, data confidentiality,
data integrity, and user privacy** as first-class concerns — including user consent before using
non-3GPP sensor data and regulatory compliance before sensing in an area. **Energy efficiency**
is also built in: sensing transmitters and receivers can be disabled when idle and tuned to
minimise energy use.

## Why it matters for 6G

ISAC converges with other 6G directions: sub-THz spectrum gives finer sensing resolution,
AI-native processing interprets the sensing data, digital-twin networks consume it as live input,
and extreme positioning shares the same waveforms and infrastructure. It turns the network into
an awareness layer for the physical world.

## Want the full detail?

For the complete technical analysis — roadmap, architecture, procedures, KPI tables, and open
issues — see the **ISAC deep-dive page**, which includes a downloadable PDF.

## Reference points (3GPP)

- **TS 22.137** — ISAC service requirements (Stage 1).
- **TS 23.137** — ISAC architecture (Stage 2), including the Sensing Function.

*Source: 3GPP study items and specification corpus, paraphrased. No non-3GPP or proprietary
content.*
