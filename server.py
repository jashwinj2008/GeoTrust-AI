import http.server
import json
import os
import urllib.parse

PORT = 8080
BASE_DIR = os.path.dirname(os.path.abspath(__file__))

DATABASE = {
    # CASE 1: Apex Retail LLC (Score 95 - Green / High Confidence)
    "1": {
        "caseId": "CASE / 2026-001",
        "caseKey": "1",
        "badgeText": "Credible",
        "badgeType": "green",
        "category": "Risk intelligence / Entity verification",
        "analysisType": "Presentation scenario · Static analysis",
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
        "coordinates": "33.8361° N, 81.1637° W",
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
                "desc": "Parcel zoned commercial/active demo commercial zone",
                "badge": "Aligned",
                "status": "verified"
            },
            {
                "title": "Employee Activity",
                "desc": "Record of preliminary activity across workforce feeds.",
                "badge": "Present",
                "status": "verified"
            },
            {
                "title": "Footprint Consistency",
                "desc": "Observed footprint support for the claimed 2,500 sq ft.",
                "badge": "Normal",
                "status": "verified"
            },
            {
                "title": "Address Occupancy",
                "desc": "One sole tenant associated with the demo suite.",
                "badge": "Single-occupancy",
                "status": "verified"
            }
        ]
    },

    # CASE 2: Titanium Steel Smelting (Score 15 - Red / Severe Anomaly)
    "2": {
        "caseId": "CASE / 2026-002",
        "caseKey": "2",
        "badgeText": "Severe Anomaly",
        "badgeType": "red",
        "category": "Risk intelligence / Entity verification",
        "analysisType": "Presentation scenario · Static analysis",
        "name": "Titanium Steel Smelting",
        "industry": "Heavy metal manufacturing",
        "claimedSqFt": "35,000 sq ft",
        "address": "451 Market St, Unit 2, Sample City, SC 00000",
        "confidenceScore": 15,
        "statusBanner": "Low entity confidence",
        "statusType": "red",
        "statusSubtext": "Demo outcome: claimed operation lacks evidence.",
        "zoneContext": "ZONE CONTEXT: RESIDENTIAL",
        "zoneName": "Residential neighborhood",
        "zoneDescription": "Quiet residential parcel in contradiction with a heavy industrial facility.",
        "coordinates": "34.0012° N, 81.0348° W",
        "claimedAreaNumber": "35,000 sq ft",
        "observedAreaNumber": "1,200 sq ft",
        "areaDiscrepancy": "Severe contradiction: R-1 residential lot",
        "mapLabel": "451 Market St",
        "streetName1": "MARKET_ST",
        "streetName2": "RESIDENTIAL ZONE",
        "streetName3": "OAK_LANE",
        "legendText": "Contradiction / Exceeds boundary",
        "signals": [
            {
                "title": "Zoning Match",
                "desc": "Residential demo zone excludes industrial smelting.",
                "badge": "Conflict",
                "status": "contradiction"
            },
            {
                "title": "Employee Activity",
                "desc": "No observing workforce activity in the demo surface.",
                "badge": "Absent",
                "status": "contradiction"
            },
            {
                "title": "Footprint Consistency",
                "desc": "Small parcel cannot support the claimed 35,000 sq ft.",
                "badge": "Mismatch",
                "status": "contradiction"
            },
            {
                "title": "Address Occupancy",
                "desc": "No industrial occupant linked to the demo address.",
                "badge": "Unverified",
                "status": "contradiction"
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
        "analysisType": "Presentation scenario · Static analysis",
        "name": "Global Shell Holdings",
        "industry": "Investment holding company",
        "claimedSqFt": "12,000 sq ft",
        "address": "210 Commerce Ave, Suite 500, Sample City, SC 00000",
        "confidenceScore": 45,
        "statusBanner": "Mixed entity confidence",
        "statusType": "amber",
        "statusSubtext": "Demo outcome: shared occupancy needs review.",
        "zoneContext": "ZONE CONTEXT: MIXED-USE",
        "zoneName": "Multi-tenant office district",
        "zoneDescription": "Shared office parcel is plausible, but the entity's exclusive footprint is unclear.",
        "coordinates": "33.8415° N, 81.1580° W",
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
                "status": "amber"
            },
            {
                "title": "Employee Activity",
                "desc": "Activity detected but inconsistent for stated firm density.",
                "badge": "Ambiguous",
                "status": "amber"
            },
            {
                "title": "Footprint Consistency",
                "desc": "Claimed 12,000 sq ft exceeds apparent suite share.",
                "badge": "Skewed",
                "status": "amber"
            },
            {
                "title": "Address Occupancy",
                "desc": "Multiple distinct organizations share the same suite.",
                "badge": "Shared space",
                "status": "amber"
            }
        ]
    },

    # CASE 4: Fulton Supply Co. (Score 78 - Lime / Review Needed)
    "GT-02481": {
        "caseId": "CASE GT-02481",
        "caseKey": "GT-02481",
        "badgeText": "Manual Review",
        "badgeType": "lime",
        "category": "Risk intelligence / Entity verification",
        "analysisType": "Presentation scenario · Static analysis",
        "name": "Fulton Supply Co.",
        "industry": "Wholesale building materials",
        "claimedSqFt": "4,800 sq ft",
        "address": "1840 W Fulton St, Chicago, IL 60612",
        "confidenceScore": 78,
        "statusBanner": "Manual review · 2 contradictions",
        "statusType": "lime",
        "statusSubtext": "Claim confidence, not a fraud-risk probability.",
        "zoneContext": "ZONE CONTEXT: COMMERCIAL / INDUSTRIAL",
        "zoneName": "Fulton Market corridor",
        "zoneDescription": "Building footprint observed smaller than applicant claimed square footage.",
        "coordinates": "41.8867° N, 87.6734° W",
        "claimedAreaNumber": "4,800 sq ft",
        "observedAreaNumber": "3,100 sq ft",
        "areaDiscrepancy": "35% below claimed area",
        "mapLabel": "1840 W Fulton St",
        "streetName1": "W_FULTON_ST",
        "streetName2": "FULTON MARKET",
        "streetName3": "N_LAKE_ST",
        "legendText": "Subject parcel / Footprint contradiction",
        "signals": [
            {
                "title": "Business registry",
                "desc": "Legal name and active status matched",
                "badge": "IL SOS",
                "status": "verified"
            },
            {
                "title": "Address validation",
                "desc": "Deliverable commercial address",
                "badge": "USPS",
                "status": "verified"
            },
            {
                "title": "Commercial zoning",
                "desc": "Wholesale use permitted in M2-3",
                "badge": "CITY",
                "status": "verified"
            },
            {
                "title": "Building footprint",
                "desc": "3,100 sq ft observed vs. 4,800 claimed",
                "badge": "PARCEL",
                "status": "contradiction"
            },
            {
                "title": "Industry alignment",
                "desc": "Current listing indicates self-storage",
                "badge": "PLACES",
                "status": "contradiction"
            }
        ]
    }
}

ALIASES = {
    "1": "1",
    "case 1": "1",
    "case1": "1",
    "apex": "1",
    "2026-001": "1",
    "2": "2",
    "case 2": "2",
    "case2": "2",
    "titanium": "2",
    "2026-002": "2",
    "3": "3",
    "case 3": "3",
    "case3": "3",
    "shell": "3",
    "global": "3",
    "2026-003": "3",
    "fulton": "GT-02481",
    "gt-02481": "GT-02481",
    "1840": "GT-02481"
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

        # Serve index.html for root
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
