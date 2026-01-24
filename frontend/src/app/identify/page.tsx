'use client';

import { useState, useRef, useEffect } from 'react';
import { motion, AnimatePresence } from 'framer-motion';
import { Upload, X, CheckCircle, AlertTriangle, Loader2, Zap, History, Sparkles, ShieldCheck, Leaf, ArrowLeft, Camera, Sprout } from 'lucide-react';
import Link from 'next/link';
import axios from 'axios';
import jsPDF from 'jspdf';
import html2canvas from 'html2canvas';

interface Result {
    plant: string;
    disease: string;
    confidence: string;
    severity: string;
    cause: string;
    organic_remedy: string;
    chemical_remedy: string;
    prevention: string;
    error?: string;
    message?: string;
}

import Navbar from '@/components/Navbar';
import { useTranslation } from 'react-i18next';

export default function Identify() {
    const { t } = useTranslation();
    const [mounted, setMounted] = useState(false);

    useEffect(() => {
        setMounted(true);
    }, []);

    const [image, setImage] = useState<File | null>(null);
    const [preview, setPreview] = useState<string | null>(null);
    const [loading, setLoading] = useState(false);
    const [result, setResult] = useState<Result | null>(null);
    const [error, setError] = useState<string | null>(null);
    const [history, setHistory] = useState<Result[]>([]);
    const [downloading, setDownloading] = useState(false);
    const [scanProgress, setScanProgress] = useState(0);
    const [scanStatus, setScanStatus] = useState('');
    const reportRef = useRef<HTMLDivElement>(null);

    useEffect(() => {
        const savedHistory = localStorage.getItem('agro_scan_history');
        if (savedHistory) setHistory(JSON.parse(savedHistory));
    }, []);

    const saveToHistory = (newResult: Result) => {
        const updated = [newResult, ...history].slice(0, 5);
        setHistory(updated);
        localStorage.setItem('agro_scan_history', JSON.stringify(updated));
    };

    const handleImageChange = (e: React.ChangeEvent<HTMLInputElement>) => {
        if (e.target.files && e.target.files[0]) {
            const file = e.target.files[0];
            setImage(file);
            setPreview(URL.createObjectURL(file));
            setResult(null);
            setError(null);
        }
    };

    const analyzeImage = async () => {
        if (!image) return;
        setLoading(true);
        setError(null);
        setResult(null);
        setScanProgress(0);

        const statuses = [
            'Initializing Neural Link...',
            'Extracting Bio-Markers...',
            'Analyzing Texture Patterns...',
            'Cross-Referencing Global Flora DB...',
            'Synthesizing Diagnosis...'
        ];

        let statusIdx = 0;
        const statusInterval = setInterval(() => {
            if (statusIdx < statuses.length) {
                setScanStatus(statuses[statusIdx]);
                setScanProgress(prev => Math.min(prev + 20, 95));
                statusIdx++;
            }
        }, 1200);

        const formData = new FormData();
        formData.append('file', image);

        try {
            const response = await axios.post('http://localhost:8000/predict', formData);
            clearInterval(statusInterval);
            setScanProgress(100);

            if (response.data.error) {
                setError(response.data.message);
            } else {
                const finalResult = response.data;
                setResult(finalResult);
                saveToHistory(finalResult);
            }
        } catch (err) {
            clearInterval(statusInterval);
            setError("AI Service is offline. Please ensure the backend is running.");
        } finally {
            setLoading(false);
        }
    };

    const downloadPDF = async () => {
        if (!reportRef.current || !result) return;
        setDownloading(true);

        try {
            // Ensure layout is settled
            await new Promise(resolve => setTimeout(resolve, 500));

            const captureElement = reportRef.current;
            const canvas = await html2canvas(captureElement, {
                scale: 2,
                useCORS: true,
                allowTaint: true,
                logging: false,
                backgroundColor: '#ffffff',
                width: captureElement.offsetWidth,
                height: captureElement.offsetHeight,
                scrollX: -window.scrollX,
                scrollY: -window.scrollY,
                onclone: (clonedDoc) => {
                    const el = clonedDoc.body.querySelector('#agro-report-card') as HTMLElement;
                    if (el) {
                        el.style.borderRadius = '0px';
                        el.style.border = 'none';
                        el.style.transform = 'none';
                        el.style.position = 'static';
                        el.style.width = '1000px';

                        const blurs = clonedDoc.querySelectorAll('.backdrop-blur-md');
                        blurs.forEach((b: any) => {
                            b.style.backdropFilter = 'none';
                            b.style.webkitBackdropFilter = 'none';
                            b.style.backgroundColor = 'rgba(255, 255, 255, 0.1)';
                        });
                    }
                }
            });

            const imgWidth = 210;
            const imgHeight = (canvas.height * imgWidth) / canvas.width;
            const imgData = canvas.toDataURL('image/jpeg', 0.8);

            const pdf = new jsPDF('p', 'mm', 'a4');
            pdf.addImage(imgData, 'JPEG', 0, 0, imgWidth, imgHeight, undefined, 'FAST');

            pdf.save(`AgroDoctor_Report_${result.plant.replace(/\s+/g, '_')}.pdf`);
        } catch (err) {
            console.error("Critical PDF capture failure:", err);
            try {
                const pdf = new jsPDF();
                const primaryColor = result.disease === 'Healthy' ? [22, 163, 74] : [220, 38, 38];

                pdf.setFillColor(primaryColor[0], primaryColor[1], primaryColor[2]);
                pdf.rect(0, 0, 210, 40, 'F');
                pdf.setTextColor(255, 255, 255);
                pdf.setFontSize(22);
                pdf.text("AGRO DOCTOR DIAGNOSIS", 105, 20, { align: "center" });
                pdf.setFontSize(10);
                pdf.text("Official AI-Inference Digital Report", 105, 30, { align: "center" });

                pdf.setTextColor(0, 0, 0);
                pdf.setFontSize(14);
                pdf.text(`Plant Detected: ${result.plant}`, 15, 55);
                pdf.setFontSize(18);
                pdf.text(`Health Status: ${result.disease}`, 15, 65);

                pdf.setFontSize(10);
                pdf.setTextColor(100, 100, 100);
                pdf.text(`Confidence: ${result.confidence} | Severity: ${result.severity}`, 15, 75);

                pdf.setTextColor(0, 0, 0);
                pdf.setFontSize(12);
                pdf.text("ROOT CAUSE:", 15, 95);
                pdf.setFontSize(10);
                pdf.text(result.cause, 15, 102, { maxWidth: 180 });

                pdf.setFontSize(12);
                pdf.text("TREATMENT PLAN:", 15, 125);
                pdf.setFontSize(10);
                pdf.text(`Organic: ${result.organic_remedy}`, 15, 132, { maxWidth: 180 });
                pdf.text(`Chemical: ${result.chemical_remedy}`, 15, 150, { maxWidth: 180 });

                pdf.setFontSize(12);
                pdf.text("PREVENTION:", 15, 175);
                pdf.setFontSize(10);
                pdf.text(result.prevention, 15, 182, { maxWidth: 180 });

                pdf.save(`AgroDoctor_Report_Verified.pdf`);
                alert("Report generated successfully using high-compatibility mode.");
            } catch (secondErr) {
                alert("Critical error: Unable to generate PDF. Please try a screenshot.");
            }
        } finally {
            setDownloading(false);
        }
    };

    if (!mounted) return null;

    return (
        <main className="min-h-screen pt-40 pb-20 px-6">
            <Navbar />
            <div className="max-w-6xl mx-auto w-full">

                <div className="text-center mb-20">
                    <motion.div
                        initial={{ opacity: 0, scale: 0.9 }}
                        animate={{ opacity: 1, scale: 1 }}
                        className="inline-flex items-center gap-2 px-4 py-2 rounded-full bg-agro-100 dark:bg-agro-800 text-agro-700 dark:text-agro-300 text-[10px] font-black uppercase tracking-widest mb-4"
                    >
                        <Zap className="w-3 h-3" />
                        {t('identify.subtitle')}
                    </motion.div>
                    <h1 className="text-5xl lg:text-6xl font-black text-slate-900 dark:text-white mb-6 tracking-tight">{t('identify.title')}</h1>
                    <p className="text-slate-500 dark:text-agro-200 font-medium max-w-xl mx-auto">{t('identify.subtitle')}</p>
                </div>

                <div className="grid lg:grid-cols-12 gap-10 items-start">
                    <div className="lg:col-span-7">
                        <div className="bg-white dark:bg-agro-900/50 p-8 rounded-[3rem] shadow-premium border border-slate-100 dark:border-agro-800">
                            <div className={`relative border-2 border-dashed rounded-[2rem] aspect-video flex flex-col items-center justify-center overflow-hidden transition-all duration-500 ${preview ? 'border-agro-500 bg-agro-50/50 dark:bg-agro-800/20' : 'border-slate-200 dark:border-agro-800 bg-slate-50 dark:bg-agro-900 hover:border-agro-300'}`}>
                                <AnimatePresence mode="wait">
                                    {preview ? (
                                        <motion.div initial={{ opacity: 0 }} animate={{ opacity: 1 }} exit={{ opacity: 0 }} className="relative w-full h-full">
                                            <img src={preview} alt="Preview" className="w-full h-full object-cover" />
                                            {loading && (
                                                <>
                                                    <motion.div
                                                        initial={{ top: '0%' }}
                                                        animate={{ top: '100%' }}
                                                        transition={{ duration: 1.5, repeat: Infinity, ease: "linear" }}
                                                        className="absolute left-0 right-0 h-1.5 bg-agro-500 shadow-[0_0_20px_#22c55e] z-10"
                                                    />
                                                    <div className="absolute inset-0 bg-black/40 backdrop-blur-sm flex flex-col items-center justify-center p-10 text-center">
                                                        <div className="w-64 h-2 bg-white/20 rounded-full overflow-hidden mb-4 border border-white/10">
                                                            <motion.div
                                                                className="h-full bg-agro-500"
                                                                initial={{ width: '0%' }}
                                                                animate={{ width: `${scanProgress}%` }}
                                                            />
                                                        </div>
                                                        <div className="text-white font-black text-xs uppercase tracking-[0.3em] animate-pulse">
                                                            {scanStatus}
                                                        </div>
                                                    </div>
                                                </>
                                            )}
                                            <button onClick={() => { setImage(null); setPreview(null); setResult(null); }} className="absolute top-6 right-6 p-2 bg-white/90 dark:bg-agro-900/90 rounded-2xl shadow-xl hover:bg-red-500 hover:text-white transition-all transform hover:rotate-90 z-20">
                                                <X className="w-6 h-6" />
                                            </button>
                                        </motion.div>
                                    ) : (
                                        <label className="w-full h-full flex flex-col items-center justify-center cursor-pointer p-10 group">
                                            <div className="bg-white dark:bg-agro-800 w-20 h-20 rounded-[1.5rem] shadow-xl flex items-center justify-center mb-6 group-hover:scale-110 transition-transform">
                                                <Upload className="w-8 h-8 text-agro-600" />
                                            </div>
                                            <span className="text-slate-900 dark:text-white font-black text-lg mb-2">{t('identify.upload')}</span>
                                            <span className="text-slate-400 font-bold text-xs uppercase tracking-widest">JPG, PNG, HEIC up to 10MB</span>
                                            <input type="file" className="hidden" onChange={handleImageChange} accept="image/*" />
                                        </label>
                                    )}
                                </AnimatePresence>
                            </div>

                            <div className="mt-8 flex gap-4">
                                <button
                                    onClick={analyzeImage}
                                    disabled={!image || loading}
                                    className="flex-1 btn-premium py-5 text-lg flex items-center justify-center gap-3 disabled:opacity-50 disabled:scale-100"
                                >
                                    {loading ? (
                                        <>
                                            <Loader2 className="w-6 h-6 animate-spin" />
                                            <span>{t('identify.processing')}</span>
                                        </>
                                    ) : (
                                        <>
                                            <Sparkles className="w-6 h-6" />
                                            <span>{t('identify.button')}</span>
                                        </>
                                    )}
                                </button>
                                <button className="bg-slate-100 dark:bg-agro-800 p-5 rounded-3xl text-slate-500 dark:text-agro-200">
                                    <Camera className="w-6 h-6" />
                                </button>
                            </div>
                        </div>

                        {error && (
                            <motion.div initial={{ opacity: 0, y: 10 }} animate={{ opacity: 1, y: 0 }} className="mt-6 p-4 bg-red-50 dark:bg-red-950/30 text-red-600 dark:text-red-400 rounded-2xl text-sm font-bold flex items-center gap-3 border border-red-100 dark:border-red-900/50">
                                <AlertTriangle className="w-5 h-5 flex-shrink-0" />
                                {error}
                            </motion.div>
                        )}
                    </div>

                    <div className="lg:col-span-5">
                        <AnimatePresence mode="wait">
                            {!result && !loading ? (
                                <motion.div key="empty" initial={{ opacity: 0 }} animate={{ opacity: 1 }} className="h-full min-h-[500px] flex flex-col p-12 bg-white dark:bg-agro-900/30 rounded-[3rem] border border-slate-100 dark:border-agro-800">
                                    <div className="flex-1 flex flex-col items-center justify-center text-center">
                                        <History className="w-16 h-16 text-slate-200 dark:text-agro-800 mb-8" />
                                        <h3 className="text-xl font-black text-slate-400 dark:text-agro-700 uppercase tracking-widest">Diagnostic Module</h3>
                                        <p className="text-slate-400 dark:text-agro-800 text-sm mt-4 font-medium leading-relaxed max-w-xs">Your professional diagnosis report will appear here after scanning a leaf.</p>
                                    </div>

                                    {history.length > 0 && (
                                        <div className="mt-10 pt-10 border-t border-slate-100 dark:border-agro-800">
                                            <h4 className="text-[10px] font-black text-slate-400 uppercase tracking-widest mb-6">Recent Scans</h4>
                                            <div className="space-y-4">
                                                {history.map((h, i) => (
                                                    <div key={i} className="flex items-center justify-between p-4 bg-slate-50 dark:bg-agro-950/30 rounded-2xl border border-slate-100 dark:border-agro-800">
                                                        <div>
                                                            <div className="text-xs font-black text-slate-900 dark:text-white">{h.plant}</div>
                                                            <div className="text-[10px] font-bold text-agro-600 uppercase tracking-wider">{h.disease}</div>
                                                        </div>
                                                        <div className={`px-3 py-1 rounded-lg text-[8px] font-black uppercase ${h.severity === 'None' ? 'bg-green-100 text-green-600' : 'bg-red-100 text-red-600'}`}>
                                                            {h.severity}
                                                        </div>
                                                    </div>
                                                ))}
                                            </div>
                                        </div>
                                    )}
                                </motion.div>
                            ) : result ? (
                                <motion.div key="result" initial={{ opacity: 0, x: 50 }} animate={{ opacity: 1, x: 0 }} className="bg-white dark:bg-agro-900 rounded-[3rem] overflow-hidden shadow-premium h-full border border-slate-100 dark:border-agro-800 flex flex-col">
                                    <div ref={reportRef} id="agro-report-card">
                                        <div className="p-10 text-white relative overflow-hidden" style={{ backgroundColor: result.disease === 'Healthy' ? '#16a34a' : '#dc2626' }}>
                                            <div className="relative z-20">
                                                <div className="flex items-center justify-between mb-6">
                                                    <div className="flex items-center gap-2">
                                                        <Sprout className="w-5 h-5" />
                                                        <span className="text-[10px] font-black uppercase tracking-[0.3em]">{t('identify.report.header')}</span>
                                                    </div>
                                                    <span className="text-[10px] font-bold opacity-70">{new Date().toLocaleDateString()}</span>
                                                </div>
                                                <div className="bg-white/20 backdrop-blur-md px-4 py-1.5 rounded-full w-fit mb-4 text-[10px] font-black uppercase tracking-widest border border-white/20">
                                                    {t('data.messages.Detected')}: {t(`data.plants.${result.plant}`, { defaultValue: result.plant })}
                                                </div>
                                                <div className="flex items-center gap-2 mb-3">
                                                    {result.disease === 'Healthy' ? <CheckCircle className="w-5 h-5" /> : <AlertTriangle className="w-5 h-5" />}
                                                    <span className="text-[10px] font-black uppercase tracking-[0.3em]">{t('identify.report.complete')}</span>
                                                </div>
                                                <h2 className="text-4xl font-black">{t(`data.diseases.${result.disease}`, { defaultValue: result.disease })}</h2>
                                            </div>
                                            <div className="absolute top-0 right-0 p-10 opacity-10 blur-sm">
                                                {result.disease === 'Healthy' ? <ShieldCheck className="w-48 h-48" /> : <Leaf className="w-48 h-48" />}
                                            </div>
                                        </div>

                                        <div className="p-10 space-y-8 flex-1">
                                            <div className="grid grid-cols-2 gap-6">
                                                <div>
                                                    <div className="text-[10px] font-black text-slate-400 dark:text-agro-500 uppercase tracking-widest mb-1">{t('identify.report.confidence')}</div>
                                                    <div className="text-2xl font-black text-agro-600">{result.confidence}</div>
                                                </div>
                                                <div>
                                                    <div className="text-[10px] font-black text-slate-400 dark:text-agro-500 uppercase tracking-widest mb-1">{t('identify.report.severity')}</div>
                                                    <div className={`text-2xl font-black ${result.severity === 'None' ? 'text-agro-600' : 'text-red-500'}`}>{result.severity}</div>
                                                </div>
                                            </div>

                                            <div className="bg-slate-50 dark:bg-agro-950/50 p-6 rounded-[2rem] border border-slate-100 dark:border-agro-800">
                                                <h4 className="text-[10px] font-black uppercase tracking-widest text-slate-400 mb-4 flex items-center gap-2">
                                                    <div className="w-1 h-3 bg-agro-500 rounded-full"></div>
                                                    {t('identify.report.cause')}
                                                </h4>
                                                <p className="text-sm font-bold text-slate-700 dark:text-agro-200 leading-relaxed">
                                                    {result.cause.includes('Optimal growth') ? t('data.messages.OptimalGrowth') : result.cause}
                                                </p>
                                            </div>

                                            <div className="space-y-4">
                                                <div className="flex gap-4 p-5 rounded-[2rem] bg-agro-50 dark:bg-agro-800/30 border border-agro-100 dark:border-agro-700">
                                                    <div className="bg-white dark:bg-agro-800 p-2 rounded-xl shadow-sm h-fit">
                                                        <Leaf className="w-5 h-5 text-agro-600" />
                                                    </div>
                                                    <div>
                                                        <h5 className="text-[10px] font-black text-agro-800 dark:text-agro-300 uppercase tracking-widest mb-1">{t('identify.report.organic')}</h5>
                                                        <p className="text-sm font-bold text-agro-700 dark:text-agro-100">
                                                            {result.organic_remedy.includes('Continue existing care') ? t('data.messages.ContinueCare') : result.organic_remedy}
                                                        </p>
                                                    </div>
                                                </div>
                                                <div className="flex gap-4 p-5 rounded-[2rem] bg-blue-50 dark:bg-blue-900/10 border border-blue-100 dark:border-blue-900/30">
                                                    <div className="bg-white dark:bg-agro-800 p-2 rounded-xl shadow-sm h-fit">
                                                        <Zap className="w-5 h-5 text-blue-600" />
                                                    </div>
                                                    <div>
                                                        <h5 className="text-[10px] font-black text-blue-800 dark:text-blue-300 uppercase tracking-widest mb-1">{t('identify.report.chemical')}</h5>
                                                        <p className="text-sm font-bold text-blue-700 dark:text-blue-100">
                                                            {result.chemical_remedy.includes('None - Plant is Healthy') ? t('data.messages.ChemicalHealthy') : result.chemical_remedy}
                                                        </p>
                                                    </div>
                                                </div>
                                            </div>

                                            {result.disease !== 'Healthy' && (
                                                <div className="mt-8 pt-8 border-t border-slate-100 dark:border-agro-800">
                                                    <h4 className="text-[10px] font-black uppercase tracking-widest text-slate-400 mb-6 flex items-center gap-2">
                                                        <div className="w-1 h-3 bg-red-500 rounded-full"></div>
                                                        7-Day Recovery Roadmap
                                                    </h4>
                                                    <div className="space-y-4">
                                                        <div className="flex gap-4">
                                                            <div className="w-8 h-8 rounded-full bg-agro-100 dark:bg-agro-800 flex items-center justify-center text-[10px] font-black text-agro-600 shrink-0">D1</div>
                                                            <div className="text-xs font-bold text-slate-600 dark:text-agro-300">Isolate affected plants & apply organic remedy.</div>
                                                        </div>
                                                        <div className="flex gap-4">
                                                            <div className="w-8 h-8 rounded-full bg-slate-100 dark:bg-agro-800 flex items-center justify-center text-[10px] font-black text-slate-400 shrink-0">D3</div>
                                                            <div className="text-xs font-bold text-slate-400 dark:text-agro-500">Monitor leaf moisture and sunlight exposure.</div>
                                                        </div>
                                                        <div className="flex gap-4">
                                                            <div className="w-8 h-8 rounded-full bg-slate-100 dark:bg-agro-800 flex items-center justify-center text-[10px] font-black text-slate-400 shrink-0">D7</div>
                                                            <div className="text-xs font-bold text-slate-400 dark:text-agro-500">Re-scan to verify recovery progress.</div>
                                                        </div>
                                                    </div>
                                                </div>
                                            )}
                                        </div>
                                    </div>

                                    <div className="p-10 pt-0 mt-auto">
                                        <button
                                            onClick={downloadPDF}
                                            disabled={downloading}
                                            className="w-full py-5 bg-agro-950 dark:bg-white text-white dark:text-agro-900 rounded-3xl font-black text-sm uppercase tracking-[0.2em] hover:scale-[1.02] transition-transform flex items-center justify-center gap-3 disabled:opacity-50"
                                        >
                                            {downloading ? (
                                                <Loader2 className="w-5 h-5 animate-spin" />
                                            ) : (
                                                <span>{t('identify.report.download')}</span>
                                            )}
                                        </button>
                                    </div>
                                </motion.div>
                            ) : null}
                        </AnimatePresence>
                    </div>
                </div>
            </div>
        </main>
    );
}
