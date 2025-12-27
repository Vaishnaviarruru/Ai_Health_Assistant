import { useState } from "react";
import { post } from "../api";
import OutputBox from "./OutputBox";
import GeneralProfileForm from "./GeneralProfileForm";

export default function GeneralMode() {
  const [profile, setProfile] = useState(null);
  const [output, setOutput] = useState("");

  async function run(endpoint) {
    const res = await post(endpoint, profile);
    const key = Object.keys(res)[0];
    setOutput(res[key]);
  }

  // 1️⃣ If profile not filled → show form
  if (!profile) {
    return <GeneralProfileForm onSubmit={setProfile} />;
  }

  // 2️⃣ After profile → dashboard
  return (
    <div>
      <h2>📱 General Fitness Dashboard</h2>
      <p>Welcome, <strong>{profile.name}</strong></p>

      <div className="buttons">
        <button onClick={() => run("/general/diet")}>🥗 Diet Plan</button>
        <button onClick={() => run("/general/workout")}>🏋️ Workout Plan</button>
        <button onClick={() => run("/general/summary")}>📊 Health Summary</button>
        <button onClick={() => run("/general/mental")}>🧠 Mental Wellness</button>
        <button onClick={() => run("/general/protein")}>🥩 Protein Planning</button>
        <button onClick={() => run("/general/what-if")}>🔮 What-If Simulation</button>
      </div>

      <OutputBox title="AI Response" content={output} />
    </div>
  );
}
