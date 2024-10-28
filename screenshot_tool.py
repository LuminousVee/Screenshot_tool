import tkinter as tk
from tkinter import ttk, messagebox
from PIL import ImageGrab
import os
from datetime import datetime
import time
import json

class ScreenshotTool:
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("Screenshot Tool")
        self.root.geometry("400x500")
        
        # Initialize variables
        self.screenshot_count = 0
        self.auto_capture_active = False
        self.setup_variables()
        self.create_output_directory()
        self.create_gui()

    def setup_variables(self):
        """Initialize all GUI variables"""
        self.delay_var = tk.StringVar(value="5")
        self.auto_delay_var = tk.StringVar(value="30")
        self.auto_minimize_var = tk.BooleanVar(value=True)
        
    def create_output_directory(self):
        """Create directory for saving screenshots"""
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        self.output_dir = f"screenshots_{timestamp}"
        if not os.path.exists(self.output_dir):
            os.makedirs(self.output_dir)
            
    def create_gui(self):
        """Create the main GUI elements"""
        # Create main frame
        main_frame = ttk.Frame(self.root, padding="10")
        main_frame.pack(fill=tk.BOTH, expand=True)
        
        # Instant capture button
        ttk.Button(
            main_frame, 
            text="Take Screenshot Now",
            command=self.take_screenshot
        ).pack(fill=tk.X, pady=5)
        
        # Delayed capture frame
        delay_frame = ttk.LabelFrame(main_frame, text="Delayed Capture", padding="5")
        delay_frame.pack(fill=tk.X, pady=5)
        
        ttk.Label(delay_frame, text="Delay (seconds):").pack(side=tk.LEFT)
        ttk.Entry(
            delay_frame,
            textvariable=self.delay_var,
            width=5
        ).pack(side=tk.LEFT, padx=5)
        
        ttk.Button(
            delay_frame,
            text="Take Delayed Screenshot",
            command=self.delayed_screenshot
        ).pack(side=tk.LEFT, padx=5)
        
        # Auto capture frame
        auto_frame = ttk.LabelFrame(main_frame, text="Auto Capture", padding="5")
        auto_frame.pack(fill=tk.X, pady=5)
        
        ttk.Label(auto_frame, text="Interval (seconds):").pack(side=tk.LEFT)
        ttk.Entry(
            auto_frame,
            textvariable=self.auto_delay_var,
            width=5
        ).pack(side=tk.LEFT, padx=5)
        
        self.auto_capture_btn = ttk.Button(
            auto_frame,
            text="Start Auto Capture",
            command=self.toggle_auto_capture
        )
        self.auto_capture_btn.pack(side=tk.LEFT, padx=5)
        
        # Options frame
        options_frame = ttk.LabelFrame(main_frame, text="Options", padding="5")
        options_frame.pack(fill=tk.X, pady=5)
        
        ttk.Checkbutton(
            options_frame,
            text="Auto-minimize before capture",
            variable=self.auto_minimize_var
        ).pack(pady=5)
        
        # Statistics frame
        stats_frame = ttk.LabelFrame(main_frame, text="Statistics", padding="5")
        stats_frame.pack(fill=tk.X, pady=5)
        
        self.stats_label = ttk.Label(stats_frame, text="Screenshots taken: 0")
        self.stats_label.pack(pady=5)
        
        # Status bar
        self.status_label = ttk.Label(
            self.root,
            text="Ready",
            relief=tk.SUNKEN,
            padding="2"
        )
        self.status_label.pack(side=tk.BOTTOM, fill=tk.X)

    def update_status(self, message):
        """Update status bar message"""
        self.status_label.config(text=message)
        print(message)

    def take_screenshot(self):
        """Take a screenshot"""
        try:
            if self.auto_minimize_var.get():
                self.root.iconify()
                time.sleep(0.5)

            # Take the screenshot
            screenshot = ImageGrab.grab()
            
            # Generate filename
            timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
            filename = f"screenshot_{timestamp}.png"
            filepath = os.path.join(self.output_dir, filename)
            
            # Save the screenshot
            screenshot.save(filepath)
            
            # Update statistics
            self.screenshot_count += 1
            self.stats_label.config(text=f"Screenshots taken: {self.screenshot_count}")
            
            if self.auto_minimize_var.get():
                self.root.deiconify()
                
            self.update_status(f"Saved: {filename}")

        except Exception as e:
            self.update_status(f"Error: {str(e)}")
            messagebox.showerror("Error", f"Failed to take screenshot: {str(e)}")

    def delayed_screenshot(self):
        """Take a screenshot after specified delay"""
        try:
            delay = int(self.delay_var.get())
            self.update_status(f"Taking screenshot in {delay} seconds...")
            self.root.after(delay * 1000, self.take_screenshot)
        except ValueError:
            messagebox.showerror("Error", "Please enter a valid number of seconds")

    def toggle_auto_capture(self):
        """Toggle automatic capture mode"""
        if not self.auto_capture_active:
            try:
                interval = int(self.auto_delay_var.get())
                self.auto_capture_active = True
                self.auto_capture_btn.config(text="Stop Auto Capture")
                self.update_status("Auto capture started")
                self.auto_capture(interval)
            except ValueError:
                messagebox.showerror("Error", "Please enter a valid interval in seconds")
        else:
            self.auto_capture_active = False
            self.auto_capture_btn.config(text="Start Auto Capture")
            self.update_status("Auto capture stopped")

    def auto_capture(self, interval):
        """Perform auto capture at specified interval"""
        if self.auto_capture_active:
            self.take_screenshot()
            self.root.after(interval * 1000, lambda: self.auto_capture(interval))

    def on_closing(self):
        """Handle window closing"""
        if self.auto_capture_active:
            if messagebox.askokcancel("Quit", "Auto capture is active. Do you want to quit?"):
                self.root.destroy()
        else:
            self.root.destroy()

    def run(self):
        """Start the application"""
        self.root.protocol("WM_DELETE_WINDOW", self.on_closing)
        self.root.mainloop()

def main():
    try:
        app = ScreenshotTool()
        app.run()
    except Exception as e:
        print(f"Error starting application: {str(e)}")
        input("Press Enter to exit...")

if __name__ == "__main__":
    main()
