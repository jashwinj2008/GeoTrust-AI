package com.geotrust.service;

import com.geotrust.model.BusinessProfile;
import com.geotrust.model.EvaluationResult;
import org.springframework.stereotype.Service;

import java.util.HashMap;
import java.util.Map;

@Service
public class EvaluationService {

    private final Map<String, BusinessProfile> database = new HashMap<>();

    public EvaluationService() {
        // Case IDs are mapped to "1", "2", and "3" for easier URL paths
        database.put("1", new BusinessProfile("1", "Apex Retail LLC", "Retail Store", "Commercial Strip Mall", 2500, 1, 12));
        database.put("2", new BusinessProfile("2", "Titanium Steel Smelting", "Heavy Manufacturing", "Residential Single-Family", 900, 1, 0));
        database.put("3", new BusinessProfile("3", "Global Shell Holdings", "Financial Consulting", "Virtual Office Co-working", 150, 142, 1));
    }

    public EvaluationResult evaluateRisk(String caseId) {
        BusinessProfile profile = database.get(caseId);
        
        if (profile == null) {
            throw new IllegalArgumentException("Case ID not found: " + caseId);
        }

        EvaluationResult result = new EvaluationResult();

        // Rule 1: Zoning Contradiction
        if (profile.getIndustry().contains("Heavy Manufacturing") && profile.getAddressSignal().contains("Residential")) {
            result.setConfidenceScore(result.getConfidenceScore() - 60);
            result.addExplanation("CRITICAL: Industrial business claimed at a residential zoning location.");
        }

        // Rule 2: Ghost Activity
        if (profile.getSqFt() > 2000 && profile.getEmployees() == 0) {
            result.setConfidenceScore(result.getConfidenceScore() - 30);
            result.addExplanation("WARNING: Large physical footprint with zero registered employee activity.");
        }

        // Rule 3: Shell Density
        if (profile.getRegisteredCompanies() > 10 && profile.getSqFt() < 500) {
            result.setConfidenceScore(result.getConfidenceScore() - 40);
            result.addExplanation("WARNING: High density of registered entities in constrained physical space. Strong indicator of a virtual office/shell network.");
        }
        
        if (result.getExplanations().isEmpty()) {
            result.addExplanation("All signals verified. No anomalies detected.");
        }

        return result;
    }
}
