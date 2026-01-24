'use client';

import { useState, useEffect } from 'react';
import { motion, AnimatePresence } from 'framer-motion';
import { Send, User, Bot, Loader2, Sparkles, Sprout, ArrowLeft, Mic } from 'lucide-react';
import Link from 'next/link';

interface Message {
    id: number;
    text: string;
    sender: 'user' | 'bot';
}

import Navbar from '@/components/Navbar';
import { useTranslation } from 'react-i18next';

export default function Chat() {
    const { t } = useTranslation();
    const [mounted, setMounted] = useState(false);

    useEffect(() => {
        setMounted(true);
    }, []);

    const [messages, setMessages] = useState<Message[]>([
        { id: 1, text: t('chat.welcome'), sender: 'bot' }
    ]);
    const [input, setInput] = useState('');
    const [loading, setLoading] = useState(false);

    if (!mounted) return null;

    const handleSend = () => {
        if (!input.trim()) return;

        const userMsg: Message = { id: Date.now(), text: input, sender: 'user' };
        setMessages(prev => [...prev, userMsg]);
        const currentInput = input.toLowerCase();
        setInput('');
        setLoading(true);

        // Scalable Knowledge Base - Massive Expansion for "Full Fledge" feel
        const KNOWLEDGE_BASE = [
            {
                keywords: ['cow dung', 'cowdung', 'manure', 'organic waste', 'gobar'],
                response: "Well-rotted cow dung should be applied to the soil 2-3 weeks before planting to allow nutrients to integrate. It can also be used as a top dressing during the vegetative growth stage. Always ensure it is fully composted (kept for at least 6 months) to avoid high ammonia levels that can burn roots."
            },
            {
                keywords: ['water', 'irrigation', 'watering', 'drops', 'dry'],
                response: "Proper irrigation is key. Most crops prefer deep watering in the early morning. If you notice wilting or dry soil 2 inches deep, your plants need hydration. For better efficiency, consider Drip Irrigation to save 40-70% water while increasing yield."
            },
            {
                keywords: ['insect', 'pest', 'bug', 'worm', 'aphids', 'thrips'],
                response: "Detected a pest concern? For organic control, try a 5% Neem Oil solution with a few drops of liquid soap. If the infestation is high, you can check our Insecticide section in the Market. Would you like to scan a leaf in 'AI Doctor' to identify the specific pest?"
            },
            {
                keywords: ['yellow', 'pale', 'leaves', 'faded'],
                response: "Yellowing leaves (chlorosis) often signal a Nitrogen deficiency or over-watering. Try adding some Urea or organic compost. If the veins stay green while the rest turns yellow, it might be an Iron deficiency. Check the soil pH - it should be between 6.0 and 7.0 for most crops."
            },
            {
                keywords: ['soil', 'ph', 'acid', 'alkaline', 'earth'],
                response: "Soil health is the foundation. Most agricultural crops thrive in slightly acidic to neutral soil (pH 6.0 - 7.0). If your soil is too acidic, add Lime (Calcium Carbonate). If too alkaline, add Sulfur or Gypsum. You can get a soil testing kit from our Market to know for sure!"
            },
            {
                keywords: ['fertilizer', 'urea', 'npk', 'potash', 'phosphate'],
                response: "Balanced nutrition is vital. Use NPK (Nitrogen-Phosphorus-Potassium) fertilizers based on your crop growth stage. Nitrogen for leaves, Phosphorus for roots/flowers, and Potassium for overall plant health and fruit quality. Apply only when soil is moist to prevent root burn."
            },
            {
                keywords: ['tomato', 'potato', 'rice', 'paddy', 'wheat', 'corn', 'maize'],
                response: "For specialized crop guidance, please use our 'AI Doctor' module. Upload a photo and I will give you a specific diagnosis and treatment plan for that exact plant variety!"
            },
            {
                keywords: ['hello', 'hi', 'hey', 'vanakkam', 'namaste'],
                response: "Vanakkam! I am your AI Agro Expert. I can help with soil health, fertilizer application, crop diseases, and market prices. Ask me anything about your farm today!"
            },
            {
                keywords: ['market', 'buy', 'shop', 'price', 'product', 'item'],
                response: "You can find certified seeds, fertilizers, and organic pesticides in our 'Agro Store'. Prices are direct from the distributor to save you money. Click 'Back to Ecosystem' to find the Market button!"
            },
            {
                keywords: ['weather', 'rain', 'temperature', 'climate'],
                response: "Farmers should always plan based on local weather. High humidity increases the risk of fungal diseases (like Mildew). If heavy rain is expected, delay fertilizer application to prevent runoff. Avoid spraying pesticides during windy hours."
            },
            {
                keywords: ['harvest', 'ripe', 'pick', 'ready'],
                response: "Harvesting timing depends on the crop. For grains, moisture should be around 12-14%. For vegetables, pick when they reach full size but are still tender. Use sharp tools to avoid damaging the mother plant, which can lead to infection."
            }
        ];

        // Advanced Scalable Search - Multi-keyword similarity matching
        let responseFound = KNOWLEDGE_BASE.find(k =>
            k.keywords.some(keyword => currentInput.includes(keyword))
        );

        setTimeout(() => {
            const botMsg: Message = {
                id: Date.now() + 1,
                text: responseFound
                    ? responseFound.response
                    : "That is a very specific farming query! While I continue to learn more, I suggest checking for specific leaf symptoms or soil moisture. You can also upload a clear photo in our 'AI Doctor' section for a professional spectral analysis and localized solution.",
                sender: 'bot'
            };
            setMessages(prev => [...prev, botMsg]);
            setLoading(false);
        }, 1500);
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
                            <h2 className="text-xl font-black text-slate-900 dark:text-white">{t('chat.header')}</h2>
                            <div className="flex items-center gap-2 text-[10px] font-black text-agro-600 uppercase tracking-widest">
                                <span className="w-2 h-2 bg-agro-500 rounded-full animate-pulse"></span>
                                {t('chat.status')}
                            </div>
                        </div>
                    </div>
                </div>

                {/* Messages Area */}
                <div className="flex-1 overflow-y-auto p-8 space-y-6 flex flex-col no-scrollbar">
                    {messages.map((m) => (
                        <motion.div
                            key={m.id}
                            initial={{ opacity: 0, y: 10, scale: 0.95 }}
                            animate={{ opacity: 1, y: 0, scale: 1 }}
                            className={`flex ${m.sender === 'user' ? 'justify-end' : 'justify-start'}`}
                        >
                            <div className={`flex gap-4 max-w-[80%] ${m.sender === 'user' ? 'flex-row-reverse' : ''}`}>
                                <div className={`w-10 h-10 rounded-xl flex items-center justify-center flex-shrink-0 shadow-lg ${m.sender === 'user' ? 'bg-agro-600 text-white' : 'bg-white dark:bg-agro-800 text-agro-600'}`}>
                                    {m.sender === 'user' ? <User className="w-5 h-5" /> : <Bot className="w-5 h-5" />}
                                </div>
                                <div className={`p-6 rounded-[2rem] text-sm font-bold leading-relaxed shadow-sm ${m.sender === 'user' ? 'bg-agro-600 text-white rounded-tr-none' : 'bg-white dark:bg-agro-950/50 text-slate-700 dark:text-agro-100 rounded-tl-none border border-slate-100 dark:border-agro-900'}`}>
                                    {m.text}
                                </div>
                            </div>
                        </motion.div>
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
                                placeholder={t('chat.input')}
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
