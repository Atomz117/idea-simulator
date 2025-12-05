
import random
import datetime

def analyze_idea(idea_text):
    """
    Simulates a detailed 7-stage business analysis.
    """
    
    # 1. Seed Extraction
    keywords = extract_keywords(idea_text)
    industry = determine_industry(keywords)
    
    # 2. Synthetic Construction (Personas)
    personas = get_personas(industry)
    
    # 3. Parameter Mapping (Scoring)
    scores = generate_scores(industry)
    
    # 4. Fragility Testing
    risks = identify_risks(industry, keywords)
    

    # 5. Mutation Layer (Fixes) -> Expanded to 6 Insights
    insights = generate_detailed_insights(industry, keywords, risks)
    
    # 6. Future Projection (Time Series)
    projections, timeline_labels = generate_startup_timeline()
    

    # Generate Competitors
    competitors = generate_competitors(industry)

    # New Features for final2.html
    evolution = generate_evolution_scale(industry, keywords)
    market_angles = generate_market_angles(industry, personas)
    
    # 7. Final Assembly
    report = {
        "idea_name": idea_text if len(idea_text) < 30 else idea_text[:30] + "...",
        "industry": industry,
        "summary": f"A {industry} solution focusing on {', '.join(keywords)}.",
        "personas": personas,
        "scores": scores,
        "risks": risks,
        "insights": insights,
        "projections": projections,
        "timeline_labels": timeline_labels,
        "competitors": competitors,
        "evolution": evolution,      # New
        "market_angles": market_angles, # New
        "market_size": calculate_market_size(industry),
        "growth_rate": f"+{random.randint(20, 150)}% MoM", 
        "timestamp": datetime.datetime.now().strftime("%Y-%m-%d %H:%M")
    }
    
    return report

def generate_evolution_scale(industry, keywords):
    # Returns {past, present, future}
    past_map = {
        "Consumer Technology": "Manual Service",
        "Fashion": "Brick & Mortar Store",
        "EdTech": "Textbooks",
        "FinTech": "Paper Banking",
        "Pet Care": "Neighbor Help",
        "Culinary Tech": "Phone Orders",
        "Logistics": "Courier Services",
        "Artificial Intelligence": "Rule-based Scripts"
    }
    
    future_map = {
        "Consumer Technology": "Autonomous Agents",
        "Fashion": "Virtual Wardrobes",
        "EdTech": "Neural Learning",
        "FinTech": "DeFi Integration",
        "Pet Care": "Bot Companions",
        "Culinary Tech": "3D Food Printing",
        "Logistics": "Drone Swarms",
        "Artificial Intelligence": "AGI Systems"
    }

    past = past_map.get(industry, "Traditional Methods")
    present = f"AI-First {keywords[0].capitalize()}" if keywords else "Digital Platform"
    future = future_map.get(industry, "Predictive Ecosystems")
    
    return {"past": past, "present": present, "future": future}

def generate_market_angles(industry, personas):
    # Returns {primary, secondary, marketing}
    # Use personas to inform markets if possible
    primary = personas[0]['role'] if personas else "Gen Z"
    
    sec_opts = ["SMEs", "Freelancers", "Enterprises", "Boomers", "Gen X", "Parents"]
    secondary = random.choice(sec_opts)
    
    channel_map = {
        "Fashion": "Influencer TikToks",
        "EdTech": "University Partners",
        "FinTech": "LinkedIn Ads",
        "Pet Care": "Community Groups",
        "Consumer Technology": "Product Hunt"
    }
    marketing = channel_map.get(industry, "Viral Referral Loops")
    
    return {"primary": primary, "secondary": secondary, "marketing": marketing}

def generate_detailed_insights(industry, keywords, risks):

    # We need 6 points: 2 Market, 2 Operational, 2 Strategic
    insights = []
    
    # Market
    insights.append({"title": "Niche Dominance", "desc": f"Potential to own the {keywords[0]} micro-niche before horizontal scaling."})
    insights.append({"title": "Viral Loop Multiplier", "desc": f"High organic shareability inherent in {industry} user behaviors."})
    
    # Operational
    insights.append({"title": "Lean Operations", "desc": "Can launch with minimal headcount using automated workflows."})
    insights.append({"title": "Tech Stack Efficiency", "desc": "Modern low-code tools can reduce {industry} development time by 40%."})
    
    # Strategic / Mitigation
    if risks:
        insights.append({"title": f"Mitigation: {risks[0]['title']}", "desc": f"Counteract by implementing trust-first verification loops."})
    else:
        insights.append({"title": "First Mover Advantage", "desc": "Speed to execution is critical to preempt clones."})
        
    insights.append({"title": "Exit Strategy", "desc": f"Likely acquisition target for legacy {industry} giants within 5 years."})
    
    return insights

def generate_competitors(industry):
    prefixes = ["Nov", "Syn", "Glob", "Omni", "Ver", "Trell", "Arc", "Zent"]
    suffixes = ["ia", "os", "ix", "flow", "ly", "ify", "hub", "lab"]
    
    comps = []
    for _ in range(3):
        name = random.choice(prefixes) + random.choice(suffixes)
        comps.append(name)
    return comps

def generate_startup_timeline():
    # 5 Milestones
    labels = ["Seed Phase", "Product Launch", "Traction", "Series A", "Global Scale"]
    
    # Simple S-curve-ish growth
    data = [100, 450, 1200, 3500, 9000] 
    return data, labels


def extract_keywords(text):
    common_stops = {"a", "an", "the", "for", "in", "on", "of", "to", "is", "app", "platform", "business", "service"}
    words = text.lower().replace(".", "").replace(",", "").split()
    keywords = [w for w in words if w not in common_stops and len(w) > 3]
    if not keywords:
        return ["Innovation", "Service"]
    return keywords[:3]

def determine_industry(keywords):
    industry_map = {
        "food": "Culinary Tech", "delivery": "Logistics", "coffee": "retail",
        "ai": "Artificial Intelligence", "tech": "SaaS", "data": "Big Data",
        "clothing": "Fashion", "style": "Fashion", "wear": "Fashion",
        "dog": "Pet Care", "pet": "Pet Care", "health": "HealthTech",
        "finance": "FinTech", "money": "FinTech", "bank": "FinTech",
        "school": "EdTech", "learn": "EdTech", "teach": "EdTech"
    }
    
    for k in keywords:
        if k in industry_map:
            return industry_map[k]
    return "Consumer Technology"

def get_personas(industry):
    base_personas = [
        {"role": "Primary User", "desc": "The daily power user seeking efficiency."},
        {"role": "Early Adopter", "desc": "Tech-savvy individual looking for the next big thing."},
        {"role": "Decision Maker", "desc": "Budget holder focused on ROI and reliability."}
    ]
    
    if industry == "Fashion":
        base_personas[0]["desc"] = "Fashion-conscious Gen Z seeking unique expression."
        base_personas[1]["desc"] = "Influencer looking for trendsetting tools."
    elif industry == "EdTech":
        base_personas[0]["desc"] = "Stressed student needing study aids."
        base_personas[2]["desc"] = "School administrator managing budgets."
    
    return base_personas

def generate_scores(industry):
    # Returns 0-100 scores
    base_trust = random.randint(60, 90)
    base_market = random.randint(50, 95)
    
    return {
        "trust": base_trust,
        "market_viability": base_market,
        "competition": random.randint(30, 80),
        "execution_difficulty": random.randint(40, 90)
    }

def identify_risks(industry, keywords):
    risks = [
        {"title": "Adoption Friction", "desc": "Users may hesitate to switch from existing habits."},
        {"title": "Trust Barrier", "desc": "Gaining initial user trust without social proof."}
    ]
    
    if "ai" in keywords:
        risks.append({"title": "Data Privacy", "desc": "Concerns over how user data is processed and stored."})
    if industry == "Fashion":
        risks.append({"title": "Return Rates", "desc": "High operational costs due to size/fit issues."})
        
    return risks

def generate_fixes(risks):
    fixes = []
    for r in risks:
        if r["title"] == "Adoption Friction":
            fixes.append("Implement a 'Freemium' model to lower entry barriers.")
        elif r["title"] == "Data Privacy":
            fixes.append("Add end-to-end encryption and transparent data policies.")
        else:
            fixes.append(f"Develop a mitigation strategy for {r['title']}.")
    return fixes

def generate_projections():
    # Generate 5 years of data
    base = 100
    data = []
    for i in range(5):
        growth = random.uniform(1.2, 3.0)
        base = base * growth
        data.append(int(base))
    return data

def calculate_market_size(industry):
    sizes = {
        "Fashion": "$2.5T",
        "Artificial Intelligence": "$1.8T",
        "Pet Care": "$232B",
        "EdTech": "$340B",
        "FinTech": "$500B"
    }
    return sizes.get(industry, "$1.2T")
