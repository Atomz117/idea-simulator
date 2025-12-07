import { Target, TrendingUp, Database, Lightbulb } from 'lucide-react';
import { useEffect } from 'react';

const features = [
  {
    icon: Target,
    title: 'Idea Practicality Analysis',
    description: 'Evaluate if your concept can work in real-world scenarios with actionable feasibility metrics.'
  },
  {
    icon: TrendingUp,
    title: 'Industry Fit Check',
    description: 'Understand how your idea aligns with current market trends and industry dynamics.'
  },
  {
    icon: Database,
    title: 'Data-Driven Insights',
    description: 'Get authentic intelligence from published sources, databases, and industry reports.'
  },
  {
    icon: Lightbulb,
    title: 'Improvement Suggestions',
    description: 'Receive optimization recommendations to strengthen your concept before launch.'
  }
];

export default function Features() {
  useEffect(() => {
    if (window.UnicornStudio && window.UnicornStudio.isInitialized) {
      window.UnicornStudio.init();
    }
  }, []);

  return (
    <section className="relative py-24 bg-[#080808]">
      <div
        className="absolute inset-0"
        data-us-project="6qOWy4rsrY7EO480uXsR"
        style={{
          width: '100%',
          height: '100%'
        }}
      />
      <div className="absolute inset-0 bg-gradient-to-b from-[#080808]/80 via-[#080808]/70 to-[#080808]/80" />
      <div className="relative max-w-7xl mx-auto px-6">
        <div className="text-center mb-16">
          <h2 className="text-4xl md:text-5xl font-bold mb-4">
            <span className="bg-gradient-to-r from-[#00FFF0] to-[#FF2E9F] bg-clip-text text-transparent">
              What Our Platform Does
            </span>
          </h2>
          <p className="text-gray-400 text-lg">
            Comprehensive AI simulation to validate and enhance your startup concept
          </p>
        </div>

        <div className="grid md:grid-cols-2 lg:grid-cols-4 gap-6">
          {features.map((feature, index) => (
            <div
              key={index}
              className="group relative"
            >
              <div className="absolute -inset-0.5 bg-gradient-to-r from-[#00FFF0] to-[#FF2E9F] rounded-2xl opacity-0 group-hover:opacity-100 blur transition duration-500" />

              <div className="relative h-full bg-gradient-to-br from-[#1a1a1a] to-[#080808] rounded-2xl border border-[#00FFF0]/10 p-8 hover:border-[#00FFF0]/30 transition-all duration-300">
                <div className="w-14 h-14 rounded-xl bg-gradient-to-br from-[#00FFF0]/20 to-[#FF2E9F]/20 flex items-center justify-center mb-6 group-hover:scale-110 transition-transform duration-300">
                  <feature.icon className="w-7 h-7 text-[#00FFF0]" />
                </div>

                <h3 className="text-xl font-semibold text-white mb-3">
                  {feature.title}
                </h3>

                <p className="text-gray-400 leading-relaxed">
                  {feature.description}
                </p>
              </div>
            </div>
          ))}
        </div>
      </div>
    </section>
  );
}
