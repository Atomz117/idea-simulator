import { FileInput, Cpu, Layout } from 'lucide-react';

const steps = [
  {
    icon: FileInput,
    number: '01',
    title: 'Paste Your Idea',
    description: 'Simply describe your startup concept in a few sentences'
  },
  {
    icon: Cpu,
    number: '02',
    title: 'AI Simulates Environment',
    description: 'Our AI analyzes industry data, trends, and real-world scenarios'
  },
  {
    icon: Layout,
    number: '03',
    title: 'Get Visual Results',
    description: 'Receive insights in 4 beautiful, actionable formats'
  }
];

export default function HowItWorks() {
  return (
    <section className="relative py-24 bg-[#080808]">
      <div className="max-w-7xl mx-auto px-6">
        <div className="text-center mb-16">
          <h2 className="text-4xl md:text-5xl font-bold mb-4">
            <span className="bg-gradient-to-r from-[#00FFF0] to-[#3A0CA3] bg-clip-text text-transparent">
              How It Works
            </span>
          </h2>
          <p className="text-gray-400 text-lg">
            Three simple steps to validate your startup idea
          </p>
        </div>

        <div className="grid md:grid-cols-3 gap-12 relative">
          <div className="hidden md:block absolute top-1/2 left-0 right-0 h-0.5 bg-gradient-to-r from-transparent via-[#00FFF0]/20 to-transparent -translate-y-1/2" />

          {steps.map((step, index) => (
            <div key={index} className="relative">
              <div className="relative group">
                <div className="absolute -inset-4 bg-gradient-to-r from-[#00FFF0]/0 via-[#00FFF0]/5 to-[#00FFF0]/0 rounded-3xl opacity-0 group-hover:opacity-100 blur-xl transition duration-500" />

                <div className="relative text-center">
                  <div className="inline-flex items-center justify-center w-24 h-24 rounded-2xl bg-gradient-to-br from-[#1a1a1a] to-[#080808] border border-[#00FFF0]/20 mb-6 group-hover:border-[#00FFF0]/40 transition-all duration-300 group-hover:scale-110">
                    <div className="absolute inset-0 bg-gradient-to-br from-[#00FFF0]/10 to-[#FF2E9F]/10 rounded-2xl" />
                    <step.icon className="w-10 h-10 text-[#00FFF0] relative z-10" />
                  </div>

                  <div className="absolute -top-4 -right-4 w-16 h-16 rounded-full bg-gradient-to-br from-[#00FFF0] to-[#FF2E9F] flex items-center justify-center font-bold text-2xl text-[#080808] shadow-[0_0_30px_rgba(0,255,240,0.5)]">
                    {step.number}
                  </div>

                  <h3 className="text-2xl font-bold text-white mb-3">
                    {step.title}
                  </h3>

                  <p className="text-gray-400 leading-relaxed">
                    {step.description}
                  </p>
                </div>
              </div>

              {index < steps.length - 1 && (
                <div className="hidden md:block absolute top-12 -right-6 text-[#00FFF0]/30">
                  <svg width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" strokeWidth="2">
                    <path d="M5 12h14M12 5l7 7-7 7" />
                  </svg>
                </div>
              )}
            </div>
          ))}
        </div>
      </div>
    </section>
  );
}
