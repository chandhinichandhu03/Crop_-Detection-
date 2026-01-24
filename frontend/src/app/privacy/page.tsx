'use client';

import { motion } from 'framer-motion';
import { Shield, Lock, Eye, CheckCircle } from 'lucide-react';
import Navbar from '@/components/Navbar';

export default function Privacy() {
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
                            <Shield className="w-8 h-8 text-agro-600" />
                        </div>
                        <div>
                            <h1 className="text-4xl font-black text-slate-900 dark:text-white">Privacy Policy</h1>
                            <p className="text-slate-400 font-bold text-xs uppercase tracking-widest mt-1">Last Updated: Jan 2026</p>
                        </div>
                    </div>

                    <div className="space-y-10">
                        <section>
                            <h2 className="text-2xl font-black text-slate-900 dark:text-white mb-4 flex items-center gap-3">
                                <Eye className="w-6 h-6 text-agro-500" />
                                1. Data Collection
                            </h2>
                            <p className="text-slate-500 dark:text-agro-200 leading-relaxed font-medium">
                                We collect crop images, soil data, and location information provided by you to perform AI diagnostics. This data helps us improve our spectral models for all farmers.
                            </p>
                        </section>

                        <section>
                            <h2 className="text-2xl font-black text-slate-900 dark:text-white mb-4 flex items-center gap-3">
                                <Lock className="w-6 h-6 text-agro-500" />
                                2. Data Security
                            </h2>
                            <p className="text-slate-500 dark:text-agro-200 leading-relaxed font-medium">
                                Your personal farm data is encrypted using banking-grade SSL. We never sell your personal information to third parties. Only anonymized crop data is used for research.
                            </p>
                        </section>

                        <section>
                            <h2 className="text-2xl font-black text-slate-900 dark:text-white mb-4 flex items-center gap-3">
                                <CheckCircle className="w-6 h-6 text-agro-500" />
                                3. Your Rights
                            </h2>
                            <p className="text-slate-500 dark:text-agro-200 leading-relaxed font-medium">
                                You can request access, correction, or deletion of your data at any time through our Support portal. We are compliant with international data protection standards.
                            </p>
                        </section>
                    </div>
                </motion.div>
            </div>
        </main>
    );
}
