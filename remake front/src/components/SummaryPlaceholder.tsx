export default function SummaryPlaceholder() {
  return (
    <div className="space-y-4">
      {[100, 85, 90, 75, 95].map((width, idx) => (
        <div key={idx} className="flex items-center gap-3">
          <div className="w-2 h-2 rounded-full bg-[#00FFF0]/50 flex-shrink-0" />
          <div className="h-2 bg-gradient-to-r from-[#1a1a1a] to-[#0f0f0f] rounded-full" style={{ width: `${width}%` }} />
        </div>
      ))}
    </div>
  );
}
