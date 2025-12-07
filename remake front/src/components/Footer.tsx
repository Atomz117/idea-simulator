import { Sparkles } from 'lucide-react';

export default function Footer() {
  const links = {
    product: [
      { name: 'About', href: '#' },
      { name: 'Blog', href: '#' },
      { name: 'Contact', href: '#' }
    ],
    legal: [
      { name: 'Privacy', href: '#' },
      { name: 'Terms', href: '#' }
    ]
  };

  return (
    <footer className="relative bg-[#080808] border-t border-[#00FFF0]/10">
      <div className="max-w-7xl mx-auto px-6 py-12">
        <div className="grid md:grid-cols-4 gap-8 mb-8">
          <div className="md:col-span-2">
            <div className="flex items-center gap-2 mb-4">
              <div className="w-10 h-10 rounded-xl bg-gradient-to-br from-[#00FFF0] to-[#FF2E9F] flex items-center justify-center">
                <Sparkles className="w-6 h-6 text-[#080808]" />
              </div>
              <span className="text-xl font-bold text-white">IdeaSim AI</span>
            </div>
            <p className="text-gray-400 max-w-md">
              AI-powered startup idea validation through real-world environment simulation. Make smarter decisions with data-driven insights.
            </p>
          </div>

          <div>
            <h4 className="text-white font-semibold mb-4">Product</h4>
            <ul className="space-y-2">
              {links.product.map((link, idx) => (
                <li key={idx}>
                  <a href={link.href} className="text-gray-400 hover:text-[#00FFF0] transition-colors">
                    {link.name}
                  </a>
                </li>
              ))}
            </ul>
          </div>

          <div>
            <h4 className="text-white font-semibold mb-4">Legal</h4>
            <ul className="space-y-2">
              {links.legal.map((link, idx) => (
                <li key={idx}>
                  <a href={link.href} className="text-gray-400 hover:text-[#00FFF0] transition-colors">
                    {link.name}
                  </a>
                </li>
              ))}
            </ul>
          </div>
        </div>

        <div className="pt-8 border-t border-[#00FFF0]/10">
          <div className="flex flex-col md:flex-row items-center justify-between gap-4">
            <p className="text-gray-500 text-sm">
              © 2024 IdeaSim AI. All rights reserved.
            </p>
            <div className="flex items-center gap-4 text-sm text-gray-500">
              <span>Powered by AI</span>
              <div className="w-1.5 h-1.5 bg-[#00FFF0] rounded-full animate-pulse" />
              <span>Built for Innovators</span>
            </div>
          </div>
        </div>
      </div>
    </footer>
  );
}
