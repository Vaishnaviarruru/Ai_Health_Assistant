import { useState } from "react";
import StudentProfileForm from "./StudentProfileForm";
import StudentDashboard from "./StudentDashboard";

export default function StudentMode() {
  const [student, setStudent] = useState(null);

  if (!student) {
    return <StudentProfileForm onCreated={setStudent} />;
  }

  return <StudentDashboard student={student} />;
}
