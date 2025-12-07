import { Sparkles, ArrowRight } from 'lucide-react';
import { useState, useEffect } from 'react';

export default function Hero() {
  const [idea, setIdea] = useState('');

  useEffect(() => {
    const script = document.createElement('script');
    script.src = 'https://cdn.jsdelivr.net/gh/hiunicornstudio/unicornstudio.js@v1.5.2/dist/unicornStudio.umd.js';
    script.onload = () => {
      if (window.UnicornStudio && !window.UnicornStudio.isInitialized) {
        window.UnicornStudio.init();
        window.UnicornStudio.isInitialized = true;
      }
    };
    document.head.appendChild(script);
  }, []);

  return (
    <section className="relative min-h-screen flex items-center justify-center overflow-hidden bg-[#080808]">
      <div className="absolute inset-0 opacity-30">
        <div className="absolute inset-0 bg-gradient-to-br from-[#3A0CA3] via-[#080808] to-[#080808]" />
        <div className="absolute top-20 left-20 w-96 h-96 bg-[#00FFF0] rounded-full blur-[120px] opacity-20 animate-pulse" />
        <div className="absolute bottom-20 right-20 w-96 h-96 bg-[#FF2E9F] rounded-full blur-[120px] opacity-20 animate-pulse" style={{ animationDelay: '1s' }} />
      </div>

      <div
        className="absolute inset-0 flex items-center justify-center opacity-40"
        style={{
          pointerEvents: 'none'
        }}
      >
        <div
          data-us-project="8qeX81n9mdTiVvngzM3y"
          style={{
            width: '100%',
            height: '100%',
            maxWidth: '1440px',
            maxHeight: '900px'
          }}
        />
      </div>
      <div className="absolute inset-0 bg-gradient-to-b from-[#080808]/20 via-transparent to-[#080808]/60" />

      <div className="relative z-10 max-w-6xl mx-auto px-6 py-20 text-center">
        <div className="inline-flex items-center gap-2 px-4 py-2 rounded-full bg-gradient-to-r from-[#00FFF0]/10 to-[#FF2E9F]/10 border border-[#00FFF0]/20 mb-8 backdrop-blur-sm">
          <Sparkles className="w-4 h-4 text-[#00FFF0]" />
          <span className="text-sm text-gray-300">AI-Powered Environment Simulation</span>
        </div>

        <h1 className="text-5xl md:text-7xl font-bold mb-6 leading-tight">
          <span className="bg-gradient-to-r from-[#00FFF0] via-[#FF2E9F] to-[#3A0CA3] bg-clip-text text-transparent">
            Test Your Startup Idea
          </span>
          <br />
          <span className="text-white">Instantly with AI</span>
        </h1>

        <p className="text-xl text-gray-400 mb-12 max-w-3xl mx-auto">
          Paste your idea and get real-world feasibility insights, improvements, and industry-backed analysis powered by authentic data sources.
        </p>

        <div className="max-w-4xl mx-auto mb-8">
          <div className="relative group">
            <div className="absolute -inset-1 bg-gradient-to-r from-[#00FFF0] via-[#FF2E9F] to-[#3A0CA3] rounded-2xl blur opacity-25 group-hover:opacity-40 transition duration-500" />

            <div className="relative bg-[#080808]/90 backdrop-blur-xl rounded-2xl border border-[#00FFF0]/20 p-6 shadow-2xl">
              <textarea
                value={idea}
                onChange={(e) => setIdea(e.target.value)}
                placeholder="Paste your startup idea… e.g., 'A platform that helps students find last-minute tutors in their city.'"
                className="w-full bg-transparent text-white placeholder-gray-500 text-lg outline-none resize-none mb-4"
                rows={4}
              />

              <button className="w-full md:w-auto px-8 py-4 bg-gradient-to-r from-[#00FFF0] to-[#FF2E9F] text-[#080808] font-semibold rounded-xl hover:shadow-[0_0_30px_rgba(0,255,240,0.5)] transition-all duration-300 flex items-center justify-center gap-2 group">
                <span>Analyze Idea</span>
                <ArrowRight className="w-5 h-5 group-hover:translate-x-1 transition-transform" />
              </button>
            </div>
          </div>
        </div>

        <div className="flex flex-wrap items-center justify-center gap-8 text-sm text-gray-500">
          <div className="flex items-center gap-2">
            <div className="w-2 h-2 bg-[#00FFF0] rounded-full animate-pulse" />
            <span>Authentic Data Sources</span>
          </div>
          <div className="flex items-center gap-2">
            <div className="w-2 h-2 bg-[#FF2E9F] rounded-full animate-pulse" style={{ animationDelay: '0.5s' }} />
            <span>Industry Insights</span>
          </div>
          <div className="flex items-center gap-2">
            <div className="w-2 h-2 bg-[#3A0CA3] rounded-full animate-pulse" style={{ animationDelay: '1s' }} />
            <span>Instant Analysis</span>
          </div>
        </div>
      </div>

      <div className="absolute bottom-0 left-0 right-0 h-32 bg-gradient-to-t from-[#080808] to-transparent" />
    </section>
  );
}
