import { Clock, CheckCircle2, Globe, Users } from 'lucide-react';

const benefits = [
  {
    icon: Clock,
    title: 'Saves Weeks of Research',
    description: 'Get instant insights that would take weeks to compile manually'
  },
  {
    icon: CheckCircle2,
    title: 'Validates Feasibility',
    description: 'Know if your idea can work before investing time and money'
  },
  {
    icon: Globe,
    title: 'Authentic Source Data',
    description: 'Backed by real industry databases and published reports'
  },
  {
    icon: Users,
    title: 'Perfect for Innovators',
    description: 'Ideal for founders, students, and entrepreneurs at any stage'
  }
];

export default function WhyUse() {
  return (
    <section className="relative py-24 bg-gradient-to-b from-[#0a0a0a] to-[#080808] overflow-hidden">
      <div className="absolute inset-0 opacity-10">
        <div className="absolute top-20 right-20 w-96 h-96 bg-[#00FFF0] rounded-full blur-[120px]" />
        <div className="absolute bottom-20 left-20 w-96 h-96 bg-[#FF2E9F] rounded-full blur-[120px]" />
      </div>

      <div className="relative max-w-7xl mx-auto px-6">
        <div className="text-center mb-16">
          <h2 className="text-4xl md:text-5xl font-bold mb-4">
            <span className="bg-gradient-to-r from-[#FF2E9F] to-[#00FFF0] bg-clip-text text-transparent">
              Why Use This Platform?
            </span>
          </h2>
          <p className="text-gray-400 text-lg">
            The smartest way to validate and refine your startup concepts
          </p>
        </div>

        <div className="grid md:grid-cols-2 lg:grid-cols-4 gap-6">
          {benefits.map((benefit, index) => (
            <div
              key={index}
              className="group relative"
            >
              <div className="absolute -inset-0.5 bg-gradient-to-r from-[#00FFF0]/30 to-[#FF2E9F]/30 rounded-2xl opacity-0 group-hover:opacity-100 blur transition duration-500" />

              <div className="relative h-full bg-gradient-to-br from-[#1a1a1a] to-[#0f0f0f] rounded-2xl border border-[#00FFF0]/10 p-8 group-hover:border-[#00FFF0]/30 transition-all duration-300">
                <div className="flex flex-col items-center text-center">
                  <div className="w-16 h-16 rounded-xl bg-gradient-to-br from-[#00FFF0]/20 to-[#FF2E9F]/20 flex items-center justify-center mb-6 group-hover:scale-110 transition-transform duration-300">
                    <benefit.icon className="w-8 h-8 text-[#00FFF0]" />
                  </div>

                  <h3 className="text-xl font-semibold text-white mb-3">
                    {benefit.title}
                  </h3>

                  <p className="text-gray-400 leading-relaxed">
                    {benefit.description}
                  </p>
                </div>
              </div>
            </div>
          ))}
        </div>

        <div className="mt-16 text-center">
          <div className="inline-flex flex-col items-center gap-4 px-8 py-6 rounded-2xl bg-gradient-to-br from-[#1a1a1a] to-[#0f0f0f] border border-[#00FFF0]/20">
            <p className="text-gray-300 text-lg">
              Join innovative founders making smarter decisions with data
            </p>
            <div className="flex items-center gap-6 text-sm text-gray-500">
              <div className="flex items-center gap-2">
                <div className="w-2 h-2 bg-[#00FFF0] rounded-full" />
                <span>No credit card required</span>
              </div>
              <div className="flex items-center gap-2">
                <div className="w-2 h-2 bg-[#FF2E9F] rounded-full" />
                <span>Instant results</span>
              </div>
            </div>
          </div>
        </div>
      </div>
    </section>
  );
}
