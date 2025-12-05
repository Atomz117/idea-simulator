# Idea Simulator Lab - Quick Start

## How to Run
1.  **Open Terminal** on your Mac.
2.  **Go to the folder**:
    ```bash
    cd /Users/rajdeepmalladeb/Downloads/aiall
    ```
3.  **Start the Server**:
    ```bash
    python3 app.py
    ```
4.  **Open your Browser** and go to:
    [http://127.0.0.1:5000](http://127.0.0.1:5000)

## How to Use
1.  Type your business idea in the box.
2.  Click **Simulate**.
3.  Wait for the analysis.
4.  Read your report and click **Download** to save it.


## How to Stop
- Press `Control + C` in the terminal window to stop the server.

## Remote Access (Tunneling)
To share the simulation with others or test on mobile:
1.  Open a new terminal tab.
2.  Run the tunnel script:
    ```bash
    ./start_tunnel.sh
    ```

3.  Copy the `https://...` link provided in the output and share it.

## ⚠️ Important Disclaimer
- **Keep Your Laptop Open**: The server and remote link will **STOP** working if your laptop goes to sleep or if you close the lid. You must keep your computer awake and connected to Wi-Fi.

- **Stopping**: The server does not stop automatically. You must press `Control + C` in the terminal to shut it down when you are finished.

## 🚀 Quick Execution
**1. Start App:** Paste this to start the simulator:
```bash
cd /Users/rajdeepmalladeb/Downloads/aiall && python3 app.py
```

**2. Start Tunnel:** (Open a NEW terminal tab and paste this):
```bash
cd /Users/rajdeepmalladeb/Downloads/aiall && ./start_tunnel.sh
```

**3. Access Links:**
- **Local (Laptop):** [http://127.0.0.1:5000](http://127.0.0.1:5000)
- **Remote (Mobile):** [https://dbd847612d35a9.lhr.life](https://dbd847612d35a9.lhr.life) *(Note: Check terminal output if this changes)*

to end it and kill the server press CTRL + C in the terminal window.