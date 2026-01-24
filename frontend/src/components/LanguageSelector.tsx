'use client';

import { useState, useRef, useEffect } from 'react';
import { useTranslation } from 'react-i18next';
import { Languages, ChevronDown, Check } from 'lucide-react';
import { motion, AnimatePresence } from 'framer-motion';

const languages = [
    { code: 'en', name: 'English', flag: '🇺🇸' },
    { code: 'ta', name: 'தமிழ் (Tamil)', flag: '🇮🇳' },
    { code: 'hi', name: 'हिन्दी (Hindi)', flag: '🇮🇳' },
    { code: 'mr', name: 'मराठी (Marathi)', flag: '🇮🇳' },
    { code: 'fr', name: 'Français (French)', flag: '🇫🇷' },
    { code: 'ja', name: '日本語 (Japanese)', flag: '🇯🇵' },
    { code: 'zh', name: '中文 (Chinese)', flag: '🇨🇳' }
];

export default function LanguageSelector() {
    const { i18n } = useTranslation();
    const [isOpen, setIsOpen] = useState(false);
    const dropdownRef = useRef<HTMLDivElement>(null);

    const currentLanguage = languages.find(l => l.code === (i18n.language?.split('-')[0] || 'en')) || languages[0];

    const changeLanguage = (code: string) => {
        i18n.changeLanguage(code);
        setIsOpen(false);
    };

    useEffect(() => {
        const handleClickOutside = (event: MouseEvent) => {
            if (dropdownRef.current && !dropdownRef.current.contains(event.target as Node)) {
                setIsOpen(false);
            }
        };
        document.addEventListener('mousedown', handleClickOutside);
        return () => document.removeEventListener('mousedown', handleClickOutside);
    }, []);

    return (
        <div className="relative" ref={dropdownRef}>
            <button
                onClick={() => setIsOpen(!isOpen)}
                className="flex items-center gap-2 p-3 bg-slate-100 dark:bg-agro-800 rounded-2xl text-slate-600 dark:text-agro-200 hover:scale-105 active:scale-95 transition-all shadow-sm group"
            >
                <Languages className="w-5 h-5 text-agro-600 group-hover:rotate-12 transition-transform" />
                <span className="text-[10px] font-black uppercase tracking-widest hidden lg:block">
                    {currentLanguage.code}
                </span>
                <ChevronDown className={`w-3 h-3 opacity-50 transition-transform ${isOpen ? 'rotate-180' : ''}`} />
            </button>

            <AnimatePresence>
                {isOpen && (
                    <motion.div
                        initial={{ opacity: 0, y: 10, scale: 0.95 }}
                        animate={{ opacity: 1, y: 0, scale: 1 }}
                        exit={{ opacity: 0, y: 10, scale: 0.95 }}
                        className="absolute right-0 mt-4 w-60 glass-card rounded-3xl p-3 z-[200] border-white/20 dark:border-agro-800/50 shadow-2xl"
                    >
                        <div className="space-y-1">
                            {languages.map((lang) => (
                                <button
                                    key={lang.code}
                                    onClick={() => changeLanguage(lang.code)}
                                    className={`w-full flex items-center justify-between p-4 rounded-2xl transition-all ${currentLanguage.code === lang.code
                                        ? 'bg-agro-600 text-white'
                                        : 'hover:bg-slate-50 dark:hover:bg-agro-800/60 text-slate-600 dark:text-agro-200'
                                        }`}
                                >
                                    <div className="flex items-center gap-3">
                                        <span className="text-lg">{lang.flag}</span>
                                        <span className="text-sm font-bold">{lang.name}</span>
                                    </div>
                                    {currentLanguage.code === lang.code && <Check className="w-4 h-4" />}
                                </button>
                            ))}
                        </div>
                    </motion.div>
                )}
            </AnimatePresence>
        </div>
    );
}
