package com.geotrust.model;

public class BusinessProfile {
    private String caseId;
    private String name;
    private String industry;
    private String addressSignal;
    private int sqFt;
    private int registeredCompanies;
    private int employees;

    public BusinessProfile(String caseId, String name, String industry, String addressSignal, int sqFt, int registeredCompanies, int employees) {
        this.caseId = caseId;
        this.name = name;
        this.industry = industry;
        this.addressSignal = addressSignal;
        this.sqFt = sqFt;
        this.registeredCompanies = registeredCompanies;
        this.employees = employees;
    }

    public String getCaseId() { return caseId; }
    public String getName() { return name; }
    public String getIndustry() { return industry; }
    public String getAddressSignal() { return addressSignal; }
    public int getSqFt() { return sqFt; }
    public int getRegisteredCompanies() { return registeredCompanies; }
    public int getEmployees() { return employees; }
}
