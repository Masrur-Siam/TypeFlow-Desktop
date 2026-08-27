# ⚡ TypeFlow Desktop Pro

**TypeFlow Desktop Pro** is a modern, cross-platform auto-typer application designed to simulate natural human typing across any code editor, text processor, or browser. It works seamlessly on **Windows, macOS, and Linux** with a zero-setup, 1-click launch experience.

---

## ✨ Key Features

- ⏱ **Smart Duration Control:** Set custom minutes and seconds to ensure typing finishes within your exact timeframe.
- ⌨ **Conflict-Free Global Hotkeys:** Built with unique system shortcuts that prevent OS-level paste collisions.
- ⏸ **Smart Pause & Resume:** Hit `ESC` to pause and resume later from the exact character where you left off.
- 📊 **Real-Time Progress:** Dynamic live percentage tracker (`0%` to `100%`) on the UI.
- 🧹 **Auto-Clear:** Automatically clears the input box once typing completes successfully.
- 🚀 **1-Click Launchers:** Pre-configured executable scripts for Windows, macOS, and Linux—no manual pip commands required.

---

## 🚀 How to Run (1-Click Setup)

Clone or download the project as a ZIP, extract it, and follow the instructions for your operating system:

### 🪟 Windows
1. Double-click the **`run_windows.bat`** file.
*(It will automatically install missing dependencies and launch the application).*

### 🍎 macOS
1. Double-click the **`run_mac.command`** file.
> **Note for macOS Users:** To allow global hotkeys, grant Accessibility permissions to your Terminal/IDE via:  
> `System Settings` ➔ `Privacy & Security` ➔ `Accessibility` ➔ Toggle **ON** for your Terminal.

### 🐧 Linux (Ubuntu / Debian / Mint)
1. Right-click **`run_linux.desktop`** and select **"Allow Launching"**.
2. Double-click the file to start the application.

---

## ⌨️ Shortcuts & Controls

| Action | Shortcut Key | Description |
| :--- | :--- | :--- |
| **Start / Resume** | `Alt + Shift + X` | Starts typing or resumes from paused position |
| **Alternative Start** | `Ctrl + Alt + K` | Secondary trigger for starting/resuming |
| **Pause / Stop** | `ESC` | Immediately pauses typing |

### 📝 Step-by-Step Usage:
1. Open **TypeFlow Desktop Pro** and paste your text into the input area.
2. Set your desired typing duration (Minutes & Seconds) and click **Save & Activate**.
3. Switch to your target software (VS Code, Notepad, Browser, Discord, etc.) and place your cursor where you want to type.
4. Press **`Alt + Shift + X`** to begin typing.

---

## 🛠️ Manual Installation (Optional)

If you prefer to run the application manually from the terminal:

```bash
# 1. Install dependencies
pip install -r requirements.txt

# 2. Run the application
python app.py
