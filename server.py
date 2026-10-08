import http.server
import json
import os
import urllib.parse

PORT = 8080
BASE_DIR = os.path.dirname(os.path.abspath(__file__))

DATABASE = {
    # CASE 1: Apex Retail LLC (Score 95 - Green / Credible)
    "1": {
        "caseId": "CASE / 2026-001",
        "caseKey": "1",
        "badgeText": "Credible",
        "badgeType": "green",
        "category": "Risk intelligence / Entity verification",
        "name": "Apex Retail LLC",
        "industry": "Consumer goods retail",
        "claimedSqFt": "2,500 sq ft",
        "address": "120 Commerce Ave, Suite 100, Sample City, SC 00000",
        "confidenceScore": 95,
        "statusBanner": "High entity confidence",
        "statusType": "green",
        "statusSubtext": "Demo outcome: consistent operating footprint.",
        "zoneContext": "ZONE CONTEXT: COMMERCIAL",
        "zoneName": "Commercial retail corridor",
        "zoneDescription": "Storefront footprint and retail zoning align with the intended use.",
        "coordinates": "33.8361\u00b0 N, 81.1637\u00b0 W",
        "claimedAreaNumber": "2,500 sq ft",
        "observedAreaNumber": "2,500 sq ft",
        "areaDiscrepancy": "Aligned with parcel boundary",
        "mapLabel": "120 Commerce Ave",
        "streetName1": "COMMERCE_AVE",
        "streetName2": "RETAIL DISTRICT",
        "streetName3": "MAIN_ST",
        "legendText": "Commercial / Expected boundary",
        "signals": [
            {
                "title": "Zoning Match",
                "desc": "Parcel zoned commercial \u00b7 active demo commercial zone.",
                "badge": "Aligned",
                "status": "verified",
                "source": "CITY"
            },
            {
                "title": "Employee Activity",
                "desc": "Record of workforce activity across multiple payroll feeds.",
                "badge": "Present",
                "status": "verified",
                "source": "STATE REG"
            },
            {
                "title": "Footprint Consistency",
                "desc": "Observed parcel supports the claimed 2,500 sq ft footprint.",
                "badge": "Normal",
                "status": "verified",
                "source": "PARCEL"
            },
            {
                "title": "Address Occupancy",
                "desc": "One sole tenant confirmed at the commercial suite.",
                "badge": "Single-occupancy",
                "status": "verified",
                "source": "USPS"
            }
        ]
    },

    # CASE 2: Phantom Logistics LLC (Score 12 - Red / Ghost Address)
    "2": {
        "caseId": "CASE / 2026-002",
        "caseKey": "2",
        "badgeText": "Ghost Address",
        "badgeType": "red",
        "category": "Risk intelligence / Entity verification",
        "name": "Phantom Logistics LLC",
        "industry": "Freight & cargo transportation",
        "claimedSqFt": "18,000 sq ft",
        "address": "9 Industrial Blvd, Unit 7, Vacant Lot, SC 00000",
        "confidenceScore": 12,
        "statusBanner": "Ghost address detected",
        "statusType": "red",
        "statusSubtext": "Demo outcome: address does not correspond to any real structure.",
        "zoneContext": "ZONE CONTEXT: VACANT / UNVERIFIABLE",
        "zoneName": "Vacant lot \u00b7 No structure confirmed",
        "zoneDescription": "Satellite and parcel data show an empty undeveloped lot. No warehouse, dock, or commercial structure exists at this address.",
        "coordinates": "33.9211\u00b0 N, 81.0499\u00b0 W",
        "claimedAreaNumber": "18,000 sq ft",
        "observedAreaNumber": "0 sq ft (vacant)",
        "areaDiscrepancy": "No structure observed at GPS coordinates",
        "mapLabel": "9 Industrial Blvd",
        "streetName1": "INDUSTRIAL_BLVD",
        "streetName2": "VACANT LOT \u00b7 UNBUILT",
        "streetName3": "FREIGHT_RD",
        "legendText": "Ghost address \u00b7 No observable structure",
        "signals": [
            {
                "title": "Address Deliverability",
                "desc": "USPS flags address as undeliverable \u00b7 no structure on record.",
                "badge": "Undeliverable",
                "status": "contradiction",
                "source": "USPS"
            },
            {
                "title": "Parcel Structure",
                "desc": "Satellite imagery confirms vacant undeveloped land at coordinates.",
                "badge": "No structure",
                "status": "contradiction",
                "source": "PARCEL"
            },
            {
                "title": "Employee Activity",
                "desc": "Zero workforce registrations or payroll filings at this address.",
                "badge": "Zero activity",
                "status": "contradiction",
                "source": "STATE REG"
            },
            {
                "title": "Utility Connections",
                "desc": "No active electricity, water, or commercial utility accounts found.",
                "badge": "No utilities",
                "status": "contradiction",
                "source": "UTILITY"
            },
            {
                "title": "Business Registry",
                "desc": "Entity filed with state but agent address differs from claimed location.",
                "badge": "Agent mismatch",
                "status": "contradiction",
                "source": "IL SOS"
            }
        ]
    },

    # CASE 3: Global Shell Holdings (Score 45 - Amber / Shared Location)
    "3": {
        "caseId": "CASE / 2026-003",
        "caseKey": "3",
        "badgeText": "Shared Location",
        "badgeType": "amber",
        "category": "Risk intelligence / Entity verification",
        "name": "Global Shell Holdings",
        "industry": "Investment holding company",
        "claimedSqFt": "12,000 sq ft",
        "address": "210 Commerce Ave, Suite 500, Sample City, SC 00000",
        "confidenceScore": 45,
        "statusBanner": "Mixed entity confidence",
        "statusType": "amber",
        "statusSubtext": "Demo outcome: shared occupancy requires further review.",
        "zoneContext": "ZONE CONTEXT: MIXED-USE",
        "zoneName": "Multi-tenant office district",
        "zoneDescription": "Shared office parcel is plausible, but the entity's exclusive footprint is unclear.",
        "coordinates": "33.8415\u00b0 N, 81.1580\u00b0 W",
        "claimedAreaNumber": "12,000 sq ft",
        "observedAreaNumber": "1,800 sq ft suite",
        "areaDiscrepancy": "Multiple entities registered to shared suite",
        "mapLabel": "210 Commerce Ave",
        "streetName1": "COMMERCE_AVE",
        "streetName2": "FINANCIAL DISTRICT",
        "streetName3": "PINE_ST",
        "legendText": "Commercial / Shared boundaries",
        "signals": [
            {
                "title": "Zoning Match",
                "desc": "Office use permitted in commercial zone.",
                "badge": "Partial",
                "status": "verified",
                "source": "CITY"
            },
            {
                "title": "Employee Activity",
                "desc": "Activity detected but inconsistent for stated firm density.",
                "badge": "Ambiguous",
                "status": "contradiction",
                "source": "STATE REG"
            },
            {
                "title": "Footprint Consistency",
                "desc": "Claimed 12,000 sq ft exceeds apparent suite share.",
                "badge": "Skewed",
                "status": "contradiction",
                "source": "PARCEL"
            },
            {
                "title": "Address Occupancy",
                "desc": "Multiple distinct organizations share the same suite address.",
                "badge": "Shared space",
                "status": "contradiction",
                "source": "USPS"
            }
        ]
    }
}

ALIASES = {
    "1": "1", "apex": "1", "retail": "1", "credible": "1",
    "2": "2", "phantom": "2", "ghost": "2", "logistics": "2", "vacant": "2",
    "3": "3", "shell": "3", "global": "3", "holdings": "3", "shared": "3",
}

def resolve_case(query):
    if not query:
        return DATABASE["1"]
    q = query.strip()
    if q in DATABASE:
        return DATABASE[q]
    q_lower = q.lower()
    for alias_key, target in ALIASES.items():
        if alias_key in q_lower:
            return DATABASE[target]
    for k, v in DATABASE.items():
        if (q_lower in k.lower() or
                q_lower in v["name"].lower() or
                q_lower in v["address"].lower() or
                q_lower in v["caseId"].lower()):
            return v
    return DATABASE["1"]


class GeoTrustHandler(http.server.SimpleHTTPRequestHandler):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, directory=BASE_DIR, **kwargs)

    def end_headers(self):
        self.send_header("Access-Control-Allow-Origin", "*")
        self.send_header("Access-Control-Allow-Methods", "GET, OPTIONS")
        self.send_header("Access-Control-Allow-Headers", "Content-Type")
        super().end_headers()

    def do_OPTIONS(self):
        self.send_response(200)
        self.end_headers()

    def do_GET(self):
        parsed = urllib.parse.urlparse(self.path)
        path = parsed.path

        if path.startswith("/api/evaluate"):
            case_id = path.replace("/api/evaluate/", "").replace("/api/evaluate", "").strip()
            case_id = urllib.parse.unquote(case_id)
            data = resolve_case(case_id if case_id else "1")
            result = dict(data)
            result["explanations"] = [
                f"{'CRITICAL: ' if s['status'] == 'contradiction' else 'VERIFIED: '}{s['title']} - {s['desc']}"
                for s in data["signals"]
            ]
            self.send_response(200)
            self.send_header("Content-Type", "application/json")
            self.end_headers()
            self.wfile.write(json.dumps(result).encode("utf-8"))
            return

        if path in ("", "/"):
            self.path = "/index.html"

        return super().do_GET()


def run():
    server_address = ("", PORT)
    httpd = http.server.ThreadingHTTPServer(server_address, GeoTrustHandler)
    print(f"GeoTrust AI server running at http://localhost:{PORT}")
    try:
        httpd.serve_forever()
    except KeyboardInterrupt:
        pass
    finally:
        httpd.server_close()


if __name__ == "__main__":
    run()
