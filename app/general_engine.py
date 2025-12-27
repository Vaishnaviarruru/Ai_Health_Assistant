from app.ai_core import (
    safe_run,
    diet_agent,
    workout_agent,
    mental_agent,
)

# ============================================================
# 🥗 GENERATE CUSTOMIZED DIET PLAN
# ============================================================

def generate_diet(profile: dict):
    prompt = f"""
🥗 CUSTOMIZED DIET PLAN
============================================================

USER PROFILE:
{profile}

You are a Professional Fitness Nutritionist.

Generate a LONG, DETAILED, PRACTICAL diet plan including:

### 1. Nutrition Goal Explanation
- Explain goal relevance (fat loss / muscle gain / endurance)

### 2. Daily Meal Structure
- Breakfast
- Lunch
- Dinner
- Snacks

### 3. Food Choices (Indian Context)
- Veg and non-veg options
- Portion guidance
- Affordable substitutions

### 4. Weekly Meal Plan (Sample)
- Day-wise suggestions

### 5. Hydration & Micronutrients
- Water intake
- Fruits & vegetables

### 6. Common Mistakes to Avoid
### 7. Sustainability Tips

Use markdown headings, bullet points, and friendly tone.
Avoid medical claims.
"""
    return safe_run(diet_agent, prompt)


# ============================================================
# 🏋️ GENERATE CUSTOMIZED WORKOUT PLAN
# ============================================================

def generate_workout(profile: dict):
    prompt = f"""
🏋️ CUSTOMIZED WORKOUT PLAN
============================================================

USER PROFILE:
{profile}

You are a Certified Fitness Trainer.

Generate a LONG, DETAILED workout plan including:

### 1. Fitness Goal Alignment
### 2. Weekly Workout Split
- Strength days
- Cardio days
- Rest days

### 3. Exercise Selection
- Beginner-friendly
- No-equipment / gym alternatives

### 4. Sets, Reps & Intensity
### 5. Recovery & Mobility
### 6. Safety & Injury Prevention

Use clear structure and motivational tone.
"""
    return safe_run(workout_agent, prompt)


# ============================================================
# 💪 COMPLETE HEALTH SUMMARY (DIET + WORKOUT)
# ============================================================

def generate_health_summary(profile: dict):
    prompt = f"""
📊 COMPLETE HEALTH SUMMARY
============================================================

USER PROFILE:
{profile}

Provide a LONG, HOLISTIC health overview including:

### 1. BMI & Body Composition Interpretation
### 2. Strengths & Positive Habits
### 3. Current Health Risks
### 4. Diet Improvement Focus Areas
### 5. Workout Improvement Focus Areas
### 6. 30-Day Action Plan

Use encouraging, coach-style language.
"""
    return safe_run(diet_agent, prompt)


# ============================================================
# 🧠 MENTAL WELLNESS SUPPORT
# ============================================================

def mental_wellness_support(profile: dict):
    prompt = f"""
🧠 MENTAL WELLNESS SUPPORT
============================================================

USER PROFILE:
{profile}

You are a Mental Wellness Coach.

Provide a DETAILED response including:

### 1. Common Stress Sources
### 2. Mental Health Risks
### 3. Daily Stress-Reduction Techniques
### 4. Mindfulness & Focus Practices
### 5. Motivation & Consistency Tips
### 6. When to Seek Professional Help

Keep the tone supportive and non-clinical.
"""
    return safe_run(mental_agent, prompt)


# ============================================================
# 🥩 PROTEIN PLANNING
# ============================================================

def protein_planning(profile: dict):
    prompt = f"""
🥩 PROTEIN PLANNING GUIDE
============================================================

USER PROFILE:
{profile}

Generate a LONG, DETAILED protein guide including:

### 1. Daily Protein Requirement
### 2. Veg Protein Sources
### 3. Non-Veg Protein Sources
### 4. Budget-Friendly Options
### 5. Protein Timing
### 6. Common Myths & Mistakes

Use Indian food examples.
"""
    return safe_run(diet_agent, prompt)


# ============================================================
# 🔮 WHAT-IF SIMULATION
# ============================================================

def what_if_simulation(profile: dict):
    prompt = f"""
🔮 WHAT-IF HEALTH SIMULATION
============================================================

USER PROFILE:
{profile}

Simulate outcomes if the user:

### 1. Improves Diet Consistency
### 2. Exercises 4–5 Days/Week
### 3. Sleeps 7–8 Hours Daily

For each scenario:
- Physical changes
- Mental changes
- Energy & productivity

Predict outcomes after:
- 2 weeks
- 1 month
- 3 months

Use realistic expectations and motivating tone.
"""
    return safe_run(workout_agent, prompt)
