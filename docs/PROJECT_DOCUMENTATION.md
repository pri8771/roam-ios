# Roam — Project Documentation

_Updated 2026-06-30 to match the shipped product and launch scope. See LAUNCH_READINESS.md._

GitHub is the source of truth for this project documentation. Notion indexes this file in the Priyansh App Factory Command Center.

## 00. Executive Summary
Roam is a privacy-first, local-first iOS app that **automatically records the ZIP Code Areas (U.S. Census ZCTAs) you visit, entirely on-device**, and visualizes them on a map and timeline. It is implemented as a working SwiftUI app (~81 Swift files, ~7.8k LOC incl. tests; 52 XCTest cases) with a real on-device detection pipeline (CoreLocation → quality filter → SQLite R*Tree → point-in-polygon → anti-jitter visit segmentation → SwiftData), MapKit boundary overlays, statistics/milestones, and JSON/CSV export. The product is **MVP Ready**: the core loop runs end-to-end against a bundled sample dataset, with TestFlight gated mainly on (1) building/bundling the production national ZCTA dataset and (2) earning Always Location via the pre-prompt onboarding. The shipped surface includes onboarding, permission education, dashboard, map, history/detail, stats, export/delete, data-status transparency, and privacy/help.

## 01. Product
MVP scope (built): pre-permission onboarding, two-step location permission (When-In-Use → Always) with an education gate, on-device ZCTA detection + anti-jitter visit segmentation, map with zoom-aware boundary overlays + pins, dashboard with live current-area card, history (timeline + by-area) with search/sort/swipe, per-area detail, statistics + milestones, JSON/CSV export via share sheet, data-status/bundle transparency, and privacy controls (toggles + type-to-confirm delete-all). Out of scope for v1: cloud/account/sync, analytics, reverse geocoding, routing, venue search, social, and monetization. ZCTAs approximate (do not equal) USPS ZIP Codes; copy stays "ZIP Code Areas / Census ZCTA boundaries."

## 02. Design
Map-first, calm, private, travel-journal feel. Screens: onboarding, permission rationale, map, timeline, place detail, export/delete, settings.

## 03. Frontend Technical
SwiftUI with MapKit and CoreLocation. Store visits, points, trips, preferences, and retention settings locally.

## 04. Backend Technical
No backend for v1. Future services may include encrypted sync, trip summaries, map enrichment, or remote config.

## 05. Business
Business model: premium local features, export packs, or optional encrypted sync later.

## 06. Marketing
Positioning: your private map memory. Channels: travel journaling, privacy-focused audiences, personal analytics communities.

## 07. User Acquisition
Beta with travelers, quantified-self users, and city explorers. Metrics: permission grant, first recorded visit, weekly map view, export/delete usage, retention.

## 08. Execution
Plan: audit repo, audit permissions, freeze privacy-first MVP, build MapKit view, add timeline/storage, QA/TestFlight.

## 09. QA
Test permission states, app relaunch, map load, timeline load, delete history, export, low-signal behavior, airplane mode, and device sizes.

## 10. Legal / Compliance
Explain what location data is stored, where it is stored, and how it can be deleted/exported. Match privacy labels to final implementation.

## 11. Operations
Release process: internal device test, privacy beta, TestFlight, launch decision. Post-launch: trip summaries, encrypted sync, widgets.
