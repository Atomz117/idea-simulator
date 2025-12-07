import { Sparkles, Download } from 'lucide-react';
import BarChart from './BarChart';
import VennDiagram from './VennDiagram';
import FlowDiagram from './FlowDiagram';
import SummaryPlaceholder from './SummaryPlaceholder';

export default function DemoPreview() {
  return (
    <section className="relative py-24 bg-[#080808]">
      <div className="max-w-7xl mx-auto px-6">
        <div className="text-center mb-16">
          <h2 className="text-4xl md:text-5xl font-bold mb-4">
            <span className="bg-gradient-to-r from-[#3A0CA3] via-[#FF2E9F] to-[#00FFF0] bg-clip-text text-transparent">
              See It in Action
            </span>
          </h2>
          <p className="text-gray-400 text-lg">
            A glimpse of your comprehensive startup analysis dashboard
          </p>
        </div>

        <div className="relative group">
          <div className="absolute -inset-4 bg-gradient-to-r from-[#00FFF0] via-[#FF2E9F] to-[#3A0CA3] rounded-3xl opacity-20 group-hover:opacity-30 blur-2xl transition duration-700" />

          <div className="relative bg-gradient-to-br from-[#1a1a1a] to-[#0f0f0f] rounded-3xl border border-[#00FFF0]/20 overflow-hidden shadow-2xl">
            <div className="flex items-center gap-2 px-6 py-4 bg-[#0a0a0a] border-b border-[#00FFF0]/10">
              <div className="flex gap-2">
                <div className="w-3 h-3 rounded-full bg-[#FF2E9F]" />
                <div className="w-3 h-3 rounded-full bg-[#00FFF0]" />
                <div className="w-3 h-3 rounded-full bg-[#3A0CA3]" />
              </div>
              <div className="flex-1 text-center text-sm text-gray-500">
                Analysis Dashboard
              </div>
              <Sparkles className="w-4 h-4 text-[#00FFF0]" />
            </div>

            <div className="p-8">
              <div className="space-y-8">
                <div className="grid lg:grid-cols-3 gap-6">
                  <div className="p-6 bg-gradient-to-br from-[#0f0f0f] to-[#080808] rounded-2xl border border-[#FF2E9F]/10">
                    <h3 className="text-lg font-semibold text-[#FF2E9F] mb-6">Viability Score</h3>
                    <div className="flex items-end gap-2 mb-6">
                      <div className="text-5xl font-bold bg-gradient-to-r from-[#00FFF0] to-[#FF2E9F] bg-clip-text text-transparent">
                        82
                      </div>
                      <div className="text-gray-400 mb-2">/100</div>
                    </div>
                    <div className="h-2 bg-[#1a1a1a] rounded-full overflow-hidden">
                      <div className="h-full w-[82%] bg-gradient-to-r from-[#00FFF0] to-[#FF2E9F] rounded-full shadow-[0_0_15px_rgba(0,255,240,0.5)]" />
                    </div>
                  </div>

                  <div className="lg:col-span-2 p-6 bg-gradient-to-br from-[#0f0f0f] to-[#080808] rounded-2xl border border-[#00FFF0]/10">
                    <h3 className="text-lg font-semibold text-[#00FFF0] mb-4">Analysis Metrics</h3>
                    <BarChart />
                  </div>
                </div>

                <div className="grid lg:grid-cols-2 gap-6">
                  <div className="p-6 bg-gradient-to-br from-[#0f0f0f] to-[#080808] rounded-2xl border border-[#3A0CA3]/10">
                    <h3 className="text-lg font-semibold text-[#3A0CA3] mb-6">Factor Analysis</h3>
                    <VennDiagram />
                  </div>

                  <div className="p-6 bg-gradient-to-br from-[#0f0f0f] to-[#080808] rounded-2xl border border-[#FF2E9F]/10">
                    <h3 className="text-lg font-semibold text-[#FF2E9F] mb-6">Process Flow</h3>
                    <FlowDiagram />
                  </div>
                </div>

                <div className="grid lg:grid-cols-2 gap-6">
                  <div className="p-6 bg-gradient-to-br from-[#0f0f0f] to-[#080808] rounded-2xl border border-[#00FFF0]/10">
                    <h3 className="text-lg font-semibold text-[#00FFF0] mb-6">Summary Preview</h3>
                    <SummaryPlaceholder />
                  </div>

                  <div className="flex flex-col justify-between p-6 bg-gradient-to-br from-[#0f0f0f] to-[#080808] rounded-2xl border border-[#3A0CA3]/10">
                    <div>
                      <h3 className="text-lg font-semibold text-[#3A0CA3] mb-6">Generated Reports</h3>
                      <div className="space-y-3 mb-6">
                        {[
                          'Market Analysis Report',
                          'Competitive Landscape',
                          'Execution Roadmap'
                        ].map((report, idx) => (
                          <div key={idx} className="flex items-center gap-3 p-3 rounded-lg bg-[#0a0a0a] border border-[#3A0CA3]/20">
                            <div className="w-2 h-2 rounded-full bg-[#3A0CA3]" />
                            <span className="text-sm text-gray-300">{report}</span>
                          </div>
                        ))}
                      </div>
                    </div>

                    <button className="w-full px-6 py-3 rounded-xl font-semibold text-white flex items-center justify-center gap-2 bg-gradient-to-r from-[#00FFF0]/20 to-[#FF2E9F]/20 border border-[#00FFF0]/30 hover:border-[#00FFF0]/60 hover:from-[#00FFF0]/30 hover:to-[#FF2E9F]/30 transition duration-300 shadow-[0_0_20px_rgba(0,255,240,0.1)]">
                      <Download className="w-4 h-4" />
                      Export Data
                    </button>
                  </div>
                </div>
              </div>
            </div>
          </div>
        </div>
      </div>
    </section>
  );
}
