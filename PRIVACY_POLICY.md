# Roam Privacy Policy

_Updated 2026-06-30 to match the shipped product and launch scope. See LAUNCH_READINESS.md._

**Effective Date:** June 2026

## Overview

Roam is a local-first iOS app that automatically records the **ZIP Code Areas (U.S. Census ZIP Code Tabulation Areas, "ZCTAs")** you visit, privately on your device. There is no account, no cloud, and no backend.

## What "ZIP Code Areas / ZCTAs" means

The boundaries Roam uses are **U.S. Census ZCTAs** — generalized statistical approximations of ZIP Code geography. They are **not** official USPS delivery boundaries, and not every USPS ZIP Code has a matching ZCTA. Roam never claims USPS accuracy.

## Data Collection

### Location Data
- Your location is used **only while you have enabled tracking**.
- Background location (Always authorization) is used to detect the ZIP Code Areas you enter even when the app is closed.
- Location is processed **entirely on-device** to identify ZCTAs against a bundled SQLite dataset using a local R*Tree spatial index and point-in-polygon test.
- **No reverse geocoding** and **no network calls** are made for ZIP/ZCTA detection (no `CLGeocoder`, `MKLocalSearch`, or external ZIP API).
- Your visit history (codes, timestamps, coordinates, durations) is stored locally in the app's on-device SwiftData store.

### Data Storage
- All data stays in the app's private on-device container.
- **No cloud sync. No account. No backend.** Data persists only on your device and is removed when you delete it or uninstall the app.

## Third-Party Services

Roam uses:
- **iOS Location Services** — on-device processing only.
- **Static Census ZCTA reference data** — bundled with the app; never transmitted.

Roam does **NOT** use:
- Analytics or telemetry SDKs
- Crash-reporting services that transmit data off-device
- Cloud storage
- Advertising
- Any third-party tracking (the app's `PrivacyInfo.xcprivacy` declares `NSPrivacyTracking = false` with empty collected-data and tracking-domain lists)

On-device MetricKit diagnostics (e.g., crash/hang signals) may be written to the app's local storage to aid development. These are **never transmitted anywhere**.

## Permissions

- **Location (When In Use, then Always)** — required for the core feature: detecting the ZIP Code Areas you enter. Always is needed only for background detection. You can use the app and review your data without enabling tracking.

## Data Control

You have full control:
- Delete individual visits or tracked ZIP Code Areas in the app.
- "Delete All Data" (type-to-confirm) removes all tracked areas, visits, and diagnostic logs.
- Disable tracking at any time in Settings (or revoke location access in iOS Settings).
- Export your data (JSON/CSV) locally; it leaves the device only if you explicitly share it via the system share sheet.
- Uninstalling the app removes all on-device data.

## Questions?

GitHub: https://github.com/pri8771/roam-ios
Support: _add a support email before App Store submission._
