'use client';

import { useState, useEffect } from 'react';
import { motion, AnimatePresence } from 'framer-motion';
import { ShieldCheck, Database, FileText, Activity, Layers, Upload, ArrowRight, Loader2, CheckCircle, AlertCircle, RefreshCw } from 'lucide-react';
import Navbar from '@/components/Navbar';
import axios from 'axios';
import { useAuth } from '@/context/AuthContext';

interface LogItem {
    id: number;
    user: string;
    action: string;
    details: string;
    time: string;
}

export default function Admin() {
    const { token, user } = useAuth();
    
    // Knowledge upload states
    const [title, setTitle] = useState('');
    const [content, setContent] = useState('');
    const [docType, setDocType] = useState('Manual');
    const [source, setSource] = useState('Government Circular');
    
    // DB backup/restore states
    const [backupMessage, setBackupMessage] = useState('');
    const [backupFile, setBackupFile] = useState('');
    const [restoreStatus, setRestoreStatus] = useState('');

    // Logs states
    const [logs, setLogs] = useState<LogItem[]>([]);
    
    const [activeTab, setActiveTab] = useState<'rag' | 'db' | 'logs'>('rag');
    const [loading, setLoading] = useState(false);
    const [submitting, setSubmitting] = useState(false);
    const [successMessage, setSuccessMessage] = useState('');

    const loadLogs = async () => {
        if (!token || user?.role !== 'Admin') return;
        setLoading(true);
        try {
            const res = await axios.get('http://localhost:8000/api/admin/logs', {
                headers: { Authorization: `Bearer ${token}` }
            });
            setLogs(res.data);
        } catch (err) {
            console.error("Failed to load audit logs", err);
        } finally {
            setLoading(false);
        }
    };

    useEffect(() => {
        if (activeTab === 'logs') {
            loadLogs();
        }
    }, [activeTab, token]);

    const handleUploadRAG = async (e: React.FormEvent) => {
        e.preventDefault();
        setSubmitting(true);
        setSuccessMessage('');
        
        try {
            const formData = new FormData();
            formData.append('title', title);
            formData.append('content', content);
            formData.append('document_type', docType);
            formData.append('source', source);

            await axios.post('http://localhost:8000/api/admin/upload-kb', formData, {
                headers: { Authorization: `Bearer ${token}` }
            });
            setSuccessMessage(`Document "${title}" has been added to the offline RAG vector index!`);
            setTitle('');
            setContent('');
            setTimeout(() => setSuccessMessage(''), 4000);
        } catch (err) {
            alert("RAG index update failed. Verify your administrative token.");
        } finally {
            setSubmitting(false);
        }
    };

    const handleBackup = async () => {
        setLoading(true);
        setBackupMessage('');
        try {
            const res = await axios.post('http://localhost:8000/api/admin/backup', {}, {
                headers: { Authorization: `Bearer ${token}` }
            });
            setBackupMessage(res.data.message);
        } catch (err) {
            setBackupMessage("Database backup failed.");
        } finally {
            setLoading(false);
        }
    };

    const handleRestore = async (e: React.FormEvent) => {
        e.preventDefault();
        if (!backupFile.trim()) return;
        setLoading(true);
        setRestoreStatus('');
        try {
            const formData = new FormData();
            formData.append('backup_name', backupFile);

            const res = await axios.post('http://localhost:8000/api/admin/restore', formData, {
                headers: { Authorization: `Bearer ${token}` }
            });
            setRestoreStatus(res.data.message);
            setBackupFile('');
        } catch (err: any) {
            if (err.response && err.response.data && err.response.data.detail) {
                setRestoreStatus(`Restore error: ${err.response.data.detail}`);
            } else {
                setRestoreStatus("Database restore failed.");
            }
        } finally {
            setLoading(false);
        }
    };

    if (user?.role !== 'Admin') {
        return (
            <main className="min-h-screen flex items-center justify-center p-6 text-center">
                <div className="max-w-md p-8 bg-white dark:bg-slate-900 rounded-[2rem] border shadow-xl">
                    <AlertCircle className="w-16 h-16 text-rose-500 mx-auto mb-6" />
                    <h2 className="text-xl font-black text-slate-800 dark:text-white uppercase tracking-wider">Access Forbidden</h2>
                    <p className="text-slate-400 text-sm mt-3 leading-relaxed">You do not have administrative credentials. Please log in as an administrator to access these settings.</p>
                </div>
            </main>
        );
    }

    return (
        <main className="min-h-screen pt-40 pb-20 px-6 bg-slate-50/50 dark:bg-black/10">
            <Navbar />
            <div className="max-w-5xl mx-auto w-full">

                <div className="mb-10 flex items-center justify-between">
                    <div>
                        <h1 className="text-4xl font-black text-slate-900 dark:text-white mb-2">Ecosystem Control Panel</h1>
                        <p className="text-slate-500 font-bold text-xs uppercase tracking-widest">Administrator Operations dashboard</p>
                    </div>
                    <div className="p-3 bg-agro-600 rounded-2xl text-white shadow-lg shrink-0">
                        <ShieldCheck className="w-8 h-8" />
                    </div>
                </div>

                {/* Tab select */}
                <div className="flex bg-white dark:bg-slate-900 p-2 rounded-2xl gap-2 border border-slate-100 dark:border-agro-800 mb-8 max-w-lg">
                    {[
                        { tab: 'rag', label: 'RAG Knowledge', icon: FileText },
                        { tab: 'db', label: 'Database Backup', icon: Database },
                        { tab: 'logs', label: 'Audit Logs', icon: Activity }
                    ].map((t) => (
                        <button
                            key={t.tab}
                            onClick={() => setActiveTab(t.tab as any)}
                            className={`flex-1 py-3 px-4 rounded-xl text-xs font-black uppercase tracking-wider flex items-center justify-center gap-2 transition-all ${activeTab === t.tab ? 'bg-agro-600 text-white shadow-md' : 'text-slate-400 hover:text-slate-700 dark:hover:text-white'}`}
                        >
                            <t.icon className="w-4 h-4" />
                            {t.label}
                        </button>
                    ))}
                </div>

                {/* Tab contents */}
                <AnimatePresence mode="wait">
                    {activeTab === 'rag' && (
                        <motion.form
                            key="rag"
                            initial={{ opacity: 0, y: 10 }}
                            animate={{ opacity: 1, y: 0 }}
                            exit={{ opacity: 0 }}
                            onSubmit={handleUploadRAG}
                            className="bg-white dark:bg-agro-900/40 p-8 rounded-[3rem] shadow-premium border border-slate-100 dark:border-agro-800 space-y-6"
                        >
                            <div>
                                <h2 className="text-2xl font-black text-slate-900 dark:text-white mb-2">Upload Agriculture Manuals</h2>
                                <p className="text-slate-400 text-xs font-bold uppercase tracking-wider">Chunk and vectorise documents in the local SQLite matrix</p>
                            </div>

                            <div className="grid md:grid-cols-2 gap-6">
                                <div className="space-y-1">
                                    <label className="text-[9px] font-black text-slate-400 uppercase tracking-widest ml-2">Document Title</label>
                                    <input
                                        type="text"
                                        value={title}
                                        onChange={(e) => setTitle(e.target.value)}
                                        className="w-full h-12 px-4 bg-slate-50 dark:bg-slate-900 border border-slate-200 dark:border-slate-800 rounded-xl outline-none focus:border-agro-500 text-sm font-bold text-slate-900 dark:text-white"
                                        placeholder="e.g. Rice Blast prevention guide"
                                        required
                                    />
                                </div>
                                <div className="space-y-1">
                                    <label className="text-[9px] font-black text-slate-400 uppercase tracking-widest ml-2">Source Agency</label>
                                    <input
                                        type="text"
                                        value={source}
                                        onChange={(e) => setSource(e.target.value)}
                                        className="w-full h-12 px-4 bg-slate-50 dark:bg-slate-900 border border-slate-200 dark:border-slate-800 rounded-xl outline-none focus:border-agro-500 text-sm font-bold text-slate-900 dark:text-white"
                                        placeholder="e.g. ICAR Research Bulletin"
                                        required
                                    />
                                </div>
                                <div className="col-span-2">
                                    <label className="text-[9px] font-black text-slate-400 uppercase tracking-widest ml-2">Document Type</label>
                                    <select
                                        value={docType}
                                        onChange={(e) => setDocType(e.target.value)}
                                        className="w-full h-12 px-4 bg-slate-50 dark:bg-slate-900 border border-slate-200 dark:border-slate-800 rounded-xl outline-none focus:border-agro-500 text-sm font-bold text-slate-900 dark:text-white"
                                    >
                                        <option value="Manual">Manual</option>
                                        <option value="Research Paper">Research Paper</option>
                                        <option value="Guide">Crop Guide</option>
                                        <option value="Circular">Government Circular</option>
                                    </select>
                                </div>
                                <div className="col-span-2 space-y-1">
                                    <label className="text-[9px] font-black text-slate-400 uppercase tracking-widest ml-2">Content Text Chunks</label>
                                    <textarea
                                        value={content}
                                        onChange={(e) => setContent(e.target.value)}
                                        className="w-full h-44 p-4 bg-slate-50 dark:bg-slate-900 border border-slate-200 dark:border-slate-800 rounded-2xl outline-none focus:border-agro-500 text-sm font-bold text-slate-900 dark:text-white resize-none"
                                        placeholder="Paste agricultural book pages, treatment recommendations, NPK schedules, or insect control metrics here..."
                                        required
                                    />
                                </div>
                            </div>

                            {successMessage && (
                                <div className="p-4 bg-emerald-50 dark:bg-emerald-950/20 text-emerald-600 dark:text-emerald-400 rounded-xl text-xs font-black uppercase tracking-widest flex items-center gap-3 border border-emerald-100 dark:border-emerald-900/30">
                                    <CheckCircle className="w-5 h-5 flex-shrink-0" />
                                    {successMessage}
                                </div>
                            )}

                            <button
                                type="submit"
                                disabled={submitting}
                                className="px-8 py-4 bg-agro-600 hover:bg-agro-700 text-white rounded-xl text-xs font-black uppercase tracking-wider flex items-center gap-2 disabled:opacity-50 transition-colors shadow-lg"
                            >
                                {submitting && <Loader2 className="w-4 h-4 animate-spin" />}
                                Vectorise Document
                            </button>
                        </motion.form>
                    )}

                    {activeTab === 'db' && (
                        <motion.div
                            key="db"
                            initial={{ opacity: 0, y: 10 }}
                            animate={{ opacity: 1, y: 0 }}
                            exit={{ opacity: 0 }}
                            className="grid md:grid-cols-2 gap-8"
                        >
                            {/* Backup Control */}
                            <div className="bg-white dark:bg-agro-900/40 p-8 rounded-[3rem] border border-slate-100 dark:border-agro-800 space-y-6">
                                <h3 className="text-lg font-black text-slate-900 dark:text-white">Save Backup</h3>
                                <p className="text-slate-400 text-xs font-bold uppercase tracking-wider">Creates a copy of local_agro.db SQLite database file with a timestamp.</p>
                                <button
                                    onClick={handleBackup}
                                    disabled={loading}
                                    className="w-full py-4 bg-agro-600 hover:bg-agro-700 text-white rounded-xl text-xs font-black uppercase tracking-[0.15em] flex items-center justify-center gap-2"
                                >
                                    {loading && <Loader2 className="w-4 h-4 animate-spin" />}
                                    Run Backup
                                </button>
                                {backupMessage && (
                                    <div className="text-xs font-black text-agro-600 uppercase tracking-widest mt-2">{backupMessage}</div>
                                )}
                            </div>

                            {/* Restore Control */}
                            <form
                                onSubmit={handleRestore}
                                className="bg-white dark:bg-agro-900/40 p-8 rounded-[3rem] border border-slate-100 dark:border-agro-800 space-y-6"
                            >
                                <h3 className="text-lg font-black text-slate-900 dark:text-white">Restore Database</h3>
                                <p className="text-slate-400 text-xs font-bold uppercase tracking-wider">Enter the backup filename to overwrite the active database state.</p>
                                <input
                                    type="text"
                                    value={backupFile}
                                    onChange={(e) => setBackupFile(e.target.value)}
                                    placeholder="e.g. backup_agro_260626_142312.db"
                                    className="w-full h-12 px-4 bg-slate-50 dark:bg-slate-900 border border-slate-200 dark:border-slate-800 rounded-xl outline-none focus:border-agro-500 text-sm font-bold text-slate-900 dark:text-white"
                                    required
                                />
                                <button
                                    type="submit"
                                    disabled={loading}
                                    className="w-full py-4 bg-slate-900 dark:bg-white text-white dark:text-slate-900 rounded-xl text-xs font-black uppercase tracking-[0.15em] flex items-center justify-center gap-2"
                                >
                                    Restore Backup
                                </button>
                                {restoreStatus && (
                                    <div className="text-xs font-black text-rose-500 uppercase tracking-widest mt-2">{restoreStatus}</div>
                                )}
                            </form>
                        </motion.div>
                    )}

                    {activeTab === 'logs' && (
                        <motion.div
                            key="logs"
                            initial={{ opacity: 0, y: 10 }}
                            animate={{ opacity: 1, y: 0 }}
                            exit={{ opacity: 0 }}
                            className="bg-white dark:bg-agro-900/40 p-8 rounded-[3rem] border border-slate-100 dark:border-agro-800 space-y-6"
                        >
                            <div className="flex justify-between items-center">
                                <h3 className="text-lg font-black text-slate-900 dark:text-white">System Audit & Login Trails</h3>
                                <button onClick={loadLogs} className="p-2.5 bg-slate-50 dark:bg-slate-950 rounded-xl hover:bg-slate-100 text-slate-500">
                                    <RefreshCw className="w-4 h-4" />
                                </button>
                            </div>

                            {loading ? (
                                <div className="text-center py-10">
                                    <Loader2 className="w-8 h-8 animate-spin text-agro-600 mx-auto" />
                                </div>
                            ) : logs.length === 0 ? (
                                <p className="text-slate-400 text-sm text-center py-10">No audit logs recorded.</p>
                            ) : (
                                <div className="space-y-3 max-h-[50vh] overflow-y-auto pr-2 no-scrollbar">
                                    {logs.map((l) => (
                                        <div key={l.id} className="p-4 bg-slate-50 dark:bg-slate-950/40 rounded-xl border border-slate-100 dark:border-slate-800 text-xs flex justify-between gap-4 items-start">
                                            <div className="space-y-1">
                                                <div className="flex gap-2 items-center">
                                                    <span className="font-black text-slate-900 dark:text-white">{l.user}</span>
                                                    <span className="px-2 py-0.5 bg-slate-200 dark:bg-slate-800 text-[8px] font-black uppercase text-slate-500 rounded">{l.action}</span>
                                                </div>
                                                <p className="text-slate-500 dark:text-agro-200/60 font-bold">{l.details}</p>
                                            </div>
                                            <span className="text-[9px] font-bold text-slate-400 shrink-0">{l.time}</span>
                                        </div>
                                    ))}
                                </div>
                            )}
                        </motion.div>
                    )}
                </AnimatePresence>
            </div>
        </main>
    );
}
