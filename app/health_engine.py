from app.ai_core import (
    safe_run,
    student_health_agent,
    sleep_analyzer_agent,
    nutrient_risk_agent,
    student_advisor_agent,
    mess_food_agent,
    budget_meal_agent,
)

# ============================================================
# ⚠️ COMPREHENSIVE STUDENT HEALTH RISK ANALYSIS
# ============================================================

def analyze_student_health(profile: dict, logs: list):
    prompt = f"""
⚠️ COMPREHENSIVE STUDENT HEALTH RISK ANALYSIS
============================================================

STUDENT PROFILE:
{profile}

RECENT HEALTH LOGS:
{logs}

You are an expert College Student Health Risk Analyst.

Generate a LONG, DETAILED report including:

### 1. Overall Health Risk Overview
- Physical health risks
- Mental health risks
- Lifestyle imbalance indicators

### 2. Lifestyle Risk Factors
- Sleep patterns
- Junk food frequency
- Energy levels
- Budget constraints

### 3. Academic Performance Impact
- Focus
- Memory
- Exam performance
- Burnout risk

### 4. Short-Term Risks (Next 3–6 months)
### 5. Long-Term Risks (If habits continue)

### 6. Practical, Hostel-Friendly Improvements
- Daily habits
- Study-life balance
- Affordable fixes

### 7. Warning Signs & When to Seek Help

Use Indian college context.
Use bullet points and headings.
Avoid medical diagnosis.
"""
    return safe_run(student_health_agent, prompt)


# ============================================================
# 😴 SLEEP PATTERN ANALYSIS
# ============================================================

def analyze_sleep_patterns(profile: dict, logs: list):
    prompt = f"""
😴 SLEEP PATTERN ANALYSIS FOR COLLEGE STUDENT
============================================================

STUDENT PROFILE:
{profile}

SLEEP DATA:
{logs}

Analyze in detail:

### 1. Average Sleep Duration
### 2. Sleep Consistency vs Irregularity
### 3. Sleep Debt Accumulation
### 4. Impact on Energy, Mood & Focus
### 5. Hostel-Specific Sleep Challenges
### 6. 7-Day Sleep Improvement Plan
### 7. Red Flags & When to Seek Help

Use practical, student-friendly language.
Avoid medical diagnosis.
"""
    return safe_run(sleep_analyzer_agent, prompt)


# ============================================================
# 🔬 NUTRIENT DEFICIENCY RISK ASSESSMENT
# ============================================================

def analyze_nutrient_deficiency(profile: dict, logs: list):
    prompt = f"""
🔬 NUTRIENT DEFICIENCY RISK ASSESSMENT
============================================================

STUDENT PROFILE:
{profile}

RECENT HEALTH LOGS:
{logs}

Analyze the risk of deficiencies for:

### Protein
### Iron
### Vitamin B12
### Vitamin D
### Calcium
### Fiber

For EACH nutrient:
- Risk Level (Low / Moderate / High)
- Why this risk exists
- Common symptoms to watch
- Budget-friendly Indian food sources
- Hostel-friendly options

Do NOT diagnose.
Focus on risk awareness and food-based improvements.
"""
    return safe_run(nutrient_risk_agent, prompt)


# ============================================================
# 💡 PERSONALIZED STUDENT ADVICE
# ============================================================

def generate_personalized_student_advice(profile: dict, logs: list):
    prompt = f"""
💡 PERSONALIZED STUDENT ADVICE
============================================================
**Comprehensive College Student Advice**

STUDENT PROFILE:
{profile}

RECENT LOGS:
{logs}

You are a Senior College Lifestyle & Wellness Mentor.

Generate a VERY LONG, STRUCTURED response with:

### 1. Academic Success (3 Year Specific)
- Semester-wise study schedule (table)
- Exam preparation strategies
- Time management techniques

### 2. Budget Healthy Eating (₹200–400/week)
- Weekly shopping list with prices
- Hostel meal preparation tips
- Snack planning

### 3. Hostel Room Fitness
- 15-minute daily routines
- Study break exercises
- Using hostel furniture safely

### 4. Stress Management
- Academic stress sources
- Relaxation techniques
- Social life balance

### 5. Health Monitoring
- Warning signs to watch
- Campus health resources
- When to seek professional help

### Additional Tips
- Journaling
- Habit tracking
- Motivation & consistency

Use markdown tables, bullet points, and headings.
Use encouraging, student-friendly tone.
Avoid medical diagnosis.
"""
    return safe_run(student_advisor_agent, prompt)


# ============================================================
# 🥗 BUDGET MEAL PLAN
# ============================================================

def generate_budget_meal_plan(profile: dict, logs: list):
    prompt = f"""
🥗 BUDGET MEAL PLAN FOR HOSTEL STUDENT
============================================================

STUDENT PROFILE:
{profile}

RECENT LOGS:
{logs}

Create a LONG, PRACTICAL plan including:

### Weekly Budget Breakdown (₹200–400)
### Weekly Shopping List with Prices
### Breakfast Options
### Lunch Options
### Dinner Options
### Mess Food Optimization
### Study Snacks
### Money-Saving Tips

Assume limited cooking facilities.
Use realistic Indian prices.
"""
    return safe_run(budget_meal_agent, prompt)


# ============================================================
# 🍽️ MESS FOOD OPTIMIZATION
# ============================================================

def analyze_mess_food(profile: dict, logs: list):
    prompt = f"""
🍽️ MESS FOOD OPTIMIZATION GUIDE
============================================================

STUDENT PROFILE:
{profile}

EATING PATTERNS:
{logs}

Provide detailed guidance on:

### Best Mess Food Choices
### Nutrient Pairing Strategies
### Junk Food Alternatives
### Budget Supplements
### Weekend & Eating-Out Strategy

Focus on Indian hostel mess context.
Be extremely practical and realistic.
"""
    return safe_run(mess_food_agent, prompt)


# ============================================================
# 🏋️ HOSTEL ROOM WORKOUT PLAN
# ============================================================

def generate_hostel_room_workout(profile: dict, logs: list):
    prompt = f"""
🏋️ HOSTEL ROOM WORKOUT PLAN
============================================================

STUDENT PROFILE:
{profile}

RECENT LOGS:
{logs}

Generate a detailed plan including:

### 15-Minute Daily Workout Routine
### Quiet Room-Friendly Exercises
### Study Break Movements
### Weekly Frequency Plan
### Safety Guidelines

No equipment.
Small room.
Student-safe intensity.
"""
    return safe_run(student_health_agent, prompt)
