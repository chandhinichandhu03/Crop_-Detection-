#!/bin/bash

# Agro Doctor Unified Startup Script
echo "🚀 Starting Agro Doctor Ecosystem..."

# Cleanup: Kill any processes already using the standard ports
echo "🧹 Cleaning up existing processes..."
lsof -ti :3000,5000,8000 | xargs kill -9 2>/dev/null || true

# Install concurrently if missing
if ! npx concurrently --version &> /dev/null; then
    echo "📦 Installing startup dependencies..."
    npm install
fi

# Run everything
npm start
