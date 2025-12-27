import { useState } from "react";
import { post } from "../api";

export default function StudentProfileForm({ onCreated }) {
  const [form, setForm] = useState({
    name: "",
    age: "",
    height: "",
    weight: "",
    year: "",
    budget: "",
  });

  function handleChange(e) {
    setForm({ ...form, [e.target.name]: e.target.value });
  }

  async function handleSubmit(e) {
    e.preventDefault();

    const res = await post("/student/create", {
      age: Number(form.age),
      height: Number(form.height),
      weight: Number(form.weight),
      budget: form.budget,
      bmi: (form.weight / ((form.height / 100) ** 2)).toFixed(2),
    });

    // store student_id internally
    onCreated({ ...form, student_id: res.student_id });
  }

  return (
    <form onSubmit={handleSubmit}>
      <h2>🎓 Student Health Profile</h2>

      <input name="name" placeholder="Name" onChange={handleChange} required />
      <input name="age" type="number" placeholder="Age" onChange={handleChange} required />
      <input name="height" type="number" placeholder="Height (cm)" onChange={handleChange} required />
      <input name="weight" type="number" placeholder="Weight (kg)" onChange={handleChange} required />
      <input name="year" type="number" placeholder="Year of Study" onChange={handleChange} required />
      <input name="budget" placeholder="Weekly Budget (₹)" onChange={handleChange} required />

      <button type="submit">Continue</button>
    </form>
  );
}
