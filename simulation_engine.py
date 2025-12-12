import random
import datetime

# --- STAGE 1: LEXICAL-SEMANTIC PARSING & DNA EXTRACTION ---

def parse_input_and_extract_dna(idea_text, selected_industry=None):
    """
    Tokenizes input, extracts action-noun pairs, determines domain,
    identifies target user, and flags constraints.
    """
    text_lower = idea_text.lower()
    
    # 1. Domain Classification
    domain_keywords = {
        "Health": ["health", "sleep", "diet", "fitness", "doctor", "medical", "patient", "workout", "monitor", "gym", "mental", "hospital", "wellness"],
        "Productivity": ["work", "manage", "track", "task", "time", "focus", "schedule", "calendar", "note", "job", "team", "project"],
        "FinTech": ["money", "save", "invest", "stock", "crypto", "bank", "pay", "wallet", "budget", "finance", "loan", "upi", "rupee"],
        "EdTech": ["learn", "study", "course", "tutor", "school", "class", "exam", "grade", "skill", "education", "student"],
        "E-Commerce": ["buy", "sell", "shop", "store", "marketplace", "delivery", "fashion", "brand", "retail", "product"],
        "Social": ["connect", "meet", "chat", "friends", "community", "network", "share", "social", "media"],
        "Food": ["food", "eat", "restaurant", "delivery", "chef", "cook", "recipe", "dining", "meal", "kitchen"],
        "GreenTech": ["recycl", "green", "carbon", "sustainab", "solar", "energy", "waste", "climate"]
    }
    
    detected_domain = selected_industry if selected_industry else "General Consumer"
    
    if not selected_industry:
        max_matches = 0
        for domain, keywords in domain_keywords.items():
            matches = sum(1 for k in keywords if k in text_lower)
            if matches > max_matches:
                max_matches = matches
                detected_domain = domain
                
        if max_matches == 0 and ("ai" in text_lower or "artificial intelligence" in text_lower):
            detected_domain = "Productivity" # Default for generic AI ideas

    # 2. Target User Extraction
    target_user_map = {
        "parent": {"archetype": "parent", "time_scarcity": "high", "income_tier": "mid"},
        "student": {"archetype": "student", "time_scarcity": "mid", "income_tier": "low"},
        "professional": {"archetype": "professional", "time_scarcity": "high", "income_tier": "high"},
        "doctor": {"archetype": "professional", "time_scarcity": "extreme", "income_tier": "high"},
        "freelancer": {"archetype": "freelancer", "time_scarcity": "variable", "income_tier": "variable"},
        "gamer": {"archetype": "gamer", "time_scarcity": "low", "income_tier": "low-mid"},
        "elderly": {"archetype": "elderly", "time_scarcity": "low", "income_tier": "mid"},
        "sme": {"archetype": "small_business_owner", "time_scarcity": "extreme", "income_tier": "mid"},
    }
    
    extracted_user = {"archetype": "general_user", "time_scarcity": "mid", "income_tier": "mid"}
    for keyword, traits in target_user_map.items():
        if keyword in text_lower:
            extracted_user = traits
            break
            
    # 3. Action Logic
    action_type = "utility"
    if any(x in text_lower for x in ["monitor", "track", "measure", "analyze"]):
        action_type = "monitoring"
    elif any(x in text_lower for x in ["connect", "match", "network"]):
        action_type = "network"
    elif any(x in text_lower for x in ["buy", "sell", "order", "book"]):
        action_type = "transaction"

    # 4. Constraint Detection & Monetization
    constraints = []
    monetization = []
    
    if "offline" in text_lower or "no wifi" in text_lower: constraints.append("offline_capable")
    if "cheap" in text_lower or "free" in text_lower: constraints.append("low_cost")
    if "privacy" in text_lower: constraints.append("high_privacy")
    
    if "subscription" in text_lower: monetization.append("subscription")
    if "freemium" in text_lower: monetization.append("freemium")
    if "commission" in text_lower: monetization.append("commission")

    # 5. Complexity Score
    tech_terms = ["ai", "blockchain", "vr", "ar", "machine learning", "crypto", "biometric"]
    tech_density = sum(1 for t in tech_terms if t in text_lower)
    complexity = min(10, 3 + tech_density * 2)

    return {
        "domain": detected_domain,
        "action_type": action_type,
        "target_user": extracted_user,
        "constraints": constraints,
        "monetization": monetization,
        "complexity_score": complexity,
        "tech_dependency_level": "high" if tech_density > 0 else "mid",
        "original_text": idea_text,
        "geo_context": "India" # Defaulting context to India per requirement
    }

# --- STAGE 2: SYNTHETIC MODEL CONSTRUCTION ---

def construct_synthetic_model(seed):
    """
    Builds personas and user journey based on seed data.
    """
    domain = seed["domain"]
    user = seed["target_user"]
    
    # Value Proposition
    verb_map = {"monitoring": "Gain visibility into metrics", "network": "Connect with peers", "transaction": "Seamlessly exchange value", "utility": "Optimize daily tasks"}
    val_prop_start = verb_map.get(seed["action_type"], "Improve life quality")
    value_prop = f"{val_prop_start} to reduce {user['time_scarcity']} time scarcity."

    # 5 Persona Generation (Enhanced)
    base_personas = [
        {"role": "Primary User", "type": user["archetype"], "adoption": "High"},
        {"role": "Early Adopter", "type": "Tech Enthusiast", "adoption": "Very High"},
        {"role": "Skeptic", "type": "Traditionalist", "adoption": "Low"},
        {"role": "Economic Buyer", "type": "Value Seeker", "adoption": "Medium"},
        {"role": "Influencer", "type": "Community Lead", "adoption": "High"}
    ]
    
    personas = []
    for p in base_personas:
        personas.append({
            "name": f"{p['type']} ({p['role']})",
            "role": p['role'],
            "primary_pain": "Inefficiency" if p['role'] == "Primary User" else "Cost/Risk",
            "decision_driver": "Innovation" if p['role'] == "Early Adopter" else "ROI",
            "adoption_likelihood": 85 if p['adoption'] == "Very High" else (30 if p['adoption'] == "Low" else 60)
        })
    
    # User Journey Map
    journey_friction = {
        "awareness": 10,
        "evaluation": 20 + (seed["complexity_score"] * 2),
        "onboarding": 15 if seed["action_type"] == "monitoring" else 5,
        "adoption": 30 if seed["tech_dependency_level"] == "high" else 10
    }
    
    return {
        "value_prop": value_prop,
        "personas": personas,
        "journey_map": journey_friction
    }

# --- STAGE 3: ENVIRONMENTAL PARAMETER CALCULATION (P-SET) ---

# --- INTERNAL KNOWLEDGE BASE (INDIAN MARKET - 2024 BENCHMARKS) ---
INDIAN_MARKET_DATA = {
    "Health": {
        "cac": 800, "trust_baseline": 45, "growth_rate": 0.18, 
        "competitors": 65, "reg_risk": 85, "digital_adoption": 40
    },
    "FinTech": {
        "cac": 1200, "trust_baseline": 55, "growth_rate": 0.25, 
        "competitors": 90, "reg_risk": 95, "digital_adoption": 75
    },
    "Productivity": {
        "cac": 450, "trust_baseline": 65, "growth_rate": 0.12, 
        "competitors": 50, "reg_risk": 15, "digital_adoption": 60
    },
    "EdTech": {
        "cac": 1500, "trust_baseline": 70, "growth_rate": 0.22, 
        "competitors": 85, "reg_risk": 30, "digital_adoption": 65
    },
    "E-Commerce": {
        "cac": 600, "trust_baseline": 60, "growth_rate": 0.20, 
        "competitors": 95, "reg_risk": 25, "digital_adoption": 80
    },
    "Food": {
        "cac": 250, "trust_baseline": 65, "growth_rate": 0.30, 
        "competitors": 92, "reg_risk": 40, "digital_adoption": 85
    },
    "Social": {
        "cac": 150, "trust_baseline": 50, "growth_rate": 0.45, 
        "competitors": 88, "reg_risk": 60, "digital_adoption": 90
    },
    "GreenTech": {
        "cac": 900, "trust_baseline": 60, "growth_rate": 0.15, 
        "competitors": 30, "reg_risk": 50, "digital_adoption": 35
    },
    "General Consumer": {
        "cac": 400, "trust_baseline": 55, "growth_rate": 0.10, 
        "competitors": 60, "reg_risk": 20, "digital_adoption": 50
    }
}

# --- STAGE 3: ENVIRONMENTAL PARAMETER CALCULATION (INDIAN CONTEXT) ---

def calculate_physics(seed, model):
    """
    Calculates detailed parameters using the Internal Knowledge Base.
    """
    domain = seed["domain"]
    user_tier = seed["target_user"]["income_tier"]
    
    # Fetch Benchmarks
    benchmarks = INDIAN_MARKET_DATA.get(domain, INDIAN_MARKET_DATA["General Consumer"])
    
    # 1. Trust Score (T_score)
    t_score = benchmarks["trust_baseline"]
    if "high_privacy" in seed["constraints"]: t_score -= 10
    if user_tier == "low": t_score -= 15 # Lower trust baseline in mass market
    
    # 2. Price Fit (P_fit)
    p_fit = 60
    if "low_cost" in seed["constraints"] and user_tier in ["low", "mid"]: p_fit += 25
    if "subscription" in seed["monetization"] and user_tier == "low": p_fit -= 30
    
    # 3. Market Size (M_size) - Derived from Digital Adoption & Growth
    m_size_score = int(benchmarks["digital_adoption"] * 1.2)
    if seed["target_user"]["archetype"] == "professional": m_size_score = 50 # Niche
    
    # 4. Digital Literacy Alignment (D_lit)
    d_lit = 70
    if seed["tech_dependency_level"] == "high" and user_tier == "low": d_lit = 30
    
    # 5. Competition (Comp) - Based on Density
    comp = benchmarks["competitors"]
    if "ai" in seed["original_text"].lower(): comp += 15
    
    # 6. Infrastructure Readiness (Infra)
    infra = 80
    if "offline_capable" in seed["constraints"]: infra = 95
    if seed["action_type"] == "transaction" and user_tier == "low": infra = 60
        
    return {
        "t_score": min(100, max(0, t_score)),
        "c_int": int(comp / 10),
        "factors": {
            "trust": min(100, max(0, t_score)),
            "price_fit": min(100, max(0, p_fit)),
            "market_size": min(100, max(0, m_size_score)),
            "digital_literacy": min(100, max(0, d_lit)),
            "competition": min(100, max(0, comp)),
            "infrastructure": min(100, max(0, infra))
        },
        "benchmarks": benchmarks # Pass for reporting
    }

# --- STAGE 4: COLLISION DETECTION ---

# --- STAGE 4 & 5: COLLISION DETECTION & MUTATION (BLOCKER & FIX) ---

def detect_collisions(p_set, model, seed):
    """
    Identifies the #1 Blocker and generates Urgent/Next actions.
    """
    factors = p_set["factors"]
    blocker = {}
    
    # Rules for Blocker Identification
    if factors["trust"] < 50:
        blocker = {
            "type": "Trust Deficit",
            "title": "Low User Trust",
            "desc": "Users are wary of sharing data or money due to lack of brand authority.",
            "severity": 9,
            "urgent_action": "Add 'Verified by' badges",
            "next_step": "Partner with a known entity"
        }
    elif factors["price_fit"] < 40:
        blocker = {
            "type": "Value Misalignment",
            "title": "Price Sensitivity Clash",
            "desc": "The perceived cost is too high for this income tier.",
            "severity": 8,
            "urgent_action": "Launch a 'Lite' version",
            "next_step": "Implement micro-transaction model"
        }
    elif factors["digital_literacy"] < 50:
        blocker = {
            "type": "Usability Fail",
            "title": "Too Complex",
            "desc": "Target users struggle with the tech interface.",
            "severity": 8,
            "urgent_action": "Simplify onboarding to 2 steps",
            "next_step": "Add voice-guided navigation"
        }
    elif factors["competition"] > 80:
        blocker = {
            "type": "Market Saturation",
            "title": "High Competition",
            "desc": "Market is crowded with established players.",
            "severity": 7,
            "urgent_action": "Focus on a hyper-niche feature",
            "next_step": "Target an underserved geo-region"
        }
    else:
        blocker = {
            "type": "Growth Stagnation",
            "title": "Slow Viral Growth",
            "desc": "Organic coefficient is low.",
            "severity": 5,
            "urgent_action": "Implement WhatsApp referral loop",
            "next_step": "Create shareable user content"
        }
        
    return blocker

# --- STAGE 5: MUTATION ENGINE (V2) ---
# Integrated into Collision Detection for simpler linking

# --- STAGE 6: TEMPORAL PROJECTION (INR) ---

# --- STAGE 6: TEMPORAL PROJECTION (INR - Multi-Scenario) ---

def run_temporal_projection_inr(seed, p_set, blocker):
    """
    Generates Worst/Expected/Best case scenarios for Week 1, Month 1, Month 3, Month 6, Year 1.
    Values in INR.
    """
    # Base LTV (Lifetime Value) in INR
    # Low income tier: ₹300, Mid: ₹1500, High: ₹5000
    base_ltv = 1500
    if seed["target_user"]["income_tier"] == "low": base_ltv = 300
    elif seed["target_user"]["income_tier"] == "high": base_ltv = 5000
    
    # Scenarios logic
    scenarios = {
        "worst": {"multiplier": 0.2, "growth_rate": 0.05, "driver": "Organic Search"},
        "expected": {"multiplier": 1.0, "growth_rate": 0.15, "driver": "Paid Ads"},
        "best": {"multiplier": 2.5, "growth_rate": 0.35, "driver": "Viral Social"}
    }
    
    projections = {}
    
    for case, params in scenarios.items():
        mult = params["multiplier"]
        
        # Initial Users (Week 1)
        w1_users = int(100 * mult)
        
        # Month 1
        m1_users = int(w1_users * (1 + params["growth_rate"])**4)
        m1_rev = m1_users * base_ltv * 0.1 # 10% conversion
        
        # Month 6
        m6_users = int(m1_users * (1 + params["growth_rate"])**24)
        
        # Year 1
        y1_users = int(m1_users * (1 + params["growth_rate"])**52)
        y1_rev = int(y1_users * base_ltv * 0.12) # Slightly better conversion
        
        projections[case] = {
            "w1_users": f"{w1_users}",
            "m1_users": f"{m1_users}",
            "m1_rev": f"₹{m1_rev/100000:.2f}L" if m1_rev > 99999 else f"₹{m1_rev:,}",
            "y1_users": f"{y1_users/1000:.1f}k" if y1_users > 1000 else f"{y1_users}",
            "y1_rev": f"₹{y1_rev/10000000:.2f}Cr" if y1_rev > 9999999 else (f"₹{y1_rev/100000:.2f}L" if y1_rev > 99999 else f"₹{y1_rev:,}"),
            "driver": params["driver"]
        }
        
    return projections

# --- STAGE 8: NORTH STAR ASSESSMENT ---

def assess_north_star(seed):
    """
    Determines the North Star Metric and assigns a Badge Level (1-5).
    """
    action = seed["action_type"]
    domain = seed["domain"]
    
    metric_map = {
        "transaction": "Gross Transaction Volume (GTV)",
        "monitoring": "Daily Active Users (DAU)",
        "network": "Weekly Retention Rate",
        "utility": "Time Saved Per User"
    }
    
    metric = metric_map.get(action, "Monthly Recurring Revenue (MRR)")
    
    # Logic for Badge Level (1-5)
    # 5 = Perfect alignment with value, 1 = Vanity metric
    level = 4
    if seed["monetization"] and "commission" in seed["monetization"] and action == "transaction":
        level = 5 # Perfect align
    if action == "network" and domain == "Social":
        level = 5
        
    return {
        "metric": metric,
        "badge_level": level,
        "label": f"Level {level} North Star Metric"
    }

# --- STAGE 9: DATA ASSEMBLY ---

def assemble_frontend_data(seed, p_set, blocker, projections, north_star, personas, summary, full_report_text):
    return {
        "north_star": north_star,
        "summary": summary,
        "idea_title": f"{seed['domain']} {seed['original_text'][:15].title()}..." if len(seed['original_text']) > 15 else seed['original_text'].title(),
        "blocker": blocker,
        "growth_projections": projections,
        "environmental_factors": p_set["factors"],
        "personas": personas[:3], # Top 3
        "full_report_text": full_report_text
    }

# --- MAIN CONTROLLER ---

def analyze_idea(idea_text, industry=None):
    seed = parse_input_and_extract_dna(idea_text, industry)
    model = construct_synthetic_model(seed)
    p_set = calculate_physics(seed, model)
    blocker = detect_collisions(p_set, model, seed) # This now includes mutations
    projections = run_temporal_projection_inr(seed, p_set, blocker)
    north_star = assess_north_star(seed)
    
    # Generate concise summary
    summary_text = f"A {seed['domain']} concept targeting {len(p_set['factors'])} key market variables. Trusted by {model['personas'][0]['name']} types, facing specific friction in {blocker['type']}."

    # Generate Full Text Report
    full_report = generate_full_report_text(seed, model, p_set, blocker, projections, north_star)

    # Assemble Final JSON
    data = assemble_frontend_data(
        seed, 
        p_set, 
        blocker, 
        projections, 
        north_star, 
        model['personas'], 
        summary_text,
        full_report
    )
    
    return data

def generate_full_report_text(seed, model, p_set, blocker, projections, north_star):
    """
    Generates a comprehensive, cited text report.
    """
    domain = seed['domain']
    idea = seed['original_text']
    benchmarks = p_set.get("benchmarks", {})
    
    report = f"""
==================================================
IDEA SIMULATION REPORT (V2.4)
Generated by Idea Simulator Lab
==================================================

[1] CONCEPT OVERVIEW
--------------------
Idea: {idea}
Sector: {domain}
North Star Metric: {north_star['metric']} ({north_star['label']})

[2] MARKET PHYSICS ANALYSIS (INDIAN CONTEXT)
--------------------------------------------
Methodology: Scored against 2024 Indian Industry Benchmarks.

> Trust Score: {p_set['t_score']}/100
  (Baseline for {domain}: {benchmarks.get('trust_baseline', 'N/A')}/100)
  Analysis: User willingness to engage is {p_set['t_score'] - benchmarks.get('trust_baseline', 0):+d} vs sector avg.

> Competition Intensity: {p_set['factors']['competition']}/100
  (Sector Density: {benchmarks.get('competitors', 'N/A')}/100)
  
> Digital Literacy Requirement: {p_set['factors']['digital_literacy']}/100
  (Target Segment Adoption: {benchmarks.get('digital_adoption', 'N/A')}%)

[3] CRITICAL BLOCKER IDENTIFIED
-------------------------------
Primary Growth Barrier: {blocker['title']}
Severity: {blocker['severity']}/10
Detailed Diagnosis: {blocker['desc']}

[4] STRATEGIC ROADMAP
---------------------
(A) URGENT ACTION (Immediate | 3-5 Days)
    Strategy: {blocker['urgent_action']}
    Expected Impact: Clear initial traction and validation.

(B) NEXT STEP (Strategic | 1-3 Months)
    Strategy: {blocker['next_step']}
    Goal: Sustainable growth loops.

[5] FINANCIAL PROJECTIONS (INR)
------------------------------
Forecast based on {domain} Average Revenue Per User (ARPU) and Indian cac benchmarks.

| Scenario   | Year 1 Users | Year 1 Revenue | Driver         |
|------------|--------------|----------------|----------------|
| Worst Case | {projections['worst']['y1_users']}        | {projections['worst']['y1_rev']}       | {projections['worst']['driver']} |
| EXPECTED   | {projections['expected']['y1_users']}       | {projections['expected']['y1_rev']}      | {projections['expected']['driver']}       |
| Best Case  | {projections['best']['y1_users']}       | {projections['best']['y1_rev']}      | {projections['best']['driver']}   |

[6] TARGET PERSONA PROFILES
---------------------------
Primary User: {model['personas'][0]['name']}
> Pain Point: {model['personas'][0]['primary_pain']}
> Decision Driver: {model['personas'][0]['decision_driver']}

Early Adopter: {model['personas'][1]['name']}
> Adoption Likelihood: {model['personas'][1]['adoption_likelihood']}%

==================================================
END OF REPORT
    """
    return report.strip()
