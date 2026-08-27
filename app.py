import customtkinter as ctk
import pyautogui
import pyperclip
import threading
import time
from pynput import keyboard

# CustomTkinter Theme Setup
ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("blue")

class TypeFlowApp(ctk.CTk):
    def __init__(self):
        super().__init__()

        self.title("TypeFlow Studio Pro (Cross-Platform)")
        self.geometry("420x560")
        self.resizable(False, False)

        self.is_running = False
        self.is_paused = False
        self.target_text = ""
        self.current_index = 0
        self.total_duration = 10

        # Header
        self.header_label = ctk.CTkLabel(
            self, text="⚡ TypeFlow Studio Pro", font=ctk.CTkFont(size=18, weight="bold"), text_color="#818cf8"
        )
        self.header_label.pack(pady=(15, 5))

        # Text Area
        self.text_box = ctk.CTkTextbox(self, width=380, height=140, corner_radius=8)
        self.text_box.pack(pady=10)
        self.text_box.insert("0.0", " ")

        # Duration Grid
        self.time_frame = ctk.CTkFrame(self, width=380, fg_color="#1e293b", corner_radius=8)
        self.time_frame.pack(pady=5, padx=20, fill="x")

        self.min_label = ctk.CTkLabel(self.time_frame, text="Minutes:", font=ctk.CTkFont(size=12))
        self.min_label.grid(row=0, column=0, padx=(15, 5), pady=10)
        self.min_entry = ctk.CTkEntry(self.time_frame, width=50)
        self.min_entry.insert(0, "0")
        self.min_entry.grid(row=0, column=1, padx=5, pady=10)

        self.sec_label = ctk.CTkLabel(self.time_frame, text="Seconds:", font=ctk.CTkFont(size=12))
        self.sec_label.grid(row=0, column=2, padx=(15, 5), pady=10)
        self.sec_entry = ctk.CTkEntry(self.time_frame, width=50)
        self.sec_entry.insert(0, "10")
        self.sec_entry.grid(row=0, column=3, padx=5, pady=10)

        # Status Label
        self.status_label = ctk.CTkLabel(
            self, text="Status: Ready", text_color="#34d399", font=ctk.CTkFont(size=12, weight="bold")
        )
        self.status_label.pack(pady=8)

        # Buttons
        self.btn_frame = ctk.CTkFrame(self, fg_color="transparent")
        self.btn_frame.pack(pady=5)

        self.deploy_btn = ctk.CTkButton(
            self.btn_frame, text="Save & Activate", width=180, command=self.activate_typing, fg_color="#6366f1", hover_color="#4f46e5"
        )
        self.deploy_btn.grid(row=0, column=0, padx=5)

        self.clear_btn = ctk.CTkButton(
            self.btn_frame, text="Clear", width=80, command=self.clear_text, fg_color="#334155", hover_color="#ef4444"
        )
        self.clear_btn.grid(row=0, column=1, padx=5)

        # Shortcuts Info Card
        self.hint_card = ctk.CTkFrame(self, fg_color="#0f172a", corner_radius=8)
        self.hint_card.pack(pady=12, padx=20, fill="x")

        self.hint_text = ctk.CTkLabel(
            self.hint_card,
            text="⚡ Start / Resume: Alt + Shift + X (or Ctrl + Alt + K)\n⛔ Pause: Press ESC (Resumes from where left off)\n✔ Auto-clears box when finished",
            font=ctk.CTkFont(size=11),
            text_color="#94a3b8",
            justify="left"
        )
        self.hint_text.pack(padx=12, pady=10)

        # Cross-Platform Hotkey Listener using pynput
        self.start_hotkey_listener()

    def start_hotkey_listener(self):
        hotkeys = {
            '<alt>+<shift>+x': self.trigger_start_or_resume,
            '<ctrl>+<alt>+k': self.trigger_start_or_resume,
            '<esc>': self.handle_esc
        }
        self.listener = keyboard.GlobalHotKeys(hotkeys)
        self.listener.daemon = True
        self.listener.start()

    def clear_text(self):
        self.text_box.delete("0.0", "end")
        self.target_text = ""
        self.current_index = 0
        self.is_paused = False
        self.status_label.configure(text="Status: Cleared", text_color="#ef4444")

    def activate_typing(self):
        text = self.text_box.get("0.0", "end").strip()
        if not text or text == "Paste your text here...":
            self.status_label.configure(text="Status: Enter text first!", text_color="#ef4444")
            return
        self.target_text = text
        self.current_index = 0
        self.is_paused = False
        self.status_label.configure(text="Status: Activated! Press Alt+Shift+X", text_color="#34d399")

    def trigger_start_or_resume(self):
        if not self.is_running:
            threading.Thread(target=self.run_typing, daemon=True).start()

    def handle_esc(self):
        if self.is_running:
            self.is_running = False
            self.is_paused = True
            percent = int((self.current_index / len(self.target_text)) * 100) if self.target_text else 0
            self.status_label.configure(text=f"Status: Paused at {percent}% (Press Alt+Shift+X to Resume)", text_color="#f59e0b")

    def run_typing(self):
        if not self.target_text:
            text = self.text_box.get("0.0", "end").strip()
            if not text or text == "Paste your text here...":
                return
            self.target_text = text
            self.current_index = 0

        try:
            mins = int(self.min_entry.get())
            secs = int(self.sec_entry.get())
            self.total_duration = (mins * 60) + secs
            if self.total_duration <= 0:
                self.total_duration = 10
        except ValueError:
            self.total_duration = 10

        self.is_running = True
        self.is_paused = False

        total_chars = len(self.target_text)
        time_per_char = self.total_duration / total_chars
        start_time = time.perf_counter() - (self.current_index * time_per_char)

        try:
            pyperclip.copy("")
        except Exception:
            pass

        time.sleep(0.3)  # Brief OS transition buffer

        while self.current_index < total_chars and self.is_running:
            char = self.target_text[self.current_index]

            expected_elapsed = (self.current_index + 1) * time_per_char
            actual_elapsed = time.perf_counter() - start_time
            wait_time = expected_elapsed - actual_elapsed
            
            if wait_time > 0:
                time.sleep(wait_time)

            if not self.is_running:
                break

            if char == '\n':
                pyautogui.press('enter')
            else:
                pyautogui.write(char)

            self.current_index += 1

            percent = int((self.current_index / total_chars) * 100)
            self.after(0, lambda p=percent: self.status_label.configure(
                text=f"Status: Typing... {p}%", text_color="#60a5fa"
            ))

        self.is_running = False

        if self.current_index >= total_chars and not self.is_paused:
            self.current_index = 0
            self.target_text = ""
            self.after(0, lambda: [
                self.text_box.delete("0.0", "end"),
                self.status_label.configure(text="Status: Done & Auto-Cleared! ✔", text_color="#34d399")
            ])

if __name__ == "__main__":
    app = TypeFlowApp()
    app.mainloop()