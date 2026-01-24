'use client';

import { motion } from 'framer-motion';
import { Sprout, Sun, Moon, ShoppingBag, MessageSquare, Zap, User, Menu, X, Languages } from 'lucide-react';
import Link from 'next/link';
import { useTheme } from '@/context/ThemeContext';
import { useState, useEffect } from 'react';
import LanguageSelector from './LanguageSelector';
import { useTranslation } from 'react-i18next';
import { useAuth } from '@/context/AuthContext';

export default function Navbar() {
    const { theme, toggleTheme } = useTheme();
    const { isLoggedIn, logout } = useAuth();
    const { t } = useTranslation();
    const [isOpen, setIsOpen] = useState(false);
    const [mounted, setMounted] = useState(false);

    useEffect(() => {
        setMounted(true);
    }, []);

    const navLinks = [
        { name: t('nav.identify'), href: '/identify', icon: Zap },
        { name: t('nav.market'), href: '/market', icon: ShoppingBag },
        { name: t('nav.chat'), href: '/chat', icon: MessageSquare },
    ];

    if (!mounted) return null;

    return (
        <nav className="fixed top-0 left-0 right-0 z-[100] transition-all duration-500">
            <div className="max-w-7xl mx-auto px-6 py-4">
                <div className="glass-card rounded-[2rem] px-8 py-4 flex items-center justify-between border-white/20 dark:border-agro-800/50">
                    {/* Logo */}
                    <Link href="/" className="flex items-center gap-3 group">
                        <div className="bg-agro-600 p-2 rounded-xl group-hover:rotate-12 transition-transform">
                            <Sprout className="text-white w-6 h-6" />
                        </div>
                        <span className="text-xl font-black tracking-tighter text-slate-900 dark:text-white uppercase">
                            Agro <span className="text-agro-600">Doctor</span>
                        </span>
                    </Link>

                    {/* Desktop Nav */}
                    <div className="hidden md:flex items-center gap-8">
                        {navLinks.map((link) => (
                            <Link
                                key={link.name}
                                href={link.href}
                                className="text-sm font-black text-slate-600 dark:text-agro-200 hover:text-agro-600 dark:hover:text-agro-400 transition-colors uppercase tracking-widest"
                            >
                                {link.name}
                            </Link>
                        ))}
                    </div>

                    {/* Actions */}
                    <div className="flex items-center gap-4">
                        <LanguageSelector />
                        <button
                            onClick={toggleTheme}
                            className="p-3 bg-slate-100 dark:bg-agro-800 rounded-2xl text-slate-600 dark:text-agro-200 hover:scale-110 active:scale-95 transition-all shadow-sm"
                        >
                            {theme === 'light' ? <Moon className="w-5 h-5" /> : <Sun className="w-5 h-5" />}
                        </button>

                        {isLoggedIn ? (
                            <button
                                onClick={logout}
                                className="hidden sm:flex items-center gap-2 bg-red-500 text-white px-6 py-3 rounded-2xl text-xs font-black hover:scale-105 active:scale-95 transition-all shadow-lg shadow-red-500/20 uppercase tracking-widest"
                            >
                                <X className="w-4 h-4" />
                                Logout
                            </button>
                        ) : (
                            <Link
                                href="/auth"
                                className="hidden sm:flex items-center gap-2 bg-agro-900 dark:bg-white text-white dark:text-agro-900 px-6 py-3 rounded-2xl text-xs font-black hover:scale-105 active:scale-95 transition-all shadow-lg shadow-agro-900/20 dark:shadow-white/10 uppercase tracking-widest"
                            >
                                <User className="w-4 h-4" />
                                {t('nav.portal')}
                            </Link>
                        )}

                        {/* Mobile Toggle */}
                        <button
                            onClick={() => setIsOpen(!isOpen)}
                            className="md:hidden p-3 bg-slate-100 dark:bg-agro-800 rounded-2xl text-slate-600 dark:text-agro-200"
                        >
                            {isOpen ? <X className="w-5 h-5" /> : <Menu className="w-5 h-5" />}
                        </button>
                    </div>
                </div>
            </div>

            {/* Mobile Menu */}
            <motion.div
                initial={false}
                animate={isOpen ? { height: 'auto', opacity: 1 } : { height: 0, opacity: 0 }}
                className="md:hidden overflow-hidden px-6"
            >
                <div className="glass-card rounded-[2rem] p-8 mb-4 border-white/20 dark:border-agro-800/50 space-y-6">
                    {navLinks.map((link) => (
                        <Link
                            key={link.name}
                            href={link.href}
                            onClick={() => setIsOpen(false)}
                            className="flex items-center gap-4 text-lg font-black text-slate-900 dark:text-white uppercase tracking-widest"
                        >
                            <link.icon className="w-6 h-6 text-agro-600" />
                            {link.name}
                        </Link>
                    ))}
                    <div className="pt-4 border-t border-slate-100 dark:border-agro-800">
                        {isLoggedIn ? (
                            <button
                                onClick={() => { logout(); setIsOpen(false); }}
                                className="w-full py-4 bg-red-500 text-white rounded-2xl flex items-center justify-center gap-3 font-black uppercase text-xs"
                            >
                                <X className="w-5 h-5" />
                                Logout
                            </button>
                        ) : (
                            <Link
                                href="/auth"
                                onClick={() => setIsOpen(false)}
                                className="w-full py-4 btn-premium flex items-center justify-center gap-3"
                            >
                                <User className="w-5 h-5" />
                                {t('nav.portal')}
                            </Link>
                        )}
                    </div>
                </div>
            </motion.div>
        </nav>
    );
}
