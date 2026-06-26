'use client';

import { useState } from 'react';
import { motion, AnimatePresence } from 'framer-motion';
import { Sprout, Mail, Lock, ArrowRight, ShieldCheck, User, Phone, MapPin, Layers, Award, Loader2, AlertCircle } from 'lucide-react';
import { useRouter } from 'next/navigation';
import { useAuth } from '@/context/AuthContext';
import axios from 'axios';

export default function Auth() {
    const { login } = useAuth();
    const [mode, setMode] = useState<'login' | 'register'>('login');
    
    // Login states
    const [loginEmail, setLoginEmail] = useState('');
    const [loginPassword, setLoginPassword] = useState('');
    
    // Register states
    const [name, setName] = useState('');
    const [email, setEmail] = useState('');
    const [password, setPassword] = useState('');
    const [phone, setPhone] = useState('');
    const [address, setAddress] = useState('');
    const [farmSize, setFarmSize] = useState('');
    const [state, setState] = useState('');
    const [district, setDistrict] = useState('');
    const [village, setVillage] = useState('');
    const [cropTypes, setCropTypes] = useState('');
    const [role, setRole] = useState('Farmer'); // Farmer, Expert, Admin

    const [loading, setLoading] = useState(false);
    const [error, setError] = useState('');
    const router = useRouter();

    const handleSubmit = async (e: React.FormEvent) => {
        e.preventDefault();
        setLoading(true);
        setError('');

        try {
            if (mode === 'login') {
                // Hitting FastAPI OAuth2 Login
                const params = new URLSearchParams();
                params.append('username', loginEmail.trim());
                params.append('password', loginPassword);

                const response = await axios.post('http://localhost:8000/api/auth/login', params, {
                    headers: { 'Content-Type': 'application/x-www-form-urlencoded' }
                });

                const { access_token, user } = response.data;
                login(access_token, user);
            } else {
                // Registering with all Farmer Profile parameters
                const formData = new FormData();
                formData.append('name', name.trim());
                formData.append('email', email.trim());
                formData.append('password', password);
                formData.append('phone', phone.trim());
                formData.append('address', address.trim());
                formData.append('farm_size', farmSize.trim());
                formData.append('state', state.trim());
                formData.append('district', district.trim());
                formData.append('village', village.trim());
                formData.append('crop_types', cropTypes.trim());
                formData.append('role', role);

                const response = await axios.post('http://localhost:8000/api/auth/register', formData);
                const { access_token, user } = response.data;
                login(access_token, user);
            }
        } catch (err: any) {
            console.error(err);
            if (err.response && err.response.data && err.response.data.detail) {
                setError(err.response.data.detail);
            } else {
                setError('Authentication failed. Please ensure the python server is online.');
            }
        } finally {
            setLoading(false);
        }
    };

    return (
        <main className="min-h-screen flex flex-col md:flex-row overflow-hidden font-sans">
            {/* Left Side: Branding / Visual */}
            <div className="hidden md:flex md:w-1/2 premium-gradient p-20 flex-col justify-between relative overflow-hidden bg-gradient-to-br from-emerald-900 via-green-800 to-teal-950">
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
                        Join 50,000+ farmers using offline AI to protect crops and increase yields.
                    </p>
                </div>

                <div className="relative z-10 flex items-center gap-8">
                    <div>
                        <div className="text-2xl font-black text-white">99%</div>
                        <div className="text-[10px] font-bold text-white/50 uppercase tracking-widest">Accuracy</div>
                    </div>
                    <div className="w-px h-10 bg-white/20"></div>
                    <div>
                        <div className="text-2xl font-black text-white">100%</div>
                        <div className="text-[10px] font-bold text-white/50 uppercase tracking-widest">Offline RAG</div>
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
            <div className="flex-1 flex flex-col justify-center items-center p-6 md:p-16 py-12 overflow-y-auto max-h-screen">
                <motion.div
                    key={mode}
                    initial={{ opacity: 0, y: 30 }}
                    animate={{ opacity: 1, y: 0 }}
                    className="w-full max-w-lg"
                >
                    <div className="md:hidden flex items-center gap-3 mb-10 justify-center">
                        <div className="bg-agro-600 p-2 rounded-xl">
                            <Sprout className="text-white w-6 h-6" />
                        </div>
                        <span className="text-xl font-black tracking-tight text-agro-900 dark:text-white uppercase text-center">Agro Doctor</span>
                    </div>

                    <div className="mb-8 text-center md:text-left">
                        <h1 className="text-4xl font-black text-slate-900 dark:text-white mb-2">
                            {mode === 'login' ? 'Welcome Back' : 'Join Ecosystem'}
                        </h1>
                        <p className="text-slate-500 font-bold text-xs uppercase tracking-widest">
                            {mode === 'login' ? 'Access your farm dashboard (Demo: admin / agro123)' : 'Create your agricultural profile'}
                        </p>
                    </div>

                    <form onSubmit={handleSubmit} className="space-y-4">
                        {mode === 'login' ? (
                            <>
                                <div className="space-y-1">
                                    <label className="text-[10px] font-black text-slate-400 uppercase tracking-widest ml-4">Email / Username</label>
                                    <div className="relative group">
                                        <Mail className="absolute left-6 top-1/2 -translate-y-1/2 w-5 h-5 text-slate-300 group-focus-within:text-agro-600 transition-colors" />
                                        <input
                                            type="text"
                                            value={loginEmail}
                                            onChange={(e) => setLoginEmail(e.target.value)}
                                            placeholder="Enter email or 'admin'"
                                            className="w-full h-14 pl-16 pr-6 bg-white dark:bg-slate-900 border border-slate-200 dark:border-slate-800 rounded-2xl outline-none focus:border-agro-500 shadow-sm font-bold text-slate-900 dark:text-white transition-all text-sm"
                                            required
                                        />
                                    </div>
                                </div>
                                <div className="space-y-1">
                                    <label className="text-[10px] font-black text-slate-400 uppercase tracking-widest ml-4">Password</label>
                                    <div className="relative group">
                                        <Lock className="absolute left-6 top-1/2 -translate-y-1/2 w-5 h-5 text-slate-300 group-focus-within:text-agro-600 transition-colors" />
                                        <input
                                            type="password"
                                            value={loginPassword}
                                            onChange={(e) => setLoginPassword(e.target.value)}
                                            placeholder="••••••••"
                                            className="w-full h-14 pl-16 pr-6 bg-white dark:bg-slate-900 border border-slate-200 dark:border-slate-800 rounded-2xl outline-none focus:border-agro-500 shadow-sm font-bold text-slate-900 dark:text-white transition-all text-sm"
                                            required
                                        />
                                    </div>
                                </div>
                            </>
                        ) : (
                            <div className="space-y-4 max-h-[60vh] overflow-y-auto pr-2 no-scrollbar">
                                {/* Section 1: Basic Info */}
                                <div className="border-b pb-4 border-slate-100 dark:border-slate-800">
                                    <h3 className="text-xs font-bold text-agro-600 uppercase tracking-wider mb-2">1. Credentials</h3>
                                    <div className="grid grid-cols-1 gap-3">
                                        <input
                                            type="text"
                                            placeholder="Full Name"
                                            value={name}
                                            onChange={(e) => setName(e.target.value)}
                                            className="w-full h-12 px-4 bg-white dark:bg-slate-900 border border-slate-200 dark:border-slate-800 rounded-xl outline-none focus:border-agro-500 text-sm font-bold text-slate-900 dark:text-white"
                                            required
                                        />
                                        <input
                                            type="email"
                                            placeholder="Email Address"
                                            value={email}
                                            onChange={(e) => setEmail(e.target.value)}
                                            className="w-full h-12 px-4 bg-white dark:bg-slate-900 border border-slate-200 dark:border-slate-800 rounded-xl outline-none focus:border-agro-500 text-sm font-bold text-slate-900 dark:text-white"
                                            required
                                        />
                                        <input
                                            type="password"
                                            placeholder="Password (min 6 characters)"
                                            value={password}
                                            onChange={(e) => setPassword(e.target.value)}
                                            className="w-full h-12 px-4 bg-white dark:bg-slate-900 border border-slate-200 dark:border-slate-800 rounded-xl outline-none focus:border-agro-500 text-sm font-bold text-slate-900 dark:text-white"
                                            required
                                        />
                                    </div>
                                </div>

                                {/* Section 2: Farm Specifics */}
                                <div className="border-b pb-4 border-slate-100 dark:border-slate-800">
                                    <h3 className="text-xs font-bold text-agro-600 uppercase tracking-wider mb-2">2. Farm Details & Role</h3>
                                    <div className="grid grid-cols-2 gap-3">
                                        <input
                                            type="tel"
                                            placeholder="Phone Number"
                                            value={phone}
                                            onChange={(e) => setPhone(e.target.value)}
                                            className="w-full h-12 px-4 bg-white dark:bg-slate-900 border border-slate-200 dark:border-slate-800 rounded-xl outline-none focus:border-agro-500 text-sm font-bold text-slate-900 dark:text-white"
                                        />
                                        <input
                                            type="text"
                                            placeholder="Farm Size (e.g. 5 Acres)"
                                            value={farmSize}
                                            onChange={(e) => setFarmSize(e.target.value)}
                                            className="w-full h-12 px-4 bg-white dark:bg-slate-900 border border-slate-200 dark:border-slate-800 rounded-xl outline-none focus:border-agro-500 text-sm font-bold text-slate-900 dark:text-white"
                                        />
                                        <input
                                            type="text"
                                            placeholder="Main Crops (e.g. Tomato, Rice)"
                                            value={cropTypes}
                                            onChange={(e) => setCropTypes(e.target.value)}
                                            className="w-full h-12 px-4 col-span-2 bg-white dark:bg-slate-900 border border-slate-200 dark:border-slate-800 rounded-xl outline-none focus:border-agro-500 text-sm font-bold text-slate-900 dark:text-white"
                                        />
                                        <div className="col-span-2">
                                            <label className="text-[9px] font-black text-slate-400 uppercase tracking-widest mb-1 block">Account Role</label>
                                            <select
                                                value={role}
                                                onChange={(e) => setRole(e.target.value)}
                                                className="w-full h-12 px-4 bg-white dark:bg-slate-900 border border-slate-200 dark:border-slate-800 rounded-xl outline-none focus:border-agro-500 text-sm font-bold text-slate-900 dark:text-white"
                                            >
                                                <option value="Farmer">Farmer</option>
                                                <option value="Agriculture Expert">Agriculture Expert</option>
                                                <option value="Admin">System Administrator</option>
                                            </select>
                                        </div>
                                    </div>
                                </div>

                                {/* Section 3: Geographical Coordinates */}
                                <div>
                                    <h3 className="text-xs font-bold text-agro-600 uppercase tracking-wider mb-2">3. Location Info</h3>
                                    <div className="grid grid-cols-3 gap-3 mb-2">
                                        <input
                                            type="text"
                                            placeholder="State"
                                            value={state}
                                            onChange={(e) => setState(e.target.value)}
                                            className="w-full h-12 px-4 bg-white dark:bg-slate-900 border border-slate-200 dark:border-slate-800 rounded-xl outline-none focus:border-agro-500 text-sm font-bold text-slate-900 dark:text-white"
                                        />
                                        <input
                                            type="text"
                                            placeholder="District"
                                            value={district}
                                            onChange={(e) => setDistrict(e.target.value)}
                                            className="w-full h-12 px-4 bg-white dark:bg-slate-900 border border-slate-200 dark:border-slate-800 rounded-xl outline-none focus:border-agro-500 text-sm font-bold text-slate-900 dark:text-white"
                                        />
                                        <input
                                            type="text"
                                            placeholder="Village"
                                            value={village}
                                            onChange={(e) => setVillage(e.target.value)}
                                            className="w-full h-12 px-4 bg-white dark:bg-slate-900 border border-slate-200 dark:border-slate-800 rounded-xl outline-none focus:border-agro-500 text-sm font-bold text-slate-900 dark:text-white"
                                        />
                                    </div>
                                    <textarea
                                        placeholder="Full Farm Address Details"
                                        value={address}
                                        onChange={(e) => setAddress(e.target.value)}
                                        className="w-full h-20 p-3 bg-white dark:bg-slate-900 border border-slate-200 dark:border-slate-800 rounded-xl outline-none focus:border-agro-500 text-sm font-bold text-slate-900 dark:text-white resize-none"
                                    />
                                </div>
                            </div>
                        )}

                        {error && (
                            <motion.div
                                initial={{ opacity: 0, scale: 0.95 }}
                                animate={{ opacity: 1, scale: 1 }}
                                className="p-3 bg-red-50 text-red-600 rounded-xl text-[10px] font-black uppercase tracking-widest flex items-center gap-3 border border-red-100"
                            >
                                <AlertCircle className="w-5 h-5 flex-shrink-0" />
                                <span>{error}</span>
                            </motion.div>
                        )}

                        <button
                            type="submit"
                            disabled={loading}
                            className="w-full py-4 bg-agro-600 hover:bg-agro-700 text-white rounded-2xl text-xs font-black uppercase tracking-[0.2em] flex items-center justify-center gap-3 disabled:opacity-50 transition-colors shadow-lg shadow-agro-600/20"
                        >
                            {loading ? (
                                <Loader2 className="w-5 h-5 animate-spin" />
                            ) : (
                                <>
                                    <span>{mode === 'login' ? 'Sign In' : 'Initialize Account'}</span>
                                    <ArrowRight className="w-4 h-4" />
                                </>
                            )}
                        </button>
                    </form>

                    <p className="mt-8 text-center text-slate-400 font-bold text-xs uppercase tracking-widest">
                        {mode === 'login' ? "Don't have an account?" : "Already have an account?"}{' '}
                        <button
                            onClick={() => setMode(mode === 'login' ? 'register' : 'login')}
                            className="text-agro-600 hover:underline font-black ml-1 uppercase"
                        >
                            {mode === 'login' ? 'Create One' : 'Log In'}
                        </button>
                    </p>
                </motion.div>
            </div>
        </main>
    );
}
