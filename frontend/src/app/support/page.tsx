'use client';

import { motion } from 'framer-motion';
import { HelpCircle, Mail, Phone, MessageSquare, Send } from 'lucide-react';
import Navbar from '@/components/Navbar';
import Link from 'next/link';

export default function Support() {
    return (
        <main className="min-h-screen pt-40 pb-20 px-6">
            <Navbar />
            <div className="max-w-4xl mx-auto">

                <div className="grid md:grid-cols-3 gap-8">
                    <motion.div
                        initial={{ opacity: 0, y: 20 }}
                        animate={{ opacity: 1, y: 0 }}
                        className="md:col-span-1 space-y-6"
                    >
                        <div className="bg-white dark:bg-agro-900 rounded-[2.5rem] p-8 shadow-premium border border-slate-100 dark:border-agro-800 text-center">
                            <div className="bg-agro-100 dark:bg-agro-800 w-16 h-16 rounded-2xl flex items-center justify-center mx-auto mb-6">
                                <HelpCircle className="w-8 h-8 text-agro-600" />
                            </div>
                            <h1 className="text-3xl font-black text-slate-900 dark:text-white mb-2">Support</h1>
                            <p className="text-slate-400 text-xs font-bold uppercase tracking-widest">24/7 Farmer Helpline</p>
                        </div>

                        <div className="bg-agro-600 rounded-[2.5rem] p-8 text-white shadow-xl shadow-agro-600/30">
                            <h3 className="font-black text-lg mb-4 uppercase tracking-tighter">Fast Connect</h3>
                            <div className="space-y-4">
                                <div className="flex items-center gap-3">
                                    <Mail className="w-5 h-5 opacity-60" />
                                    <span className="text-sm font-bold">help@agrodoctor.in</span>
                                </div>
                                <div className="flex items-center gap-3">
                                    <Phone className="w-5 h-5 opacity-60" />
                                    <span className="text-sm font-bold">+91 800-AGRO-DOC</span>
                                </div>
                                <div className="flex items-center gap-3">
                                    <MessageSquare className="w-5 h-5 opacity-60" />
                                    <span className="text-sm font-bold">Live AI Chat</span>
                                </div>
                            </div>
                        </div>
                    </motion.div>

                    <motion.div
                        initial={{ opacity: 0, y: 20 }}
                        animate={{ opacity: 1, y: 0 }}
                        transition={{ delay: 0.1 }}
                        className="md:col-span-2 bg-white dark:bg-agro-900 rounded-[3rem] p-10 shadow-premium border border-slate-100 dark:border-agro-800"
                    >
                        <h2 className="text-2xl font-black text-slate-900 dark:text-white mb-8">Send a Quick Message</h2>
                        <form className="space-y-6">
                            <div className="grid sm:grid-cols-2 gap-6">
                                <div className="space-y-2">
                                    <label className="text-[10px] font-black text-slate-400 uppercase tracking-widest ml-4">Full Name</label>
                                    <input type="text" placeholder="John Doe" className="w-full h-14 px-6 bg-slate-50 dark:bg-agro-950 border border-slate-200 dark:border-agro-800 rounded-2xl outline-none focus:border-agro-500 font-bold transition-all" />
                                </div>
                                <div className="space-y-2">
                                    <label className="text-[10px] font-black text-slate-400 uppercase tracking-widest ml-4">Farm Region</label>
                                    <input type="text" placeholder="Tamil Nadu" className="w-full h-14 px-6 bg-slate-50 dark:bg-agro-950 border border-slate-200 dark:border-agro-800 rounded-2xl outline-none focus:border-agro-500 font-bold transition-all" />
                                </div>
                            </div>

                            <div className="space-y-2">
                                <label className="text-[10px] font-black text-slate-400 uppercase tracking-widest ml-4">Issue Description</label>
                                <textarea rows={4} placeholder="Tell us what's happening with your crops..." className="w-full p-6 bg-slate-50 dark:bg-agro-950 border border-slate-200 dark:border-agro-800 rounded-2xl outline-none focus:border-agro-500 font-bold transition-all resize-none"></textarea>
                            </div>

                            <button type="button" className="w-full py-5 btn-premium flex items-center justify-center gap-3">
                                <span>Submit Inquiry</span>
                                <Send className="w-5 h-5" />
                            </button>
                        </form>
                    </motion.div>
                </div>
            </div>
        </main>
    );
}
