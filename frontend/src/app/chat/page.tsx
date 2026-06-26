'use client';

import { useState, useEffect } from 'react';
import { motion, AnimatePresence } from 'framer-motion';
import { Send, User, Bot, Loader2, Sparkles, Sprout, ArrowLeft, Mic, FileText, Check } from 'lucide-react';
import Link from 'next/link';
import axios from 'axios';

interface Citation {
    title: string;
    content: string;
    document_type: string;
    source: string;
    similarity_score: number;
}

interface Message {
    id: number;
    text: string;
    sender: 'user' | 'bot';
    citations?: Citation[];
}

import Navbar from '@/components/Navbar';
import { useTranslation } from 'react-i18next';

export default function Chat() {
    const { t } = useTranslation();
    const [mounted, setMounted] = useState(false);

    useEffect(() => {
        setMounted(true);
    }, []);

    const [messages, setMessages] = useState<Message[]>([]);
    const [input, setInput] = useState('');
    const [loading, setLoading] = useState(false);

    // Initial welcome message
    useEffect(() => {
        if (mounted) {
            setMessages([
                { 
                    id: 1, 
                    text: "Vanakkam! I am your AI Agro Expert chatbot. I run completely offline using a local vector index of ICAR manuals and soil guidelines. Ask me any questions about crop diseases, organic fertilizers (like cow dung or bio-algae), or water management!", 
                    sender: 'bot' 
                }
            ]);
        }
    }, [mounted]);

    if (!mounted) return null;

    const handleSend = async () => {
        if (!input.trim()) return;

        const userMsg: Message = { id: Date.now(), text: input, sender: 'user' };
        setMessages(prev => [...prev, userMsg]);
        const queryText = input;
        setInput('');
        setLoading(true);

        try {
            const formData = new FormData();
            formData.append('message', queryText);

            const response = await axios.post('http://localhost:8000/api/chat', formData);
            
            const botMsg: Message = {
                id: Date.now() + 1,
                text: response.data.message,
                sender: 'bot',
                citations: response.data.citations
            };
            setMessages(prev => [...prev, botMsg]);
        } catch (err) {
            const errorMsg: Message = {
                id: Date.now() + 1,
                text: "I am having trouble accessing the local RAG indexing service. Please ensure the Python FastAPI backend is running on http://localhost:8000.",
                sender: 'bot'
            };
            setMessages(prev => [...prev, errorMsg]);
        } finally {
            setLoading(false);
        }
    };

    return (
        <main className="min-h-screen pt-40 pb-10 px-6">
            <Navbar />
            <div className="max-w-4xl mx-auto w-full flex flex-col h-[70vh] bg-white/50 dark:bg-agro-900/40 backdrop-blur-xl rounded-[3rem] shadow-premium border border-slate-100 dark:border-agro-800 overflow-hidden relative">

                {/* Visual Header Inside Card */}
                <div className="p-8 border-b border-white/20 dark:border-agro-800/50 flex items-center justify-between bg-white/20 dark:bg-black/10">
                    <div className="flex items-center gap-4">
                        <div className="bg-agro-600 p-3 rounded-2xl shadow-lg">
                            <Bot className="text-white w-6 h-6" />
                        </div>
                        <div>
                            <h2 className="text-xl font-black text-slate-900 dark:text-white">AI Agro Advisor</h2>
                            <div className="flex items-center gap-2 text-[10px] font-black text-agro-600 uppercase tracking-widest">
                                <span className="w-2 h-2 bg-agro-500 rounded-full animate-pulse"></span>
                                Local RAG Vector Search Active
                            </div>
                        </div>
                    </div>
                </div>

                {/* Messages Area */}
                <div className="flex-1 overflow-y-auto p-8 space-y-6 flex flex-col no-scrollbar">
                    {messages.map((m) => (
                        <div
                            key={m.id}
                            className={`flex ${m.sender === 'user' ? 'justify-end' : 'justify-start'}`}
                        >
                            <div className={`flex gap-4 max-w-[80%] ${m.sender === 'user' ? 'flex-row-reverse' : ''}`}>
                                <div className={`w-10 h-10 rounded-xl flex items-center justify-center flex-shrink-0 shadow-lg ${m.sender === 'user' ? 'bg-agro-600 text-white' : 'bg-white dark:bg-agro-800 text-agro-600'}`}>
                                    {m.sender === 'user' ? <User className="w-5 h-5" /> : <Bot className="w-5 h-5" />}
                                </div>
                                <div className="space-y-2">
                                    <div className={`p-6 rounded-[2rem] text-sm font-bold leading-relaxed shadow-sm ${m.sender === 'user' ? 'bg-agro-600 text-white rounded-tr-none' : 'bg-white dark:bg-agro-950/50 text-slate-700 dark:text-agro-100 rounded-tl-none border border-slate-100 dark:border-agro-900'}`}>
                                        <p className="whitespace-pre-line">{m.text}</p>
                                    </div>
                                    
                                    {/* Citations display in bot responses */}
                                    {m.citations && m.citations.length > 0 && (
                                        <div className="pl-4 space-y-2">
                                            <div className="text-[9px] font-black text-slate-400 uppercase tracking-widest">Document Citations:</div>
                                            {m.citations.map((c, cidx) => (
                                                <div key={cidx} className="p-3 bg-emerald-50/50 dark:bg-emerald-950/20 border border-emerald-100/50 dark:border-emerald-900/30 rounded-xl max-w-md text-[10px] font-medium text-slate-500 dark:text-agro-300">
                                                    <div className="flex justify-between items-center mb-1">
                                                        <span className="font-bold text-slate-800 dark:text-white">{c.title} ({c.source})</span>
                                                        <span className="text-[8px] px-1.5 py-0.2 bg-emerald-100 text-emerald-800 dark:bg-emerald-900/40 rounded">Match {c.similarity_score}</span>
                                                    </div>
                                                    <p className="italic">"{c.content}"</p>
                                                </div>
                                            ))}
                                        </div>
                                    )}
                                </div>
                            </div>
                        </div>
                    ))}
                    {loading && (
                        <div className="flex justify-start">
                            <div className="flex gap-4 items-center">
                                <div className="w-10 h-10 bg-white dark:bg-agro-800 rounded-xl flex items-center justify-center">
                                    <Bot className="w-5 h-5 text-agro-600" />
                                </div>
                                <div className="p-4 bg-white/50 dark:bg-agro-950/50 rounded-2xl flex gap-2">
                                    <span className="w-2 h-2 bg-agro-400 rounded-full animate-bounce"></span>
                                    <span className="w-2 h-2 bg-agro-500 rounded-full animate-bounce [animation-delay:0.2s]"></span>
                                    <span className="w-2 h-2 bg-agro-600 rounded-full animate-bounce [animation-delay:0.4s]"></span>
                                </div>
                            </div>
                        </div>
                    )}
                </div>

                {/* Input Area */}
                <div className="p-8 bg-slate-50/50 dark:bg-black/20 border-t border-slate-100 dark:border-agro-800">
                    <div className="relative flex items-center gap-4">
                        <button className="p-4 bg-white dark:bg-agro-900 rounded-2xl text-slate-400 hover:text-agro-600 shadow-sm transition-colors">
                            <Mic className="w-6 h-6" />
                        </button>
                        <div className="flex-1 relative">
                            <input
                                type="text"
                                placeholder="Ask about soil pH, early blight, NPK levels..."
                                value={input}
                                onChange={(e) => setInput(e.target.value)}
                                onKeyPress={(e) => e.key === 'Enter' && handleSend()}
                                className="w-full h-16 pl-6 pr-16 bg-white dark:bg-agro-900 border border-slate-200 dark:border-agro-800 rounded-2xl outline-none focus:border-emerald-500 transition-all font-bold text-slate-900 dark:text-white shadow-sm"
                            />
                            <button
                                onClick={handleSend}
                                className="absolute right-3 top-1/2 -translate-y-1/2 p-3 bg-agro-600 text-white rounded-xl hover:bg-agro-700 transition-colors shadow-lg shadow-agro-600/30"
                            >
                                <Send className="w-5 h-5" />
                            </button>
                        </div>
                    </div>
                </div>
            </div>
        </main>
    );
}
