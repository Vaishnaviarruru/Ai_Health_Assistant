const BASE_URL = "http://127.0.0.1:8000";

export async function post(endpoint, data) {
  const res = await fetch(`${BASE_URL}${endpoint}`, {
    method: "POST",
    headers: {
      "Content-Type": "application/json",
    },
    body: JSON.stringify(data),
  });

  if (!res.ok) {
    throw new Error("API request failed");
  }

  return await res.json();
}
