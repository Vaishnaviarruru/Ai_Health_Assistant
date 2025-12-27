# ================= STUDENT MODE =================

STUDENT_HEALTH_ANALYSIS_PROMPT = """
⚠️ COMPREHENSIVE STUDENT HEALTH RISK ANALYSIS
============================================================

STUDENT PROFILE:
{profile}

RECENT HEALTH LOGS:
{logs}

Generate a LONG, DETAILED report with:

### 1. Overall Health Risk Overview
### 2. Lifestyle Risk Factors
- Sleep
- Junk food
- Energy levels
- Budget constraints

### 3. Academic Performance Impact
### 4. Short-Term Risks (3–6 months)
### 5. Long-Term Risks (1–3 years)
### 6. Practical Hostel-Friendly Improvements
### 7. Warning Signs & When to Seek Help

Use clear headings, bullet points, and Indian college context.
No medical diagnosis.
"""

SLEEP_ANALYSIS_PROMPT = """
😴 SLEEP PATTERN ANALYSIS
============================================================

PROFILE:
{profile}

SLEEP DATA:
{logs}

Include:
### Average Sleep Duration
### Sleep Consistency
### Sleep Debt
### Impact on Energy & Focus
### Hostel-Specific Issues
### 7-Day Improvement Plan
### Red Flags
"""

NUTRIENT_DEFICIENCY_PROMPT = """
🔬 NUTRIENT DEFICIENCY RISK ASSESSMENT
============================================================

PROFILE:
{profile}

LOGS:
{logs}

For EACH nutrient (Protein, Iron, B12, Vitamin D, Calcium, Fiber):
- Risk level
- Why risk exists
- Symptoms to watch
- Budget-friendly Indian food sources
"""

PERSONALIZED_ADVICE_PROMPT = """
💡 PERSONALIZED STUDENT ADVICE
============================================================

**Comprehensive College Student Advice**

PROFILE:
{profile}

LOGS:
{logs}

Generate a VERY LONG, STRUCTURED response with:

### 1. Academic Success (Year-Specific)
- Semester-wise study table
- Exam strategies
- Time management

### 2. Budget Healthy Eating (₹200–400/week)
- Weekly shopping list with prices
- Hostel meal prep

### 3. Hostel Room Fitness
- 15-min routines
- Study break exercises
- Using hostel furniture

### 4. Stress Management
- Academic stress
- Relaxation techniques
- Social balance

### 5. Health Monitoring
- Warning signs
- Campus resources
- When to seek help

Use markdown tables, bullet points, and detailed explanations.
"""

BUDGET_MEAL_PROMPT = """
🥗 BUDGET MEAL PLAN FOR HOSTEL STUDENT
============================================================

PROFILE:
{profile}

LOGS:
{logs}

Provide:
- Weekly budget breakdown
- Shopping list with prices
- Breakfast/Lunch/Dinner
- Mess integration
- Snacks
- Money-saving tips
"""

HOSTEL_WORKOUT_PROMPT = """
🏋️ HOSTEL ROOM WORKOUT PLAN
============================================================

PROFILE:
{profile}

LOGS:
{logs}

Include:
- 15-min daily routine
- Quiet room exercises
- Study break movements
- Weekly frequency
- Safety tips
"""

MESS_FOOD_PROMPT = """
🍽️ MESS FOOD OPTIMIZATION
============================================================

PROFILE:
{profile}

EATING PATTERNS:
{logs}

Include:
- Best mess food choices
- Nutrient pairing
- Junk food alternatives
- Budget supplements
- Weekend eating strategy
"""

# ================= GENERAL MODE =================

GENERAL_DIET_PROMPT = """
🥗 COMPREHENSIVE DIET PLAN
============================================================
PROFILE:
{profile}

Provide:
- Goals
- Daily structure
- Weekly plan
- Sustainability tips
"""

GENERAL_WORKOUT_PROMPT = """
🏋️ COMPLETE WORKOUT PLAN
============================================================
PROFILE:
{profile}

Provide:
- Weekly split
- Progression
- Recovery
"""

GENERAL_SUMMARY_PROMPT = """
📊 HEALTH SUMMARY
============================================================
PROFILE:
{profile}

Include BMI, strengths, risks, and improvement plan.
"""

GENERAL_MENTAL_PROMPT = """
🧠 MENTAL WELLNESS SUPPORT
============================================================
PROFILE:
{profile}

Include stress sources, coping strategies, and habits.
"""

GENERAL_PROTEIN_PROMPT = """
🥩 PROTEIN PLANNING
============================================================
PROFILE:
{profile}

Include requirements, sources, budget options.
"""

GENERAL_WHAT_IF_PROMPT = """
🔮 WHAT-IF SIMULATION
============================================================
PROFILE:
{profile}

Simulate 3-month outcomes for better diet, sleep, activity.
"""
