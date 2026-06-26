'use client';

import React, { createContext, useContext, useState, useEffect } from 'react';
import { useRouter, usePathname } from 'next/navigation';
import axios from 'axios';

interface UserProfile {
    id: number;
    name: string;
    email: string;
    phone?: string;
    address?: string;
    farm_size?: string;
    state?: string;
    district?: string;
    village?: string;
    crop_types?: string;
    role: string;
}

interface AuthContextType {
    isLoggedIn: boolean;
    user: UserProfile | null;
    token: string | null;
    login: (token: string, profile: UserProfile) => void;
    logout: () => void;
    refreshProfile: () => Promise<void>;
}

const AuthContext = createContext<AuthContextType | undefined>(undefined);

export function AuthProvider({ children }: { children: React.ReactNode }) {
    const [isLoggedIn, setIsLoggedIn] = useState(false);
    const [user, setUser] = useState<UserProfile | null>(null);
    const [token, setToken] = useState<string | null>(null);
    const [loading, setLoading] = useState(true);
    const router = useRouter();
    const pathname = usePathname();

    const fetchProfile = async (authToken: string) => {
        try {
            const res = await axios.get('http://localhost:8000/api/auth/profile', {
                headers: { Authorization: `Bearer ${authToken}` }
            });
            setUser(res.data);
            setIsLoggedIn(true);
            setToken(authToken);
            localStorage.setItem('agro_token', authToken);
        } catch (err) {
            logout();
        }
    };

    useEffect(() => {
        const savedToken = localStorage.getItem('agro_token');
        if (savedToken) {
            fetchProfile(savedToken).finally(() => setLoading(false));
        } else {
            setLoading(false);
        }
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

    const login = (authToken: string, profile: UserProfile) => {
        setToken(authToken);
        setUser(profile);
        setIsLoggedIn(true);
        localStorage.setItem('agro_token', authToken);
        router.push('/');
    };

    const logout = () => {
        setIsLoggedIn(false);
        setUser(null);
        setToken(null);
        localStorage.removeItem('agro_token');
        router.push('/auth');
    };

    const refreshProfile = async () => {
        const currentToken = token || localStorage.getItem('agro_token');
        if (currentToken) {
            await fetchProfile(currentToken);
        }
    };

    return (
        <AuthContext.Provider value={{ isLoggedIn, user, token, login, logout, refreshProfile }}>
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
