const express = require('express');
const cors = require('cors');
const dotenv = require('dotenv');
const mongoose = require('mongoose');

dotenv.config();

const app = express();
const PORT = process.env.PORT || 5000;

// Middleware
app.use(cors());
app.use(express.json());

// Mock Database with high-quality Amazon-style product images and usage data
const products = [
    {
        id: 1,
        name: "Organic Pesticide",
        category: "Organic",
        price: 450,
        description: "Pure organic pesticide for all types of crops.",
        usage: "Mix 5ml with 1L water. Spray mornings.",
        image: "https://images.unsplash.com/photo-1592982537447-7440770cbfc9?auto=format&fit=crop&q=80&w=800&h=800"
    },
    {
        id: 2,
        name: "Hybrid Tomato Seeds",
        category: "Seeds",
        price: 850,
        description: "High-yield disease resistant tomato seeds.",
        usage: "Sow 1/4 inch deep in trays. Water daily.",
        image: "https://images.unsplash.com/photo-1542332213-9b5a5a3fad35?auto=format&fit=crop&q=80&w=800&h=800"
    },
    {
        id: 3,
        name: "Cold-Pressed Neem Oil",
        category: "Organic",
        price: 200,
        description: "Natural pest repellent and antifungal oil.",
        usage: "Mix 4ml in 1L soapy water. Spray leaves.",
        image: "https://images.unsplash.com/photo-1628352081506-83c43123ed6d?auto=format&fit=crop&q=80&w=800&h=800"
    },
    {
        id: 4,
        name: "NPK 19-19-19 Soluble",
        category: "Fertilizer",
        price: 350,
        description: "Balanced fertilizer for growth and bloom.",
        usage: "Mix 5g in 2L water. Apply to roots.",
        image: "https://images.unsplash.com/photo-1581093191140-5e6402ec9f44?auto=format&fit=crop&q=80&w=800&h=800"
    },
    {
        id: 5,
        name: "Bio-Fertilizer (BGA)",
        category: "Fertilizer",
        price: 150,
        description: "Natural nitrogen-fixing blue green algae.",
        usage: "Apply 10kg/acre in standing water field.",
        image: "https://images.unsplash.com/photo-1589923188900-85dae523342b?auto=format&fit=crop&q=80&w=800&h=800"
    },
    {
        id: 6,
        name: "Sonamasuri Paddy Seeds",
        category: "Seeds",
        price: 1200,
        description: "Authentic fine grain paddy seeds.",
        usage: "Sow in nursery beds; transplant in 25 days.",
        image: "https://images.unsplash.com/photo-1543157148-f819d161763f?auto=format&fit=crop&q=80&w=800&h=800"
    },
    {
        id: 7,
        name: "Trichoderma Fungicide",
        category: "Organic",
        price: 280,
        description: "Biological control agent for soil diseases.",
        usage: "Mix 1kg with manure and spread in soil.",
        image: "https://images.unsplash.com/photo-1595273670150-bd0c3c392e46?auto=format&fit=crop&q=80&w=800&h=800"
    },
    {
        id: 8,
        name: "Bio-Insecticide (Acephate)",
        category: "Insecticide",
        price: 550,
        description: "Systemic insecticide for sucking and biting insects.",
        usage: "Mix 2g per Liter of water. Spray on foliage.",
        image: "https://images.unsplash.com/photo-1585314062340-f1a5a7c9328d?auto=format&fit=crop&q=80&w=800&h=800"
    },
    {
        id: 9,
        name: "Broad Spectrum Pesticide",
        category: "Pesticide",
        price: 680,
        description: "Powerful pesticide for diverse crop protection.",
        usage: "Dilute 3ml in 1L water. Apply every 15 days.",
        image: "https://images.unsplash.com/photo-1605000797499-95a51c5269ae?auto=format&fit=crop&q=80&w=800&h=800"
    }
];

// Routes
app.get('/api/products', (req, res) => {
    res.json(products);
});

app.get('/api/health', (req, res) => {
    res.json({ status: "Backend is healthy", version: "2.0.0" });
});

// Start Server
app.listen(PORT, () => {
    console.log(`Backend server running on http://localhost:${PORT}`);
});
