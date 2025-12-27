import { useState } from "react";
import StudentMode from "./components/StudentMode";
import GeneralMode from "./components/GeneralMode";
import "./styles.css";

export default function App() {
  const [mode, setMode] = useState("student");

  return (
    <div className="container">
      <header>
        <h1>AI Health Assistant</h1>

        <div>
          <button onClick={() => setMode("student")}>
            Student Mode
          </button>
          <button onClick={() => setMode("general")}>
            General Mode
          </button>
        </div>
      </header>

      {mode === "student" ? <StudentMode /> : <GeneralMode />}
    </div>
  );
}

