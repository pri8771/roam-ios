# Roam – Beta Testing Plan

_Updated 2026-06-30 to match the shipped product and launch scope. See LAUNCH_READINESS.md._

**Version:** 2.0
**Date:** June 30, 2026
**App:** Roam – private, on-device ZIP Code Area (Census ZCTA) visit tracker
**Repo:** https://github.com/pri8771/roam-ios

---

## Overview

Roam is a local-first iOS app that automatically records the **ZIP Code Areas (Census ZCTAs)** you visit, entirely on-device. It uses CoreLocation (When-In-Use → Always), MapKit, SwiftData, and a bundled SQLite ZCTA dataset. No account, no cloud, no analytics.

This 3-phase plan covers internal alpha, external TestFlight beta, and pre-launch polish. The single most important thing to validate is **permission trust** — whether testers grant Always Location after the pre-prompt onboarding/education — followed by **detection correctness** and **battery impact**.

> **Data caveat:** until the production ZCTA bundle is built and bundled (see `Scripts/README_PREPROCESSING.md`), detection only works inside the bundled **sample** area (San Francisco `94102/94103/94107`). Label this clearly for testers, or ship beta on a clearly-labeled limited geography.

---

## Phase 1: Internal Alpha (Week 1–2)

**Goal:** validate the core detection loop, persistence, permission flow, and data controls on internal devices.

### Testers
- Developers + close collaborators (3–5)
- Devices: a spread of iPhone models; iOS 17 and 18

### Test Cases

#### Permission flow (highest priority)
- [ ] Fresh install → onboarding shows **before** any system location prompt
- [ ] Enabling tracking requests **When In Use** first
- [ ] Education sheet appears, then **Always** is requested
- [ ] Deny → "Open Settings" affordance shown; app does not crash
- [ ] Reduced (coarse) accuracy → one-time precise-accuracy prompt; reduced state surfaced
- [ ] Revoke in iOS Settings → app reflects the change gracefully

#### Core detection loop
- [ ] Simulate Route / Step Next (DEBUG) colors the sample ZCTAs through the real pipeline
- [ ] A new area creates a tracked ZCTA + open visit; haptic fires
- [ ] Crossing a confirmed boundary closes the old visit and opens a new one
- [ ] Low-confidence / coarse fixes do **not** color a wrong area (bias-to-not-color holds)

#### Background & relaunch
- [ ] With Always granted, force-quit; move; reopen → background visits recorded
- [ ] App resumes tracking after an iOS location relaunch

#### Map & UI
- [ ] Visited/current/selected boundaries color correctly; zoom changes resolution
- [ ] Pins appear; tapping opens the selected-area card and detail
- [ ] Dashboard current-area card shows a live timer + confidence

#### Data persistence & control
- [ ] Force-quit/relaunch and device restart preserve data
- [ ] Delete a visit decrements parent counts correctly
- [ ] "Delete All Data" (type DELETE) clears everything
- [ ] Export JSON/Visits CSV/Summary CSV write files and present the share sheet

#### Data status
- [ ] Data Status correctly reports Sample (DEBUG) or Production; RELEASE blocks tracking on non-production data

### Alpha Success Criteria
- Zero crashes on primary flows
- Permission walk works across all auth states
- Detection correct on the sample area; no wrong-area coloring
- Data persists across restart; export/delete work

---

## Phase 2: External Beta via TestFlight (Week 3–5)

**Goal:** validate real-world permission trust, detection on the **production** bundle, and battery impact across devices.

### Tester Recruitment
- 25–50 external testers: privacy-conscious travelers, city explorers, quantified-self users
- Device spread across iPhone models; iOS 17+

### Focus Areas
- [ ] **Permission grant rate** to Always after onboarding/education (the key metric)
- [ ] Detection correctness across diverse real locations (requires production bundle)
- [ ] Battery impact per tracking mode (Battery Saver / Balanced / High Accuracy)
- [ ] Background reliability (transitions recorded while app closed)
- [ ] Onboarding clarity (value + privacy understood without instruction)
- [ ] Trust: testers keep tracking on; no "creepy"/over-ask feedback
- [ ] Export/delete feel trustworthy and complete

### Edge Cases
- [ ] Areas with no ZCTA coverage → "unknown" handled gracefully
- [ ] Reduced-accuracy environments
- [ ] Long commutes / many transitions in a day
- [ ] Airplane mode / no signal (app still functions; no detection)

### External Beta Success Criteria
- Crash-free rate > 99%
- Strong Always-permission grant rate after the pre-prompt
- No P0 bugs; no wrong-area coloring reports
- Positive trust feedback; acceptable battery reports

---

## Phase 3: Polish & Pre-Launch (Week 6)

### Accessibility Audit
- [ ] VoiceOver labels on interactive elements and cards
- [ ] Dynamic Type scales across the 5 tabs and permission sheets
- [ ] Reduce Motion respected; high-contrast legibility
- [ ] No color-only information on the map (paired with labels/glyphs)

### App Store Readiness
- [ ] Final 1024×1024 opaque app icon (replace placeholder)
- [ ] Screenshots (6.7"/6.5") of map coloring, current-area card, history, privacy story
- [ ] Description/keywords match the ZIP-Code-Area product
- [ ] Privacy Nutrition Label = **Data Not Collected** (matches `PrivacyInfo.xcprivacy`)
- [ ] Age rating 4+; valid Support URL/email
- [ ] PRIVACY_POLICY.md and TERMS_OF_SERVICE.md reviewed and linked

### Final QA
- [ ] Clean install run; DEBUG/developer tools absent in RELEASE
- [ ] CI green (build + tests) — fix the broken build-for-testing step first
- [ ] Production ZCTA bundle present and validated; Data Status reads "Production"
- [ ] No unnecessary permissions requested

---

## Bug Severity Levels

| Level | Description | Resolution |
|---|---|---|
| P0 – Critical | Crash, data loss, privacy/security issue, wrong-area coloring | Block launch, fix immediately |
| P1 – High | Core loop or permission flow broken | Fix before submission |
| P2 – Medium | Minor feature/edge-case issue | Fix in v1.1 if not blocking |
| P3 – Low | Cosmetic / copy | Backlog |

---

## Success Metrics for Launch Readiness

| Metric | Target |
|---|---|
| Crash-free rate | > 99.5% |
| P0 bugs | 0 |
| P1 bugs | 0 |
| Always-permission grant (beta-reported) | High enough to validate the loop |
| No wrong-area coloring reports | Required |
| CI build status | Green |
| Accessibility audit | Pass |

---

## Timeline Summary

| Phase | Duration | Goal |
|---|---|---|
| Phase 1: Internal Alpha | Week 1–2 | Core loop + permission validation |
| Phase 2: External Beta | Week 3–5 | Real-world trust + production data |
| Phase 3: Polish | Week 6 | App Store readiness |
| **App Store Submission** | Week 7 | Launch |

---

## Contacts
- **Developer:** pri8771
- **GitHub Repo:** https://github.com/pri8771/roam-ios
- **TestFlight Feedback:** via App Store Connect
