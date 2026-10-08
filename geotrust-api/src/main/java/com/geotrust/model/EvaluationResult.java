package com.geotrust.model;

import java.util.ArrayList;
import java.util.List;

public class EvaluationResult {
    private int confidenceScore;
    private List<String> explanations;

    public EvaluationResult() {
        this.confidenceScore = 100;
        this.explanations = new ArrayList<>();
    }

    public int getConfidenceScore() { return confidenceScore; }
    public void setConfidenceScore(int confidenceScore) { this.confidenceScore = confidenceScore; }

    public List<String> getExplanations() { return explanations; }
    public void addExplanation(String explanation) { this.explanations.add(explanation); }
}
