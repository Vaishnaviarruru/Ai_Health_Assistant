import ReactMarkdown from "react-markdown";

export default function CollapsibleMarkdown({ content }) {
  if (!content) return null;

  const sections = content.split("\n### ").map((block, index) => {
    if (index === 0) {
      return { title: "Overview", body: block };
    }

    const lines = block.split("\n");
    const title = lines[0];
    const body = lines.slice(1).join("\n");

    return { title, body };
  });

  return (
    <div>
      {sections.map((section, idx) => (
        <details key={idx} open={idx === 0}>
          <summary>
            <strong>{section.title}</strong>
          </summary>
          <ReactMarkdown>{section.body}</ReactMarkdown>
        </details>
      ))}
    </div>
  );
}
