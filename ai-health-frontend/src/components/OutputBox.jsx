import CollapsibleMarkdown from "./CollapsibleMarkdown";

export default function OutputBox({ title, content }) {
  if (!content) return null;

  return (
    <div className="output">
      <h3>{title}</h3>
      <CollapsibleMarkdown content={content} />
    </div>
  );
}
