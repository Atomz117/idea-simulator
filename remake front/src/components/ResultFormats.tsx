import { FileText, BarChart3, Shield, Map } from 'lucide-react';

export default function ResultFormats() {
  return (
    <section className="relative py-24 bg-gradient-to-b from-[#080808] to-[#0a0a0a]">
      <div className="absolute inset-0 opacity-20">
        <div className="absolute top-1/2 left-1/4 w-96 h-96 bg-[#3A0CA3] rounded-full blur-[150px]" />
        <div className="absolute top-1/3 right-1/4 w-96 h-96 bg-[#FF2E9F] rounded-full blur-[150px]" />
      </div>

      <div className="relative max-w-7xl mx-auto px-6">
        <div className="text-center mb-16">
          <h2 className="text-4xl md:text-5xl font-bold mb-4">
            <span className="bg-gradient-to-r from-[#FF2E9F] via-[#00FFF0] to-[#3A0CA3] bg-clip-text text-transparent">
              Get Results in 4 Stunning Formats
            </span>
          </h2>
          <p className="text-gray-400 text-lg max-w-2xl mx-auto">
            Your analysis delivered in multiple visual formats for maximum clarity and impact
          </p>
        </div>

        <div className="grid md:grid-cols-2 gap-8">
          <div className="group relative">
            <div className="absolute -inset-1 bg-gradient-to-r from-[#00FFF0] to-[#FF2E9F] rounded-3xl opacity-20 group-hover:opacity-40 blur-xl transition duration-500" />

            <div className="relative bg-[#0f0f0f]/80 backdrop-blur-xl rounded-3xl border border-[#00FFF0]/20 p-8 hover:border-[#00FFF0]/40 transition-all duration-300">
              <div className="flex items-center gap-4 mb-6">
                <div className="w-12 h-12 rounded-xl bg-gradient-to-br from-[#00FFF0]/20 to-[#FF2E9F]/20 flex items-center justify-center">
                  <FileText className="w-6 h-6 text-[#00FFF0]" />
                </div>
                <h3 className="text-2xl font-bold text-white">Short Summary</h3>
              </div>

              <div className="bg-gradient-to-br from-[#1a1a1a] to-[#0f0f0f] rounded-2xl p-6 border border-[#00FFF0]/10">
                <div className="space-y-4">
                  <div className="flex items-start gap-3">
                    <div className="w-1.5 h-1.5 bg-[#00FFF0] rounded-full mt-2 animate-pulse" />
                    <p className="text-gray-300 leading-relaxed">
                      <span className="text-[#00FFF0] font-semibold">High market demand</span> identified with moderate competition in target segment.
                    </p>
                  </div>
                  <div className="flex items-start gap-3">
                    <div className="w-1.5 h-1.5 bg-[#FF2E9F] rounded-full mt-2 animate-pulse" style={{ animationDelay: '0.5s' }} />
                    <p className="text-gray-300 leading-relaxed">
                      Recommended to <span className="text-[#FF2E9F] font-semibold">narrow target audience</span> and validate pricing through customer surveys.
                    </p>
                  </div>
                  <div className="flex items-start gap-3">
                    <div className="w-1.5 h-1.5 bg-[#3A0CA3] rounded-full mt-2 animate-pulse" style={{ animationDelay: '1s' }} />
                    <p className="text-gray-300 leading-relaxed">
                      Strong potential with <span className="text-[#3A0CA3] font-semibold">strategic positioning</span> adjustments.
                    </p>
                  </div>
                </div>
              </div>
            </div>
          </div>

          <div className="group relative">
            <div className="absolute -inset-1 bg-gradient-to-r from-[#FF2E9F] to-[#3A0CA3] rounded-3xl opacity-20 group-hover:opacity-40 blur-xl transition duration-500" />

            <div className="relative bg-[#0f0f0f]/80 backdrop-blur-xl rounded-3xl border border-[#FF2E9F]/20 p-8 hover:border-[#FF2E9F]/40 transition-all duration-300">
              <div className="flex items-center gap-4 mb-6">
                <div className="w-12 h-12 rounded-xl bg-gradient-to-br from-[#FF2E9F]/20 to-[#3A0CA3]/20 flex items-center justify-center">
                  <BarChart3 className="w-6 h-6 text-[#FF2E9F]" />
                </div>
                <h3 className="text-2xl font-bold text-white">Chart Diagram</h3>
              </div>

              <div className="bg-gradient-to-br from-[#1a1a1a] to-[#0f0f0f] rounded-2xl p-6 border border-[#FF2E9F]/10">
                <div className="space-y-6">
                  <div className="space-y-3">
                    <div className="flex items-center justify-between text-sm">
                      <span className="text-gray-400">Market Viability</span>
                      <span className="text-[#00FFF0] font-semibold">85%</span>
                    </div>
                    <div className="h-3 bg-[#1a1a1a] rounded-full overflow-hidden">
                      <div className="h-full w-[85%] bg-gradient-to-r from-[#00FFF0] to-[#FF2E9F] rounded-full shadow-[0_0_15px_rgba(0,255,240,0.5)]" />
                    </div>
                  </div>

                  <div className="space-y-3">
                    <div className="flex items-center justify-between text-sm">
                      <span className="text-gray-400">Competition Level</span>
                      <span className="text-[#FF2E9F] font-semibold">62%</span>
                    </div>
                    <div className="h-3 bg-[#1a1a1a] rounded-full overflow-hidden">
                      <div className="h-full w-[62%] bg-gradient-to-r from-[#FF2E9F] to-[#3A0CA3] rounded-full shadow-[0_0_15px_rgba(255,46,159,0.5)]" />
                    </div>
                  </div>

                  <div className="space-y-3">
                    <div className="flex items-center justify-between text-sm">
                      <span className="text-gray-400">Implementation Ease</span>
                      <span className="text-[#3A0CA3] font-semibold">78%</span>
                    </div>
                    <div className="h-3 bg-[#1a1a1a] rounded-full overflow-hidden">
                      <div className="h-full w-[78%] bg-gradient-to-r from-[#3A0CA3] to-[#00FFF0] rounded-full shadow-[0_0_15px_rgba(58,12,163,0.5)]" />
                    </div>
                  </div>
                </div>
              </div>
            </div>
          </div>

          <div className="group relative">
            <div className="absolute -inset-1 bg-gradient-to-r from-[#3A0CA3] to-[#00FFF0] rounded-3xl opacity-20 group-hover:opacity-40 blur-xl transition duration-500" />

            <div className="relative bg-[#0f0f0f]/80 backdrop-blur-xl rounded-3xl border border-[#3A0CA3]/20 p-8 hover:border-[#3A0CA3]/40 transition-all duration-300">
              <div className="flex items-center gap-4 mb-6">
                <div className="w-12 h-12 rounded-xl bg-gradient-to-br from-[#3A0CA3]/20 to-[#00FFF0]/20 flex items-center justify-center">
                  <Shield className="w-6 h-6 text-[#3A0CA3]" />
                </div>
                <h3 className="text-2xl font-bold text-white">Strengths & Risks</h3>
              </div>

              <div className="bg-gradient-to-br from-[#1a1a1a] to-[#0f0f0f] rounded-2xl p-6 border border-[#3A0CA3]/10">
                <div className="grid grid-cols-2 gap-6">
                  <div className="space-y-3">
                    <h4 className="text-[#00FFF0] font-semibold text-sm uppercase tracking-wide">Strengths</h4>
                    <div className="space-y-2">
                      <div className="flex items-center gap-2">
                        <div className="w-2 h-2 bg-[#00FFF0] rounded-full" />
                        <span className="text-gray-300 text-sm">Unmet demand</span>
                      </div>
                      <div className="flex items-center gap-2">
                        <div className="w-2 h-2 bg-[#00FFF0] rounded-full" />
                        <span className="text-gray-300 text-sm">Easy adoption</span>
                      </div>
                      <div className="flex items-center gap-2">
                        <div className="w-2 h-2 bg-[#00FFF0] rounded-full" />
                        <span className="text-gray-300 text-sm">Scalable model</span>
                      </div>
                    </div>
                  </div>

                  <div className="space-y-3">
                    <h4 className="text-[#FF2E9F] font-semibold text-sm uppercase tracking-wide">Risks</h4>
                    <div className="space-y-2">
                      <div className="flex items-center gap-2">
                        <div className="w-2 h-2 bg-[#FF2E9F] rounded-full" />
                        <span className="text-gray-300 text-sm">High competition</span>
                      </div>
                      <div className="flex items-center gap-2">
                        <div className="w-2 h-2 bg-[#FF2E9F] rounded-full" />
                        <span className="text-gray-300 text-sm">Complex ops</span>
                      </div>
                      <div className="flex items-center gap-2">
                        <div className="w-2 h-2 bg-[#FF2E9F] rounded-full" />
                        <span className="text-gray-300 text-sm">Funding needs</span>
                      </div>
                    </div>
                  </div>
                </div>
              </div>
            </div>
          </div>

          <div className="group relative">
            <div className="absolute -inset-1 bg-gradient-to-r from-[#00FFF0] via-[#FF2E9F] to-[#3A0CA3] rounded-3xl opacity-20 group-hover:opacity-40 blur-xl transition duration-500" />

            <div className="relative bg-[#0f0f0f]/80 backdrop-blur-xl rounded-3xl border border-[#00FFF0]/20 p-8 hover:border-[#00FFF0]/40 transition-all duration-300">
              <div className="flex items-center gap-4 mb-6">
                <div className="w-12 h-12 rounded-xl bg-gradient-to-br from-[#00FFF0]/20 to-[#3A0CA3]/20 flex items-center justify-center">
                  <Map className="w-6 h-6 text-[#00FFF0]" />
                </div>
                <h3 className="text-2xl font-bold text-white">Improvement Roadmap</h3>
              </div>

              <div className="bg-gradient-to-br from-[#1a1a1a] to-[#0f0f0f] rounded-2xl p-6 border border-[#00FFF0]/10">
                <div className="space-y-4">
                  {[
                    { step: '01', text: 'Validate customer segment', color: '#00FFF0' },
                    { step: '02', text: 'Map competition landscape', color: '#FF2E9F' },
                    { step: '03', text: 'Adjust pricing strategy', color: '#3A0CA3' },
                    { step: '04', text: 'Prototype & test pilot', color: '#00FFF0' }
                  ].map((item, idx) => (
                    <div key={idx} className="flex items-center gap-4">
                      <div
                        className="w-10 h-10 rounded-lg flex items-center justify-center font-bold text-sm"
                        style={{
                          background: `linear-gradient(135deg, ${item.color}20, ${item.color}10)`,
                          color: item.color,
                          border: `1px solid ${item.color}30`
                        }}
                      >
                        {item.step}
                      </div>
                      <div className="flex-1 text-gray-300">
                        {item.text}
                      </div>
                      {idx < 3 && (
                        <div className="absolute left-[37px] w-0.5 h-4 bg-gradient-to-b from-[#00FFF0]/30 to-transparent" style={{ top: `${(idx + 1) * 60 + 40}px` }} />
                      )}
                    </div>
                  ))}
                </div>
              </div>
            </div>
          </div>
        </div>
      </div>
    </section>
  );
}
