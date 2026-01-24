'use client';

import { useState, useEffect } from 'react';
import { motion } from 'framer-motion';
import { ShieldCheck, Zap, ArrowRight, Star, Leaf, Users, Globe, Cpu, ChevronRight, Sparkles, TrendingUp, Award, Sprout } from 'lucide-react';
import Link from 'next/link';
import Navbar from '@/components/Navbar';
import { useTranslation } from 'react-i18next';

export default function Home() {
  const { t } = useTranslation();
  const [mounted, setMounted] = useState(false);

  useEffect(() => {
    setMounted(true);
  }, []);

  if (!mounted) return null;

  return (
    <main className="min-h-screen">
      <Navbar />

      {/* Hero Section */}
      <section className="relative pt-48 pb-32 px-6 overflow-hidden">
        <div className="max-w-7xl mx-auto relative z-10">
          <div className="grid lg:grid-cols-2 gap-16 items-center">
            <motion.div
              initial={{ opacity: 0, x: -50 }}
              animate={{ opacity: 1, x: 0 }}
              transition={{ duration: 0.8, ease: "easeOut" }}
            >
              <motion.div
                initial={{ opacity: 0, y: 10 }}
                animate={{ opacity: 1, y: 0 }}
                transition={{ delay: 0.2 }}
                className="inline-flex items-center gap-3 px-5 py-2.5 rounded-full bg-agro-100/50 dark:bg-agro-800/30 text-agro-700 dark:text-agro-300 text-[10px] font-black uppercase tracking-[0.2em] mb-10 border border-agro-200/50 dark:border-agro-700/50 backdrop-blur-sm"
              >
                <Sparkles className="w-3.5 h-3.5" />
                Next-Gen Precision ecosystem
              </motion.div>

              <h1 className="text-7xl lg:text-[100px] font-black text-slate-950 dark:text-white leading-[0.9] mb-10 tracking-[-0.05em]">
                Cultivating <span className="text-agro-600">Futures</span>
                <span className="block text-slate-400/50">With AI.</span>
              </h1>

              <p className="text-lg text-slate-500 dark:text-agro-200/60 mb-12 max-w-lg font-bold leading-relaxed">
                Unlock the full potential of your farm with instant bio-spectral diagnosis and a direct-to-consumer digital infrastructure.
              </p>

              <div className="flex flex-col sm:flex-row gap-6">
                <Link href="/identify" className="btn-premium flex items-center justify-center gap-4 px-10 group h-16">
                  <span className="text-sm">START DIAGNOSIS</span>
                  <Zap className="w-5 h-5 fill-white group-hover:scale-125 transition-transform" />
                </Link>
                <Link href="/market" className="px-10 h-16 rounded-[2rem] bg-white dark:bg-agro-900 text-slate-900 dark:text-white font-black border border-slate-200 dark:border-agro-800 shadow-xl hover:shadow-2xl hover:translate-y-[-2px] transition-all flex items-center justify-center gap-3">
                  <span className="text-sm">EXPLORE STORE</span>
                </Link>
              </div>

              <div className="mt-20 flex items-center gap-12">
                {[
                  { val: '99.2%', lab: 'Accuracy', icon: Award },
                  { val: '65K+', lab: 'Farmers', icon: Users },
                  { val: '₹12Cr', lab: 'Saved', icon: TrendingUp }
                ].map((stat, i) => (
                  <motion.div
                    key={i}
                    initial={{ opacity: 0 }}
                    animate={{ opacity: 1 }}
                    transition={{ delay: 0.5 + (i * 0.1) }}
                    className="flex flex-col gap-1"
                  >
                    <div className="flex items-center gap-2 text-agro-600">
                      <stat.icon className="w-3.5 h-3.5" />
                      <span className="text-2xl font-black text-slate-900 dark:text-white tracking-tighter">{stat.val}</span>
                    </div>
                    <span className="text-[10px] font-black text-slate-400 dark:text-agro-500 uppercase tracking-widest">{stat.lab}</span>
                  </motion.div>
                ))}
              </div>
            </motion.div>

            <motion.div
              initial={{ opacity: 0, scale: 0.9, rotate: 5 }}
              animate={{ opacity: 1, scale: 1, rotate: 0 }}
              transition={{ duration: 1, ease: "circOut" }}
              className="relative"
            >
              <div className="relative rounded-[4rem] overflow-hidden shadow-[0_50px_100px_-20px_rgba(20,83,45,0.4)] border-[12px] border-white dark:border-agro-900 float-animation">
                <img
                  src="https://images.unsplash.com/photo-1523348837708-15d4a09cfac2?auto=format&fit=crop&q=80&w=1200&h=1500"
                  alt="Precision Farming"
                  className="w-full aspect-[4/5] object-cover hover:scale-110 transition-transform duration-[2s]"
                />
                <div className="absolute inset-0 bg-gradient-to-t from-agro-950/80 via-transparent to-transparent"></div>

                <div className="absolute bottom-10 left-10 right-10 p-10 glass-card rounded-[2.5rem] border-white/30">
                  <div className="flex items-center gap-4 mb-3">
                    <div className="bg-agro-500 p-2.5 rounded-2xl shadow-lg shadow-agro-500/50">
                      <ShieldCheck className="w-6 h-6 text-white" />
                    </div>
                    <span className="font-black text-agro-900 dark:text-white text-xs uppercase tracking-widest">Spectral Scan Active</span>
                  </div>
                  <div className="w-full bg-slate-200 dark:bg-agro-800/50 h-1.5 rounded-full mb-4 overflow-hidden">
                    <motion.div
                      initial={{ width: 0 }}
                      animate={{ width: '85%' }}
                      transition={{ duration: 2, repeat: Infinity }}
                      className="bg-agro-500 h-full shadow-[0_0_10px_#22c55e]"
                    />
                  </div>
                  <p className="text-[10px] font-bold text-slate-500 dark:text-agro-200 uppercase tracking-widest">Scanning leaf tissue density... 85% complete</p>
                </div>
              </div>

              {/* Glowing Background Orbs */}
              <div className="absolute -top-20 -right-20 w-80 h-80 bg-agro-500/20 dark:bg-agro-500/30 rounded-full blur-[100px] -z-10 animate-pulse"></div>
              <div className="absolute -bottom-40 -left-40 w-96 h-96 bg-blue-500/10 dark:bg-blue-600/20 rounded-full blur-[120px] -z-10"></div>
            </motion.div>
          </div>
        </div>
      </section>

      {/* Features Grid */}
      <section className="py-40 px-6 relative bg-white/30 dark:bg-agro-950/20 backdrop-blur-3xl">
        <div className="max-w-7xl mx-auto">
          <motion.div
            initial={{ opacity: 0, y: 30 }}
            whileInView={{ opacity: 1, y: 0 }}
            viewport={{ once: true }}
            className="text-center mb-24"
          >
            <h2 className="text-5xl lg:text-7xl font-black text-slate-950 dark:text-white mb-8 tracking-tighter">Engineered for <span className="text-agro-600">Excellence</span>.</h2>
            <p className="text-slate-500 dark:text-agro-300 font-bold max-w-2xl mx-auto text-lg leading-relaxed">Integrated tools built on enterprise-grade infrastructure to revolutionize your yield.</p>
          </motion.div>

          <div className="grid md:grid-cols-3 gap-10">
            {[
              {
                icon: Cpu,
                title: 'Neural Diagnosis',
                desc: 'Upload a leaf and let our MobileNet-V2 inference engine identify over 40+ species and diseases in milliseconds.',
                href: '/identify',
                color: 'bg-emerald-500'
              },
              {
                icon: Globe,
                title: 'Market Integrity',
                desc: 'Access certified seeds and organic inputs directly from verified distributors with transparent tracking protocols.',
                href: '/market',
                color: 'bg-agro-600'
              },
              {
                icon: Zap,
                title: 'Real-Time Insights',
                desc: 'Ask our AI expert about soil toxicity, moisture levels, or crop rotation strategies for your specific region.',
                href: '/chat',
                color: 'bg-blue-500'
              }
            ].map((feature, i) => (
              <motion.div
                key={i}
                initial={{ opacity: 0, y: 40 }}
                whileInView={{ opacity: 1, y: 0 }}
                viewport={{ once: true }}
                transition={{ delay: i * 0.1, duration: 0.7 }}
                className="p-10 rounded-[3rem] border border-slate-100 dark:border-agro-800/50 bg-white/50 dark:bg-agro-900/40 hover:shadow-[0_40px_80px_-20px_rgba(0,0,0,0.1)] dark:hover:shadow-[0_40px_80px_-20px_rgba(20,83,45,0.3)] hover:translate-y-[-10px] transition-all group flex flex-col h-full overflow-hidden relative"
              >
                <div className={`w-16 h-16 rounded-2xl ${feature.color} flex items-center justify-center mb-10 shadow-2xl shadow-emerald-500/20 group-hover:scale-125 group-hover:rotate-6 transition-all duration-500`}>
                  <feature.icon className="w-8 h-8 text-white" />
                </div>
                <h3 className="text-3xl font-black text-slate-950 dark:text-white mb-6 tracking-tighter">{feature.title}</h3>
                <p className="text-slate-500 dark:text-agro-200/70 font-bold leading-relaxed mb-12 flex-1">{feature.desc}</p>
                <Link
                  href={feature.href}
                  className="inline-flex items-center gap-3 text-[10px] font-black uppercase tracking-[0.2em] text-agro-600 hover:text-agro-700 dark:hover:text-agro-400 group/link"
                >
                  INITIALIZE MODULE
                  <ChevronRight className="w-4 h-4 group-hover/link:translate-x-1 transition-transform" />
                </Link>
                {/* Decorative Pattern Component */}
                <div className="absolute top-0 right-0 w-32 h-32 opacity-[0.03] dark:opacity-[0.05] pointer-events-none group-hover:scale-150 transition-transform">
                  <feature.icon className="w-full h-full" />
                </div>
              </motion.div>
            ))}
          </div>
        </div>
      </section>

      {/* Footer */}
      <footer className="py-24 px-6 bg-slate-950 text-white relative z-10">
        <div className="max-w-7xl mx-auto">
          <div className="flex flex-col md:flex-row justify-between items-start md:items-center gap-16 pb-16 border-b border-white/10">
            <div>
              <div className="flex items-center gap-4 mb-8">
                <div className="bg-agro-600 p-2.5 rounded-2xl">
                  <Sprout className="text-white w-8 h-8" />
                </div>
                <span className="text-3xl font-black tracking-tighter uppercase">Agro Doctor</span>
              </div>
              <p className="text-slate-400 font-bold max-w-sm text-sm leading-relaxed mb-10">
                Transforming the backbone of the nation through precision digital agriculture and deep bio-analysis.
              </p>
            </div>

            <div className="grid grid-cols-2 sm:grid-cols-3 gap-16 sm:gap-24">
              <div>
                <h4 className="text-[10px] font-black uppercase tracking-widest text-agro-500 mb-8">Ecosystem</h4>
                <ul className="space-y-4 font-black text-xs uppercase tracking-widest">
                  <li><Link href="/identify" className="hover:text-agro-500 transition-colors">Doctor</Link></li>
                  <li><Link href="/market" className="hover:text-agro-500 transition-colors">Market</Link></li>
                  <li><Link href="/chat" className="hover:text-agro-500 transition-colors">Expert</Link></li>
                </ul>
              </div>
              <div>
                <h4 className="text-[10px] font-black uppercase tracking-widest text-agro-500 mb-8">Connect</h4>
                <ul className="space-y-4 font-black text-xs uppercase tracking-widest">
                  <li><Link href="/privacy" className="hover:text-agro-500 transition-colors">Privacy</Link></li>
                  <li><Link href="/terms" className="hover:text-agro-500 transition-colors">Terms</Link></li>
                  <li><Link href="/support" className="hover:text-agro-500 transition-colors">Support</Link></li>
                </ul>
              </div>
            </div>
          </div>

          <div className="pt-10 flex flex-col sm:flex-row justify-between items-center gap-6">
            <p className="text-slate-500 text-[10px] font-black uppercase tracking-[0.3em]">© 2026 Agro Doctor Ecosystem v2.1.0 Ready</p>
            <div className="flex gap-4">
              {[...Array(4)].map((_, i) => (
                <div key={i} className="w-8 h-8 rounded-lg bg-white/5 border border-white/10 hover:bg-white/10 transition-colors cursor-pointer flex items-center justify-center">
                  <div className="w-1 h-1 bg-white/20 rounded-full" />
                </div>
              ))}
            </div>
          </div>
        </div>
      </footer>
    </main>
  );
}
