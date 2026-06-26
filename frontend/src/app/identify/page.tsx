'use client';

import { useState, useRef, useEffect } from 'react';
import { motion, AnimatePresence } from 'framer-motion';
import { Upload, X, CheckCircle, AlertTriangle, Loader2, Zap, History, Sparkles, ShieldCheck, Leaf, Camera, Eye, Info, Sprout, FileText, Check, Layers, Search, Compass, HelpCircle } from 'lucide-react';
import axios from 'axios';
import jsPDF from 'jspdf';
import html2canvas from 'html2canvas';

interface RagCitation {
  title: string;
  content: string;
  document_type: string;
  source: string;
  similarity_score: number;
}

interface Result {
  crop: string;
  scientific_name: string;
  season: string;
  location: string;
  disease: string;
  confidence: string;
  severity: string;
  affected_area_percentage: string;
  health_score: number;
  leaf_quality: string;
  spots_count: number;
  recovery_score: number;
  bounding_box: number[];
  spots_boxes: number[][];
  visual_overlay: string;
  heatmap_overlay: string;
  cause: string;
  organic_remedy: string;
  chemical_remedy: string;
  prevention: string;
  rag_citations?: RagCitation[];
  error?: boolean;
  message?: string;
  plant_id?: number | null;
  is_animal?: boolean;
  detected_animal?: string;
  is_unknown?: boolean;
  alternative_candidates?: Array<{name: string, scientific_name: string, confidence: string}>;
  warning?: string;
  top_predictions?: Array<{name: string, scientific_name: string, confidence: string}>;
}


import Navbar from '@/components/Navbar';
import { useTranslation } from 'react-i18next';

function CropEncyclopedia({ plant }: { plant: any }) {
  const [activeTab, setActiveTab] = useState<'taxonomy' | 'climate' | 'cultivation' | 'threats' | 'deficiencies'>('taxonomy');

  if (!plant) return null;

  return (
    <div className="bg-white dark:bg-agro-900/30 p-6 rounded-[2.5rem] border border-slate-100 dark:border-agro-800 space-y-6 shadow-premium">
      <div className="flex flex-col md:flex-row justify-between items-start md:items-center pb-4 border-b border-slate-100 dark:border-agro-800 gap-2">
        <div>
          <span className="text-[9px] font-black uppercase tracking-[0.2em] text-agro-600 dark:text-agro-400">Botanical Profile</span>
          <h3 className="text-2xl font-black text-slate-900 dark:text-white uppercase">{plant.name}</h3>
        </div>
        {plant.scientific_name && (
          <span className="text-xs italic font-bold text-slate-400 dark:text-slate-500 bg-slate-50 dark:bg-slate-900 px-3 py-1.5 rounded-xl border border-slate-100 dark:border-slate-800">
            {plant.scientific_name} {plant.plant_authority || ""}
          </span>
        )}
      </div>

      {plant.overview && (
        <p className="text-xs font-bold text-slate-500 dark:text-agro-200/70 leading-relaxed">
          {plant.overview}
        </p>
      )}

      {/* Tabs Selector */}
      <div className="flex flex-wrap gap-1.5 p-1 bg-slate-50 dark:bg-slate-900/50 rounded-2xl border border-slate-100 dark:border-agro-800">
        {[
          { id: 'taxonomy', label: 'Taxonomy', icon: Info },
          { id: 'climate', label: 'Climate & Soil', icon: Compass },
          { id: 'cultivation', label: 'Cultivation', icon: Sprout },
          { id: 'threats', label: 'Threats', icon: AlertTriangle },
          { id: 'deficiencies', label: 'Deficiencies', icon: Leaf }
        ].map((tab) => {
          const Icon = tab.icon;
          return (
            <button
              key={tab.id}
              onClick={() => setActiveTab(tab.id as any)}
              className={`flex-1 py-2.5 px-3 rounded-xl text-[10px] font-black uppercase tracking-wider flex items-center justify-center gap-1.5 transition-all ${activeTab === tab.id
                  ? 'bg-agro-600 text-white shadow-md'
                  : 'text-slate-400 hover:text-slate-900 dark:hover:text-white'
                }`}
            >
              <Icon className="w-3.5 h-3.5" />
              <span className="hidden sm:inline">{tab.label}</span>
            </button>
          );
        })}
      </div>

      {/* Tab Content */}
      <AnimatePresence mode="wait">
        <motion.div
          key={activeTab}
          initial={{ opacity: 0, y: 10 }}
          animate={{ opacity: 1, y: 0 }}
          exit={{ opacity: 0, y: -10 }}
          className="space-y-4 text-sm font-bold text-slate-700 dark:text-agro-200"
        >
          {activeTab === 'taxonomy' && (
            <div className="space-y-4">
              <div className="text-[10px] font-black text-slate-400 uppercase tracking-widest">Taxonomic Hierarchy</div>

              <div className="grid grid-cols-2 sm:grid-cols-4 md:grid-cols-7 gap-2.5">
                {[
                  { label: 'Kingdom', val: plant.classification?.kingdom || "Plantae" },
                  { label: 'Division', val: plant.classification?.division || "Tracheophyta" },
                  { label: 'Class', val: plant.classification?.class_name || "Magnoliopsida" },
                  { label: 'Order', val: plant.classification?.order_name || "N/A" },
                  { label: 'Family', val: plant.family?.name || "N/A" },
                  { label: 'Genus', val: plant.genus?.name || "N/A" },
                  { label: 'Species', val: plant.species?.name || plant.scientific_name?.split(" ")[1] || "N/A" }
                ].map((item, idx) => (
                  <div key={idx} className="p-3 bg-slate-50 dark:bg-slate-900/50 rounded-2xl text-center border border-slate-100 dark:border-slate-800">
                    <div className="text-[8px] font-black text-slate-400 uppercase tracking-widest">{item.label}</div>
                    <div className="text-xs font-black text-agro-600 dark:text-agro-400 mt-1 truncate" title={item.val}>{item.val}</div>
                  </div>
                ))}
              </div>

              <div className="grid sm:grid-cols-2 gap-4 mt-2">
                {plant.local_names && (
                  <div className="p-4 bg-slate-50 dark:bg-slate-900/50 rounded-2xl border border-slate-100 dark:border-slate-800">
                    <div className="text-[9px] text-slate-400 uppercase tracking-widest mb-1">Local Names</div>
                    <div className="text-xs font-black text-slate-900 dark:text-white">{plant.local_names}</div>
                  </div>
                )}
                {plant.synonyms && (
                  <div className="p-4 bg-slate-50 dark:bg-slate-900/50 rounded-2xl border border-slate-100 dark:border-slate-800">
                    <div className="text-[9px] text-slate-400 uppercase tracking-widest mb-1">Synonyms</div>
                    <div className="text-xs font-black text-slate-900 dark:text-white italic">{plant.synonyms}</div>
                  </div>
                )}
              </div>

              {plant.morphology && (
                <div className="p-4 bg-slate-50 dark:bg-slate-900/50 rounded-2xl border border-slate-100 dark:border-slate-800 text-xs leading-relaxed">
                  <span className="text-[9px] text-slate-400 uppercase tracking-widest block mb-1.5">Morphological Description</span>
                  {plant.morphology}
                </div>
              )}
            </div>
          )}

          {activeTab === 'climate' && (
            <div className="space-y-6">
              <div className="grid sm:grid-cols-3 gap-4">
                <div className="p-4 bg-slate-50 dark:bg-slate-900/50 rounded-2xl border border-slate-100 dark:border-slate-800">
                  <div className="text-[9px] text-slate-400 uppercase tracking-widest mb-1">Temperature Need</div>
                  <div className="text-sm font-black text-slate-900 dark:text-white">{plant.climate?.temperature_requirement || "N/A"}</div>
                </div>
                <div className="p-4 bg-slate-50 dark:bg-slate-900/50 rounded-2xl border border-slate-100 dark:border-slate-800">
                  <div className="text-[9px] text-slate-400 uppercase tracking-widest mb-1">Rainfall Need</div>
                  <div className="text-sm font-black text-slate-900 dark:text-white">{plant.climate?.rainfall_requirement || "N/A"}</div>
                </div>
                <div className="p-4 bg-slate-50 dark:bg-slate-900/50 rounded-2xl border border-slate-100 dark:border-slate-800">
                  <div className="text-[9px] text-slate-400 uppercase tracking-widest mb-1">Humidity Need</div>
                  <div className="text-sm font-black text-slate-900 dark:text-white">{plant.climate?.humidity_requirement || "N/A"}</div>
                </div>
              </div>

              {plant.soil && (
                <div className="p-5 bg-slate-50 dark:bg-slate-900/50 rounded-3xl border border-slate-100 dark:border-slate-800 space-y-4">
                  <div className="text-[10px] font-black text-slate-400 uppercase tracking-widest">Soil Specifications</div>
                  <div className="grid sm:grid-cols-2 gap-4 text-xs">
                    <div>
                      <span className="text-[9px] text-slate-400 uppercase tracking-widest block mb-0.5">Preferred Soil</span>
                      <span className="text-slate-950 dark:text-white font-black block">{plant.soil.preferred_soil || "N/A"}</span>
                    </div>
                    <div>
                      <span className="text-[9px] text-slate-400 uppercase tracking-widest block mb-0.5">Drainage</span>
                      <span className="text-slate-950 dark:text-white font-black block">{plant.soil.drainage || "N/A"}</span>
                    </div>
                    <div>
                      <span className="text-[9px] text-slate-400 uppercase tracking-widest block mb-0.5">Organic Matter</span>
                      <span className="text-slate-950 dark:text-white font-black block">{plant.soil.organic_matter || "N/A"}</span>
                    </div>
                    <div>
                      <span className="text-[9px] text-slate-400 uppercase tracking-widest block mb-0.5">Soil Texture</span>
                      <span className="text-slate-950 dark:text-white font-black block">{plant.soil.texture || "N/A"}</span>
                    </div>
                  </div>

                  {(() => {
                    const phRange = plant.soil?.soil_ph_range || "6.0 - 7.0";
                    const phNumbers = phRange.match(/[\d.]+/g)?.map(Number) || [6.0, 7.0];
                    const minPh = phNumbers[0] || 6.0;
                    const maxPh = phNumbers[1] || 7.0;
                    const startPct = (minPh / 14) * 100;
                    const widthPct = ((maxPh - minPh) / 14) * 100;

                    return (
                      <div className="space-y-2 pt-2 border-t border-slate-200/50 dark:border-slate-800/50">
                        <div className="flex justify-between text-[10px] text-slate-400 uppercase font-black">
                          <span>Soil pH Scale</span>
                          <span className="text-agro-600 dark:text-agro-400 font-black">Optimal: {phRange}</span>
                        </div>
                        <div className="relative h-4 bg-gradient-to-r from-red-400 via-green-400 to-blue-500 rounded-full overflow-hidden shadow-inner">
                          <div
                            className="absolute top-0 bottom-0 bg-white/50 border-l border-r border-white flex items-center justify-center text-[8px] font-black text-slate-900"
                            style={{ left: `${startPct}%`, width: `${widthPct}%` }}
                          >
                          </div>
                        </div>
                        <div className="flex justify-between text-[8px] font-bold text-slate-400 px-1">
                          <span>0 (Acidic)</span>
                          <span>7 (Neutral)</span>
                          <span>14 (Alkaline)</span>
                        </div>
                      </div>
                    );
                  })()}
                </div>
              )}
            </div>
          )}

          {activeTab === 'cultivation' && (
            <div className="space-y-5">
              {plant.stages && plant.stages.length > 0 && (
                <div className="p-5 bg-slate-50 dark:bg-slate-900/50 rounded-3xl border border-slate-100 dark:border-slate-800">
                  <div className="text-[10px] font-black text-slate-400 uppercase tracking-widest mb-4">Growth Timeline</div>
                  <div className="relative border-l-2 border-slate-200/55 dark:border-slate-800 ml-3 pl-5 space-y-5">
                    {plant.stages.map((stg: any, idx: number) => (
                      <div key={idx} className="relative">
                        <div className="absolute -left-[27px] top-1 w-3 h-3 rounded-full bg-agro-600 border-2 border-white dark:border-slate-900" />
                        <div className="flex justify-between items-start">
                          <div>
                            <span className="text-xs font-black text-slate-950 dark:text-white">{stg.name}</span>
                            <p className="text-[10px] text-slate-400 font-medium mt-0.5 leading-normal">{stg.description}</p>
                          </div>
                          <span className="px-2 py-0.5 bg-white dark:bg-slate-800 text-[8px] font-black uppercase text-agro-600 dark:text-agro-300 rounded border border-slate-100 dark:border-slate-750 shrink-0 ml-2">
                            {stg.duration_days} Days
                          </span>
                        </div>
                      </div>
                    ))}
                  </div>
                </div>
              )}

              <div className="grid sm:grid-cols-2 gap-4">
                {plant.irrigation && (
                  <div className="p-4 bg-slate-50 dark:bg-slate-900/50 rounded-2xl border border-slate-100 dark:border-slate-800 text-xs">
                    <span className="text-[9px] text-slate-400 uppercase tracking-widest block mb-1.5">Irrigation Schedule</span>
                    <div className="space-y-1">
                      <div>Water Need: <span className="text-slate-950 dark:text-white font-black">{plant.irrigation.water_requirement}</span></div>
                      <div>Weekly Need: <span className="text-slate-950 dark:text-white font-black">{plant.irrigation.weekly_water_need}</span></div>
                      {plant.irrigation.drip_recommendation && <div className="text-[10px] text-slate-400 mt-1.5 leading-relaxed">{plant.irrigation.drip_recommendation}</div>}
                    </div>
                  </div>
                )}
                {plant.harvest && (
                  <div className="p-4 bg-slate-50 dark:bg-slate-900/50 rounded-2xl border border-slate-100 dark:border-slate-800 text-xs">
                    <span className="text-[9px] text-slate-400 uppercase tracking-widest block mb-1.5">Harvest Information</span>
                    <div className="space-y-1">
                      <div>Harvest Time: <span className="text-slate-950 dark:text-white font-black">{plant.harvest.harvest_time}</span></div>
                      <div>Shelf Life: <span className="text-slate-950 dark:text-white font-black">{plant.harvest.shelf_life}</span></div>
                      {plant.harvest.harvest_indicators && <div className="text-[10px] text-slate-400 mt-1.5 leading-relaxed">{plant.harvest.harvest_indicators}</div>}
                    </div>
                  </div>
                )}
              </div>
            </div>
          )}

          {activeTab === 'threats' && (
            <div className="space-y-4">
              {plant.diseases && plant.diseases.length > 0 && (
                <div className="space-y-3">
                  <div className="text-[10px] font-black text-slate-400 uppercase tracking-widest">Common Pathogens & Diseases</div>
                  {plant.diseases.map((dis: any, idx: number) => (
                    <div key={idx} className="p-4 bg-red-50/30 dark:bg-red-950/10 rounded-2xl border border-red-100/50 dark:border-red-900/20 text-xs space-y-2">
                      <div className="flex justify-between items-center">
                        <span className="text-xs font-black text-red-700 dark:text-red-400">{dis.name}</span>
                        <span className={`px-2 py-0.5 rounded text-[8px] font-black uppercase ${dis.risk_level === 'High' || dis.risk_level === 'Critical'
                            ? 'bg-red-100 text-red-700 dark:bg-red-900/40 dark:text-red-300'
                            : 'bg-yellow-100 text-yellow-700 dark:bg-yellow-900/40 dark:text-yellow-300'
                          }`}>
                          {dis.risk_level} Risk
                        </span>
                      </div>
                      {dis.pathogen_name && <div className="italic text-[10px] text-slate-400">Pathogen: {dis.pathogen_name} ({dis.disease_type || "Fungal"})</div>}
                      {dis.economic_impact && <p className="text-[10px] text-slate-500 leading-normal">{dis.economic_impact}</p>}
                    </div>
                  ))}
                </div>
              )}

              {plant.pests && plant.pests.length > 0 && (
                <div className="space-y-3 pt-2">
                  <div className="text-[10px] font-black text-slate-400 uppercase tracking-widest">Insect Pests</div>
                  {plant.pests.map((pest: any, idx: number) => (
                    <div key={idx} className="p-4 bg-slate-50 dark:bg-slate-900/50 rounded-2xl border border-slate-100 dark:border-slate-800 text-xs space-y-2">
                      <div className="flex justify-between items-center">
                        <span className="text-xs font-black text-slate-950 dark:text-white">{pest.name}</span>
                        {pest.scientific_name && <span className="text-[10px] italic text-slate-400">{pest.scientific_name}</span>}
                      </div>
                      <p className="text-[10px] text-slate-500 leading-normal">{pest.identification}</p>
                      <div className="pt-1.5 border-t border-slate-200/50 dark:border-slate-800/50 space-y-1 text-[10px]">
                        <div><span className="font-bold text-agro-600 dark:text-agro-400">Organic Control:</span> {pest.organic_control}</div>
                        <div><span className="font-bold text-blue-600 dark:text-blue-400">Chemical Control:</span> {pest.chemical_control}</div>
                      </div>
                    </div>
                  ))}
                </div>
              )}
            </div>
          )}

          {activeTab === 'deficiencies' && (
            <div className="space-y-4">
              {plant.deficiencies && plant.deficiencies.length > 0 && (
                <div className="space-y-3">
                  <div className="text-[10px] font-black text-slate-400 uppercase tracking-widest">Nutrient Deficiencies & Signs</div>
                  {plant.deficiencies.map((def: any, idx: number) => (
                    <div key={idx} className="p-4 bg-slate-50 dark:bg-slate-900/50 rounded-2xl border border-slate-100 dark:border-slate-800 text-xs space-y-2">
                      <div className="text-xs font-black text-slate-950 dark:text-white flex items-center gap-1.5">
                        <div className="w-2 h-2 rounded-full bg-yellow-500" />
                        {def.nutrient_name} Deficiency
                      </div>
                      <p className="text-[10px] text-slate-500 leading-normal">{def.symptoms}</p>
                      <div className="text-[10px] bg-white dark:bg-slate-900 p-2.5 rounded-xl border border-slate-150 dark:border-slate-800 text-slate-600 dark:text-agro-200">
                        <span className="font-bold text-agro-700 dark:text-agro-400">Correction:</span> {def.correction_methods}
                      </div>
                    </div>
                  ))}
                </div>
              )}
            </div>
          )}
        </motion.div>
      </AnimatePresence>
    </div>
  );
}

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

  // Crop search states
  const [searchQuery, setSearchQuery] = useState('');
  const [cropSearchResult, setCropSearchResult] = useState<any | null>(null);
  const [searchLoading, setSearchLoading] = useState(false);
  const [searchError, setSearchError] = useState<string | null>(null);

  const handleCropSearch = async (e: React.FormEvent) => {
    e.preventDefault();
    if (!searchQuery.trim()) return;
    setSearchLoading(true);
    setSearchError(null);
    setCropSearchResult(null);
    try {
      const res = await axios.get(`http://localhost:8000/api/crops/${searchQuery.trim()}`);
      setCropSearchResult(res.data);
    } catch (err: any) {
      if (err.response && err.response.data && err.response.data.detail) {
        setSearchError(err.response.data.detail);
      } else {
        setSearchError("Crop details search failed. Please verify the Python backend is running.");
      }
    } finally {
      setSearchLoading(false);
    }
  };
  const [error, setError] = useState<string | null>(null);
  const [history, setHistory] = useState<Result[]>([]);
  const [downloading, setDownloading] = useState(false);
  const [scanProgress, setScanProgress] = useState(0);
  const [scanStatus, setScanStatus] = useState('');
  const [imageMode, setImageMode] = useState<'original' | 'bounding_box' | 'heatmap'>('original');
  const reportRef = useRef<HTMLDivElement>(null);

  useEffect(() => {
    const savedHistory = localStorage.getItem('agro_scan_history_db');
    if (savedHistory) setHistory(JSON.parse(savedHistory));
  }, []);

  const saveToHistory = (newResult: Result) => {
    const updated = [newResult, ...history].slice(0, 5);
    setHistory(updated);
    localStorage.setItem('agro_scan_history_db', JSON.stringify(updated));
  };

  const handleImageChange = (e: React.ChangeEvent<HTMLInputElement>) => {
    if (e.target.files && e.target.files[0]) {
      const file = e.target.files[0];
      setImage(file);
      setPreview(URL.createObjectURL(file));
      setResult(null);
      setError(null);
      setImageMode('original');
    }
  };

  const analyzeImage = async () => {
    if (!image) return;
    setLoading(true);
    setError(null);
    setResult(null);
    setScanProgress(0);

    const statuses = [
      'Enhancing Exposure Contrast...',
      'Isolating Leaf Contours (OpenCV)...',
      'Applying HSV Chromatic Filters...',
      'Analyzing Pathogen Cell Area...',
      'Re-compiling Cosine TF-IDF Index...',
      'Finalizing Diagnostic Report...'
    ];

    let statusIdx = 0;
    const statusInterval = setInterval(() => {
      if (statusIdx < statuses.length) {
        setScanStatus(statuses[statusIdx]);
        setScanProgress(prev => Math.min(prev + 16, 95));
        statusIdx++;
      }
    }, 800);

    const token = localStorage.getItem('agro_token');
    const formData = new FormData();
    formData.append('file', image);
    if (token) {
      formData.append('token', token);
    }

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
        setImageMode('bounding_box'); // auto show bounding boxes
      }
    } catch (err) {
      clearInterval(statusInterval);
      setError("AI Detection service is offline. Please start the backend FastAPI server.");
    } finally {
      setLoading(false);
    }
  };

  const downloadPDF = async () => {
    if (!reportRef.current || !result) return;
    setDownloading(true);

    try {
      await new Promise(resolve => setTimeout(resolve, 500));
      const captureElement = reportRef.current;
      const canvas = await html2canvas(captureElement, {
        scale: 2,
        useCORS: true,
        backgroundColor: '#ffffff'
      });

      const imgWidth = 210;
      const imgHeight = (canvas.height * imgWidth) / canvas.width;
      const imgData = canvas.toDataURL('image/jpeg', 0.95);

      const pdf = new jsPDF('p', 'mm', 'a4');
      pdf.addImage(imgData, 'JPEG', 0, 0, imgWidth, imgHeight, undefined, 'FAST');
      pdf.save(`AgroDoctor_Diagnosis_${result.crop.replace(/\s+/g, '_')}.pdf`);
    } catch (err) {
      console.error("PDF capture failure:", err);
      alert("Error downloading styled PDF. A simple report will be downloaded.");
    } finally {
      setDownloading(false);
    }
  };

  if (!mounted) return null;

  return (
    <main className="min-h-screen pt-40 pb-20 px-6">
      <Navbar />
      <div className="max-w-7xl mx-auto w-full">

        <div className="text-center mb-16">
          <motion.div
            initial={{ opacity: 0, scale: 0.9 }}
            animate={{ opacity: 1, scale: 1 }}
            className="inline-flex items-center gap-2 px-4 py-2 rounded-full bg-agro-100 dark:bg-agro-800/50 text-agro-700 dark:text-agro-300 text-[10px] font-black uppercase tracking-widest mb-4 border border-agro-200/50 dark:border-agro-700/50"
          >
            <Zap className="w-3 h-3" />
            Next-Gen Computer Vision
          </motion.div>
          <h1 className="text-5xl lg:text-6xl font-black text-slate-900 dark:text-white mb-6 tracking-tight">AI Crop Diagnostic Lab</h1>
          <p className="text-slate-500 dark:text-agro-200/60 font-medium max-w-xl mx-auto">Upload a leaf photo to isolate diseases, run offline RAG queries, and calculate crop health metrics locally.</p>
        </div>

        <div className="grid lg:grid-cols-12 gap-10 items-start">
          {/* Left: Uploader and Image View */}
          <div className="lg:col-span-6 space-y-6">

            {/* Crop Search Box */}
            <div className="bg-white dark:bg-agro-900/40 p-6 rounded-[3rem] shadow-premium border border-slate-100 dark:border-agro-800 space-y-4">
              <h3 className="text-xs font-black uppercase tracking-widest text-slate-400 flex items-center gap-2">
                <Search className="w-4 h-4 text-agro-600" />
                Search Crop Botanical Database
              </h3>
              <form onSubmit={handleCropSearch} className="flex gap-2">
                <input
                  type="text"
                  placeholder="Enter crop name (e.g. Tomato, Rice, Wheat...)"
                  value={searchQuery}
                  onChange={(e) => setSearchQuery(e.target.value)}
                  className="flex-1 h-12 px-4 bg-slate-50 dark:bg-slate-900 border border-slate-200 dark:border-slate-850 rounded-xl outline-none focus:border-agro-500 text-sm font-bold text-slate-900 dark:text-white"
                />
                <button
                  type="submit"
                  disabled={searchLoading}
                  className="px-6 h-12 bg-agro-600 text-white rounded-xl text-xs font-black uppercase tracking-wider hover:bg-agro-700 transition-colors disabled:opacity-50 shrink-0"
                >
                  {searchLoading ? <Loader2 className="w-4 h-4 animate-spin" /> : "Search"}
                </button>
              </form>

              {searchError && (
                <div className="text-xs font-bold text-red-500 flex items-center gap-1.5 mt-1">
                  <AlertTriangle className="w-4 h-4 flex-shrink-0" />
                  {searchError}
                </div>
              )}

              {/* Search Results Display */}
              <AnimatePresence>
                {cropSearchResult && (
                  <motion.div
                    initial={{ opacity: 0, height: 0 }}
                    animate={{ opacity: 1, height: 'auto' }}
                    exit={{ opacity: 0, height: 0 }}
                    className="p-4 bg-slate-50 dark:bg-slate-900/50 border border-slate-100 dark:border-slate-800 rounded-2xl space-y-3 overflow-hidden text-sm font-bold"
                  >
                    <div className="flex justify-between items-center pb-2 border-b border-slate-200/50 dark:border-slate-800">
                      <span className="text-md font-black text-slate-900 dark:text-white uppercase">{cropSearchResult.name}</span>
                      <span className="text-xs italic text-slate-400">{cropSearchResult.scientific_name}</span>
                    </div>
                    <div className="grid grid-cols-2 gap-3 text-xs">
                      <div>
                        <div className="text-[9px] text-slate-400 uppercase tracking-widest">Season</div>
                        <div className="text-slate-700 dark:text-agro-200 mt-0.5">{cropSearchResult.season}</div>
                      </div>
                      <div>
                        <div className="text-[9px] text-slate-400 uppercase tracking-widest">Origins</div>
                        <div className="text-slate-700 dark:text-agro-200 mt-0.5 leading-relaxed">{cropSearchResult.location}</div>
                      </div>
                    </div>
                    <div>
                      <div className="text-[9px] text-slate-400 uppercase tracking-widest mb-1.5">Common Susceptible Diseases</div>
                      <div className="flex flex-wrap gap-2">
                        {cropSearchResult.diseases.map((d: any, idx: number) => (
                          <span key={idx} className="px-2.5 py-1 bg-white dark:bg-agro-800 border border-slate-200 dark:border-slate-700 text-[10px] font-black uppercase text-agro-600 dark:text-agro-300 rounded-lg">
                            {typeof d === 'object' && d !== null ? d.name : d}
                          </span>
                        ))}
                      </div>
                    </div>
                  </motion.div>
                )}
              </AnimatePresence>
            </div>

            <div className="bg-white dark:bg-agro-900/40 p-6 rounded-[3rem] shadow-premium border border-slate-100 dark:border-agro-800">

              {/* Main Preview Screen */}
              <div className={`relative border-2 border-dashed rounded-[2rem] aspect-square flex flex-col items-center justify-center overflow-hidden transition-all duration-500 ${preview ? 'border-agro-500 bg-agro-50/50 dark:bg-agro-800/20' : 'border-slate-200 dark:border-agro-800 bg-slate-50 dark:bg-agro-900 hover:border-agro-300'}`}>
                <AnimatePresence mode="wait">
                  {preview ? (
                    <motion.div initial={{ opacity: 0 }} animate={{ opacity: 1 }} exit={{ opacity: 0 }} className="relative w-full h-full">
                      {imageMode === 'original' && (
                        <img src={preview} alt="Original Leaf" className="w-full h-full object-cover" />
                      )}
                      {imageMode === 'bounding_box' && (
                        <img src={result?.visual_overlay || preview} alt="Bounding Box Overlay" className="w-full h-full object-cover" />
                      )}
                      {imageMode === 'heatmap' && (
                        <img src={result?.heatmap_overlay || preview} alt="Grad-CAM Heatmap" className="w-full h-full object-cover" />
                      )}

                      {loading && (
                        <>
                          <motion.div
                            initial={{ top: '0%' }}
                            animate={{ top: '100%' }}
                            transition={{ duration: 1.5, repeat: Infinity, ease: "linear" }}
                            className="absolute left-0 right-0 h-1.5 bg-agro-500 shadow-[0_0_20px_#22c55e] z-10"
                          />
                          <div className="absolute inset-0 bg-black/40 backdrop-blur-sm flex flex-col items-center justify-center p-10 text-center z-10">
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
                      <button onClick={() => { setImage(null); setPreview(null); setResult(null); }} className="absolute top-6 right-6 p-2.5 bg-white/90 dark:bg-slate-900/90 rounded-2xl shadow-xl hover:bg-red-500 hover:text-white transition-all transform hover:rotate-90 z-20 text-slate-800 dark:text-white">
                        <X className="w-5 h-5" />
                      </button>
                    </motion.div>
                  ) : (
                    <label className="w-full h-full flex flex-col items-center justify-center cursor-pointer p-10 group">
                      <div className="bg-white dark:bg-agro-850 w-20 h-20 rounded-[1.5rem] shadow-xl flex items-center justify-center mb-6 group-hover:scale-110 transition-transform">
                        <Upload className="w-8 h-8 text-agro-600" />
                      </div>
                      <span className="text-slate-900 dark:text-white font-black text-lg mb-2">Upload Crop Image</span>
                      <span className="text-slate-400 font-bold text-xs uppercase tracking-widest">Supports JPG, PNG, WEBP, BMP</span>
                      <input type="file" className="hidden" onChange={handleImageChange} accept="image/*" />
                    </label>
                  )}
                </AnimatePresence>
              </div>

              {/* CV Tabs (Only shown when result is ready) */}
              {result && (
                <div className="mt-4 p-2 bg-slate-50 dark:bg-slate-900/50 rounded-2xl flex gap-2 border border-slate-100 dark:border-slate-800">
                  {[
                    { mode: 'original', label: 'Original', icon: Eye },
                    { mode: 'bounding_box', label: 'Leaf contours', icon: Layers },
                    { mode: 'heatmap', label: 'Lesion Heatmap', icon: Zap }
                  ].map((tab) => (
                    <button
                      key={tab.mode}
                      onClick={() => setImageMode(tab.mode as any)}
                      className={`flex-1 py-3 px-4 rounded-xl text-xs font-black uppercase tracking-wider flex items-center justify-center gap-2 transition-all ${imageMode === tab.mode ? 'bg-agro-600 text-white shadow-lg' : 'text-slate-400 hover:text-slate-900 dark:hover:text-white'}`}
                    >
                      <tab.icon className="w-4 h-4" />
                      {tab.label}
                    </button>
                  ))}
                </div>
              )}

              <div className="mt-6 flex gap-4">
                <button
                  onClick={analyzeImage}
                  disabled={!image || loading}
                  className="flex-1 btn-premium py-5 text-md flex items-center justify-center gap-3 disabled:opacity-50 disabled:scale-100"
                >
                  {loading ? (
                    <>
                      <Loader2 className="w-5 h-5 animate-spin" />
                      <span>Analyzing...</span>
                    </>
                  ) : (
                    <>
                      <Sparkles className="w-5 h-5" />
                      <span>Scan Crop Health</span>
                    </>
                  )}
                </button>
              </div>
            </div>

            {error && (
              <motion.div initial={{ opacity: 0, y: 10 }} animate={{ opacity: 1, y: 0 }} className="p-5 bg-red-50 dark:bg-red-950/20 text-red-600 dark:text-red-400 rounded-3xl text-sm font-bold flex items-center gap-3 border border-red-100 dark:border-red-900/30">
                <AlertTriangle className="w-5 h-5 flex-shrink-0" />
                {error}
              </motion.div>
            )}

            {/* Botanical details */}
            {result && (
              <motion.div
                initial={{ opacity: 0, y: 20 }}
                animate={{ opacity: 1, y: 0 }}
                className="p-6 bg-white dark:bg-agro-900/30 rounded-[2.5rem] border border-slate-100 dark:border-agro-800 space-y-4"
              >
                <h3 className="text-xs font-black uppercase tracking-widest text-slate-400 flex items-center gap-2">
                  <Info className="w-4 h-4 text-agro-600" />
                  Crop Identity & Botanical details
                </h3>
                <div className="grid grid-cols-2 gap-4 text-sm font-bold">
                  <div className="p-4 bg-slate-50 dark:bg-slate-900/50 rounded-2xl">
                    <div className="text-[10px] text-slate-400 uppercase tracking-widest mb-1">Botanical Name</div>
                    <div className="text-slate-950 dark:text-white italic">{result.scientific_name}</div>
                  </div>
                  <div className="p-4 bg-slate-50 dark:bg-slate-900/50 rounded-2xl">
                    <div className="text-[10px] text-slate-400 uppercase tracking-widest mb-1">Cultivation Season</div>
                    <div className="text-slate-950 dark:text-white">{result.season}</div>
                  </div>
                </div>
                <div className="p-4 bg-slate-50 dark:bg-slate-900/50 rounded-2xl text-sm font-bold">
                  <div className="text-[10px] text-slate-400 uppercase tracking-widest mb-1">Global/Indian Origins & Coordinates</div>
                  <div className="text-slate-700 dark:text-agro-200 leading-relaxed">{result.location}</div>
                </div>
              </motion.div>
            )}
          </div>

          {/* Right: Diagnosis & Local RAG Retrieval */}
          <div className="lg:col-span-6">
            <AnimatePresence mode="wait">
              {!result && !loading ? (
                <motion.div key="empty" initial={{ opacity: 0 }} animate={{ opacity: 1 }} className="h-full min-h-[550px] flex flex-col p-12 bg-white dark:bg-agro-900/30 rounded-[3rem] border border-slate-100 dark:border-agro-800">
                  <div className="flex-1 flex flex-col items-center justify-center text-center">
                    <History className="w-16 h-16 text-slate-200 dark:text-agro-800 mb-8 animate-pulse" />
                    <h3 className="text-xl font-black text-slate-400 dark:text-agro-700 uppercase tracking-widest">Diagnostic Panel</h3>
                    <p className="text-slate-400 dark:text-agro-800 text-sm mt-4 font-medium leading-relaxed max-w-xs">Your full diagnostics, health stats, and RAG literature citations will appear here once scanning completes.</p>
                  </div>

                  {history.length > 0 && (
                    <div className="mt-8 pt-8 border-t border-slate-100 dark:border-agro-800">
                      <h4 className="text-[10px] font-black text-slate-400 uppercase tracking-widest mb-4">Historical Scans</h4>
                      <div className="space-y-3">
                        {history.map((h, i) => (
                          <div key={i} className="flex items-center justify-between p-4 bg-slate-50 dark:bg-slate-900/40 rounded-2xl border border-slate-100 dark:border-agro-800">
                            <div>
                              <div className="text-xs font-black text-slate-900 dark:text-white">{h.crop}</div>
                              <div className="text-[10px] font-bold text-agro-600 uppercase tracking-wider">{h.disease}</div>
                            </div>
                            <div className={`px-2.5 py-1 rounded-lg text-[9px] font-black uppercase ${h.severity === 'Healthy' ? 'bg-green-100 text-green-600 dark:bg-green-950/30 dark:text-green-400' : 'bg-red-100 text-red-600 dark:bg-red-950/30 dark:text-red-400'}`}>
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
                  {result.is_animal ? (
                    <div className="p-12 text-center space-y-8 flex flex-col items-center justify-center my-auto min-h-[500px]">
                      <div className="w-24 h-24 bg-red-100 dark:bg-red-950/30 rounded-full flex items-center justify-center text-red-500 shadow-xl border border-red-200/50 dark:border-red-900/30">
                        <AlertTriangle className="w-12 h-12" />
                      </div>
                      <div className="space-y-3">
                        <h3 className="text-3xl font-black text-slate-900 dark:text-white">This image is not a plant.</h3>
                        <p className="text-sm text-slate-400 font-medium max-w-sm">Our neural classifier has detected a non-plant object in your photo.</p>
                      </div>
                      <div className="p-6 bg-slate-50 dark:bg-slate-900/50 rounded-[2.5rem] border border-slate-100 dark:border-slate-800 w-full max-w-sm">
                        <div className="text-[9px] text-slate-400 font-black uppercase tracking-widest mb-1">Detected Category</div>
                        <div className="text-xl font-black text-red-600 dark:text-red-400">{result.detected_animal}</div>
                        <div className="text-[10px] text-slate-400 font-bold mt-2 uppercase tracking-wider">Confidence Score: <span className="font-black text-slate-700 dark:text-white">{result.confidence}</span></div>
                      </div>
                      <button onClick={() => { setImage(null); setPreview(null); setResult(null); }} className="btn-premium px-8 py-4 text-xs font-black uppercase tracking-widest">
                        Upload Plant Photo
                      </button>
                    </div>
                  ) : result.is_unknown ? (
                    <div className="p-12 text-center space-y-8 flex flex-col items-center justify-center my-auto min-h-[500px]">
                      <div className="w-24 h-24 bg-yellow-100 dark:bg-yellow-950/30 rounded-full flex items-center justify-center text-yellow-500 shadow-xl border border-yellow-200/50 dark:border-yellow-900/30 animate-pulse">
                        <HelpCircle className="w-12 h-12" />
                      </div>
                      <div className="space-y-3">
                        <h3 className="text-3xl font-black text-slate-900 dark:text-white">Unknown Plant</h3>
                        <p className="text-sm text-slate-400 font-medium max-w-sm">Confidence: <span className="font-black text-yellow-600 dark:text-yellow-400">{result.confidence}</span></p>
                        <p className="text-sm text-slate-500 dark:text-slate-400 font-semibold italic">"{result.message}"</p>
                      </div>
                      
                      {result.top_predictions && result.top_predictions.length > 0 && (
                        <div className="w-full max-w-sm bg-slate-50 dark:bg-slate-900/50 p-6 rounded-[2.5rem] border border-slate-100 dark:border-slate-800 text-left space-y-4">
                          <h4 className="text-[9px] font-black text-slate-400 uppercase tracking-widest">Possible Matches</h4>
                          <div className="space-y-2">
                            {result.top_predictions.slice(0, 4).map((pred, pidx) => (
                              <div key={pidx} className="flex justify-between items-center p-3 bg-white dark:bg-slate-900 rounded-2xl border border-slate-100 dark:border-slate-800">
                                <div>
                                  <div className="text-xs font-black text-slate-900 dark:text-white">{pred.name}</div>
                                  {pred.scientific_name && <div className="text-[9px] text-slate-400 italic font-semibold">{pred.scientific_name}</div>}
                                </div>
                                <span className="text-[10px] font-black text-yellow-600 dark:text-yellow-400">{pred.confidence}</span>
                              </div>
                            ))}
                          </div>
                        </div>
                      )}
                      
                      <button onClick={() => { setImage(null); setPreview(null); setResult(null); }} className="btn-premium px-8 py-4 text-xs font-black uppercase tracking-widest">
                        Try Another Image
                      </button>
                    </div>
                  ) : (
                    <>
                      <div ref={reportRef} id="agro-report-card" className="bg-white dark:bg-slate-900">
                        {/* Status Header */}
                        <div className="p-8 text-white relative overflow-hidden" style={{ backgroundColor: result.disease === 'Healthy' ? '#16a34a' : '#dc2626' }}>
                          <div className="relative z-20">
                            <div className="flex items-center justify-between mb-4">
                              <div className="flex items-center gap-2">
                                <Sprout className="w-5 h-5 animate-spin" />
                                <span className="text-[10px] font-black uppercase tracking-[0.3em]">Agro Doctor Official Report</span>
                              </div>
                              <span className="text-[10px] font-bold opacity-80">{new Date().toLocaleDateString()}</span>
                            </div>
                            <div className="bg-white/20 backdrop-blur-md px-4 py-1.5 rounded-full w-fit mb-4 text-[10px] font-black uppercase tracking-widest border border-white/20">
                              Detected: {result.crop}
                            </div>
                            <h2 className="text-3xl font-black">{result.disease}</h2>
                            <div className="text-[10px] font-bold opacity-90 mt-1">Severity Levels: {result.severity} | Affected area: {result.affected_area_percentage}</div>
                          </div>
                          <div className="absolute top-0 right-0 p-8 opacity-10 blur-sm">
                            <ShieldCheck className="w-40 h-40" />
                          </div>
                        </div>

                        {/* Body of stats */}
                        <div className="p-8 space-y-6">
                          {result.warning && (
                            <div className="p-4 bg-yellow-50 dark:bg-yellow-950/20 text-yellow-700 dark:text-yellow-400 rounded-3xl text-xs font-bold flex items-center gap-3 border border-yellow-100/50 dark:border-yellow-900/20">
                              <AlertTriangle className="w-4 h-4 text-yellow-500" />
                              <span>{result.warning}</span>
                            </div>
                          )}

                          {result.alternative_candidates && result.alternative_candidates.length > 0 && (
                            <div className="p-5 bg-slate-50 dark:bg-slate-900/40 rounded-[2rem] border border-slate-100 dark:border-slate-800">
                              <h4 className="text-[9px] font-black text-slate-400 uppercase tracking-widest mb-3">Top Alternative Candidates</h4>
                              <div className="grid grid-cols-3 gap-3">
                                {result.alternative_candidates.map((cand, cidx) => (
                                  <div key={cidx} className="p-3 bg-white dark:bg-slate-900 rounded-2xl text-center border border-slate-100 dark:border-slate-800">
                                    <div className="text-[10px] font-black text-slate-800 dark:text-white truncate" title={cand.name}>{cand.name}</div>
                                    <div className="text-[8px] text-slate-400 truncate italic font-semibold">{cand.scientific_name}</div>
                                    <div className="text-[10px] font-black text-agro-600 dark:text-agro-400 mt-1">{cand.confidence}</div>
                                  </div>
                                ))}
                              </div>
                            </div>
                          )}

                          {/* Numeric Health Indicators */}
                          <div className="grid grid-cols-4 gap-3">
                            {[
                              { label: 'Health Score', val: `${result.health_score}%`, sub: 'Overall' },
                              { label: 'Leaf Quality', val: result.leaf_quality, sub: 'Structure' },
                              { label: 'Lesions Count', val: result.spots_count, sub: 'Spots' },
                              { label: 'Recovery Score', val: `${result.recovery_score}%`, sub: 'Estimated' }
                            ].map((stat, idx) => (
                              <div key={idx} className="p-3 bg-slate-50 dark:bg-slate-900/50 rounded-2xl text-center border border-slate-100 dark:border-slate-800">
                                <div className="text-[9px] font-black text-slate-400 uppercase tracking-widest">{stat.label}</div>
                                <div className="text-md font-black text-agro-600 dark:text-agro-400 mt-1">{stat.val}</div>
                                <div className="text-[8px] font-bold text-slate-400 uppercase tracking-wider">{stat.sub}</div>
                              </div>
                            ))}
                          </div>

                          {/* RAG citations section */}
                          {result.rag_citations && result.rag_citations.length > 0 && (
                            <div className="p-5 bg-gradient-to-br from-emerald-50 to-teal-50 dark:from-emerald-950/20 dark:to-teal-950/20 rounded-[2rem] border border-emerald-100 dark:border-emerald-900/30">
                              <h4 className="text-[10px] font-black uppercase tracking-widest text-emerald-800 dark:text-emerald-300 mb-3 flex items-center gap-2">
                                <FileText className="w-4 h-4" />
                                RAG Citations matched offline
                              </h4>
                              <div className="space-y-3">
                                {result.rag_citations.map((cit, cidx) => (
                                  <div key={cidx} className="p-3 bg-white/70 dark:bg-slate-900/70 rounded-xl border border-emerald-100/50 dark:border-emerald-900/20">
                                    <div className="flex justify-between items-center mb-1">
                                      <span className="text-xs font-black text-slate-900 dark:text-white">{cit.title}</span>
                                      <span className="text-[8px] font-black px-2 py-0.5 bg-emerald-100 text-emerald-700 dark:bg-emerald-900/40 dark:text-emerald-300 rounded">Score {cit.similarity_score}</span>
                                    </div>
                                    <p className="text-[10px] font-bold text-slate-500 dark:text-agro-200/70 leading-relaxed">{cit.content}</p>
                                  </div>
                                ))}
                              </div>
                            </div>
                          )}

                          <div className="bg-slate-50 dark:bg-slate-900/50 p-5 rounded-[2rem] border border-slate-100 dark:border-slate-800">
                            <h4 className="text-[10px] font-black uppercase tracking-widest text-slate-400 mb-2 flex items-center gap-2">
                              <div className="w-1.5 h-3 bg-agro-500 rounded-full"></div>
                              Pathogen analysis & Root Cause
                            </h4>
                            <p className="text-xs font-bold text-slate-700 dark:text-agro-200 leading-relaxed">
                              {result.cause}
                            </p>
                          </div>

                          <div className="space-y-3">
                            <div className="flex gap-4 p-4 rounded-[2rem] bg-agro-50 dark:bg-agro-800/30 border border-agro-100 dark:border-agro-700">
                              <div className="bg-white dark:bg-agro-800 p-2 rounded-xl shadow-sm h-fit">
                                <Leaf className="w-5 h-5 text-agro-600" />
                              </div>
                              <div>
                                <h5 className="text-[10px] font-black text-agro-800 dark:text-agro-300 uppercase tracking-widest mb-1">Organic Cure</h5>
                                <p className="text-xs font-bold text-agro-700 dark:text-agro-100 leading-relaxed">{result.organic_remedy}</p>
                              </div>
                            </div>
                            <div className="flex gap-4 p-4 rounded-[2rem] bg-blue-50 dark:bg-blue-900/10 border border-blue-100 dark:border-blue-900/30">
                              <div className="bg-white dark:bg-agro-800 p-2 rounded-xl shadow-sm h-fit">
                                <Zap className="w-5 h-5 text-blue-600" />
                              </div>
                              <div>
                                <h5 className="text-[10px] font-black text-blue-800 dark:text-blue-300 uppercase tracking-widest mb-1">Chemical compound</h5>
                                <p className="text-xs font-bold text-blue-700 dark:text-blue-100 leading-relaxed">{result.chemical_remedy}</p>
                              </div>
                            </div>
                            <div className="flex gap-4 p-4 rounded-[2rem] bg-slate-50 dark:bg-slate-900/50 border border-slate-100 dark:border-slate-800">
                              <div className="bg-white dark:bg-agro-800 p-2 rounded-xl shadow-sm h-fit">
                                <ShieldCheck className="w-5 h-5 text-slate-500" />
                              </div>
                              <div>
                                <h5 className="text-[10px] font-black text-slate-500 uppercase tracking-widest mb-1">Prevention & Maintenance</h5>
                                <p className="text-xs font-bold text-slate-600 dark:text-agro-200 leading-relaxed">{result.prevention}</p>
                              </div>
                            </div>
                          </div>
                        </div>
                      </div>

                      {/* Action Bar */}
                      <div className="p-8 pt-0 mt-auto flex gap-3">
                        <button
                          onClick={downloadPDF}
                          disabled={downloading}
                          className="flex-1 py-4 bg-slate-950 dark:bg-white text-white dark:text-agro-900 rounded-2xl font-black text-xs uppercase tracking-[0.2em] hover:scale-[1.02] transition-transform flex items-center justify-center gap-2 disabled:opacity-50"
                        >
                          {downloading ? (
                            <Loader2 className="w-4 h-4 animate-spin" />
                          ) : (
                            <>
                              <FileText className="w-4 h-4" />
                              <span>Download Report</span>
                            </>
                          )}
                        </button>
                        <button
                          onClick={() => { setImage(null); setPreview(null); setResult(null); }}
                          className="px-6 py-4 bg-slate-100 dark:bg-agro-800 text-slate-600 dark:text-agro-300 rounded-2xl font-black text-xs uppercase tracking-wider hover:bg-slate-200 transition-colors"
                        >
                          Reset
                        </button>
                      </div>
                    </>
                  )}
                </motion.div>

              ) : null}
            </AnimatePresence>
          </div>
        </div>
      </div>
    </main>
  );
}
