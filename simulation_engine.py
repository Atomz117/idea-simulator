import random
import datetime

# --- STAGE 1: LEXICAL-SEMANTIC PARSING & DNA EXTRACTION ---

def parse_input_and_extract_dna(idea_text):
    """
    Tokenizes input, extracts action-noun pairs, determines domain,
    identifies target user, and flags constraints.
    """
    text_lower = idea_text.lower()
    
    # 1. Domain Classification
    domain_keywords = {
        "Health": ["health", "sleep", "diet", "fitness", "doctor", "medical", "patient", "workout", "monitor", "gym", "mental"],
        "Productivity": ["work", "manage", "track", "task", "time", "focus", "schedule", "calendar", "note", "job"],
        "FinTech": ["money", "save", "invest", "stock", "crypto", "bank", "pay", "wallet", "budget", "finance"],
        "EdTech": ["learn", "study", "course", "tutor", "school", "class", "exam", "grade", "skill"],
        "E-Commerce": ["buy", "sell", "shop", "store", "marketplace", "delivery", "fashion", "brand"],
        "Social": ["connect", "meet", "chat", "friends", "community", "network", "share", "social"],
        "GreenTech": ["recycl", "green", "carbon", "sustainab", "solar", "energy", "waste"]
    }
    
    detected_domain = "General Consumer"
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
    elif any(x in text_lower for x in ["buy", "sell", "order"]):
        action_type = "transaction"

    # 4. Constraint Detection
    constraints = []
    if "offline" in text_lower or "no wifi" in text_lower:
        constraints.append("offline_capable")
    if "cheap" in text_lower or "under" in text_lower or "free" in text_lower:
        constraints.append("low_cost")
    if "privacy" in text_lower or "secure" in text_lower:
        constraints.append("high_privacy")

    # 5. Complexity Score
    tech_terms = ["ai", "blockchain", "vr", "ar", "machine learning", "crypto", "biometric"]
    tech_density = sum(1 for t in tech_terms if t in text_lower)
    complexity = min(10, 3 + tech_density * 2)

    return {
        "domain": detected_domain,
        "action_type": action_type,
        "target_user": extracted_user,
        "constraints": constraints,
        "complexity_score": complexity,
        "tech_dependency_level": "high" if tech_density > 0 else "mid",
        "original_text": idea_text
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

    # Persona Generation
    pain_map = {
        "parent": "lack of control", "student": "overwhelm", 
        "professional": "inefficiency", "general_user": "inconvenience",
        "elderly": "complexity"
    }
    
    primary_persona = {
        "role": user["archetype"].capitalize(),
        "primary_pain": pain_map.get(user["archetype"], "inconvenience"),
        "decision_driver": "risk_aversion" if user["income_tier"] == "low" else "convenience",
        "tech_comfort": 60 if user["archetype"] in ["parent", "doctor"] else 85,
        "price_sensitivity": 70 if user["income_tier"] == "low" else 30,
        "patience_threshold": 40 if user["time_scarcity"] == "high" else 70 
    }
    
    # User Journey Map
    journey_friction = {
        "awareness": 10,
        "evaluation": 20 + (seed["complexity_score"] * 2),
        "onboarding": 15 if seed["action_type"] == "monitoring" else 5,
        "adoption": 30 if seed["tech_dependency_level"] == "high" else 10
    }
    
    return {
        "value_prop": value_prop,
        "personas": [primary_persona],
        "journey_map": journey_friction
    }

# --- STAGE 3: ENVIRONMENTAL PARAMETER CALCULATION (P-SET) ---

def calculate_physics(seed, model):
    """
    Calculates detailed parameters including the 6 environment factors.
    """
    domain = seed["domain"]
    
    # 1. Trust Score (T_score)
    base_trust_map = {"Health": 40, "FinTech": 50, "Productivity": 70, "EdTech": 65, "Social": 45, "E-Commerce": 60, "General Consumer": 60, "GreenTech": 75}
    base_trust = base_trust_map.get(domain, 60)
    
    data_sensitivity_penalty = 0
    if seed["action_type"] == "monitoring" or "high_privacy" in seed["constraints"]:
        data_sensitivity_penalty = 0.2
        
    t_score = int(base_trust * (1 - data_sensitivity_penalty))
    
    # 2. Price Sensitivity
    p_sens_score = 5
    if seed["target_user"]["income_tier"] == "low": p_sens_score += 3
    if seed["target_user"]["income_tier"] == "high": p_sens_score -= 2
    
    # 3. Market Size
    m_size_users = 1000000 # Base
    if domain in ["Health", "FinTech"]: m_size_users *= 2
    
    # 4. Competitive Intensity
    c_int = 4
    if "ai" in seed["original_text"].lower(): c_int = 8
    
    # --- 6 Environment Factors (0-100) ---
    
    # Market Adoption
    market_adopt = 70
    if seed["tech_dependency_level"] == "high": market_adopt -= 20
    if domain in ["Social", "E-Commerce"]: market_adopt += 15
    
    # Regulatory Risk
    reg_risk = 20
    if domain == "Health": reg_risk = 85
    elif domain == "FinTech": reg_risk = 90
    elif "ai" in seed["original_text"].lower(): reg_risk = 60
    
    # Societal Trend
    soc_trend = 50
    if domain in ["GreenTech", "Health", "Productivity"]: soc_trend = 90
    
    # Tech Disruption
    tech_disrupt = 65
    if "ai" in seed["original_text"].lower(): tech_disrupt = 95
    
    # Supply Chain
    supply_risk = 30
    if domain == "E-Commerce" or seed["action_type"] == "transaction": supply_risk = 70
    
    # Capital Availability
    capital = 50
    if domain in ["FinTech", "Health"]: capital = 85
        
    return {
        "t_score": t_score,
        "p_sens": p_sens_score,
        "m_size_users": m_size_users,
        "c_int": c_int,
        "factors": {
            "market_adoption": min(100, market_adopt),
            "regulatory_risk": min(100, reg_risk),
            "societal_trend": min(100, soc_trend),
            "tech_disruption": min(100, tech_disrupt),
            "supply_chain_risk": min(100, supply_risk),
            "capital_availability": min(100, capital)
        }
    }

# --- STAGE 4: COLLISION DETECTION ---

def detect_collisions(p_set, model, seed):
    collisions = []
    
    # Trust
    if p_set["t_score"] < 50:
        collisions.append({
            "type": "trust",
            "title": "TRUST GAP DETECTED",
            "desc": "Users decline essential permissions.",
            "severity": 8,
            "solution": {"name": "Transparent Data Dashboard", "impact": "High", "time": "1 week"}
        })
        
    # Friction
    if seed["complexity_score"] > 6:
        collisions.append({
            "type": "friction",
            "title": "ADOPTION FRICTION HIGH",
            "desc": "Onboarding is too complex for this user.",
            "severity": 9,
            "solution": {"name": "1-Click Onboarding", "impact": "High", "time": "2 weeks"}
        })
        
    # Default if no major collision
    if not collisions:
        collisions.append({
            "type": "growth",
            "title": "SLOW ORGANIC GROWTH",
            "desc": "Viral coefficient is below 1.0.",
            "severity": 4,
            "solution": {"name": "Gamified Referral Loop", "impact": "Medium", "time": "3 days"}
        })
        
    return collisions

# --- STAGE 5: MUTATION ENGINE (V2) ---
# Integrated into Collision Detection for simpler linking

# --- STAGE 6: TEMPORAL PROJECTION (INR) ---

def run_temporal_projection_inr(seed, p_set, mutations):
    # INR Logic: 1 User ~ ₹500 LTV (approx $6)
    arpu = 500 
    if p_set["factors"]["capital_availability"] > 80: arpu = 1200 # Premium markets
    
    # Week 1
    w1_users = 150
    w1_rev = 0 
    
    # Month 1
    m1_users = 850
    m1_rev = int(m1_users * arpu * 0.1) # 10% conversion
    
    # Month 3 (Post Fix)
    fix_boost = 1.4 # 40% boost default
    m3_users = int(3500 * fix_boost)
    m3_rev = int(m3_users * arpu * 0.12) # Better conversion
    
    # Formatting helper
    def fmt_curr(amount):
        if amount >= 100000:
            return f"{amount/100000:.1f}L"
        elif amount >= 1000:
            return f"{amount/1000:.1f}k"
        return str(amount)

    return {
        "week1_users": f"{w1_users}",
        "month1_rev": fmt_curr(m1_rev),
        "month3_rev": fmt_curr(m3_rev)
    }

# --- MAIN CONTROLLER ---

def analyze_idea(idea_text):
    seed = parse_input_and_extract_dna(idea_text)
    model = construct_synthetic_model(seed)
    p_set = calculate_physics(seed, model)
    collisions = detect_collisions(p_set, model, seed)
    projections = run_temporal_projection_inr(seed, p_set, collisions)
    
    # Calculate Investable Status
    status = "INVESTABLE"
    status_text_color = "green" # For text classes
    
    if p_set["t_score"] < 40 or p_set["c_int"] > 7:
        status = "HIGH RISK"
        status_text_color = "red"
    if p_set["factors"]["market_adoption"] < 30:
        status = "NEEDS PIVOT"
        status_text_color = "yellow"

    # Generate Narrative Summary
    blocker = collisions[0]
    summary_text = f"Analysis of your {seed['domain']} concept indicates a {status} result. Key metrics show {p_set['factors']['market_adoption']}% market readiness. Success is contingent on addressing the '{blocker['title']}' blocker."

    # Prepare V2 Data Context
    # Generate Detailed Report
    detailed_report = generate_detailed_report(seed, model, p_set, collisions, projections, status)

    return {
        "original_idea": seed['original_text'],
        "badge_status": status,
        "badge_color": status_text_color, # 'green', 'red', 'yellow'
        "summary_text": summary_text,
        
        # Key Metrics
        "trust_score": p_set["t_score"],
        "competition_level": "HIGH" if p_set["c_int"] > 6 else "LOW",
        "pain_severity": "HIGH", 
        
        # Blocker
        "blocker_title": blocker["title"],
        "blocker_desc": blocker["desc"],
        "blocker_severity": f"{blocker['severity']}/10",
        
        # Solution
        "solution_name": blocker["solution"]["name"],
        "solution_impact": f"{blocker['solution']['impact']} Impact",
        "solution_time": blocker["solution"]["time"],
        
        # Projections
        "week1_users": projections["week1_users"],
        "month1_rev": projections["month1_rev"],
        "month3_rev": projections["month3_rev"],
        
        # Environment Sliders (0-100)
        "env_market": p_set["factors"]["market_adoption"],
        "env_reg": p_set["factors"]["regulatory_risk"],
        "env_social": p_set["factors"]["societal_trend"],
        "env_tech": p_set["factors"]["tech_disruption"],
        "env_supply": p_set["factors"]["supply_chain_risk"],
        "env_capital": p_set["factors"]["capital_availability"],
        
        # Report Text
        "full_report_text": detailed_report
    }

def generate_detailed_report(seed, model, p_set, collisions, projections, status):
    """
    Generates a comprehensive ~400 word report.
    """
    domain = seed['domain']
    idea = seed['original_text']
    blocker = collisions[0]
    
    report = f"""
CONFIDENTIAL STRATEGIC ANALYSIS REPORT
generated by Idea Simulator Lab
==================================================

1. EXECUTIVE SUMMARY
---------------------
The proposed concept regarding "{idea}" has been analyzed against current market dynamics in the {domain} sector.
Overall Viability Status: {status}

Our simulation engine has processed this input through 6 distinct environmental filters, resulting in a core Trust Score of {p_set['t_score']}/100.
The market readiness index is currently sitting at {p_set['factors']['market_adoption']}%. 

2. DETAILED MARKET ENVIRONMENT
------------------------------
The {domain} landscape is currently characterized by the following traits:
- Regulatory Risk: {p_set['factors']['regulatory_risk']}/100. (Higher scores indicate stricter compliance needs).
- Societal Trend Alignment: {p_set['factors']['societal_trend']}/100.
- Capital Availability: {p_set['factors']['capital_availability']}/100.

Your idea faces a Competition Level of {'HIGH' if p_set['c_int'] > 6 else 'LOW'}, which suggests that specific differentiation is critical.
The primary user archetype identified is "{seed['target_user']['archetype']}", whose main decision driver is "{model['personas'][0]['decision_driver']}".

3. CRITICAL BLOCKER & SOLUTION
------------------------------
The most significant impediment to growth identified is:
**{blocker['title']}**
Description: {blocker['desc']}
Severity: {blocker['severity']}/10

Recommended Course of Action:
Implement "{blocker['solution']['name']}".
Expected Impact: {blocker['solution']['impact']}.
Estimated Implementation Time: {blocker['solution']['time']}.

This solution addresses the immediate friction point, allowing the viral coefficient to potentially exceed 1.0.

4. FINANCIAL PROJECTIONS (INR)
------------------------------
Based on the implementation of the recommended fix, we project the following trajectory:
- Week 1 Users: {projections['week1_users']} (Early Adopters)
- Month 1 Revenue: ₹{projections['month1_rev']}
- Month 3 Revenue (Post-Optimization): ₹{projections['month3_rev']}

These figures assume a steady conversion rate optimization and successful mitigation of the trust gap.

5. IDEAL FUTURE & IMPLEMENTATION ROADMAP
----------------------------------------
To realize the full potential of this idea, the following roadmap is suggested for the next 6 months:

Phase 1: Validation (Weeks 1-4)
- Focus entirely on the "{blocker['solution']['name']}" to prove value.
- Conduct low-fidelity user testing with the "{seed['target_user']['archetype']}" demographic.

Phase 2: MVP Development (Weeks 5-12)
- Build the core "utility" loop.
- Ensure compliance with data regulations, especially given the {p_set['factors']['regulatory_risk']}% risk score.
- Integrate feedback loops to measure "{model['personas'][0]['primary_pain']}" reduction.

Phase 3: Growth & Scale (Month 3+)
- Leverage the 'GreenTech/Social' angle if applicable (Trend Alignment: {p_set['factors']['societal_trend']}%).
- Seek Seed Stage funding targeting investors in the {domain} space (Capital Availability: {p_set['factors']['capital_availability']}%).

CONCLUSION
----------
This idea has merit but requires precise execution to navigate the identified risks. The "Future State" depends heavily on unlocking the trust of the {seed['target_user']['archetype']} user base.
"""
    return report.strip()
