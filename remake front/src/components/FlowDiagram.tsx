export default function FlowDiagram() {
  return (
    <svg viewBox="0 0 500 120" className="w-full h-auto">
      <defs>
        <marker id="arrowhead" markerWidth="10" markerHeight="10" refX="9" refY="3" orient="auto">
          <polygon points="0 0, 10 3, 0 6" fill="rgba(0, 255, 240, 0.6)" />
        </marker>
      </defs>

      <rect x="20" y="40" width="80" height="40" rx="8" fill="rgba(58, 12, 163, 0.1)" stroke="rgba(58, 12, 163, 0.5)" strokeWidth="2" />
      <line x1="100" y1="60" x2="140" y2="60" stroke="rgba(0, 255, 240, 0.6)" strokeWidth="2" markerEnd="url(#arrowhead)" />
      <rect x="140" y="40" width="80" height="40" rx="8" fill="rgba(255, 46, 159, 0.1)" stroke="rgba(255, 46, 159, 0.5)" strokeWidth="2" />
      <line x1="220" y1="60" x2="260" y2="60" stroke="rgba(0, 255, 240, 0.6)" strokeWidth="2" markerEnd="url(#arrowhead)" />
      <rect x="260" y="40" width="80" height="40" rx="8" fill="rgba(0, 255, 240, 0.1)" stroke="rgba(0, 255, 240, 0.5)" strokeWidth="2" />
      <line x1="340" y1="60" x2="380" y2="60" stroke="rgba(0, 255, 240, 0.6)" strokeWidth="2" markerEnd="url(#arrowhead)" />
      <rect x="380" y="40" width="80" height="40" rx="8" fill="rgba(58, 12, 163, 0.1)" stroke="rgba(58, 12, 163, 0.5)" strokeWidth="2" />
    </svg>
  );
}
