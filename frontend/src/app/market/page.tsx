'use client';

import Navbar from '@/components/Navbar';

import { useState, useEffect } from 'react';
import { motion, AnimatePresence } from 'framer-motion';
import { ShoppingCart, ShoppingBag, MapPin, Loader2, Search, Filter, Plus, Minus, Trash2, Star, X, Check, ArrowRight, ArrowLeft, Sprout, CreditCard, Receipt, ShieldCheck } from 'lucide-react';
import axios from 'axios';
import Link from 'next/link';
import jsPDF from 'jspdf';
import { useTranslation } from 'react-i18next';

interface Product {
    id: number;
    name: string;
    category: string;
    price: number;
    description: string;
    usage: string;
    image: string;
}

interface CartItem extends Product {
    quantity: number;
}

export default function Market() {
    const { t } = useTranslation();
    const [mounted, setMounted] = useState(false);

    useEffect(() => {
        setMounted(true);
    }, []);

    const [products, setProducts] = useState<Product[]>([]);
    const [loading, setLoading] = useState(true);
    const [search, setSearch] = useState('');
    const [activeCategory, setActiveCategory] = useState('All');
    const [cart, setCart] = useState<CartItem[]>([]);
    const [isCartOpen, setIsCartOpen] = useState(false);
    const [generatingBill, setGeneratingBill] = useState(false);
    const [selectedProduct, setSelectedProduct] = useState<Product | null>(null);

    const categories = ['All', 'Organic', 'Seeds', 'Fertilizer', 'Insecticide', 'Pesticide'];
    // Translate the display text for categories
    const categoryLabels: Record<string, string> = {
        'All': t('market.categories.all'),
        'Organic': t('market.categories.organic'),
        'Seeds': t('market.categories.seeds'),
        'Fertilizer': t('market.categories.fertilizer'),
        'Insecticide': t('market.categories.insecticide'),
        'Pesticide': t('market.categories.pesticide')
    };

    useEffect(() => {
        const fetchProducts = async () => {
            try {
                const res = await axios.get('http://localhost:5000/api/products');
                setProducts(res.data);
            } catch (err) {
                // Fallback products as requested
                const fallback = [
                    { id: 1, name: "Organic Pesticide", category: "Organic", price: 450, usage: "Mix 5ml in 1L. Spray mornings.", description: "Highly effective organic pesticide.", image: "https://images.unsplash.com/photo-1592982537447-7440770cbfc9?auto=format&fit=crop&q=80&w=800&h=800" },
                    { id: 2, name: "Hybrid Tomato Seeds", category: "Seeds", price: 850, usage: "Sow 1/4 inch deep.", description: "Max yield hybrid seeds.", image: "https://images.unsplash.com/photo-1542332213-9b5a5a3fad35?auto=format&fit=crop&q=80&w=800&h=800" },
                    { id: 3, name: "Neem Oil", category: "Organic", price: 200, usage: "Mix 4ml in 1L soapy water.", description: "Cold pressed Neem oil.", image: "https://images.unsplash.com/photo-1628352081506-83c43123ed6d?auto=format&fit=crop&q=80&w=800&h=800" },
                    { id: 8, name: "Bio-Insecticide", category: "Insecticide", price: 550, usage: "Mix 2g in 1L water. Spray foliage.", description: "Systemic sucking pest control.", image: "https://images.unsplash.com/photo-1585314062340-f1a5a7c9328d?auto=format&fit=crop&q=80&w=800&h=800" },
                    { id: 9, name: "Spectrum Pesticide", category: "Pesticide", price: 680, usage: "Dilute 3ml in 1L water.", description: "Broad spectrum crop protection.", image: "https://images.unsplash.com/photo-1605000797499-95a51c5269ae?auto=format&fit=crop&q=80&w=800&h=800" }
                ];
                setProducts(fallback);
            } finally {
                setLoading(false);
            }
        };
        fetchProducts();
    }, []);

    const addToCart = (product: Product) => {
        setCart(prev => {
            const existing = prev.find(item => item.id === product.id);
            if (existing) {
                return prev.map(item => item.id === product.id ? { ...item, quantity: item.quantity + 1 } : item);
            }
            return [...prev, { ...product, quantity: 1 }];
        });
        setIsCartOpen(true);
    };

    const updateQuantity = (id: number, delta: number) => {
        setCart(prev => prev.map(item => {
            if (item.id === id) {
                const newQty = Math.max(1, item.quantity + delta);
                return { ...item, quantity: newQty };
            }
            return item;
        }));
    };

    const removeFromCart = (id: number) => {
        setCart(prev => prev.filter(item => item.id !== id));
    };

    const total = cart.reduce((sum, item) => sum + (item.price * item.quantity), 0);

    const generateBill = async () => {
        if (cart.length === 0) return;
        setGeneratingBill(true);

        try {
            const pdf = new jsPDF();
            const date = new Date();
            const deliveryDate = new Date();
            deliveryDate.setDate(date.getDate() + 3); // Estimated 3-day delivery

            const invoiceNo = `AD-${Math.floor(Math.random() * 900000 + 100000)}`;
            const trackingNo = `AGRO-${Math.floor(Math.random() * 100000000)}`;

            // Header
            pdf.setFillColor(20, 83, 45); // agro-900
            pdf.rect(0, 0, 210, 45, 'F');
            pdf.setTextColor(255, 255, 255);
            pdf.setFontSize(26);
            pdf.setFont("helvetica", "bold");
            pdf.text('AGRO DOCTOR STORE', 105, 22, { align: 'center' });
            pdf.setFontSize(10);
            pdf.setFont("helvetica", "normal");
            pdf.text('Official Order Confirmation & Invoice', 105, 32, { align: 'center' });

            // Order Details
            pdf.setTextColor(0, 0, 0);
            pdf.setFontSize(10);
            pdf.text('ORDER SUMMARY', 10, 55);
            pdf.setFont("helvetica", "bold");
            pdf.text(`Invoice No: ${invoiceNo}`, 10, 62);
            pdf.text(`Tracking ID: ${trackingNo}`, 10, 68);
            pdf.text(`Order Date: ${date.toLocaleString()}`, 110, 62);

            // Highlight: Delivery Date
            pdf.setFillColor(240, 253, 244); // agro-50
            pdf.rect(110, 65, 90, 10, 'F');
            pdf.setTextColor(22, 163, 74); // agro-600
            pdf.text(`ESTIMATED DELIVERY: ${deliveryDate.toDateString()}`, 115, 71);

            // Table Header
            pdf.setFillColor(241, 245, 249); // slate-100
            pdf.setTextColor(71, 85, 105); // slate-600
            pdf.rect(10, 80, 190, 10, 'F');
            pdf.setFontSize(9);
            pdf.text('ITEM DESCRIPTION', 15, 86);
            pdf.text('QTY', 120, 86);
            pdf.text('UNIT PRICE', 145, 86);
            pdf.text('TOTAL', 175, 86);

            // Item rows
            pdf.setTextColor(0, 0, 0);
            pdf.setFontSize(10);
            let y = 98;
            cart.forEach(item => {
                pdf.setFont("helvetica", "bold");
                pdf.text(item.name, 15, y);
                pdf.setFont("helvetica", "normal");
                pdf.text(item.quantity.toString(), 125, y);
                pdf.text(`Rs. ${item.price}`, 145, y);
                pdf.text(`Rs. ${item.price * item.quantity}`, 175, y);

                // ADD USAGE INSTRUCTIONS HERE
                y += 6;
                pdf.setFontSize(8);
                pdf.setTextColor(100, 116, 139);
                pdf.text(`Instruction: ${item.usage}`, 15, y);
                pdf.setTextColor(0, 0, 0);
                pdf.setFontSize(10);

                y += 10;
            });

            // Total Section
            pdf.setDrawColor(226, 232, 240); // slate-200
            pdf.line(10, y, 200, y);
            y += 12;
            pdf.setFontSize(16);
            pdf.setFont("helvetica", "bold");
            pdf.text('GRAND TOTAL:', 120, y);
            pdf.setTextColor(22, 163, 74); // agro-600
            pdf.text(`Rs. ${total}.00`, 175, y);

            // Delivery Status
            y += 20;
            pdf.setTextColor(100, 116, 139); // slate-500
            pdf.setFontSize(9);
            pdf.text('DELIVERY INFORMATION', 10, y);
            pdf.setFont("helvetica", "normal");
            pdf.text('Your order has been verified and is being prepared for dispatch.', 10, y + 6);
            pdf.text(`Expected delivery to your registered farm address by ${deliveryDate.toDateString()}.`, 10, y + 12);

            // Footer
            y = 280;
            pdf.setTextColor(148, 163, 184); // slate-400
            pdf.setFontSize(8);
            pdf.text('Agro Doctor - Empowering Indian Farmers through Precision AI', 105, y, { align: 'center' });
            pdf.text('This is a computer-generated invoice and requires no signature.', 105, y + 5, { align: 'center' });

            pdf.save(`AgroDoctor_Invoice_${invoiceNo}.pdf`);
            setCart([]);
            setIsCartOpen(false);
            alert(`Order Placed Successfully!\nInvoice: ${invoiceNo}\nEstimated Delivery: ${deliveryDate.toDateString()}`);
        } catch (err) {
            console.error("Bill generation failed:", err);
            alert("Order failed to generate invoice. Please contact support.");
        } finally {
            setGeneratingBill(false);
        }
    };

    const filtered = products.filter(p =>
        (activeCategory === 'All' || p.category === activeCategory) &&
        p.name.toLowerCase().includes(search.toLowerCase())
    );

    if (!mounted) return null;

    return (
        <main className="min-h-screen pt-40 pb-20 px-6 relative overflow-x-hidden">
            <Navbar />
            <div className="max-w-7xl mx-auto">
                <div className="flex flex-col md:flex-row md:items-end justify-between gap-10 mb-12">
                    <div>
                        <div className="inline-flex items-center gap-2 px-4 py-2 rounded-full bg-agro-100 dark:bg-agro-800 text-agro-700 dark:text-agro-300 text-[10px] font-black uppercase tracking-widest mb-4">
                            <ShoppingBag className="w-3 h-3" />
                            Premium Farmer Marketplace
                        </div>
                        <h1 className="text-5xl lg:text-7xl font-black text-slate-900 dark:text-white mb-2 leading-tight tracking-tighter">Agro <span className="text-agro-600">Store</span></h1>
                        <p className="text-slate-500 dark:text-agro-200 font-medium max-w-lg">Certified seeds and organic inputs delivered directly to your farm gate.</p>
                    </div>

                    <div className="flex items-center gap-4">
                        <div className="relative w-full md:w-80">
                            <Search className="absolute left-6 top-1/2 -translate-y-1/2 w-5 h-5 text-slate-400" />
                            <input
                                type="text"
                                placeholder={t('market.search')}
                                value={search}
                                onChange={(e) => setSearch(e.target.value)}
                                className="w-full h-16 pl-16 pr-6 bg-white dark:bg-agro-900 border border-slate-200 dark:border-agro-800 rounded-3xl outline-none focus:border-agro-500 shadow-premium transition-all font-bold text-slate-900 dark:text-white"
                            />
                        </div>
                        <button
                            onClick={() => setIsCartOpen(true)}
                            className="relative w-16 h-16 bg-white dark:bg-agro-900 rounded-3xl flex items-center justify-center shadow-premium border border-slate-100 dark:border-agro-800 hover:scale-110 transition-transform"
                        >
                            <ShoppingCart className="w-6 h-6 text-agro-600" />
                            {cart.length > 0 && (
                                <span className="absolute -top-2 -right-2 w-6 h-6 bg-red-500 text-white rounded-full text-[10px] font-black flex items-center justify-center animate-bounce">
                                    {cart.reduce((s, i) => s + i.quantity, 0)}
                                </span>
                            )}
                        </button>
                    </div>
                </div>

                {/* Categories Tab */}
                <div className="flex flex-wrap gap-3 mb-16">
                    {categories.map((cat) => (
                        <button
                            key={cat}
                            onClick={() => setActiveCategory(cat)}
                            className={`px-8 py-3 rounded-2xl font-black text-xs uppercase tracking-widest transition-all ${activeCategory === cat ? 'bg-agro-600 text-white shadow-lg shadow-agro-600/30' : 'bg-white dark:bg-agro-900 text-slate-400 hover:text-agro-600'}`}
                        >
                            {categoryLabels[cat]}
                        </button>
                    ))}
                </div>

                {loading ? (
                    <div className="flex flex-col items-center justify-center py-32 opacity-50">
                        <Loader2 className="w-12 h-12 animate-spin text-agro-600 mb-4" />
                        <span className="font-black text-xs uppercase tracking-[0.2em] text-agro-900 dark:text-white">Accessing Inventory...</span>
                    </div>
                ) : (
                    <div className="grid grid-cols-1 sm:grid-cols-2 lg:grid-cols-3 gap-10">
                        {filtered.map((product, i) => (
                            <motion.div
                                key={product.id}
                                initial={{ opacity: 0, scale: 0.9 }}
                                animate={{ opacity: 1, scale: 1 }}
                                transition={{ delay: i * 0.1 }}
                                className="bg-white dark:bg-agro-900 rounded-[2.5rem] overflow-hidden border border-slate-100 dark:border-agro-800 shadow-premium group relative"
                            >
                                <div className="h-80 relative overflow-hidden bg-slate-100 dark:bg-agro-950 cursor-pointer" onClick={() => setSelectedProduct(product)}>
                                    <div className="absolute top-8 left-8 z-10">
                                        <div className="bg-white/90 dark:bg-agro-900/90 backdrop-blur-md px-4 py-2 rounded-2xl text-[10px] font-black text-agro-700 dark:text-agro-300 uppercase tracking-widest shadow-lg">
                                            {product.category}
                                        </div>
                                    </div>
                                    <img
                                        src={product.image}
                                        alt={product.name}
                                        className="w-full h-full object-cover group-hover:scale-110 transition-transform duration-700"
                                    />
                                    <div className="absolute inset-x-6 bottom-6 translate-y-20 group-hover:translate-y-0 transition-transform duration-500 z-10">
                                        <button
                                            onClick={(e) => { e.stopPropagation(); addToCart(product); }}
                                            className="w-full py-4 bg-agro-600 text-white rounded-2xl font-black text-xs uppercase tracking-widest shadow-xl flex items-center justify-center gap-3 active:scale-95"
                                        >
                                            <ShoppingCart className="w-4 h-4" />
                                            Add to Cart
                                        </button>
                                    </div>
                                </div>

                                <div className="p-8 cursor-pointer" onClick={() => setSelectedProduct(product)}>
                                    <div className="flex items-center gap-1 mb-2">
                                        {[...Array(5)].map((_, i) => <Star key={i} className="w-3 h-3 fill-yellow-400 text-yellow-400" />)}
                                        <span className="text-[10px] font-black text-slate-400 ml-2">(4.8)</span>
                                    </div>
                                    <h3 className="text-2xl font-black text-slate-900 dark:text-white mb-2">{product.name}</h3>
                                    <p className="text-sm font-medium text-slate-500 dark:text-agro-300 mb-8 line-clamp-2">{product.description}</p>

                                    <div className="flex items-center justify-between pt-6 border-t border-slate-50 dark:border-agro-800">
                                        <div className="text-3xl font-black text-slate-900 dark:text-white">₹{product.price}</div>
                                        <button
                                            onClick={(e) => { e.stopPropagation(); addToCart(product); }}
                                            className="w-12 h-12 bg-slate-100 dark:bg-agro-800 flex items-center justify-center rounded-xl text-agro-600 hover:bg-agro-600 hover:text-white transition-all shadow-sm"
                                        >
                                            <Plus className="w-6 h-6" />
                                        </button>
                                    </div>
                                </div>
                            </motion.div>
                        ))}
                    </div>
                )}
            </div>

            {/* Product Details Modal */}
            <AnimatePresence>
                {selectedProduct && (
                    <>
                        <motion.div
                            initial={{ opacity: 0 }}
                            animate={{ opacity: 1 }}
                            exit={{ opacity: 0 }}
                            onClick={() => setSelectedProduct(null)}
                            className="fixed inset-0 bg-slate-900/60 backdrop-blur-sm z-[150]"
                        />
                        <motion.div
                            initial={{ opacity: 0, scale: 0.9, y: 20 }}
                            animate={{ opacity: 1, scale: 1, y: 0 }}
                            exit={{ opacity: 0, scale: 0.9, y: 20 }}
                            className="fixed top-1/2 left-1/2 -translate-x-1/2 -translate-y-1/2 w-full max-w-4xl max-h-[90vh] overflow-y-auto bg-white dark:bg-agro-900 z-[151] rounded-[3rem] shadow-premium flex flex-col md:flex-row border border-slate-100 dark:border-agro-800"
                        >
                            <div className="md:w-1/2 h-80 md:h-auto bg-slate-50 dark:bg-agro-950 relative">
                                <img src={selectedProduct.image} alt={selectedProduct.name} className="w-full h-full object-cover" />
                                <button
                                    onClick={() => setSelectedProduct(null)}
                                    className="absolute top-6 left-6 p-3 bg-white/90 dark:bg-agro-900/90 rounded-2xl shadow-xl hover:bg-red-500 hover:text-white transition-all"
                                >
                                    <ArrowLeft className="w-6 h-6" />
                                </button>
                            </div>
                            <div className="md:w-1/2 p-10 flex flex-col">
                                <div className="flex-1">
                                    <div className="bg-agro-100 dark:bg-agro-800 px-4 py-2 rounded-xl text-[10px] font-black text-agro-700 dark:text-agro-300 uppercase tracking-widest w-fit mb-6">
                                        {selectedProduct.category}
                                    </div>
                                    <h2 className="text-4xl font-black text-slate-900 dark:text-white mb-4">{selectedProduct.name}</h2>
                                    <div className="flex items-center gap-2 mb-8">
                                        {[...Array(5)].map((_, i) => <Star key={i} className="w-4 h-4 fill-yellow-400 text-yellow-400" />)}
                                        <span className="text-sm font-black text-slate-400">(4.8 Verified Reviews)</span>
                                    </div>

                                    <div className="space-y-6 mb-10">
                                        <div>
                                            <h4 className="text-[10px] font-black uppercase tracking-widest text-slate-400 mb-2">Description</h4>
                                            <p className="text-slate-600 dark:text-agro-200 font-medium leading-relaxed">{selectedProduct.description}</p>
                                        </div>
                                        <div className="p-6 bg-slate-50 dark:bg-agro-950/50 rounded-3xl border border-slate-100 dark:border-agro-800">
                                            <h4 className="text-[10px] font-black uppercase tracking-widest text-agro-600 mb-2 flex items-center gap-2">
                                                <Sprout className="w-3 h-3" />
                                                Usage Instructions
                                            </h4>
                                            <p className="text-sm font-bold text-slate-700 dark:text-agro-100">{selectedProduct.usage}</p>
                                        </div>
                                    </div>
                                </div>

                                <div className="flex items-center gap-6 pt-8 border-t border-slate-100 dark:border-agro-800">
                                    <div className="text-4xl font-black text-slate-900 dark:text-white">₹{selectedProduct.price}</div>
                                    <button
                                        onClick={() => { addToCart(selectedProduct); setSelectedProduct(null); }}
                                        className="flex-1 py-5 bg-agro-600 text-white rounded-3xl font-black text-sm uppercase tracking-widest shadow-xl shadow-agro-600/30 flex items-center justify-center gap-3 hover:scale-[1.02] active:scale-95 transition-all"
                                    >
                                        <ShoppingCart className="w-5 h-5" />
                                        Add to Cart
                                    </button>
                                </div>
                            </div>
                        </motion.div>
                    </>
                )}
            </AnimatePresence>

            {/* Cart Drawer */}
            <AnimatePresence>
                {isCartOpen && (
                    <>
                        <motion.div
                            initial={{ opacity: 0 }}
                            animate={{ opacity: 1 }}
                            exit={{ opacity: 0 }}
                            onClick={() => setIsCartOpen(false)}
                            className="fixed inset-0 bg-slate-900/60 backdrop-blur-sm z-[200]"
                        />
                        <motion.div
                            initial={{ x: '100%' }}
                            animate={{ x: 0 }}
                            exit={{ x: '100%' }}
                            transition={{ type: 'spring', damping: 25, stiffness: 200 }}
                            className="fixed top-0 right-0 w-full max-w-md h-screen bg-white dark:bg-agro-900 z-[201] shadow-2xl flex flex-col"
                        >
                            <div className="p-8 border-b border-slate-100 dark:border-agro-800 flex items-center justify-between">
                                <div className="flex items-center gap-3">
                                    <ShoppingCart className="w-6 h-6 text-agro-600" />
                                    <h2 className="text-xl font-black text-slate-900 dark:text-white">Your Cart</h2>
                                </div>
                                <button onClick={() => setIsCartOpen(false)} className="p-3 bg-slate-100 dark:bg-agro-800 rounded-xl text-slate-500">
                                    <X className="w-6 h-6" />
                                </button>
                            </div>

                            <div className="flex-1 overflow-y-auto p-8 space-y-6">
                                {cart.length === 0 ? (
                                    <div className="h-full flex flex-col items-center justify-center text-center opacity-30">
                                        <div className="bg-slate-100 p-8 rounded-full mb-6">
                                            <ShoppingCart className="w-16 h-16" />
                                        </div>
                                        <h3 className="text-lg font-black uppercase tracking-widest text-slate-400">Cart is Empty</h3>
                                    </div>
                                ) : (
                                    cart.map((item) => (
                                        <div key={item.id} className="flex gap-4 p-4 rounded-3xl bg-slate-50 dark:bg-agro-950/50 border border-slate-100 dark:border-agro-800">
                                            <div className="w-20 h-20 bg-white dark:bg-agro-900 rounded-2xl overflow-hidden shadow-sm">
                                                <img src={item.image} alt={item.name} className="w-full h-full object-cover" />
                                            </div>
                                            <div className="flex-1">
                                                <div className="flex justify-between items-start mb-2">
                                                    <h4 className="font-black text-slate-900 dark:text-white text-sm leading-tight">{item.name}</h4>
                                                    <button onClick={() => removeFromCart(item.id)} className="text-slate-300 hover:text-red-500">
                                                        <Trash2 className="w-4 h-4" />
                                                    </button>
                                                </div>
                                                <div className="flex items-center justify-between gap-4 mt-auto">
                                                    <div className="text-lg font-black text-agro-600">₹{item.price}</div>
                                                    <div className="flex items-center gap-3 bg-white dark:bg-agro-800 rounded-xl p-1 shadow-sm">
                                                        <button onClick={() => updateQuantity(item.id, -1)} className="p-1 text-slate-400 hover:text-agro-600"><Minus className="w-4 h-4" /></button>
                                                        <span className="font-black text-xs w-4 text-center">{item.quantity}</span>
                                                        <button onClick={() => updateQuantity(item.id, 1)} className="p-1 text-slate-400 hover:text-agro-600"><Plus className="w-4 h-4" /></button>
                                                    </div>
                                                </div>
                                            </div>
                                        </div>
                                    ))
                                )}
                            </div>

                            <div className="p-8 bg-slate-50 dark:bg-agro-950 border-t border-slate-100 dark:border-agro-800 space-y-6">
                                <div className="space-y-2">
                                    <div className="flex justify-between text-sm font-bold text-slate-400">
                                        <span>Subtotal</span>
                                        <span>₹{total}</span>
                                    </div>
                                    <div className="flex justify-between text-sm font-bold text-slate-400">
                                        <span>Delivery</span>
                                        <span className="text-agro-600 uppercase tracking-widest text-[10px]">Free</span>
                                    </div>
                                    <div className="flex justify-between text-2xl font-black text-slate-900 dark:text-white pt-2">
                                        <span>Total</span>
                                        <span>₹{total}</span>
                                    </div>
                                </div>

                                <button
                                    onClick={generateBill}
                                    disabled={cart.length === 0 || generatingBill}
                                    className="w-full py-5 bg-agro-600 text-white rounded-3xl font-black text-sm uppercase tracking-[0.2em] shadow-xl shadow-agro-600/30 flex items-center justify-center gap-3 group disabled:opacity-50"
                                >
                                    {generatingBill ? (
                                        <Loader2 className="w-6 h-6 animate-spin" />
                                    ) : (
                                        <>
                                            <Receipt className="w-6 h-6 group-hover:rotate-12 transition-transform" />
                                            <span>CHECKOUT & GET BILL</span>
                                        </>
                                    )}
                                </button>
                                <div className="flex items-center justify-center gap-4 text-[10px] font-black text-slate-400 uppercase tracking-widest">
                                    <ShieldCheck className="w-3 h-3 text-agro-500" />
                                    Secure SSL Encrypted Checkout
                                </div>
                            </div>
                        </motion.div>
                    </>
                )}
            </AnimatePresence>
        </main>
    );
}
