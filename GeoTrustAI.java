import java.util.ArrayList;
import java.util.List;

public class GeoTrustAI {

    static class BusinessProfile {
        String caseId;
        String name;
        String industry;
        String addressSignal;
        int sqFt;
        int registeredCompanies;
        int employees;

        public BusinessProfile(String caseId, String name, String industry, String addressSignal, int sqFt, int registeredCompanies, int employees) {
            this.caseId = caseId;
            this.name = name;
            this.industry = industry;
            this.addressSignal = addressSignal;
            this.sqFt = sqFt;
            this.registeredCompanies = registeredCompanies;
            this.employees = employees;
        }
    }

    static class EvaluationResult {
        int confidenceScore;
        List<String> explanations;

        public EvaluationResult() {
            this.confidenceScore = 100;
            this.explanations = new ArrayList<>();
        }
    }

    public static void main(String[] args) {
        List<BusinessProfile> profiles = new ArrayList<>();
        profiles.add(new BusinessProfile("Case 1", "Apex Retail LLC", "Retail Store", "Commercial Strip Mall", 2500, 1, 12));
        profiles.add(new BusinessProfile("Case 2", "Titanium Steel Smelting", "Heavy Manufacturing", "Residential Single-Family", 900, 1, 0));
        profiles.add(new BusinessProfile("Case 3", "Global Shell Holdings", "Financial Consulting", "Virtual Office Co-working", 150, 142, 1));

        for (BusinessProfile profile : profiles) {
            EvaluationResult result = evaluateRisk(profile);
            printResult(profile, result);
        }
    }

    public static EvaluationResult evaluateRisk(BusinessProfile profile) {
        EvaluationResult result = new EvaluationResult();

        // Rule 1 (Zoning Contradiction): If Industry implies Heavy Manufacturing but Address Signal implies Residential
        if (profile.industry.contains("Heavy Manufacturing") && profile.addressSignal.contains("Residential")) {
            result.confidenceScore -= 60;
            result.explanations.add("CRITICAL: Industrial business claimed at a residential zoning location.");
        }

        // Rule 2 (Ghost Activity): If Sq Ft > 2000 but Employees == 0
        if (profile.sqFt > 2000 && profile.employees == 0) {
            result.confidenceScore -= 30;
            result.explanations.add("WARNING: Large physical footprint with zero registered employee activity.");
        }

        // Rule 3 (Shell Density): If Registered Companies > 10 and Sq Ft < 500
        if (profile.registeredCompanies > 10 && profile.sqFt < 500) {
            result.confidenceScore -= 40;
            result.explanations.add("WARNING: High density of registered entities in constrained physical space. Strong indicator of a virtual office/shell network.");
        }

        return result;
    }

    public static void printResult(BusinessProfile profile, EvaluationResult result) {
        System.out.println("=========================================");
        System.out.println("GEOTRUST AI - SIGNAL FUSION ENGINE");
        System.out.println("Analyzing Case: " + profile.caseId + " / " + profile.name);
        System.out.println("... Fusing Open Registry Data");
        System.out.println("... Cross-referencing Geospatial Data");
        System.out.println();
        System.out.println("FINAL CONFIDENCE SCORE: " + result.confidenceScore + "/100");
        System.out.println("Explainable Factors:");
        
        if (result.explanations.isEmpty()) {
            System.out.println("[-] All signals verified. No anomalies detected.");
        } else {
            for (String explanation : result.explanations) {
                System.out.println("[-] " + explanation);
            }
        }
        System.out.println();
    }
}
