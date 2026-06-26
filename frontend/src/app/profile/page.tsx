'use client';

import { useState, useEffect } from 'react';
import { motion, AnimatePresence } from 'framer-motion';
import { User, Phone, MapPin, Layers, Award, Calendar, RefreshCw, BarChart2, ShieldCheck, Heart, Leaf, FileText, Check, Loader2 } from 'lucide-react';
import Navbar from '@/components/Navbar';
import axios from 'axios';
import { useAuth } from '@/context/AuthContext';

interface HistoryItem {
    id: number;
    crop: string;
    scientific_name: string;
    confidence: string;
    health_score: number;
    severity: string;
    leaf_quality: string;
    spots_count: number;
    recovery_score: number;
    detection_time: string;
    disease: string;
    cause: string;
    organic_remedy: string;
    chemical_remedy: string;
    prevention: string;
    heatmap: string;
}

interface AnalyticsData {
    healthy_count: number;
    diseased_count: number;
    crop_distribution: { name: string; value: number }[];
    severity_distribution: { name: string; value: number }[];
    scans_trend: { month: string; scans: number }[];
    total_scans: number;
}

export default function Profile() {
    const { token, user, refreshProfile } = useAuth();
    const [history, setHistory] = useState<HistoryItem[]>([]);
    const [analytics, setAnalytics] = useState<AnalyticsData | null>(null);
    
    // Profile edit states
    const [name, setName] = useState('');
    const [phone, setPhone] = useState('');
    const [address, setAddress] = useState('');
    const [farmSize, setFarmSize] = useState('');
    const [state, setState] = useState('');
    const [district, setDistrict] = useState('');
    const [village, setVillage] = useState('');
    const [cropTypes, setCropTypes] = useState('');
    
    const [loading, setLoading] = useState(true);
    const [saving, setSaving] = useState(false);
    const [saveStatus, setSaveStatus] = useState('');
    const [activeTab, setActiveTab] = useState<'details' | 'history' | 'analytics'>('details');

    const loadData = async () => {
        if (!token) return;
        setLoading(true);
        try {
            // Fetch User Details
            const profileRes = await axios.get('http://localhost:8000/api/auth/profile', {
                headers: { Authorization: `Bearer ${token}` }
            });
            const u = profileRes.data;
            setName(u.name || '');
            setPhone(u.phone || '');
            setAddress(u.address || '');
            setFarmSize(u.farm_size || '');
            setState(u.state || '');
            setDistrict(u.district || '');
            setVillage(u.village || '');
            setCropTypes(u.crop_types || '');

            // Fetch History
            const historyRes = await axios.get('http://localhost:8000/api/history', {
                headers: { Authorization: `Bearer ${token}` }
            });
            setHistory(historyRes.data);

            // Fetch Analytics
            const analyticsRes = await axios.get('http://localhost:8000/api/analytics', {
                headers: { Authorization: `Bearer ${token}` }
            });
            setAnalytics(analyticsRes.data);
        } catch (err) {
            console.error("Failed to load profile details", err);
        } finally {
            setLoading(false);
        }
    };

    useEffect(() => {
        loadData();
    }, [token]);

    const handleSave = async (e: React.FormEvent) => {
        e.preventDefault();
        setSaving(true);
        setSaveStatus('');
        try {
            const formData = new FormData();
            formData.append('name', name);
            formData.append('phone', phone);
            formData.append('address', address);
            formData.append('farm_size', farmSize);
            formData.append('state', state);
            formData.append('district', district);
            formData.append('village', village);
            formData.append('crop_types', cropTypes);

            await axios.put('http://localhost:8000/api/auth/profile', formData, {
                headers: { Authorization: `Bearer ${token}` }
            });
            await refreshProfile();
            setSaveStatus('Profile updated successfully!');
            setTimeout(() => setSaveStatus(''), 3000);
        } catch (err) {
            setSaveStatus('Error saving profile.');
        } finally {
            setSaving(false);
        }
    };

    if (loading) {
        return (
            <main className="min-h-screen flex items-center justify-center">
                <div className="text-center">
                    <Loader2 className="w-12 h-12 animate-spin text-agro-600 mx-auto mb-4" />
                    <p className="text-slate-400 font-bold uppercase tracking-widest text-xs">Loading Profile Dashboard...</p>
                </div>
            </main>
        );
    }

    // Colors list for crop distributions charts
    const chartColors = ['#10b981', '#3b82f6', '#f59e0b', '#ec4899', '#8b5cf6'];

    return (
        <main className="min-h-screen pt-40 pb-20 px-6 bg-slate-50/50 dark:bg-black/10">
            <Navbar />
            <div className="max-w-6xl mx-auto w-full">

                {/* Farmer Banner Card */}
                <div className="p-8 md:p-12 bg-gradient-to-r from-emerald-950 via-agro-900 to-teal-950 rounded-[3.5rem] text-white shadow-premium border border-white/10 relative overflow-hidden mb-10">
                    <div className="relative z-10 grid md:grid-cols-2 gap-8 items-center">
                        <div className="space-y-4">
                            <div className="px-4 py-1.5 rounded-full bg-white/10 text-agro-300 w-fit text-[10px] font-black uppercase tracking-widest border border-white/10">
                                {user?.role} Profile Dashboard
                            </div>
                            <h1 className="text-4xl md:text-5xl font-black">{name || user?.name}</h1>
                            <div className="flex flex-wrap gap-4 text-xs font-medium text-white/70">
                                <span className="flex items-center gap-1"><MapPin className="w-4 h-4" /> {village ? `${village}, ${state}` : 'Location unconfigured'}</span>
                                <span className="flex items-center gap-1"><Layers className="w-4 h-4" /> {farmSize || 'Farm size unspecified'}</span>
                            </div>
                        </div>
                        <div className="flex md:justify-end gap-6 text-center">
                            <div className="p-4 bg-white/5 rounded-2xl border border-white/10 min-w-28">
                                <div className="text-[9px] font-black text-white/50 uppercase tracking-wider">Total Scans</div>
                                <div className="text-3xl font-black text-agro-400 mt-1">{history.length}</div>
                            </div>
                            <div className="p-4 bg-white/5 rounded-2xl border border-white/10 min-w-28">
                                <div className="text-[9px] font-black text-white/50 uppercase tracking-wider">Health Ratio</div>
                                <div className="text-3xl font-black text-emerald-400 mt-1">
                                    {analytics ? `${Math.round((analytics.healthy_count / (analytics.total_scans || 1)) * 100)}%` : '0%'}
                                </div>
                            </div>
                        </div>
                    </div>
                </div>

                {/* Tab Control */}
                <div className="flex border-b border-slate-200 dark:border-agro-800 mb-8 overflow-x-auto">
                    {[
                        { tab: 'details', label: 'Farmer Profile' },
                        { tab: 'history', label: 'Crop Scan Logs' },
                        { tab: 'analytics', label: 'Ecosystem Analytics' }
                    ].map((t) => (
                        <button
                            key={t.tab}
                            onClick={() => setActiveTab(t.tab as any)}
                            className={`pb-4 px-6 text-sm font-black uppercase tracking-wider transition-all border-b-2 shrink-0 ${activeTab === t.tab ? 'border-agro-600 text-agro-600 dark:text-white' : 'border-transparent text-slate-400 hover:text-slate-900'}`}
                        >
                            {t.label}
                        </button>
                    ))}
                </div>

                {/* Tab Contents */}
                <AnimatePresence mode="wait">
                    {activeTab === 'details' && (
                        <motion.form
                            key="details"
                            initial={{ opacity: 0, y: 15 }}
                            animate={{ opacity: 1, y: 0 }}
                            exit={{ opacity: 0 }}
                            onSubmit={handleSave}
                            className="bg-white dark:bg-agro-900/50 p-8 rounded-[3rem] shadow-premium border border-slate-100 dark:border-agro-800 space-y-6"
                        >
                            <h2 className="text-2xl font-black text-slate-900 dark:text-white mb-6">Edit Agriculture Profile</h2>

                            <div className="grid md:grid-cols-2 gap-6">
                                <div className="space-y-1">
                                    <label className="text-[9px] font-black text-slate-400 uppercase tracking-widest ml-2">Farmer Name</label>
                                    <input
                                        type="text"
                                        value={name}
                                        onChange={(e) => setName(e.target.value)}
                                        className="w-full h-12 px-4 bg-slate-50 dark:bg-slate-900 border border-slate-200 dark:border-slate-800 rounded-xl outline-none focus:border-agro-500 text-sm font-bold text-slate-900 dark:text-white"
                                        required
                                    />
                                </div>
                                <div className="space-y-1">
                                    <label className="text-[9px] font-black text-slate-400 uppercase tracking-widest ml-2">Phone Contact</label>
                                    <input
                                        type="tel"
                                        value={phone}
                                        onChange={(e) => setPhone(e.target.value)}
                                        className="w-full h-12 px-4 bg-slate-50 dark:bg-slate-900 border border-slate-200 dark:border-slate-800 rounded-xl outline-none focus:border-agro-500 text-sm font-bold text-slate-900 dark:text-white"
                                    />
                                </div>
                                <div className="space-y-1">
                                    <label className="text-[9px] font-black text-slate-400 uppercase tracking-widest ml-2">Farm Size (Acres / Hectares)</label>
                                    <input
                                        type="text"
                                        value={farmSize}
                                        onChange={(e) => setFarmSize(e.target.value)}
                                        className="w-full h-12 px-4 bg-slate-50 dark:bg-slate-900 border border-slate-200 dark:border-slate-800 rounded-xl outline-none focus:border-agro-500 text-sm font-bold text-slate-900 dark:text-white"
                                        placeholder="e.g. 8 Acres"
                                    />
                                </div>
                                <div className="space-y-1">
                                    <label className="text-[9px] font-black text-slate-400 uppercase tracking-widest ml-2">Cultivated Crops</label>
                                    <input
                                        type="text"
                                        value={cropTypes}
                                        onChange={(e) => setCropTypes(e.target.value)}
                                        className="w-full h-12 px-4 bg-slate-50 dark:bg-slate-900 border border-slate-200 dark:border-slate-800 rounded-xl outline-none focus:border-agro-500 text-sm font-bold text-slate-900 dark:text-white"
                                        placeholder="e.g. Tomato, Rice, Apple"
                                    />
                                </div>
                            </div>

                            <div className="border-t border-slate-100 dark:border-agro-800 pt-6 space-y-4">
                                <h3 className="text-xs font-black text-agro-600 uppercase tracking-wider">Geographical Coordinates</h3>
                                <div className="grid grid-cols-3 gap-4">
                                    <div className="space-y-1">
                                        <label className="text-[8px] font-black text-slate-400 uppercase tracking-widest ml-2">State</label>
                                        <input
                                            type="text"
                                            value={state}
                                            onChange={(e) => setState(e.target.value)}
                                            className="w-full h-12 px-4 bg-slate-50 dark:bg-slate-900 border border-slate-200 dark:border-slate-800 rounded-xl outline-none focus:border-agro-500 text-sm font-bold text-slate-900 dark:text-white"
                                        />
                                    </div>
                                    <div className="space-y-1">
                                        <label className="text-[8px] font-black text-slate-400 uppercase tracking-widest ml-2">District</label>
                                        <input
                                            type="text"
                                            value={district}
                                            onChange={(e) => setDistrict(e.target.value)}
                                            className="w-full h-12 px-4 bg-slate-50 dark:bg-slate-900 border border-slate-200 dark:border-slate-800 rounded-xl outline-none focus:border-agro-500 text-sm font-bold text-slate-900 dark:text-white"
                                        />
                                    </div>
                                    <div className="space-y-1">
                                        <label className="text-[8px] font-black text-slate-400 uppercase tracking-widest ml-2">Village</label>
                                        <input
                                            type="text"
                                            value={village}
                                            onChange={(e) => setVillage(e.target.value)}
                                            className="w-full h-12 px-4 bg-slate-50 dark:bg-slate-900 border border-slate-200 dark:border-slate-800 rounded-xl outline-none focus:border-agro-500 text-sm font-bold text-slate-900 dark:text-white"
                                        />
                                    </div>
                                </div>
                                <div className="space-y-1">
                                    <label className="text-[9px] font-black text-slate-400 uppercase tracking-widest ml-2">Full Address</label>
                                    <textarea
                                        value={address}
                                        onChange={(e) => setAddress(e.target.value)}
                                        className="w-full h-24 p-4 bg-slate-50 dark:bg-slate-900 border border-slate-200 dark:border-slate-800 rounded-2xl outline-none focus:border-agro-500 text-sm font-bold text-slate-900 dark:text-white resize-none"
                                    />
                                </div>
                            </div>

                            <div className="flex items-center gap-4 border-t border-slate-100 dark:border-agro-800 pt-6">
                                <button
                                    type="submit"
                                    disabled={saving}
                                    className="px-8 py-4 bg-agro-600 hover:bg-agro-700 text-white rounded-xl text-xs font-black uppercase tracking-wider flex items-center gap-2 disabled:opacity-50 transition-colors"
                                >
                                    {saving && <Loader2 className="w-4 h-4 animate-spin" />}
                                    Save Changes
                                </button>
                                {saveStatus && (
                                    <span className="text-xs font-black text-agro-600 uppercase tracking-widest">{saveStatus}</span>
                                )}
                            </div>
                        </motion.form>
                    )}

                    {activeTab === 'history' && (
                        <motion.div
                            key="history"
                            initial={{ opacity: 0, y: 15 }}
                            animate={{ opacity: 1, y: 0 }}
                            exit={{ opacity: 0 }}
                            className="space-y-4"
                        >
                            {history.length === 0 ? (
                                <div className="p-16 bg-white dark:bg-agro-900/30 rounded-[3rem] text-center border border-slate-100 dark:border-agro-800">
                                    <Leaf className="w-16 h-16 text-slate-200 dark:text-agro-800 mx-auto mb-6" />
                                    <h3 className="text-lg font-black text-slate-400 uppercase tracking-widest">No diagnostics logged yet</h3>
                                    <p className="text-slate-400 text-sm mt-2">Scan a leaf under the AI Doctor page to start saving records.</p>
                                </div>
                            ) : (
                                history.map((h) => (
                                    <div key={h.id} className="p-6 bg-white dark:bg-agro-900/40 rounded-[2.5rem] border border-slate-100 dark:border-agro-800 flex flex-col md:flex-row justify-between gap-6 items-start md:items-center">
                                        <div className="flex gap-4">
                                            {h.heatmap ? (
                                                <img src={h.heatmap} alt="Heatmap" className="w-16 h-16 rounded-xl object-cover border border-slate-100 dark:border-slate-800" />
                                            ) : (
                                                <div className="w-16 h-16 rounded-xl bg-agro-100 dark:bg-agro-800 flex items-center justify-center text-agro-600"><Leaf className="w-8 h-8" /></div>
                                            )}
                                            <div>
                                                <div className="flex items-center gap-2">
                                                    <h3 className="font-black text-lg text-slate-900 dark:text-white">{h.crop}</h3>
                                                    <span className="text-xs font-bold text-slate-400 italic">({h.scientific_name})</span>
                                                </div>
                                                <p className="text-xs font-black text-agro-600 uppercase tracking-wider mt-1">{h.disease}</p>
                                                <p className="text-[10px] font-bold text-slate-400 mt-2">Scanned on {h.detection_time}</p>
                                            </div>
                                        </div>
                                        <div className="flex flex-wrap gap-4 text-center">
                                            <div className="px-4 py-2 bg-slate-50 dark:bg-slate-900/60 rounded-xl">
                                                <div className="text-[8px] font-black text-slate-400 uppercase tracking-wider">Health</div>
                                                <div className="text-sm font-black text-agro-600">{h.health_score}%</div>
                                            </div>
                                            <div className="px-4 py-2 bg-slate-50 dark:bg-slate-900/60 rounded-xl">
                                                <div className="text-[8px] font-black text-slate-400 uppercase tracking-wider">Severity</div>
                                                <div className={`text-sm font-black ${h.severity === 'Healthy' ? 'text-green-600' : 'text-red-500'}`}>{h.severity}</div>
                                            </div>
                                            <div className="px-4 py-2 bg-slate-50 dark:bg-slate-900/60 rounded-xl">
                                                <div className="text-[8px] font-black text-slate-400 uppercase tracking-wider">Recovery</div>
                                                <div className="text-sm font-black text-blue-600">{h.recovery_score}%</div>
                                            </div>
                                        </div>
                                    </div>
                                ))
                            )}
                        </motion.div>
                    )}

                    {activeTab === 'analytics' && analytics && (
                        <motion.div
                            key="analytics"
                            initial={{ opacity: 0, y: 15 }}
                            animate={{ opacity: 1, y: 0 }}
                            exit={{ opacity: 0 }}
                            className="grid md:grid-cols-2 gap-8"
                        >
                            {/* Chart 1: Crop Distribution (Custom SVG Bar Chart) */}
                            <div className="p-8 bg-white dark:bg-agro-900/40 rounded-[3rem] border border-slate-100 dark:border-agro-800 space-y-6">
                                <h3 className="text-sm font-black uppercase tracking-widest text-slate-400">Crop Scan distribution</h3>
                                <div className="space-y-4">
                                    {analytics.crop_distribution.map((item, idx) => {
                                        const pct = Math.round((item.value / analytics.total_scans) * 100);
                                        const color = chartColors[idx % chartColors.length];
                                        return (
                                            <div key={idx} className="space-y-1">
                                                <div className="flex justify-between text-xs font-bold">
                                                    <span className="text-slate-700 dark:text-white">{item.name}</span>
                                                    <span className="text-slate-400">{item.value} Scans ({pct}%)</span>
                                                </div>
                                                <div className="w-full bg-slate-100 dark:bg-slate-900 h-2.5 rounded-full overflow-hidden">
                                                    <motion.div
                                                        initial={{ width: 0 }}
                                                        animate={{ width: `${pct}%` }}
                                                        className="h-full rounded-full"
                                                        style={{ backgroundColor: color }}
                                                    />
                                                </div>
                                            </div>
                                        );
                                    })}
                                </div>
                            </div>

                            {/* Chart 2: Severity Distribution (Custom SVG Pie/Donut Chart) */}
                            <div className="p-8 bg-white dark:bg-agro-900/40 rounded-[3rem] border border-slate-100 dark:border-agro-800 flex flex-col justify-between">
                                <h3 className="text-sm font-black uppercase tracking-widest text-slate-400 mb-4">Severity Levels</h3>
                                <div className="flex items-center gap-8">
                                    {/* Donut Chart SVG */}
                                    <div className="relative w-36 h-36 shrink-0">
                                        <svg viewBox="0 0 36 36" className="w-full h-full transform -rotate-90">
                                            {/* Base grey circle */}
                                            <circle cx="18" cy="18" r="15.915" fill="none" stroke="#e2e8f0" strokeWidth="3" />
                                            {/* Slice rings */}
                                            {(() => {
                                                let accumulatedPct = 0;
                                                return analytics.severity_distribution.map((item, idx) => {
                                                    const pct = (item.value / (analytics.total_scans || 1)) * 100;
                                                    if (pct === 0) return null;
                                                    const strokeDash = `${pct} ${100 - pct}`;
                                                    const strokeOffset = 100 - accumulatedPct;
                                                    accumulatedPct += pct;
                                                    const color = item.name === 'Healthy' ? '#10b981' : (item.name === 'Low' ? '#f59e0b' : '#ef4444');
                                                    return (
                                                        <circle
                                                            key={idx}
                                                            cx="18"
                                                            cy="18"
                                                            r="15.915"
                                                            fill="none"
                                                            stroke={color}
                                                            strokeWidth="3"
                                                            strokeDasharray={strokeDash}
                                                            strokeDashoffset={strokeOffset}
                                                        />
                                                    );
                                                });
                                            })()}
                                        </svg>
                                        <div className="absolute inset-0 flex flex-col items-center justify-center text-center">
                                            <span className="text-xl font-black text-slate-900 dark:text-white">{analytics.total_scans}</span>
                                            <span className="text-[8px] font-black text-slate-400 uppercase tracking-wider">Total</span>
                                        </div>
                                    </div>

                                    {/* Labels Grid */}
                                    <div className="space-y-3 font-bold text-xs">
                                        {analytics.severity_distribution.map((item, idx) => {
                                            const color = item.name === 'Healthy' ? 'bg-emerald-500' : (item.name === 'Low' ? 'bg-amber-500' : 'bg-rose-500');
                                            return (
                                                <div key={idx} className="flex items-center gap-2">
                                                    <div className={`w-3 h-3 rounded-full ${color}`}></div>
                                                    <span className="text-slate-700 dark:text-white uppercase text-[10px] tracking-wider">{item.name}: {item.value}</span>
                                                </div>
                                            );
                                        })}
                                    </div>
                                </div>
                            </div>

                            {/* Chart 3: Scan Timeline Scans trend (Custom SVG Line chart) */}
                            <div className="p-8 bg-white dark:bg-agro-900/40 rounded-[3rem] border border-slate-100 dark:border-agro-800 md:col-span-2 space-y-6">
                                <h3 className="text-sm font-black uppercase tracking-widest text-slate-400">Monthly Scan Trends</h3>
                                <div className="h-48 w-full relative">
                                    {/* Custom SVG Line drawing */}
                                    <svg className="w-full h-full" viewBox="0 0 600 150">
                                        {/* Grid lines */}
                                        <line x1="20" y1="120" x2="580" y2="120" stroke="#e2e8f0" strokeWidth="1" strokeDasharray="4 4" />
                                        <line x1="20" y1="70" x2="580" y2="70" stroke="#e2e8f0" strokeWidth="1" strokeDasharray="4 4" />
                                        <line x1="20" y1="20" x2="580" y2="20" stroke="#e2e8f0" strokeWidth="1" strokeDasharray="4 4" />

                                        {/* Draw Line */}
                                        {(() => {
                                            const points = analytics.scans_trend.map((item, idx) => {
                                                const x = 30 + (idx * 50);
                                                // map values (0 to 30) to Y space (120 down to 20)
                                                const y = 120 - (item.scans * 3.5);
                                                return { x, y, month: item.month };
                                            });

                                            const linePath = points.map((p, idx) => `${idx === 0 ? 'M' : 'L'} ${p.x} ${p.y}`).join(' ');
                                            const areaPath = `${linePath} L ${points[points.length-1].x} 120 L ${points[0].x} 120 Z`;

                                            return (
                                                <>
                                                    {/* Gradient Area Fill */}
                                                    <path d={areaPath} fill="url(#areaGrad)" opacity="0.15" />
                                                    <defs>
                                                        <linearGradient id="areaGrad" x1="0" y1="0" x2="0" y2="1">
                                                            <stop offset="0%" stopColor="#10b981" />
                                                            <stop offset="100%" stopColor="#10b981" stopOpacity="0" />
                                                        </linearGradient>
                                                    </defs>

                                                    {/* Drawing the line */}
                                                    <path d={linePath} fill="none" stroke="#10b981" strokeWidth="3" />

                                                    {/* Data points */}
                                                    {points.map((p, idx) => (
                                                        <g key={idx}>
                                                            <circle cx={p.x} cy={p.y} r="5" fill="#10b981" stroke="white" strokeWidth="1.5" />
                                                            <text x={p.x} y="140" fontSize="9" fontWeight="bold" fill="#94a3b8" textAnchor="middle">{p.month}</text>
                                                            {analytics.scans_trend[idx].scans > 0 && (
                                                                <text x={p.x} y={p.y-10} fontSize="9" fontWeight="black" fill="#10b981" textAnchor="middle">{analytics.scans_trend[idx].scans}</text>
                                                            )}
                                                        </g>
                                                    ))}
                                                </>
                                            );
                                        })()}
                                    </svg>
                                </div>
                            </div>
                        </motion.div>
                    )}
                </AnimatePresence>
            </div>
        </main>
    );
}
