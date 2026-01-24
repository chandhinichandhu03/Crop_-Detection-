'use client';

import { motion } from 'framer-motion';
import { FileText, Scale, Gavel, Info } from 'lucide-react';
import Navbar from '@/components/Navbar';

export default function Terms() {
    return (
        <main className="min-h-screen pt-40 pb-20 px-6">
            <Navbar />
            <div className="max-w-4xl mx-auto">

                <motion.div
                    initial={{ opacity: 0, y: 20 }}
                    animate={{ opacity: 1, y: 0 }}
                    className="bg-white dark:bg-agro-900 rounded-[3rem] p-12 shadow-premium border border-slate-100 dark:border-agro-800"
                >
                    <div className="flex items-center gap-4 mb-8">
                        <div className="bg-agro-100 dark:bg-agro-800 p-4 rounded-2xl">
                            <FileText className="w-8 h-8 text-agro-600" />
                        </div>
                        <div>
                            <h1 className="text-4xl font-black text-slate-900 dark:text-white">Terms of Service</h1>
                            <p className="text-slate-400 font-bold text-xs uppercase tracking-widest mt-1">Version 2.0 • Jan 2026</p>
                        </div>
                    </div>

                    <div className="space-y-10">
                        <section>
                            <h2 className="text-2xl font-black text-slate-900 dark:text-white mb-4 flex items-center gap-3">
                                <Scale className="w-6 h-6 text-agro-500" />
                                1. Service Usage
                            </h2>
                            <p className="text-slate-500 dark:text-agro-200 leading-relaxed font-medium">
                                Agro Doctor provides AI-based recommendations. While our accuracy is 99%, farming outcomes depend on various environmental factors. Use our suggestions as an expert guide alongside traditional practice.
                            </p>
                        </section>

                        <section>
                            <h2 className="text-2xl font-black text-slate-900 dark:text-white mb-4 flex items-center gap-3">
                                <Gavel className="w-6 h-6 text-agro-500" />
                                2. User Conduct
                            </h2>
                            <p className="text-slate-500 dark:text-agro-200 leading-relaxed font-medium">
                                Users agree to provide genuine crop data and images. Misuse of the platform or sharing harmful content may result in account termination to protect the farming community.
                            </p>
                        </section>

                        <section className="p-6 bg-slate-50 dark:bg-agro-950/50 rounded-2xl border border-slate-100 dark:border-agro-800">
                            <div className="flex gap-3">
                                <Info className="w-5 h-5 text-agro-600 flex-shrink-0" />
                                <p className="text-xs font-bold text-slate-500 dark:text-agro-300 italic">
                                    By using Agro Doctor, you agree to these legal terms. We reserve the right to update these terms to better serve our growing digital ecosystem.
                                </p>
                            </div>
                        </section>
                    </div>
                </motion.div>
            </div>
        </main>
    );
}
