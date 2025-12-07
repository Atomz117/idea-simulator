import Hero from './components/Hero';
import Features from './components/Features';
import ResultFormats from './components/ResultFormats';
import HowItWorks from './components/HowItWorks';
import WhyUse from './components/WhyUse';
import DemoPreview from './components/DemoPreview';
import Footer from './components/Footer';

function App() {
  return (
    <div className="min-h-screen bg-[#080808]">
      <Hero />
      <Features />
      <ResultFormats />
      <HowItWorks />
      <WhyUse />
      <DemoPreview />
      <Footer />
    </div>
  );
}

export default App;
