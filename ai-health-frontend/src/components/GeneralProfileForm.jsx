import { useState } from "react";

export default function GeneralProfileForm({ onSubmit }) {
  const [profile, setProfile] = useState({
    name: "",
    age: "",
    height: "",
    weight: "",
    goal: "",
    activity_level: "",
    diet_type: "",
  });

  function handleChange(e) {
    setProfile({ ...profile, [e.target.name]: e.target.value });
  }

  function handleSubmit(e) {
    e.preventDefault();
    onSubmit(profile);
  }

  return (
    <form onSubmit={handleSubmit}>
      <h2>🏋️ General Fitness Profile</h2>

      <input name="name" placeholder="Name" onChange={handleChange} required />
      <input name="age" placeholder="Age" type="number" onChange={handleChange} required />
      <input name="height" placeholder="Height (cm)" type="number" onChange={handleChange} required />
      <input name="weight" placeholder="Weight (kg)" type="number" onChange={handleChange} required />

      <input name="goal" placeholder="Fitness Goal (Weight Loss / Muscle Gain)" onChange={handleChange} required />
      <input name="activity_level" placeholder="Activity Level (1–5)" type="number" onChange={handleChange} required />
      <input name="diet_type" placeholder="Diet Type (Veg / Non-Veg)" onChange={handleChange} required />

      <button type="submit">Continue</button>
    </form>
  );
}
