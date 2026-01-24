'use client';

import React, { createContext, useContext, useState, useEffect } from 'react';
import { useRouter, usePathname } from 'next/navigation';

interface AuthContextType {
    isLoggedIn: boolean;
    login: (username: string) => void;
    logout: () => void;
    user: string | null;
}

const AuthContext = createContext<AuthContextType | undefined>(undefined);

export function AuthProvider({ children }: { children: React.ReactNode }) {
    const [isLoggedIn, setIsLoggedIn] = useState(false);
    const [user, setUser] = useState<string | null>(null);
    const [loading, setLoading] = useState(true);
    const router = useRouter();
    const pathname = usePathname();

    useEffect(() => {
        // Check localStorage on mount
        const savedUser = localStorage.getItem('agro_user');
        if (savedUser) {
            setIsLoggedIn(true);
            setUser(savedUser);
        }
        setLoading(false);
    }, []);

    useEffect(() => {
        if (!loading) {
            if (!isLoggedIn && pathname !== '/auth') {
                router.push('/auth');
            } else if (isLoggedIn && pathname === '/auth') {
                router.push('/');
            }
        }
    }, [isLoggedIn, pathname, loading, router]);

    const login = (username: string) => {
        setIsLoggedIn(true);
        setUser(username);
        localStorage.setItem('agro_user', username);
        router.push('/');
    };

    const logout = () => {
        setIsLoggedIn(false);
        setUser(null);
        localStorage.removeItem('agro_user');
        router.push('/auth');
    };

    return (
        <AuthContext.Provider value={{ isLoggedIn, login, logout, user }}>
            {!loading && children}
        </AuthContext.Provider>
    );
}

export function useAuth() {
    const context = useContext(AuthContext);
    if (context === undefined) {
        throw new Error('useAuth must be used within an AuthProvider');
    }
    return context;
}
