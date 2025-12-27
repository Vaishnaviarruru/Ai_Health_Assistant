import os
from dotenv import load_dotenv
from agno.agent import Agent
from agno.models.groq import Groq
import json
import re
from datetime import datetime, timedelta

# ---------------- ENV ------------------
load_dotenv()
API_KEY = os.getenv("GROQ_API_KEY")
if not API_KEY:
    print("❌ GROQ_API_KEY missing in .env file")
    exit(1)

MODEL = "llama-3.1-8b-instant"


# ------------- SAFE RUN ----------------
def safe_run(agent, prompt):
    try:
        rules = """
SAFETY & RELIABILITY RULES:
- Do NOT invent medical data, vitals or numbers.
- If information is not provided, explicitly say: "Not provided".
- NO medical diagnosis. Only lifestyle & preventive guidance.
- Use neutral, safe, supportive tone.
- For health risks, use "probability/increased risk" language, not definitive statements.
- Be specific and personalized based on the data provided.
"""
        res = agent.run(rules + prompt)
        return getattr(res, "content", str(res))
    except Exception as e:
        return f"❌ Error: {e}"


# ----------- AI AGENTS -----------------
def make_agent(desc):
    return Agent(
        model=Groq(id=MODEL),
        description=desc,
        markdown=True
    )

# Define specialized agents
diet_agent = make_agent("nutrition planner who creates highly personalized diet plans")
fitness_agent = make_agent("fitness expert specializing in creating customized workout plans")
team_agent = make_agent("plan merger")
mental_agent = make_agent("mental health coach")
sim_agent = make_agent("simulation engine")
nutrition_agent = make_agent("nutrition estimation agent")
workout_agent = make_agent("workout plan creator with progression and safety")

# Student-specific agents
student_health_agent = make_agent("college student health risk predictor focusing on hostel lifestyle issues")
nutrient_risk_agent = make_agent("analyzes nutrition risks from student lifestyle data, provides risk assessments and recommendations")
mess_food_agent = make_agent("analyzes hostel mess food patterns and provides improvement suggestions")
sleep_analyzer_agent = make_agent("analyzes sleep patterns and provides personalized sleep advice")
student_advisor_agent = make_agent("provides personalized advice for college students on budget, stress, and lifestyle")
budget_meal_agent = make_agent("creates budget-friendly meal plans for students")


# ---------------- Calculators ------------------
def bmi_calc(weight, height):
    h = height / 100
    bmi = weight / (h * h)
    if bmi < 18.5: category = "Underweight"
    elif bmi < 24.9: category = "Healthy"
    elif bmi < 29.9: category = "Overweight"
    else: category = "Obese"
    return round(bmi, 2), category

def calc_protein_requirement(weight, goal):
    if goal == "Muscle Gain":
        return int(weight * 2.0)
    elif goal == "Weight Loss":
        return int(weight * 1.6)
    elif goal == "Endurance":
        return int(weight * 1.4)
    else:
        return int(weight * 1.2)


# ---------------- STUDENT HEALTH TRACKER ------------------
class StudentHealthTracker:
    def __init__(self):
        self.student_profile = {}
        self.health_log = []
    
    def setup_student_profile(self):
        """Set up hostel student profile"""
        print("\n" + "="*60)
        print("🏠 HOSTEL STUDENT HEALTH PROFILE")
        print("="*60)
        
        profile = {}
        profile['name'] = input("Your name: ").strip() or "Student"
        profile['age'] = int(input("Age: ").strip() or "20")
        profile['weight'] = float(input("Weight (kg): ").strip() or "65")
        profile['height'] = float(input("Height (cm): ").strip() or "170")
        profile['year'] = input("Academic Year (1st/2nd/3rd/4th): ").strip() or "2nd"
        profile['college'] = input("College name: ").strip() or "University"
        profile['hostel_type'] = input("Hostel Type (College/Private/PG): ").strip() or "College"
        profile['has_mess'] = input("Have Mess Facility? (yes/no): ").strip().lower() == "yes"
        
        if profile['has_mess']:
            profile['mess_timing_issue'] = input("Miss mess due to timing? (yes/no): ").strip().lower() == "yes"
        
        # Budget
        print("\n💰 Weekly Food Budget:")
        print("1. Less than ₹200")
        print("2. ₹200-400")
        print("3. ₹400-600")
        print("4. More than ₹600")
        budget_choice = input("Select (1-4): ").strip() or "2"
        budget_map = {"1": "<200", "2": "200-400", "3": "400-600", "4": ">600"}
        profile['weekly_budget'] = budget_map.get(budget_choice, "200-400")
        
        # Calculate BMI
        bmi, bmi_cat = bmi_calc(profile['weight'], profile['height'])
        profile['bmi'] = bmi
        profile['bmi_category'] = bmi_cat
        
        self.student_profile = profile
        print(f"\n✅ Profile saved for {profile['name']}!")
        return profile
    
    def log_daily_health(self):
        """Log daily health metrics"""
        print("\n" + "="*60)
        print(f"📝 DAILY CHECK-IN for {self.student_profile.get('name', 'Student')}")
        print("="*60)
        
        # Ask which day they're logging for
        print("\n📅 Which day are you logging for?")
        print("1. Today")
        print("2. Yesterday")
        print("3. Custom date")
        
        day_choice = input("Select (1-3): ").strip() or "1"
        
        if day_choice == "1":
            log_date = datetime.now()
            date_str = log_date.strftime("%Y-%m-%d %A")
            print(f"\n📅 Logging for TODAY: {date_str}")
        elif day_choice == "2":
            log_date = datetime.now() - timedelta(days=1)
            date_str = log_date.strftime("%Y-%m-%d %A")
            print(f"\n📅 Logging for YESTERDAY: {date_str}")
        else:
            date_input = input("Enter date (YYYY-MM-DD or DD/MM/YYYY): ").strip()
            try:
                # Try different date formats
                if "-" in date_input:
                    log_date = datetime.strptime(date_input, "%Y-%m-%d")
                else:
                    log_date = datetime.strptime(date_input, "%d/%m/%Y")
                date_str = log_date.strftime("%Y-%m-%d %A")
                print(f"\n📅 Logging for: {date_str}")
            except:
                print("⚠️ Invalid date format. Using today's date.")
                log_date = datetime.now()
                date_str = log_date.strftime("%Y-%m-%d %A")
        
        day_name = date_str.split()[1]  # Get day name (Monday, Tuesday, etc.)
        date_only = date_str.split()[0]  # Get date (2024-01-15)
        
        print(f"\n📅 Date: {day_name} ({date_only})")
        
        # Sleep
        print(f"\n😴 SLEEP on {day_name}:")
        sleep_hours = float(input(f"How many hours did you sleep? ").strip() or "6")
        sleep_quality = input("Sleep quality (1-5, 5=best): ").strip() or "3"
        bed_time = input(f"Approx bedtime (e.g., 11pm, 1am): ").strip() or "12am"
        
        # Meals
        print(f"\n🍽️ MEALS on {day_name}:")
        meals_data = {}
        for meal in ["Breakfast", "Lunch", "Dinner"]:
            ate = input(f"Did you eat {meal}? (yes/no/skipped): ").strip().lower()
            if ate == "yes":
                food = input(f"What did you eat for {meal}? ").strip()
                meals_data[meal.lower()] = food
            else:
                meals_data[meal.lower()] = ate
        
        # Additional info
        ate_junk = input(f"Ate any junk/instant food? (yes/no): ").strip().lower() == "yes"
        junk_details = ""
        if ate_junk:
            junk_details = input("What? (Maggi, pizza, chips, etc): ").strip()
        
        ate_fruits = input(f"Ate any fruits? (yes/no): ").strip().lower() == "yes"
        water_glasses = int(input(f"Glasses of water: ").strip() or "6")
        
        # Energy & Symptoms
        print(f"\n⚡ ENERGY & SYMPTOMS on {day_name}:")
        energy_level = input("Energy level (1-5, 5=high): ").strip() or "3"
        focus_level = input("Focus level (1-5, 5=good): ").strip() or "3"
        
        symptoms = []
        print(f"\nAny symptoms? (enter numbers, comma separated)")
        print("1. Fatigue/tiredness")
        print("2. Headache")
        print("3. Digestive issues")
        print("4. Poor concentration")
        print("5. Mood swings")
        print("6. None")
        
        symptom_input = input("Symptoms: ").strip()
        if symptom_input != "6":
            symptoms = symptom_input.split(",") if symptom_input else []
        
        # Create log entry
        daily_entry = {
            "date": date_str,
            "sleep": {
                "hours": sleep_hours,
                "quality": int(sleep_quality),
                "bed_time": bed_time
            },
            "meals": {
                "breakfast": meals_data.get("breakfast", "no"),
                "lunch": meals_data.get("lunch", "no"),
                "dinner": meals_data.get("dinner", "no"),
                "ate_junk": ate_junk,
                "junk_details": junk_details,
                "ate_fruits": ate_fruits,
                "water_glasses": water_glasses
            },
            "energy": {
                "level": int(energy_level),
                "focus": int(focus_level),
                "symptoms": symptoms
            }
        }
        
        self.health_log.append(daily_entry)
        print(f"\n✅ Log recorded for {day_name} ({date_only})!")
        return daily_entry
    
    def analyze_health_risks(self):
        """LLM-based health risk analysis"""
        if len(self.health_log) < 2:
            return "Need at least 2 days of data for analysis. Please log more days."
        
        recent_logs = self.health_log[-5:]  # Last 5 days
        
        # Format data for LLM
        data_summary = self._format_data_for_analysis(recent_logs)
        
        prompt = f"""
        Analyze health risks for this college student:
        
        STUDENT PROFILE:
        Name: {self.student_profile.get('name', 'Student')}
        Age: {self.student_profile.get('age', 20)}
        Year: {self.student_profile.get('year', '2nd')} year
        College: {self.student_profile.get('college', 'University')}
        Hostel: {self.student_profile.get('hostel_type', 'College')}
        Budget: ₹{self.student_profile.get('weekly_budget', '200-400')}/week
        BMI: {self.student_profile.get('bmi', 'N/A')} ({self.student_profile.get('bmi_category', 'N/A')})
        
        RECENT HEALTH DATA (last {len(recent_logs)} days):
        {data_summary}
        
        Provide a COMPREHENSIVE HEALTH RISK ANALYSIS including:
        
        1. NUTRIENT DEFICIENCY RISKS:
           - Protein, Iron, B12, Vitamin D, Calcium, Vitamin C
           - For each: Risk level (Low/Moderate/High), Reasons, Specific symptoms to watch
        
        2. LIFESTYLE RISK PATTERNS:
           - Sleep patterns and impact
           - Meal regularity issues
           - Junk food consumption patterns
        
        3. ACADEMIC PERFORMANCE IMPACT:
           - How current habits affect studies
           - Focus and energy patterns
        
        4. PERSONALIZED RECOMMENDATIONS:
           - Specific dietary adjustments within budget
           - Sleep improvement strategies
           - Quick fixes for immediate improvement
           - When to consider medical checkup
        
        Be specific, practical, and use "increased risk/probability" language.
        Format with clear sections and bullet points.
        """
        
        analysis = safe_run(student_health_agent, prompt)
        return analysis
    
    def _format_data_for_analysis(self, recent_logs):
        """Format health data for LLM analysis"""
        summary = []
        
        for log in recent_logs:
            day_summary = f"Day: {log['date']}\n"
            
            # Sleep
            sleep = log['sleep']
            day_summary += f"  Sleep: {sleep['hours']}h, quality {sleep['quality']}/5, bed at {sleep['bed_time']}\n"
            
            # Meals
            meals = log['meals']
            meals_eaten = sum(1 for m in [meals['breakfast'], meals['lunch'], meals['dinner']] if m == 'yes')
            day_summary += f"  Meals: {meals_eaten}/3 eaten"
            if meals['ate_junk']:
                day_summary += f", junk: {meals['junk_details']}"
            if meals['ate_fruits']:
                day_summary += ", ate fruits"
            day_summary += f", water: {meals['water_glasses']} glasses\n"
            
            # Energy
            energy = log['energy']
            symptom_map = {"1": "Fatigue", "2": "Headache", "3": "Digestive", "4": "Poor focus", "5": "Mood swings"}
            symptoms = [symptom_map.get(s, s) for s in energy['symptoms'] if s in symptom_map]
            day_summary += f"  Energy: {energy['level']}/5, Focus: {energy['focus']}/5"
            if symptoms:
                day_summary += f", Symptoms: {', '.join(symptoms)}"
            day_summary += "\n"
            
            summary.append(day_summary)
        
        return "\n".join(summary)
    
    def analyze_nutrient_risks(self):
        """LLM-based nutrient risk analysis"""
        if len(self.health_log) < 2:
            return "Need more data for nutrient analysis."
        
        recent_logs = self.health_log[-5:]
        data_summary = self._format_data_for_analysis(recent_logs)
        
        prompt = f"""
        Analyze SPECIFIC NUTRIENT RISKS for this student:
        
        PROFILE:
        Name: {self.student_profile.get('name', 'Student')}
        Age: {self.student_profile.get('age', 20)}
        Budget: ₹{self.student_profile.get('weekly_budget', '200-400')}/week
        Hostel: {self.student_profile.get('hostel_type', 'College')}
        
        RECENT DATA (last {len(recent_logs)} days):
        {data_summary}
        
        Analyze these SPECIFIC NUTRIENTS:
        1. PROTEIN
        2. IRON
        3. VITAMIN B12
        4. VITAMIN D
        5. CALCIUM
        6. VITAMIN C
        
        For EACH nutrient, provide:
        - RISK LEVEL: None/Low/Moderate/High (be honest)
        - REASONS: Specific behaviors causing risk
        - SYMPTOMS: Physical signs to watch for
        - IMMEDIATE ACTIONS: Specific, affordable solutions
        - FOOD SOURCES: Budget-friendly options (₹{self.student_profile.get('weekly_budget', '300')}/week)
        
        Example format for one nutrient:
        PROTEIN:
        - Risk: Moderate
        - Reasons: Only 1-2 meals daily, frequent Maggi consumption
        - Symptoms: Fatigue, muscle weakness, slow recovery
        - Actions: Add 2 boiled eggs daily, mix dal with rice, keep peanuts in room
        - Sources: Eggs (₹5 each), Dal (free in mess), Peanuts (₹20/week)
        
        Be extremely specific and practical. Mention exact foods and prices.
        """
        
        analysis = safe_run(nutrient_risk_agent, prompt)
        return analysis
    
    def analyze_mess_food(self):
        """Analyze mess food patterns"""
        if not self.student_profile.get('has_mess', False):
            return "No mess facility reported."
        
        if len(self.health_log) < 2:
            return "Need more data for mess food analysis."
        
        recent_logs = self.health_log[-5:]
        
        # Count mess vs non-mess days
        mess_patterns = []
        for log in recent_logs:
            meals = log['meals']
            # Check if they're likely eating mess (no junk mentioned, regular meals)
            if not meals['ate_junk'] and sum(1 for m in [meals['breakfast'], meals['lunch'], meals['dinner']] if m == 'yes') >= 2:
                mess_patterns.append("Likely mess food")
            elif meals['ate_junk']:
                mess_patterns.append(f"Junk: {meals['junk_details']}")
            else:
                mess_patterns.append("Irregular eating")
        
        prompt = f"""
        Analyze mess food optimization for:
        
        STUDENT: {self.student_profile.get('name', 'Student')}
        COLLEGE: {self.student_profile.get('college', 'University')}
        BUDGET: ₹{self.student_profile.get('weekly_budget', '200-400')}/week
        
        RECENT EATING PATTERNS (last {len(recent_logs)} days):
        {chr(10).join([f"Day {i+1}: {pattern}" for i, pattern in enumerate(mess_patterns)])}
        
        Provide SPECIFIC mess food optimization advice:
        
        1. HOW TO MAXIMIZE MESS NUTRITION:
           - Best items to prioritize in mess
           - How to supplement mess meals
           - Timing strategies
        
        2. BUDGET SUPPLEMENTATION (₹{self.student_profile.get('weekly_budget', '300')}/week):
           - Exact items to buy weekly
           - How to store in hostel
           - When to eat them
        
        3. JUNK FOOD ALTERNATIVES:
           - Healthy swaps for common junk foods
           - Quick hostel-room snacks
        
        4. WEEKEND/EATING-OUT STRATEGIES:
           - Budget-friendly options
           - Healthier choices
        
        Be specific about Indian hostel food context.
        """
        
        analysis = safe_run(mess_food_agent, prompt)
        return analysis
    
    def analyze_sleep_patterns(self):
        """Analyze sleep patterns"""
        if len(self.health_log) < 2:
            return "Need more sleep data."
        
        recent_logs = self.health_log[-5:]
        
        sleep_data = []
        for log in recent_logs:
            sleep = log['sleep']
            energy = log['energy']
            sleep_data.append(f"• {sleep['hours']}h sleep, bed at {sleep['bed_time']}, quality {sleep['quality']}/5, next day energy {energy['level']}/5")
        
        prompt = f"""
        Analyze sleep patterns for:
        
        STUDENT: {self.student_profile.get('name', 'Student')}
        YEAR: {self.student_profile.get('year', '2nd')} year
        RECENT SLEEP DATA:
        {chr(10).join(sleep_data)}
        
        Provide PERSONALIZED SLEEP ANALYSIS:
        
        1. CURRENT PATTERNS:
           - Sleep duration analysis
           - Bedtime consistency
           - Sleep quality issues
        
        2. ACADEMIC IMPACT:
           - How sleep affects {self.student_profile.get('year', '2nd')} year studies
           - Focus and memory impact
           - Energy levels
        
        3. HOSTEL-SPECIFIC SOLUTIONS:
           - Managing noise/roommates
           - Study-sleep balance
           - Power nap strategies
        
        4. ACTION PLAN:
           - Immediate improvements
           - Weekend recovery
           - Exam period strategies
        
        Be practical and specific to college life.
        """
        
        analysis = safe_run(sleep_analyzer_agent, prompt)
        return analysis
    
    def get_student_advice(self):
        """Get comprehensive student advice"""
        prompt = f"""
        Provide COMPREHENSIVE COLLEGE STUDENT ADVICE for:
        
        STUDENT: {self.student_profile.get('name', 'Student')}
        YEAR: {self.student_profile.get('year', '2nd')} year at {self.student_profile.get('college', 'University')}
        HOSTEL: {self.student_profile.get('hostel_type', 'College')} hostel
        BUDGET: ₹{self.student_profile.get('weekly_budget', '200-400')}/week
        BMI: {self.student_profile.get('bmi', 'N/A')} ({self.student_profile.get('bmi_category', 'N/A')})
        
        Provide advice in these areas:
        
        1. ACADEMIC SUCCESS ({self.student_profile.get('year', '2nd')} YEAR SPECIFIC):
           - Study schedule for {self.student_profile.get('year', '2nd')} year
           - Exam preparation strategies
           - Time management
        
        2. BUDGET HEALTHY EATING (₹{self.student_profile.get('weekly_budget', '300')}/week):
           - Weekly shopping list with prices
           - Meal prep for hostel
           - Mess food optimization
        
        3. HOSTEL ROOM FITNESS:
           - 15-min daily routines
           - Study break exercises
           - Using hostel furniture
        
        4. STRESS MANAGEMENT:
           - {self.student_profile.get('year', '2nd')} year specific stress
           - Quick relaxation techniques
           - Social life balance
        
        5. HEALTH MONITORING:
           - Warning signs to watch
           - Campus health resources
           - When to seek help
        
        Be extremely specific and actionable.
        """
        
        advice = safe_run(student_advisor_agent, prompt)
        return advice
    
    def get_budget_meal_plan(self):
        """Get budget meal plan"""
        prompt = f"""
        Create ULTRA-SPECIFIC WEEKLY MEAL PLAN for:
        
        STUDENT: {self.student_profile.get('name', 'Student')}
        BUDGET: ₹{self.student_profile.get('weekly_budget', '200-400')} PER WEEK ONLY
        HOSTEL: {self.student_profile.get('hostel_type', 'College')} (limited cooking)
        MESS: {'Available' if self.student_profile.get('has_mess', False) else 'Not available'}
        
        Create EXACT plan:
        
        1. WEEKLY SHOPPING LIST (MUST be under ₹{self.student_profile.get('weekly_budget', 300)}):
           - Item, Quantity, Approx Price, Where to buy
        
        2. DAILY MEAL SCHEDULE (Monday-Sunday):
           - Breakfast, Lunch, Dinner, 2 snacks
           - EXACT foods and quantities
           - Preparation instructions for hostel
        
        3. MESS INTEGRATION (if available):
           - How to supplement mess food
           - What to add to basic mess meals
        
        4. WEEKEND PLAN:
           - Different for Sat/Sun
           - Dorm-room cooking ideas
        
        5. SNACKS & HYDRATION:
           - Study snacks under ₹10
           - Water intake plan
        
        Example format:
        MONDAY:
        - Breakfast: 2 boiled eggs (₹10, boil Sunday), 1 banana (₹5)
        - Mess Lunch: Rice + dal + add boiled egg
        - After-class: Tea (₹5) + 2 biscuits (₹2)
        - Dinner: Mess roti + sabzi + side sprouts (soaked overnight)
        - Late study: 1 glass milk (₹15) if budget allows
        
        Be realistic for Indian hostel students.
        """
        
        meal_plan = safe_run(budget_meal_agent, prompt)
        return meal_plan


# ---------------- HEALTH AI SYSTEM ------------------
class HealthAI:
    def __init__(self):
        self.student_tracker = StudentHealthTracker()
        self.mode = "general"
        self.user_data = {}
    
    def select_mode(self):
        """Select between general fitness or student health mode"""
        print("\n" + "="*60)
        print("🤖 HEALTH AI SYSTEM")
        print("="*60)
        print("\n1. 🏋️ General Fitness & Wellness")
        print("2. 🏠 Hostel/Student Health Tracker")
        print("\nChoose mode: ", end="")
        
        choice = input().strip()
        if choice == "2":
            self.mode = "student"
            print("\n🏠 HOSTEL STUDENT MODE ACTIVATED")
            self.student_tracker.setup_student_profile()
            self.user_data = self.student_tracker.student_profile
        else:
            self.mode = "general"
            print("\n🏋️ GENERAL FITNESS MODE ACTIVATED")
            self._get_general_profile()
        
        return self.mode
    
    def _get_general_profile(self):
        """Get general fitness profile"""
        print("\n" + "="*60)
        print("🏋️ GENERAL FITNESS PROFILE")
        print("="*60)
        
        self.user_data['name'] = input("Your name: ").strip() or "User"
        self.user_data['age'] = int(input("Age: ").strip() or "25")
        self.user_data['weight'] = float(input("Weight (kg): ").strip() or "70")
        self.user_data['height'] = float(input("Height (cm): ").strip() or "170")
        self.user_data['goal'] = input("Fitness goal (Weight Loss/Muscle Gain/Endurance): ").strip() or "Muscle Gain"
        self.user_data['activity'] = input("Activity level: ").strip() or "Moderate"
        self.user_data['diet_type'] = input("Diet type: ").strip() or "Non-Vegetarian"
        
        # Calculate metrics
        bmi, bmi_cat = bmi_calc(self.user_data['weight'], self.user_data['height'])
        self.user_data['bmi'] = bmi
        self.user_data['bmi_category'] = bmi_cat
        self.user_data['protein_target'] = calc_protein_requirement(self.user_data['weight'], self.user_data['goal'])
        
        return self.user_data
    
    def show_menu(self):
        """Show appropriate menu based on mode"""
        if self.mode == "student":
            return self._show_student_menu()
        else:
            return self._show_general_menu()
    
    def _show_general_menu(self):
        """General fitness menu"""
        print("\n" + "="*60)
        print("📱 GENERAL FITNESS MENU")
        print("="*60)
        print("1. 🥗 Generate Customized Diet Plan")
        print("2. 🏋️ Generate Customized Workout Plan")
        print("3. 💪 Complete Health Plan (Diet + Workout)")
        print("4. 🧠 Mental Wellness Support")
        print("5. 🔮 What-If Simulation")
        print("6. 📊 Health Summary")
        print("7. 🥩 Protein Planning")
        print("8. 🏃‍♂️ Quick Workouts")
        print("9. 🔄 Switch to Student Mode")
        print("0. ❌ Exit")
        print("="*60)
        
        return input("\nSelect option: ").strip()
    
    def _show_student_menu(self):
        """Student health menu"""
        name = self.user_data.get('name', 'Student')
        print(f"\n" + "="*60)
        print(f"📱 STUDENT HEALTH - {name}")
        print("="*60)
        print(f"Year: {self.user_data.get('year', 'N/A')} | Budget: ₹{self.user_data.get('weekly_budget', '200-400')}/week")
        print("="*60)
        print("1. 📝 Daily Health Check-in")
        print("2. ⚠️ Comprehensive Health Risk Analysis")
        print("3. 🔬 Nutrient Deficiency Risk Assessment")
        print("4. 🍽️ Mess Food Optimization")
        print("5. 😴 Sleep Pattern Analysis")
        print("6. 💡 Personalized Student Advice")
        print("7. 🥗 Budget Meal Plan")
        print("8. 🏋️ Hostel Room Workouts")
        print("9. 🔄 Switch to General Mode")
        print("0. ❌ Exit")
        print("="*60)
        
        return input("\nSelect option: ").strip()
    
    # ========== GENERAL FITNESS FUNCTIONS ==========
    def generate_diet_plan(self):
        """Generate diet plan for general mode"""
        prompt = f"""
        Create personalized diet plan for:
        
        Name: {self.user_data['name']}
        Age: {self.user_data['age']}
        Weight: {self.user_data['weight']}kg
        Height: {self.user_data['height']}cm
        Goal: {self.user_data['goal']}
        Activity: {self.user_data['activity']}
        Diet: {self.user_data['diet_type']}
        BMI: {self.user_data['bmi']} ({self.user_data['bmi_category']})
        
        Create a 7-day meal plan with:
        - Breakfast, Lunch, Dinner, 2 snacks daily
        - Portion sizes
        - Macronutrient breakdown
        - Grocery list
        - Meal timing
        - Hydration plan
        
        Make it practical and sustainable.
        """
        
        plan = safe_run(diet_agent, prompt)
        return plan
    
    def generate_workout_plan(self):
        """Generate workout plan for general mode"""
        prompt = f"""
        Create personalized workout plan for:
        
        Name: {self.user_data['name']}
        Age: {self.user_data['age']}
        Weight: {self.user_data['weight']}kg
        Goal: {self.user_data['goal']}
        Activity: {self.user_data['activity']}
        
        Create a 4-week program with:
        - Weekly schedule
        - Sets, reps, rest periods
        - Warm-up/cool-down
        - Exercise alternatives
        - Progression plan
        - Safety tips
        - Equipment needed
        
        Make it detailed and actionable.
        """
        
        plan = safe_run(workout_agent, prompt)
        return plan
    
    def generate_complete_plan(self):
        """Generate complete health plan"""
        diet = self.generate_diet_plan()
        workout = self.generate_workout_plan()
        
        prompt = f"""
        Merge diet and workout into cohesive plan:
        
        USER: {self.user_data['name']}
        GOAL: {self.user_data['goal']}
        
        DIET PLAN:
        {diet[:1000]}...
        
        WORKOUT PLAN:
        {workout[:1000]}...
        
        Create integrated 4-week program:
        - Daily schedule combining meals and workouts
        - Recovery nutrition
        - Progress tracking
        - Weekly adjustments
        
        Format clearly.
        """
        
        plan = safe_run(team_agent, prompt)
        return plan
    
    def mental_wellness(self):
        """Mental wellness support"""
        print("\nHow are you feeling?")
        mood = input("Describe your mood/stress: ").strip() or "stressed"
        
        prompt = f"""
        User is feeling {mood}. Provide supportive guidance:
        - Coping strategies
        - Relaxation techniques
        - Lifestyle adjustments
        - Positive psychology tips
        - When to seek professional help
        
        No medical diagnosis.
        """
        
        support = safe_run(mental_agent, prompt)
        return support
    
    def what_if_simulation(self):
        """What-if simulation"""
        print("\nEnter a 'what-if' scenario:")
        scenario = input("e.g., 'What if I sleep 8 hours daily?': ").strip()
        if not scenario:
            scenario = "What if I exercise 30 minutes daily?"
        
        prompt = f"""
        Simulate realistic outcomes for: {scenario}
        
        Consider:
        - Health benefits
        - Timeline for results
        - Potential challenges
        - How to implement
        - Expected improvements
        
        Be realistic and evidence-based.
        """
        
        simulation = safe_run(sim_agent, prompt)
        return simulation
    
    def health_summary(self):
        """Health summary"""
        summary = f"""
        📊 HEALTH SUMMARY for {self.user_data['name']}
        
        Basic Info:
        - Age: {self.user_data['age']}
        - Weight: {self.user_data['weight']}kg
        - Height: {self.user_data['height']}cm
        - BMI: {self.user_data['bmi']} ({self.user_data['bmi_category']})
        
        Goals & Preferences:
        - Primary Goal: {self.user_data['goal']}
        - Activity Level: {self.user_data['activity']}
        - Diet Type: {self.user_data['diet_type']}
        - Protein Target: {self.user_data['protein_target']}g/day
        
        Recommendations:
        """
        
        if self.user_data['bmi_category'] == "Underweight":
            summary += "- Focus on calorie surplus for healthy weight gain\n"
            summary += "- Include strength training to build muscle\n"
            summary += "- Eat protein-rich foods every 3-4 hours\n"
        elif self.user_data['bmi_category'] in ["Overweight", "Obese"]:
            summary += "- Create moderate calorie deficit\n"
            summary += "- Combine cardio and strength training\n"
            summary += "- Focus on whole foods and portion control\n"
        else:
            summary += "- Maintain current healthy habits\n"
            summary += "- Focus on specific fitness goals\n"
            summary += "- Ensure balanced nutrition\n"
        
        return summary
    
    def protein_planning(self):
        """Protein planning"""
        prompt = f"""
        Create protein-focused meal plans for:
        
        Name: {self.user_data['name']}
        Diet: {self.user_data['diet_type']}
        Protein Target: {self.user_data['protein_target']}g/day
        Goal: {self.user_data['goal']}
        
        Provide 3 different daily plans reaching the target.
        Include specific foods and quantities.
        """
        
        plans = safe_run(diet_agent, prompt)
        return plans
    
    def quick_workouts(self):
        """Quick workout recommendations"""
        prompt = f"""
        Provide 3 quick workout options for:
        - Goal: {self.user_data['goal']}
        - Time: 15-30 minutes
        - Equipment: Minimal/basic
        
        Include duration, exercises, and intensity.
        """
        
        workouts = safe_run(fitness_agent, prompt)
        return workouts
    
    # ========== STUDENT FUNCTIONS ==========
    def handle_student_choice(self, choice):
        """Handle student menu choices"""
        if choice == "1":
            self.student_tracker.log_daily_health()
            input("\nPress Enter to continue...")
            
        elif choice == "2":
            print("\n" + "="*60)
            print("⚠️ COMPREHENSIVE HEALTH RISK ANALYSIS")
            print("="*60)
            analysis = self.student_tracker.analyze_health_risks()
            print(analysis)
            print("="*60)
            input("\nPress Enter to continue...")
            
        elif choice == "3":
            print("\n" + "="*60)
            print("🔬 NUTRIENT DEFICIENCY RISK ASSESSMENT")
            print("="*60)
            analysis = self.student_tracker.analyze_nutrient_risks()
            print(analysis)
            print("="*60)
            input("\nPress Enter to continue...")
            
        elif choice == "4":
            print("\n" + "="*60)
            print("🍽️ MESS FOOD OPTIMIZATION")
            print("="*60)
            analysis = self.student_tracker.analyze_mess_food()
            print(analysis)
            print("="*60)
            input("\nPress Enter to continue...")
            
        elif choice == "5":
            print("\n" + "="*60)
            print("😴 SLEEP PATTERN ANALYSIS")
            print("="*60)
            analysis = self.student_tracker.analyze_sleep_patterns()
            print(analysis)
            print("="*60)
            input("\nPress Enter to continue...")
            
        elif choice == "6":
            print("\n" + "="*60)
            print("💡 PERSONALIZED STUDENT ADVICE")
            print("="*60)
            advice = self.student_tracker.get_student_advice()
            print(advice)
            print("="*60)
            input("\nPress Enter to continue...")
            
        elif choice == "7":
            print("\n" + "="*60)
            print("🥗 BUDGET MEAL PLAN")
            print("="*60)
            meal_plan = self.student_tracker.get_budget_meal_plan()
            print(meal_plan)
            print("="*60)
            input("\nPress Enter to continue...")
            
        elif choice == "8":
            print("\n" + "="*60)
            print("🏋️ HOSTEL ROOM WORKOUTS")
            print("="*60)
            workouts = self._get_hostel_workouts()
            print(workouts)
            print("="*60)
            input("\nPress Enter to continue...")
            
        elif choice == "9":
            # Switch to general mode
            self.mode = "general"
            print("\n🔄 SWITCHING TO GENERAL FITNESS MODE")
            self._get_general_profile()
            return "switch"
            
        else:
            print("\n❌ Invalid choice")
        
        return None
    
    def _get_hostel_workouts(self):
        """Get hostel room workouts"""
        prompt = f"""
        Create hostel room workouts for:
        
        Student: {self.user_data.get('name', 'Student')}
        Year: {self.user_data.get('year', '2nd')} year
        Space: Small hostel room
        Equipment: Bodyweight only
        Time: 15-20 minutes
        
        Include:
        1. Morning wake-up routine (5 min)
        2. Study break routine (3 min)
        3. Evening full-body (15 min)
        4. Quiet exercises for shared room
        5. Using hostel furniture
        
        Be specific with exercises and reps.
        """
        
        workouts = safe_run(fitness_agent, prompt)
        return workouts


# ---------------- MAIN APPLICATION ------------------
def main():
    health_ai = HealthAI()
    
    # Select mode
    health_ai.select_mode()
    
    # Main loop
    while True:
        choice = health_ai.show_menu()
        
        if choice == "0" or choice == "99":
            print("\n👋 Thank you for using Health AI! Stay healthy!")
            break
        
        if health_ai.mode == "student":
            result = health_ai.handle_student_choice(choice)
            if result == "switch":
                continue  # Already switched mode
        else:
            # General mode
            if choice == "1":
                print("\n" + "="*60)
                print("🥗 CUSTOMIZED DIET PLAN")
                print("="*60)
                plan = health_ai.generate_diet_plan()
                print(plan)
                print("="*60)
                input("\nPress Enter to continue...")
                
            elif choice == "2":
                print("\n" + "="*60)
                print("🏋️ CUSTOMIZED WORKOUT PLAN")
                print("="*60)
                plan = health_ai.generate_workout_plan()
                print(plan)
                print("="*60)
                input("\nPress Enter to continue...")
                
            elif choice == "3":
                print("\n" + "="*60)
                print("💪 COMPLETE HEALTH PLAN")
                print("="*60)
                plan = health_ai.generate_complete_plan()
                print(plan[:2000])
                if len(plan) > 2000:
                    print("\n... [Plan continues]")
                print("="*60)
                input("\nPress Enter to continue...")
                
            elif choice == "4":
                print("\n" + "="*60)
                print("🧠 MENTAL WELLNESS SUPPORT")
                print("="*60)
                support = health_ai.mental_wellness()
                print(support)
                print("="*60)
                input("\nPress Enter to continue...")
                
            elif choice == "5":
                print("\n" + "="*60)
                print("🔮 WHAT-IF SIMULATION")
                print("="*60)
                simulation = health_ai.what_if_simulation()
                print(simulation)
                print("="*60)
                input("\nPress Enter to continue...")
                
            elif choice == "6":
                print("\n" + "="*60)
                print("📊 HEALTH SUMMARY")
                print("="*60)
                summary = health_ai.health_summary()
                print(summary)
                print("="*60)
                input("\nPress Enter to continue...")
                
            elif choice == "7":
                print("\n" + "="*60)
                print("🥩 PROTEIN PLANNING")
                print("="*60)
                plans = health_ai.protein_planning()
                print(plans)
                print("="*60)
                input("\nPress Enter to continue...")
                
            elif choice == "8":
                print("\n" + "="*60)
                print("🏃‍♂️ QUICK WORKOUTS")
                print("="*60)
                workouts = health_ai.quick_workouts()
                print(workouts)
                print("="*60)
                input("\nPress Enter to continue...")
                
            elif choice == "9":
                # Switch to student mode
                health_ai.mode = "student"
                print("\n🔄 SWITCHING TO STUDENT MODE")
                health_ai.student_tracker.setup_student_profile()
                health_ai.user_data = health_ai.student_tracker.student_profile
                
            else:
                print("\n❌ Invalid choice")


if __name__ == "__main__":
    main()