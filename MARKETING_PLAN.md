# Roam — Marketing and Launch Plan

_Updated 2026-06-30 to match the shipped product and launch scope. See LAUNCH_READINESS.md._

**Version:** 2.0
**Date:** June 30, 2026
**App:** Roam

---

## Executive Summary

Roam is a privacy-first iOS app that **automatically colors in the ZIP Code Areas (U.S. Census ZCTAs) you visit, on-device.** No account, no cloud, no analytics. With Always Location, it passively builds a private map and timeline of where you've been — a "fill in your travels" memory you fully own.

**Target:** privacy-conscious travelers, city explorers, and quantified-self users in the U.S.
**Positioning:** A private, automatic map of the areas you've been to — your data never leaves the phone.

> **Honesty note:** Roam detects **Census ZCTAs**, which approximate (but do not equal) USPS ZIP Codes. All copy must say "ZIP Code Areas / Census ZCTA boundaries," never imply USPS delivery accuracy.

---

## App Store Positioning

### App Name
Roam

### Subtitle
Privately map the areas you visit

### Primary Keywords
zip code map, places visited, travel map, location memory, private location, areas visited, map tracker, on-device, no account, census ZCTA

### Category
Primary: Travel | Secondary: Lifestyle (or Navigation)

### Age Rating
4+

---

## Target Audience

**Primary — Privacy-conscious traveler / city explorer (25–45):**
- Enjoys a "map-completion" / travel-memory loop
- Will grant Always Location *if* value and privacy are shown first
- Hates accounts, cloud lock-in, and being the product

**Secondary — Quantified-self / personal-analytics user:**
- Wants a local, exportable record of movement by area
- Values export/delete control and no third-party data sharing

---

## Competitive Edge

| Feature | Roam | Typical "places" apps |
|---|---|---|
| Fully on-device (no backend) | Yes | Rarely |
| No account / no sign-up | Yes | Often required |
| No analytics / no tracking SDKs | Yes | Uncommon |
| Automatic (passive) area coloring | Yes | Often manual check-in |
| Honest about ZCTA vs USPS accuracy | Yes | N/A |
| Export + delete-all controls | Yes | Varies |

**Our edge:** automatic + private by construction + honest = a trust-first travel-memory loop.

---

## Pre-Launch Strategy

### App Store Optimization (ASO)
- Keyword research around "places visited," "travel map," "private location."
- 5–8 screenshots (6.7"/6.5") showing the colored-in map, current-area card, history timeline, and the privacy/permission story.
- App Preview video showing the "color in a new area as you move" moment.
- Privacy Nutrition Label configured as **Data Not Collected** (matches `PrivacyInfo.xcprivacy`).

### Community Seeding
- Reddit: r/iphone, r/privacy, r/quantifiedself, r/travel.
- Privacy-focused newsletters and indie-app roundups.
- ProductHunt "Upcoming" listing emphasizing on-device + no account.

---

## Launch Day Strategy

### ProductHunt
- **Tagline:** "Privately color in the areas you've been to — on-device, no account."
- **Target:** Top products in Travel/Privacy.

### Social
- **Twitter/X:** "Roam quietly colors in the ZIP Code Areas you visit — all on your iPhone. No account, no cloud, no tracking. #iOS #privacy"
- **Reddit:** story-driven post about building a private, on-device "places visited" map.
- **Hacker News:** "Show HN: Roam — a private, on-device map of the areas you've visited."

---

## Messaging Pillars

1. **Private by construction** — on-device detection, no backend, no analytics, no account.
2. **Automatic** — it fills in your map passively as you move (Always Location, your control).
3. **Honest** — ZIP Code Areas are Census ZCTAs, approximations of USPS ZIPs.
4. **Yours** — export anytime, delete anytime, uninstall removes everything.

---

## Monetization Roadmap

- **Launch (v1):** completely free; **no IAP** in the build. Goal: downloads, reviews, and validated permission-grant + retention.
- **Later (optional Pro):** export packs, advanced map/diagnostics, or other on-device conveniences. Any future end-to-end-encrypted sync is strictly optional and must never become a silent backend. (No StoreKit ships in v1.)

---

## Success Metrics (privacy-respecting)

Because there is no analytics backend by design, growth metrics come from App Store Connect + TestFlight, and product-health signals from TestFlight feedback (never server telemetry).

### Month 1
| Metric | Target |
|---|---|
| Downloads | 500+ |
| Rating | 4.5+ |
| Always-permission grant rate (beta-reported) | High enough to validate the loop |
| ProductHunt upvotes | 100+ |

### Month 3
| Metric | Target |
|---|---|
| Total downloads | 5,000+ |
| Tester-reported retention (tracking kept on) | Trending up |
| Export usage (trust proxy) | Observed |

---

## Launch Timeline

| Timeline | Activity |
|---|---|
| Week 1–2 | Build production ZCTA bundle, fix CI, finalize icon, alpha test |
| Week 3–5 | TestFlight external beta (privacy/travel testers), permission-grant validation |
| Week 6 | App Store submission (metadata + nutrition label aligned to the real product) |
| Week 7 | Launch (ProductHunt + social) |
| Month 2–3 | Content + community; Pro-tier decision; v1.1 |
