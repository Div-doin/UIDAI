# Aadhaar Fraud Intelligence System

## Problem Statement
Analyze Aadhaar Enrolment, Demographic Update, and Biometric Update datasets to detect patterns, anomalies, and fraud-risk indicators.  
Our objective is to identify suspicious Aadhaar identity behavior across India and build an AI-driven audit planning system.

---

## Approach
We do not classify individual Aadhaar numbers.  
Instead, we detect identity instability at a **pincode × month** level.

We combine:

1. **Enrolment Risk** — abnormal Aadhaar creation spikes  
2. **Demographic Instability** — frequent demographic corrections  
3. **Biometric Instability** — unusual biometric update behavior  

These are fused into a **Unified Aadhaar Stability Score**, and we use **Reinforcement Learning to recommend where audits should be deployed.**

---

## Datasets Used

| Dataset | Purpose | Key Columns |
|--------|--------|-------------|
| Enrolment Data | Detect abnormal enrolment spikes | date, pincode, age groups |
| Demographic Update Data | Detect identity drift | date, pincode, demographic update counts |
| Biometric Update Data | Detect biometric instability | date, pincode, biometric update counts |

---

## Pipeline Overview

Raw Aadhaar CSVs
        ↓
Cleaning & Aggregation
        ↓
Feature Engineering
        ↓
Anomaly Detection (Isolation Forest)
        ↓
Stability Score Calculation
        ↓
Reinforcement Learning Audit Recommendations

---

## Stability Score Formula


| Score | Meaning |
|------|--------|
| High | Aadhaar behavior stable (likely genuine) |
| Low | Suspicious behavior (needs audit) |

---

## Reinforcement Learning

| RL Concept | Aadhaar Meaning |
|-----------|----------------|
| Agent | UIDAI Audit Planner |
| State | Stability + anomaly + volatility features |
| Action | Select top-risk pincodes for audit |
| Reward | Stability improvement over time |

The RL model learns:
> “Which regions should be audited to reduce Aadhaar fraud risk?”

---

## Final Outputs

| File | Description |
|------|------------|
| `master_aadhaar_intelligence.csv` | Integrated Aadhaar risk intelligence |
| `rl_audit_recommendations.csv` | AI-based audit priorities |
| `high_risk_heatmap.png` | Visualization of suspicious regions |
| `top_30_high_risk_pins.csv` | Top audit-priority pincodes |

---

## How to Run

Inside your project directory:

python src/merge_pipeline.py
python src/rl_agent.py
python src/dashboard.py

---

## What Makes This Unique

- Works at a **regional level**, not individual IDs  
- Combines **3 independent fraud signals**  
- Uses **unsupervised anomaly detection**  
- Uses **Reinforcement Learning for audit optimization**  
- Privacy-preserving and scalable

---

## Team

| Member | Contribution |
|--------|-------------|
| A | Enrolment Risk Pipeline |
| J | Demographic Instability Pipeline |
| P | Biometric Anomaly Detection Pipeline |
| D | Final Integration + RL Audit System |

---

## Final Statement

We developed an AI-powered Aadhaar Stability Intelligence System that identifies suspicious regional Aadhaar behavior and recommends optimal audit deployment to prevent fraud and identity misuse.
