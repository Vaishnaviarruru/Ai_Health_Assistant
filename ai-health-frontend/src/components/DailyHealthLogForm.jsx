import { useState } from "react";
import { post } from "../api";

export default function DailyHealthLogForm({ studentId, onDone }) {
  const [log, setLog] = useState({
    sleep_hours: "",
    junk_food: false,
    energy: "",
  });

  function handleChange(e) {
    const { name, value, type, checked } = e.target;
    setLog({ ...log, [name]: type === "checkbox" ? checked : value });
  }

  async function handleSubmit(e) {
    e.preventDefault();

    await post("/student/log", {
      student_id: studentId,
      date: new Date().toISOString().slice(0, 10),
      sleep_hours: Number(log.sleep_hours),
      junk_food: log.junk_food,
      energy: Number(log.energy),
    });

    onDone();
  }

  return (
    <form onSubmit={handleSubmit}>
      <h3>📝 Daily Health Check-in</h3>

      <input
        name="sleep_hours"
        type="number"
        placeholder="Sleep Hours"
        onChange={handleChange}
        required
      />

      <label>
        <input
          type="checkbox"
          name="junk_food"
          onChange={handleChange}
        />
        Ate Junk Food Today
      </label>

      <input
        name="energy"
        type="number"
        placeholder="Energy Level (1–10)"
        onChange={handleChange}
        required
      />

      <button type="submit">Save Log</button>
    </form>
  );
}
