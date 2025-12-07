export default function BarChart() {
  const categories = ['Market', 'Competition', 'Execution', 'Scalability', 'Innovation'];
  const values = [65, 82, 54, 71, 88];

  return (
    <div className="space-y-5">
      {values.map((width, idx) => (
        <div key={idx} className="flex items-center gap-4">
          <div className="w-24 text-sm text-gray-400 truncate">{categories[idx]}</div>
          <div className="flex-1 h-3 bg-[#1a1a1a] rounded-full overflow-hidden">
            <div
              className="h-full rounded-full transition-all duration-500"
              style={{
                width: `${width}%`,
                background: `linear-gradient(90deg, hsl(${idx * 72}, 100%, 50%}) 0%, hsl(${(idx * 72) + 60}, 100%, 60%}) 100%)`
              }}
            />
          </div>
        </div>
      ))}
    </div>
  );
}
