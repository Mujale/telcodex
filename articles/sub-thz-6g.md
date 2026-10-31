# What Is Sub-THz Spectrum in 6G?

Sub-THz spectrum — very roughly the **100–300 GHz** range — is one of the most talked-about
frontiers for 6G. This page explains what it is, why 3GPP is studying it, the hard physics that
make it difficult, where it might be used, and how it relates to the nearer-term "FR3" upper
mid-band.

> **Status:** Sub-THz above about 71 GHz is still **pre-normative** in 3GPP. There is no
> approved 6G operating band or specification for it yet — it lives in feasibility studies and
> ITU-R IMT-2030 input, not in frozen standards.

## Where sub-THz sits in the frequency map

3GPP today defines three normative frequency ranges for 5G NR:

- **FR1** — roughly 410 MHz to 7.125 GHz (the sub-7 GHz "mid and low band").
- **FR2-1** — 24.25 to 52.6 GHz (millimetre wave).
- **FR2-2** — 52.6 to 71 GHz.

An emerging **FR3** label covers the **upper mid-band (about 7–24 GHz)**. Everything **above
71 GHz, up toward 300 GHz**, is "sub-THz" and has no normative range designation — it is studied
through Technical Reports and 6G/IMT-2030 contributions only.

## Why 3GPP is studying it

The attraction is simple: **bandwidth**. The appeal and the drivers are:

- **Room to grow.** Sub-7 GHz is congested and mmWave coverage is limited. Sub-THz offers large
  blocks of unused, contiguous spectrum.
- **Extreme capacity.** Channels tens of GHz wide are conceivable above 100 GHz — far beyond the
  400 MHz typical in FR2-1 — which is what makes multi-terabit-per-second peak rates plausible.
- **Short-range, high-throughput use.** Backhaul, in-venue hotspots, device-to-device links, and
  kiosk-style downloads can tolerate short range in exchange for huge throughput.
- **Sensing.** At millimetre and sub-millimetre wavelengths, compact antennas give very fine
  angular resolution — useful for the integrated sensing work happening alongside 6G.
- **Feeding ITU-R.** 3GPP must supply technology input to the IMT-2030 framework, which drives
  these feasibility studies ahead of any decisions at WRC-27.

## The hard physics

Sub-THz is difficult for three main reasons.

**Severe path loss and atmospheric absorption.** Free-space loss climbs steeply with frequency,
and molecular absorption (from oxygen and water vapour) creates peaks that make some sub-bands
unusable over distance. Usable "windows" exist around 120–160 GHz, 220–270 GHz, and 300–350 GHz.
Rain and foliage make outdoor range even shorter — potentially just tens of metres at 300 GHz.

**Near-field operation.** To overcome path loss you need large antenna arrays, but large arrays
at these frequencies push the far-field boundary (the Rayleigh distance) out to tens of metres.
That means devices may sit in the **radiative near field**, where the usual flat-wavefront
assumptions behind beamforming break down and spherical-wave models are needed. 3GPP's channel
model work (TR 38.901) is being extended to capture near-field and spatial-non-stationarity
effects, starting with the 7–24 GHz study.

**Beamforming and hardware.** Beams become extremely narrow (fractions of a degree), so even tiny
device movements break alignment and beam tracking must be fast and precise. Oscillator phase
noise, wideband "beam squint," power-amplifier efficiency, and sub-millimetre fabrication
tolerances all get harder above 100 GHz.

## Likely use cases

Within 3GPP's study framing, realistic sub-THz scenarios are short-range and capacity-focused:

- Fixed wireless **backhaul and fronthaul** over short line-of-sight hops.
- **Indoor hotspots** with extreme capacity (factories, data centres, venues).
- **Device-to-device** and intra-rack links replacing cables.
- **Kiosk/download** zones for high-rate bursts.
- **Joint sensing and communication**, using the fine resolution for imaging-grade sensing.

## Sub-THz vs FR3 (upper mid-band)

It is easy to confuse these, but they are different horizons:

- **FR3 (7–24 GHz)** is the **near-term bridge** between sub-7 GHz coverage and mmWave capacity.
  It has an emerging 3GPP designation, active channel-model work, and is expected in normative
  Release 20/21 work.
- **Sub-THz (100–300 GHz)** is the **longer-term frontier** — pure capacity, ultra-short range,
  with near-field effects as a major design constraint — dependent on WRC-27 spectrum decisions
  and the IMT-2030 outcome, likely a generation further out.

## Reference points (3GPP)

- **TR 38.807 / TR 38.808** — earlier studies on NR beyond 52.6 GHz and 52.6–71 GHz.
- **TR 38.901** — the channel model, being extended toward higher frequencies and near-field.
- **TR 22.870 / TR 38.914** — the 6G requirements and scenario studies.

## In short

Sub-THz is a genuine 6G opportunity for enormous short-range capacity, but it is early-stage in
3GPP and hard to engineer. Expect the upper mid-band (FR3) to arrive first, with sub-THz following
as the standards, spectrum, and hardware mature.
