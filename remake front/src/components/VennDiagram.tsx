export default function VennDiagram() {
  return (
    <svg viewBox="0 0 300 260" className="w-full h-auto max-w-xs mx-auto">
      <defs>
        <filter id="blur">
          <feGaussianBlur in="SourceGraphic" stdDeviation="2" />
        </filter>
      </defs>

      <circle cx="80" cy="100" r="60" fill="rgba(0, 255, 240, 0.15)" stroke="rgba(0, 255, 240, 0.4)" strokeWidth="2" filter="url(#blur)" />
      <circle cx="150" cy="100" r="60" fill="rgba(255, 46, 159, 0.15)" stroke="rgba(255, 46, 159, 0.4)" strokeWidth="2" filter="url(#blur)" />
      <circle cx="115" cy="160" r="60" fill="rgba(58, 12, 163, 0.15)" stroke="rgba(58, 12, 163, 0.4)" strokeWidth="2" filter="url(#blur)" />

      <ellipse cx="100" cy="95" rx="25" ry="30" fill="rgba(0, 255, 240, 0.3)" />
      <ellipse cx="130" cy="95" rx="25" ry="30" fill="rgba(255, 46, 159, 0.3)" />
      <ellipse cx="115" cy="140" rx="25" ry="30" fill="rgba(58, 12, 163, 0.3)" />
    </svg>
  );
}
