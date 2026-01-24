'use client';

import { useState } from 'react';
import { motion, AnimatePresence } from 'framer-motion';
import { Sprout, Mail, Lock, ArrowRight, ShieldCheck, User, Loader2, AlertCircle } from 'lucide-react';
import Link from 'next/link';
import { useRouter } from 'next/navigation';
import { useAuth } from '@/context/AuthContext';

export default function Auth() {
    const { login } = useAuth();
    const [mode, setMode] = useState<'login' | 'register'>('login');
    const [username, setUsername] = useState('');
    const [farmName, setFarmName] = useState('');
    const [password, setPassword] = useState('');
    const [loading, setLoading] = useState(false);
    const [error, setError] = useState('');
    const router = useRouter();

    const handleSubmit = (e: React.FormEvent) => {
        e.preventDefault();
        setLoading(true);
        setError('');

        // Mock Authentication / Registration
        setTimeout(() => {
            if (mode === 'login') {
                // Trim and lowercase for case-insensitive comparison
                const cleanUsername = username.trim().toLowerCase();
                const cleanPassword = password.trim();

                if (cleanUsername === 'admin' && cleanPassword === 'agro123') {
                    login(username.trim());
                } else {
                    setError('Invalid credentials. Use admin / agro123 to login.');
                    setLoading(false);
                }
            } else {
                // Mock Register
                if (username.trim().length < 3 || farmName.trim().length < 3) {
                    setError('Please enter a valid username and farm name (min 3 characters).');
                    setLoading(false);
                } else {
                    login(username.trim());
                }
            }
        }, 1500);
    };

    return (
        <main className="min-h-screen flex flex-col md:flex-row overflow-hidden font-sans">
            {/* Left Side: Branding / Visual */}
            <div className="hidden md:flex md:w-1/2 premium-gradient p-20 flex-col justify-between relative overflow-hidden">
                <div className="relative z-10">
                    <div className="flex items-center gap-3 mb-12">
                        <div className="bg-white/20 backdrop-blur-md p-3 rounded-2xl">
                            <Sprout className="text-white w-8 h-8" />
                        </div>
                        <span className="text-3xl font-black tracking-tight text-white uppercase">Agro Doctor</span>
                    </div>

                    <motion.h2
                        initial={{ opacity: 0, x: -30 }}
                        animate={{ opacity: 1, x: 0 }}
                        transition={{ delay: 0.2 }}
                        className="text-6xl font-black text-white leading-tight mb-8"
                    >
                        Empowering <br />
                        India's <br />
                        <span className="text-agro-300">Farmers.</span>
                    </motion.h2>
                    <p className="text-xl text-white/80 font-medium max-w-sm leading-relaxed">
                        Join 50,000+ farmers using AI to protect their crops and increase their yield.
                    </p>
                </div>

                <div className="relative z-10 flex items-center gap-8">
                    <div>
                        <div className="text-2xl font-black text-white">99%</div>
                        <div className="text-[10px] font-bold text-white/50 uppercase tracking-widest">Accuracy</div>
                    </div>
                    <div className="w-px h-10 bg-white/20"></div>
                    <div>
                        <div className="text-2xl font-black text-white">24/7</div>
                        <div className="text-[10px] font-bold text-white/50 uppercase tracking-widest">Expert Support</div>
                    </div>
                </div>

                {/* Decorative Pattern */}
                <div className="absolute top-0 right-0 w-full h-full opacity-10 pointer-events-none">
                    <svg width="100%" height="100%" viewBox="0 0 100 100" preserveAspectRatio="none">
                        <path d="M0 0 L100 100 M100 0 L0 100" stroke="white" strokeWidth="0.1" fill="none" />
                    </svg>
                </div>
            </div>

            {/* Right Side: Auth Form */}
            <div className="flex-1 flex flex-col justify-center items-center p-8 md:p-20 py-20">
                <motion.div
                    key={mode}
                    initial={{ opacity: 0, y: 30 }}
                    animate={{ opacity: 1, y: 0 }}
                    className="w-full max-w-md"
                >
                    <div className="md:hidden flex items-center gap-3 mb-10 justify-center">
                        <div className="bg-agro-600 p-2 rounded-xl">
                            <Sprout className="text-white w-6 h-6" />
                        </div>
                        <span className="text-xl font-black tracking-tight text-agro-900 dark:text-white uppercase text-center">Agro Doctor</span>
                    </div>

                    <div className="mb-12">
                        <h1 className="text-4xl font-black text-slate-900 dark:text-white mb-3">
                            {mode === 'login' ? 'Welcome Back' : 'Join Ecosystem'}
                        </h1>
                        <p className="text-slate-500 font-bold text-sm uppercase tracking-widest">
                            {mode === 'login' ? 'Access your farm dashboard' : 'Create your agricultural profile'}
                        </p>
                    </div>

                    <form onSubmit={handleSubmit} className="space-y-6">
                        <div className="space-y-2">
                            <label className="text-[10px] font-black text-slate-400 uppercase tracking-widest ml-4">Username</label>
                            <div className="relative group">
                                <User className="absolute left-6 top-1/2 -translate-y-1/2 w-5 h-5 text-slate-300 group-focus-within:text-agro-600 transition-colors" />
                                <input
                                    type="text"
                                    value={username}
                                    onChange={(e) => setUsername(e.target.value)}
                                    placeholder="Enter username"
                                    className="w-full h-16 pl-16 pr-6 bg-white dark:bg-agro-900 border border-slate-200 dark:border-agro-800 rounded-3xl outline-none focus:border-agro-500 shadow-sm font-bold text-slate-900 dark:text-white transition-all"
                                    required
                                />
                            </div>
                        </div>

                        {mode === 'register' && (
                            <motion.div initial={{ opacity: 0, height: 0 }} animate={{ opacity: 1, height: 'auto' }} className="space-y-2">
                                <label className="text-[10px] font-black text-slate-400 uppercase tracking-widest ml-4">Farm Name</label>
                                <div className="relative group">
                                    <ShieldCheck className="absolute left-6 top-1/2 -translate-y-1/2 w-5 h-5 text-slate-300 group-focus-within:text-agro-600 transition-colors" />
                                    <input
                                        type="text"
                                        value={farmName}
                                        onChange={(e) => setFarmName(e.target.value)}
                                        placeholder="e.g. Green Valley Farm"
                                        className="w-full h-16 pl-16 pr-6 bg-white dark:bg-agro-900 border border-slate-200 dark:border-agro-800 rounded-3xl outline-none focus:border-agro-500 shadow-sm font-bold text-slate-900 dark:text-white transition-all"
                                        required
                                    />
                                </div>
                            </motion.div>
                        )}

                        <div className="space-y-2">
                            <label className="text-[10px] font-black text-slate-400 uppercase tracking-widest ml-4">Password</label>
                            <div className="relative group">
                                <Lock className="absolute left-6 top-1/2 -translate-y-1/2 w-5 h-5 text-slate-300 group-focus-within:text-agro-600 transition-colors" />
                                <input
                                    type="password"
                                    value={password}
                                    onChange={(e) => setPassword(e.target.value)}
                                    placeholder="••••••••"
                                    className="w-full h-16 pl-16 pr-6 bg-white dark:bg-agro-900 border border-slate-200 dark:border-agro-800 rounded-3xl outline-none focus:border-agro-500 shadow-sm font-bold text-slate-900 dark:text-white transition-all"
                                    required
                                />
                            </div>
                        </div>

                        {error && (
                            <motion.div
                                initial={{ opacity: 0, scale: 0.95 }}
                                animate={{ opacity: 1, scale: 1 }}
                                className="p-4 bg-red-50 text-red-600 rounded-2xl text-xs font-black uppercase tracking-widest flex items-center gap-3 border border-red-100"
                            >
                                <AlertCircle className="w-5 h-5" />
                                {error}
                            </motion.div>
                        )}

                        <button
                            type="submit"
                            disabled={loading}
                            className="w-full py-5 btn-premium text-sm font-black uppercase tracking-[0.2em] flex items-center justify-center gap-3 disabled:opacity-50"
                        >
                            {loading ? (
                                <Loader2 className="w-6 h-6 animate-spin" />
                            ) : (
                                <>
                                    <span>{mode === 'login' ? 'Sign In' : 'Initialize Account'}</span>
                                    <ArrowRight className="w-5 h-5" />
                                </>
                            )}
                        </button>
                    </form>

                    <p className="mt-12 text-center text-slate-400 font-bold text-xs uppercase tracking-widest">
                        {mode === 'login' ? "Don't have an account?" : "Already have an account?"}{' '}
                        <button
                            onClick={() => setMode(mode === 'login' ? 'register' : 'login')}
                            className="text-agro-600 hover:underline font-black ml-1 uppercase"
                        >
                            {mode === 'login' ? 'Register Farm' : 'Login Dashboard'}
                        </button>
                    </p>
                </motion.div>

                <div className="mt-auto pt-10 flex items-center gap-4 opacity-30">
                    <ShieldCheck className="w-4 h-4" />
                    <span className="text-[10px] font-black uppercase tracking-[0.3em]">Encrypted Banking-Grade Security</span>
                </div>
            </div>
        </main>
    );
}
