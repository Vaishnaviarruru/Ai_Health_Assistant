from agno.agent import Agent
from agno.models.groq import Groq
from dotenv import load_dotenv

load_dotenv()

MODEL = "llama-3.1-8b-instant"

def safe_run(agent, prompt):
    response = agent.run(prompt)
    return getattr(response, "content", str(response))

# ===== STUDENT AGENTS =====
student_health_agent = Agent(
    model=Groq(id=MODEL),
    description="college student health risk analyst",
    markdown=True
)

sleep_analyzer_agent = Agent(
    model=Groq(id=MODEL),
    description="student sleep pattern analyst",
    markdown=True
)

nutrient_risk_agent = Agent(
    model=Groq(id=MODEL),
    description="student nutrient deficiency risk assessor",
    markdown=True
)

student_advisor_agent = Agent(
    model=Groq(id=MODEL),
    description="college lifestyle and academic advisor",
    markdown=True
)

mess_food_agent = Agent(
    model=Groq(id=MODEL),
    description="hostel mess food optimization expert",
    markdown=True
)

budget_meal_agent = Agent(
    model=Groq(id=MODEL),
    description="budget hostel meal planner",
    markdown=True
)

# ===== GENERAL AGENTS =====
diet_agent = Agent(
    model=Groq(id=MODEL),
    description="fitness diet planner",
    markdown=True
)

workout_agent = Agent(
    model=Groq(id=MODEL),
    description="fitness workout planner",
    markdown=True
)

mental_agent = Agent(
    model=Groq(id=MODEL),
    description="mental wellness coach",
    markdown=True
)
