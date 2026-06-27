#!/usr/bin/env python3
"""Write a small sample GeoJSON FeatureCollection of San Francisco ZCTAs.

Produces three simple rectangle polygons approximating SF ZCTAs. The rectangles
are deliberately sized so they contain the test points used by the app's
simulated route, while staying non-overlapping at those test points.

Standard library only.
"""

import argparse
import json
import sys


# (lon_min, lon_max, lat_min, lat_max) per ZCTA code.
RECTANGLES = {
    "94102": (-122.426, -122.412, 37.773, 37.787),
    "94103": (-122.417, -122.403, 37.766, 37.778),
    "94107": (-122.404, -122.385, 37.756, 37.773),
}

# Test points (lat, lon) the simulated route uses; each must fall in its ZCTA.
TEST_POINTS = {
    "94102": [(37.7793, -122.4193), (37.7795, -122.4190)],
    "94103": [(37.7725, -122.4109)],
    "94107": [(37.7620, -122.3940)],
}


def _rectangle_ring(lon_min, lon_max, lat_min, lat_max):
    """Closed exterior ring (CCW) as [lon, lat] pairs."""
    return [
        [lon_min, lat_min],
        [lon_max, lat_min],
        [lon_max, lat_max],
        [lon_min, lat_max],
        [lon_min, lat_min],
    ]


def _contains(rect, lat, lon):
    lon_min, lon_max, lat_min, lat_max = rect
    return lon_min <= lon <= lon_max and lat_min <= lat <= lat_max


def _verify():
    """Confirm every test point lies inside its rectangle. Raises on failure."""
    for code, points in TEST_POINTS.items():
        rect = RECTANGLES[code]
        for lat, lon in points:
            if not _contains(rect, lat, lon):
                raise SystemExit(
                    "Test point (%f, %f) is NOT inside rectangle for %s: %r"
                    % (lat, lon, code, rect)
                )
    # Confirm no test point falls inside a *different* rectangle (no overlap
    # ambiguity at the test points).
    for code, points in TEST_POINTS.items():
        for lat, lon in points:
            for other_code, rect in RECTANGLES.items():
                if other_code == code:
                    continue
                if _contains(rect, lat, lon):
                    raise SystemExit(
                        "Test point (%f, %f) for %s also falls inside %s -- "
                        "rectangles overlap at a test point."
                        % (lat, lon, code, other_code)
                    )


def build_feature_collection():
    features = []
    for code, rect in RECTANGLES.items():
        features.append(
            {
                "type": "Feature",
                "properties": {"ZCTA5CE20": code},
                "geometry": {
                    "type": "Polygon",
                    "coordinates": [_rectangle_ring(*rect)],
                },
            }
        )
    return {"type": "FeatureCollection", "features": features}


def main(argv=None):
    parser = argparse.ArgumentParser(description="Write sample SF ZCTA GeoJSON.")
    parser.add_argument("--output", required=True, help="Output GeoJSON path")
    args = parser.parse_args(argv)

    _verify()

    fc = build_feature_collection()
    with open(args.output, "w", encoding="utf-8") as fh:
        json.dump(fc, fh, indent=2)
        fh.write("\n")

    print("Wrote %d features to %s" % (len(fc["features"]), args.output))
    print("All %d test points verified inside their rectangles."
          % sum(len(p) for p in TEST_POINTS.values()))
    return 0


if __name__ == "__main__":
    sys.exit(main())
