# AI-Native 6G — What Does It Mean?

"AI-native" is one of the phrases you hear most about 6G. But what does it actually mean, and how
is it different from the AI already in 5G? This page explains the shift.

> **Status:** AI-native design is a 6G study theme in 3GPP. In 5G, AI/ML is already used in
> specific places; 6G studies making it a built-in design principle. The 6G specifics are study
> direction, not frozen standards.

## AI in 5G: a useful add-on

5G already uses machine learning, but as a **bolt-on** to specific functions rather than a
foundation. On the radio side, AI/ML was studied for particular jobs — compressing channel-state
feedback, managing beams, and improving positioning. In the core, a dedicated analytics function
(the NWDAF) collects data and produces predictions that other network functions can request and
act on. AI is a *service* the network offers, consumed where useful.

## AI-native in 6G: built in from the start

The 6G idea is to make AI a **native design principle** rather than an optional feature. Three
shifts capture it:

**In the radio.** Instead of adding AI to a few functions, 6G studies designing the air interface
with AI at its heart — learned components for channel estimation and decoding, AI-assisted
scheduling and mobility, and even learned waveforms. A key question is **where the AI runs** —
in the device, the distributed unit, the central unit, or the core — depending on how much
latency and compute each task can tolerate. Another is **how AI models are delivered** to devices
and kept up to date, with appropriate trust handling.

**In the core.** Where 5G has one analytics function alongside the others, 6G explores building
inference directly into the network functions themselves, with model training, deployment, and
lifecycle management treated as core capabilities rather than an overlay.

**In operations.** Network management becomes AI-assisted and closed-loop: the system collects
measurements, decides using AI and policy, and acts automatically — guided by high-level intent
rather than manual configuration.

## Why 6G needs it

6G networks are expected to be far larger and more dynamic than today's — more spectrum, more
devices, more services with tight requirements. That complexity is beyond efficient hand-tuning.
AI-native design lets the network adapt continuously to changing conditions, approach optimal
performance across very different scenarios, and run with less human intervention.

## The honest caveats

- "AI-native" is still being defined in study items; the exact architecture is not yet
  standardised.
- Baking AI into the standard raises hard questions 3GPP is working through — model trust and
  versioning, data provenance, explainability, and how to test and certify behaviour that learns.

## Reference points (3GPP)

- **TR 38.843** — the AI/ML for NR air-interface study (the 5G foundation this builds on).
- **TS 23.288** — the network data analytics function (NWDAF).
- **TS 28.105** — management of AI/ML functions.

## In short

AI in 5G is a capability you call on; AI-native 6G aims to make intelligence part of how the
network is built and run — across the radio, the core, and operations.
