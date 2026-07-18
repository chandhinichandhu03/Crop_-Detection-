import os
import sys
import subprocess
import time
import signal
import socket

# Config
ROOT_DIR = os.path.dirname(os.path.abspath(__file__))
BACKEND_DIR = os.path.join(ROOT_DIR, "backend")
FRONTEND_DIR = os.path.join(ROOT_DIR, "frontend")
VENV_DIR = os.path.join(BACKEND_DIR, "venv")

def is_port_in_use(port: int) -> bool:
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        return s.connect_ex(('localhost', port)) == 0

def kill_process_on_port(port: int):
    try:
        if os.name == 'posix':
            # MacOS/Linux
            pid = subprocess.check_output(["lsof", "-t", f"-i:{port}"]).decode().strip()
            if pid:
                pids = pid.split('\n')
                for p in pids:
                    os.kill(int(p), signal.SIGKILL)
                print(f"🧹 Terminated existing processes using port {port}")
        elif os.name == 'nt':
            # Windows
            out = subprocess.check_output(f"netstat -ano | findstr :{port}", shell=True).decode().strip()
            if out:
                lines = out.split('\n')
                pids = set([line.strip().split()[-1] for line in lines if line.strip()])
                for pid in pids:
                    subprocess.run(f"taskkill /F /PID {pid}", shell=True)
                print(f"🧹 Terminated existing processes using port {port}")
    except Exception:
        pass

def setup_backend():
    print("🌿 Preparing local Python FastAPI backend...")
    
    # 1. Create virtual environment
    if not os.path.exists(VENV_DIR):
        print("📦 Creating virtual environment in backend/venv...")
        subprocess.run([sys.executable, "-m", "venv", VENV_DIR], check=True)
        
    # Get local virtual env python binary path
    if os.name == 'nt':
        venv_python = os.path.join(VENV_DIR, "Scripts", "python.exe")
        venv_pip = os.path.join(VENV_DIR, "Scripts", "pip.exe")
    else:
        venv_python = os.path.join(VENV_DIR, "bin", "python")
        venv_pip = os.path.join(VENV_DIR, "bin", "pip")
        
    # 2. Upgrade pip and install packages
    print("📥 Installing/Upgrading python backend requirements...")
    reqs_path = os.path.join(BACKEND_DIR, "requirements.txt")
    subprocess.run([venv_python, "-m", "pip", "install", "--upgrade", "pip"], check=True)
    subprocess.run([venv_python, "-m", "pip", "install", "-r", reqs_path], check=True)
    
    return venv_python

def setup_frontend():
    print("⚛️ Preparing Next.js 15 frontend...")
    node_modules = os.path.join(FRONTEND_DIR, "node_modules")
    
    # Run npm install if node_modules doesn't exist
    if not os.path.exists(node_modules):
        print("📦 Installing frontend npm dependencies...")
        subprocess.run(["npm", "install"], cwd=FRONTEND_DIR, shell=(os.name == 'nt'), check=True)
    else:
        print("✅ Frontend node_modules already present.")

def main():
    print("🚀 Initiating Agro Doctor Ecosystem...")
    
    # Clean up standard ports
    kill_process_on_port(3000)
    kill_process_on_port(8000)
    
    # Setup environments
    python_bin = setup_backend()
    setup_frontend()
    
    processes = []
    
    try:
        # Start Python Backend on port 8000
        print("🔥 Starting FastAPI backend on http://localhost:8000 ...")
        backend_proc = subprocess.Popen(
            [python_bin, "-m", "uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"],
            cwd=BACKEND_DIR
        )
        processes.append(backend_proc)
        
        # Start Next.js Frontend on port 3000
        print("⚡ Starting Next.js frontend on http://localhost:3000 ...")
        frontend_proc = subprocess.Popen(
            ["npm", "run", "dev"],
            cwd=FRONTEND_DIR,
            shell=(os.name == 'nt')
        )
        processes.append(frontend_proc)
        
        print("\n🎉 Both services are running successfully!")
        print("👉 Access the web interface at: http://localhost:3000")
        print("👉 Access API Swagger documentation at: http://localhost:8000/docs")
        print("\nPress Ctrl+C to stop both services.")
        
        # Keep runner alive
        while True:
            time.sleep(1)
            
    except KeyboardInterrupt:
        print("\n🛑 Keyboard interrupt received. Shutting down ecosystem processes...")
    finally:
        for p in processes:
            try:
                p.terminate()
                p.wait(timeout=2)
            except Exception:
                try:
                    p.kill()
                except Exception:
                    pass
        print("👋 Ecosystem shut down cleanly.")

if __name__ == "__main__":
    main()
