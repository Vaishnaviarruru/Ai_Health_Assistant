import { useState } from "react";
import { post } from "../api";
import OutputBox from "./OutputBox";
import DailyHealthLogForm from "./DailyHealthLogForm";

export default function StudentDashboard({ student }) {
  const [output, setOutput] = useState("");
  const [showLogForm, setShowLogForm] = useState(false);

  async function analyze(endpoint) {
    const res = await post(endpoint, { student_id: student.student_id });
    setOutput(res.analysis);
  }

  return (
    <div>
      <h2>📱 Student Health Dashboard</h2>
      <p>
        Welcome, <strong>{student.name}</strong> (Year {student.year})
      </p>

      <div className="buttons">
        <button onClick={() => setShowLogForm(true)}>📝 Daily Health Check-in</button>
        <button onClick={() => analyze("/student/analyze")}>⚠️ Health Risk Analysis</button>
        <button onClick={() => analyze("/student/nutrient-risk")}>🔬 Nutrient Deficiency</button>
        <button onClick={() => analyze("/student/sleep-analysis")}>😴 Sleep Analysis</button>
        <button onClick={() => analyze("/student/advice")}>💡 Personalized Advice</button>
        <button onClick={() => analyze("/student/budget-meal")}>🥗 Budget Meal Plan</button>
        <button onClick={() => analyze("/student/mess-food")}>🍽️ Mess Food Optimization</button>
      </div>

      {showLogForm && (
        <DailyHealthLogForm
          studentId={student.student_id}
          onDone={() => setShowLogForm(false)}
        />
      )}

      <OutputBox title="AI Analysis" content={output} />
    </div>
  );
}
