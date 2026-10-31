# 5G Core vs 6G Core — What Changes?

The core network is the "brain" of a mobile system — it handles who can connect, how sessions
are set up, how data is routed, and what policies apply. This page compares the well-defined
**5G Core (5GC)** with the **6G core** that 3GPP is now beginning to study, in plain language.

> **Status:** The 5G Core is fully specified. The 6G core is **not** — Release 20 holds the
> first 6G study items, and the first normative 6G core specifications are expected in
> Release 21. Everything about "6G core" below reflects study direction, not frozen standards.

## The 5G Core today: a service-based architecture

The 5GC is built on a **Service-Based Architecture (SBA)**. Instead of fixed point-to-point
links, each control-plane network function exposes its capabilities as web-style services (over
HTTP/2) that other functions can call. The defining ideas:

- **Control and user planes are separated**, so the data-forwarding function can scale and be
  placed independently of the control logic.
- **Functions are modular and mostly stateless**, with their state held in shared data stores —
  which makes them easy to scale and relocate.
- **Services are reusable**, discovered through a repository function, and can be brokered
  through a proxy.
- **The core is access-agnostic**, integrating 3GPP and non-3GPP access through common interfaces.

### The main 5G Core functions

- **AMF** — access and mobility management; the entry point for devices, terminating signalling.
- **SMF** — session management; sets up data sessions and controls the user-plane function.
- **UPF** — the user plane; forwards traffic, enforces quality of service, and anchors edge
  break-out. It is the only user-plane function and is controlled by the SMF.
- **PCF** — policy control; quality-of-service, charging, and access/mobility policy.
- **UDM / UDR** — subscriber data management and the repository behind it.
- **AUSF** — authentication.
- **NRF** — the registry where functions find and authorise each other.
- **NEF** — the secure gateway that exposes network capabilities to outside applications.
- **NSSF / NSACF** — network-slice selection and admission control.
- **NWDAF** — the analytics function that produces machine-learning-based insights for other
  functions to consume.

## What the 6G core is expected to change

3GPP's early 6G study (led by the system-architecture group, SA2) is driven by demanding new use
cases — AI-native networks, integrated sensing, holographic/Tbps services, sub-millisecond
latency, extreme device density, digital twins, sustainability, and sub-THz access. These push
the core in several directions:

**AI as a native element, not a bolt-on.** In 5G, AI lives in one analytics function (NWDAF)
that others query. For 6G, the study explores building AI directly into the functions themselves,
with model training, inference, and lifecycle management treated as core capabilities.

**A more composable architecture.** The 5G SBA assumes fixed function roles. 6G studies consider
assembling capabilities on demand from smaller, composable pieces — a more dynamic service mesh
than today's monolithic functions.

**Sensing as part of the core.** 5G handles sensing at the application layer. 6G is expected to
bring a native sensing service plane into the architecture, reflecting the integrated
sensing-and-communication direction.

**Energy as a first-class concern.** An energy-information function is already appearing in the
latest 5G core specs as a precursor. 6G studies make energy-aware operation and sustainability
KPIs an architectural property, not an afterthought.

**Native multi-access and non-terrestrial integration.** Where 5G retrofits satellite support
onto existing functions, 6G is expected to treat terrestrial, non-terrestrial, and new spectrum
as first-class access types.

**Digital twin integration.** 5G has no network digital twin. 6G study areas include a live
digital model of the network for prediction and optimisation.

## Side-by-side summary

| Dimension | 5G Core (specified) | 6G core (study direction) |
|---|---|---|
| Architecture | Service-based, fixed function roles | Evolved/composable service mesh |
| AI/ML | Analytics function (NWDAF) others consume | AI as a native architectural element |
| Control/user split | Mandatory | Kept, pushed further to the edge |
| Sensing | Application-layer only | Native sensing service plane |
| Energy | Energy-information function emerging | First-class, with sustainability KPIs |
| Non-terrestrial | Retrofitted onto existing functions | Native multi-access including sub-THz |
| Digital twin | Not defined | Studied as a native function |

## Reference points (3GPP)

- **TS 23.501 / TS 23.502** — the 5G system architecture and procedures (the 5GC baseline).
- **TR 22.870 / TR 38.914** — the 6G use-case and scenario studies feeding core requirements.

## In short

The 5G Core is a mature, service-based design with a clear set of functions. The 6G core is still
being imagined in study items, but the direction is clear: more AI-native, more composable, with
sensing, energy, non-terrestrial access, and digital twins built in rather than added on.

*Source: 3GPP study items and specification corpus, paraphrased. No non-3GPP or proprietary
content.*
