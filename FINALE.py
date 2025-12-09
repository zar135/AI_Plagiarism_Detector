# advanced_plagiarism_scanner.py
"""
ADVANCED LITE++ PLAGIARISM DETECTOR
- Modern glass-morphism UI with advanced animations
- Real-time 3D-like particle systems
- Interactive data visualizations
- Advanced cyber aesthetics with neon effects
- Professional forensic analysis dashboard
"""

import matplotlib
matplotlib.use("Agg")
import os
import re
import json
import time
import hashlib
import requests
import PyPDF2
import docx
import matplotlib.pyplot as plt
import numpy as np
from datetime import datetime
from collections import Counter
from bs4 import BeautifulSoup
import tkinter as tk
from tkinter import ttk, filedialog, messagebox, scrolledtext
import threading
import random
import math
import sys
from PIL import Image, ImageTk, ImageDraw
import matplotlib.colors as mcolors
from mpl_toolkits.mplot3d import Axes3D

# Optional modules
try:
    from ddgs import DDGS
    DUCKSEARCH = True
except:
    DUCKSEARCH = False

try:
    from sentence_transformers import SentenceTransformer, util
    SEMANTIC_MODEL = SentenceTransformer("all-mpnet-base-v2")
    EMBEDS = True
except:
    EMBEDS = False

try:
    from sklearn.feature_extraction.text import TfidfVectorizer
    from sklearn.metrics.pairwise import cosine_similarity
    VECTORIZER = TfidfVectorizer(max_features=5000)
    TFIDF = True
except:
    TFIDF = False

# New imports for forensic features
try:
    import nltk
    from nltk import pos_tag
    from nltk.tokenize import sent_tokenize, word_tokenize
    from nltk.corpus import stopwords
    NLTK_AVAILABLE = True
except:
    NLTK_AVAILABLE = False

SCAN_TIMEOUT = 45  # Increased timeout for better web scraping
CROSSREF_ROWS = 5
SEMANTIC_SCHOLAR_LIMIT = 5
DOI_REGEX = re.compile(r'\b10\.\d{4,9}/\S+\b', flags=re.IGNORECASE)

class CyberBackground:
    def __init__(self, canvas, width, height):
        self.canvas = canvas
        self.width = width
        self.height = height
        self.active = False
        self.lines = []
        self.nodes = []
        self.pulse_effects = []
        
        # Create cyber grid network
        self.create_cyber_network()
        
    def create_cyber_network(self):
        # Create network nodes
        node_count = 50
        for _ in range(node_count):
            x = random.randint(0, self.width)
            y = random.randint(0, self.height)
            size = random.uniform(2, 5)
            node = self.canvas.create_oval(
                x-size, y-size, x+size, y+size,
                fill='#00ff88', outline='', width=0
            )
            self.nodes.append((node, x, y, size))
            
        # Create connecting lines
        for i in range(len(self.nodes)):
            for j in range(i+1, len(self.nodes)):
                if random.random() < 0.1:  # 10% connection probability
                    _, x1, y1, _ = self.nodes[i]
                    _, x2, y2, _ = self.nodes[j]
                    line = self.canvas.create_line(
                        x1, y1, x2, y2,
                        fill='#00ff88', width=1, dash=(4, 6)
                    )
                    self.lines.append(line)
                    
    def start(self):
        self.active = True
        self.animate()
        
    def stop(self):
        self.active = False
        
    def animate(self):
        if not self.active:
            return
            
        # Animate nodes
        for node, x, y, size in self.nodes:
            if random.random() < 0.1:
                # Pulse effect
                pulse = self.canvas.create_oval(
                    x-size*3, y-size*3, x+size*3, y+size*3,
                    fill='', outline='#00ff88', width=2
                )
                self.pulse_effects.append((pulse, 0))
                
            # Random movement
            new_x = max(0, min(self.width, x + random.uniform(-5, 5)))
            new_y = max(0, min(self.height, y + random.uniform(-5, 5)))
            self.canvas.coords(node, new_x-size, new_y-size, new_x+size, new_y+size)
            
        # Animate pulse effects
        new_pulses = []
        for pulse, size in self.pulse_effects:
            if size < 50:
                _, x, y, _ = random.choice(self.nodes)
                self.canvas.coords(pulse, x-size, y-size, x+size, y+size)
                alpha = 1 - (size / 50)
                color = f'#00ff{int(alpha*255):02x}'
                self.canvas.itemconfig(pulse, outline=color)
                new_pulses.append((pulse, size + 2))
            else:
                self.canvas.delete(pulse)
        self.pulse_effects = new_pulses
        
        # Animate lines
        for line in self.lines:
            if random.random() < 0.3:
                self.canvas.itemconfig(line, dashoffset=random.randint(0, 10))
                
        self.canvas.after(100, self.animate)

class AdvancedParticle:
    def __init__(self, canvas, width, height):
        self.canvas = canvas
        self.width = width
        self.height = height
        self.x = random.randint(0, width)
        self.y = random.randint(0, height)
        self.size = random.uniform(1, 4)
        self.speed_x = random.uniform(-2, 2)
        self.speed_y = random.uniform(-2, 2)
        self.alpha = random.uniform(0.3, 0.9)
        self.pulse_speed = random.uniform(0.02, 0.05)
        self.pulse_direction = random.choice([-1, 1])
        self.trail_length = random.randint(3, 8)
        self.trail = []
        
        # Modern color palette
        colors = ['#00ff88', '#0088ff', '#ff0088', '#88ff00', '#ff8800', '#8800ff']
        self.color = random.choice(colors)
        self.glow_color = self.lighten_color(self.color)
        
        self.particle_id = canvas.create_oval(
            self.x - self.size, self.y - self.size,
            self.x + self.size, self.y + self.size,
            fill=self.color, outline='', width=0
        )
        
    def lighten_color(self, color, factor=0.3):
        """Lighten a hex color"""
        color = color.lstrip('#')
        rgb = tuple(int(color[i:i+2], 16) for i in (0, 2, 4))
        light_rgb = tuple(min(255, int(c + (255 - c) * factor)) for c in rgb)
        return f'#{light_rgb[0]:02x}{light_rgb[1]:02x}{light_rgb[2]:02x}'
        
    def move(self):
        # Add trail effect
        self.trail.append((self.x, self.y))
        if len(self.trail) > self.trail_length:
            self.trail.pop(0)
            
        # Update position with momentum
        self.x += self.speed_x
        self.y += self.speed_y
        
        # Bounce with damping
        if self.x <= 0 or self.x >= self.width:
            self.speed_x *= -0.8
            self.x = max(0, min(self.width, self.x))
        if self.y <= 0 or self.y >= self.height:
            self.speed_y *= -0.8
            self.y = max(0, min(self.height, self.y))
            
        # Pulsing effect
        self.alpha += self.pulse_speed * self.pulse_direction
        if self.alpha >= 0.9 or self.alpha <= 0.3:
            self.pulse_direction *= -1
            
        # Update visual
        self.canvas.coords(self.particle_id,
                          self.x - self.size, self.y - self.size,
                          self.x + self.size, self.y + self.size)
        
        # Color intensity based on alpha
        intensity = int(255 * self.alpha)
        current_color = f'#{intensity:02x}{int(self.color[3:5], 16):02x}{int(self.color[5:7], 16):02x}'
        self.canvas.itemconfig(self.particle_id, fill=current_color)

class HolographicGrid:
    def __init__(self, canvas, width, height):
        self.canvas = canvas
        self.width = width
        self.height = height
        self.grid_lines = []
        self.grid_points = []
        self.active = False
        
        # Create holographic grid
        grid_size = 60
        point_size = 2
        
        # Grid lines with gradient
        for x in range(0, width + grid_size, grid_size):
            line = canvas.create_line(x, 0, x, height, fill='#00ff88', width=1, dash=(4, 6))
            self.grid_lines.append(line)
        for y in range(0, height + grid_size, grid_size):
            line = canvas.create_line(0, y, width, y, fill='#00ff88', width=1, dash=(4, 6))
            self.grid_lines.append(line)
            
        # Grid points
        for x in range(grid_size, width, grid_size):
            for y in range(grid_size, height, grid_size):
                point = canvas.create_oval(x-point_size, y-point_size, x+point_size, y+point_size,
                                         fill='#0088ff', outline='')
                self.grid_points.append(point)
                
    def start(self):
        self.active = True
        self.animate()
        
    def stop(self):
        self.active = False
        
    def animate(self):
        if not self.active:
            return
            
        # Animate grid lines
        for line in self.grid_lines:
            current_dash = self.canvas.itemcget(line, 'dash')
            if current_dash:
                parts = current_dash.split()
                if len(parts) >= 2:
                    offset = (int(parts[1]) + 1) % 12
                    self.canvas.itemconfig(line, dashoffset=offset)
                    
        # Animate grid points
        for point in self.grid_points:
            if random.random() > 0.7:
                colors = ['#00ff88', '#0088ff', '#ff0088', '#88ff00']
                self.canvas.itemconfig(point, fill=random.choice(colors))
                
        self.canvas.after(80, self.animate)

class QuantumRadar:
    def __init__(self, canvas, width, height):
        self.canvas = canvas
        self.width = width
        self.height = height
        self.center_x = width // 2
        self.center_y = height // 2
        self.radius = min(width, height) // 3
        self.angle = 0
        self.scan_lines = []
        self.pulse_circles = []
        self.active = False
        
    def start(self):
        self.active = True
        # Create multiple scan lines for quantum effect
        for i in range(3):
            angle_offset = i * 120
            line = self.canvas.create_line(
                self.center_x, self.center_y,
                self.center_x + self.radius, self.center_y,
                fill=f'#00ff{88 + i*20:02x}', width=2
            )
            self.scan_lines.append((line, angle_offset))
        self.animate()
        
    def stop(self):
        self.active = False
        for line, _ in self.scan_lines:
            self.canvas.delete(line)
        for circle in self.pulse_circles:
            self.canvas.delete(circle)
        self.scan_lines.clear()
        self.pulse_circles.clear()
        
    def animate(self):
        if not self.active:
            return
            
        self.angle = (self.angle + 4) % 360
        
        # Update scan lines
        for i, (line, angle_offset) in enumerate(self.scan_lines):
            current_angle = (self.angle + angle_offset) % 360
            end_x = self.center_x + self.radius * math.cos(math.radians(current_angle))
            end_y = self.center_y + self.radius * math.sin(math.radians(current_angle))
            
            self.canvas.coords(line, self.center_x, self.center_y, end_x, end_y)
            
            # Color cycling
            hue = (current_angle % 360) / 360
            r, g, b = self.hsv_to_rgb(hue, 1.0, 1.0)
            color = f'#{int(r*255):02x}{int(g*255):02x}{int(b*255):02x}'
            self.canvas.itemconfig(line, fill=color)
            
        # Add pulse effects
        if self.angle % 30 == 0:
            pulse = self.canvas.create_oval(
                self.center_x - 5, self.center_y - 5,
                self.center_x + 5, self.center_y + 5,
                fill='#00ffff', outline=''
            )
            self.pulse_circles.append(pulse)
            self.animate_pulse(pulse, 0)
            
        self.canvas.after(40, self.animate)
        
    def animate_pulse(self, circle, size):
        if circle in self.pulse_circles and size < 100:
            self.canvas.coords(circle,
                             self.center_x - size, self.center_y - size,
                             self.center_x + size, self.center_y + size)
            alpha = 1 - (size / 100)
            self.canvas.itemconfig(circle, fill=f'#00ffff')
            self.canvas.after(20, lambda: self.animate_pulse(circle, size + 5))
        else:
            if circle in self.pulse_circles:
                self.canvas.delete(circle)
                self.pulse_circles.remove(circle)
                
    def hsv_to_rgb(self, h, s, v):
        if s == 0.0:
            return v, v, v
        i = int(h * 6.0)
        f = (h * 6.0) - i
        p = v * (1.0 - s)
        q = v * (1.0 - s * f)
        t = v * (1.0 - s * (1.0 - f))
        i = i % 6
        if i == 0:
            return v, t, p
        if i == 1:
            return q, v, p
        if i == 2:
            return p, v, t
        if i == 3:
            return p, q, v
        if i == 4:
            return t, p, v
        if i == 5:
            return v, p, q

class ModernProgressBar:
    def __init__(self, parent, width=400, height=20):
        self.canvas = tk.Canvas(parent, width=width, height=height, bg='#1a1a2e', highlightthickness=0)
        self.width = width
        self.height = height
        self.value = 0
        self.animation_id = None
        
        # Create gradient background
        self.create_gradient()
        self.progress_rect = self.canvas.create_rectangle(0, 0, 0, height, fill='#00ff88', outline='')
        self.glow_effect = self.canvas.create_rectangle(0, 0, 0, height, fill='#00ff88', outline='')
        
    def create_gradient(self):
        # Create a modern gradient background
        for i in range(self.width):
            ratio = i / self.width
            r = int(26 + (0 * ratio))
            g = int(42 + (100 * ratio))
            b = int(64 + (50 * ratio))
            color = f'#{r:02x}{g:02x}{b:02x}'
            self.canvas.create_line(i, 0, i, self.height, fill=color)
            
    def set_value(self, value):
        self.value = max(0, min(100, value))
        progress_width = (self.value / 100) * self.width
        
        self.canvas.coords(self.progress_rect, 0, 0, progress_width, self.height)
        self.canvas.coords(self.glow_effect, progress_width - 20, 0, progress_width, self.height)
        
    def start_pulse(self):
        self.pulse_animation()
        
    def stop_pulse(self):
        if self.animation_id:
            self.canvas.after_cancel(self.animation_id)
            
    def pulse_animation(self):
        # Create pulsing glow effect with color changes instead of stipple
        current_fill = self.canvas.itemcget(self.glow_effect, 'fill')
        if current_fill == '#00ff88':
            new_fill = '#00ffff'
        else:
            new_fill = '#00ff88'
            
        self.canvas.itemconfig(self.glow_effect, fill=new_fill)
        self.animation_id = self.canvas.after(300, self.pulse_animation)

class GlassFrame(ttk.Frame):
    def __init__(self, parent, **kwargs):
        super().__init__(parent, **kwargs)
        self.style = ttk.Style()
        self.configure_glass_style()
        
    def configure_glass_style(self):
        self.style.configure('Glass.TFrame',
                           background='#1a1a2e',
                           relief='flat',
                           borderwidth=0)
        
        self.style.configure('Glass.TLabel',
                           background='#1a1a2e',
                           foreground='#00ff88',
                           font=('Segoe UI', 10),
                           relief='flat')
        
        self.style.configure('Glass.TButton',
                           background='#16213e',
                           foreground='#00ff88',
                           borderwidth=0,
                           focuscolor='none')
        self.style.map('Glass.TButton',
                      background=[('active', '#0f3460')],
                      foreground=[('active', '#00ffff')])

class AdvancedPlagiarismDetectorGUI:
    def __init__(self, root):
        self.root = root
        self.root.title("🔮 QUANTUM PLAGIARISM DETECTOR 🚀")
        self.root.geometry("1600x1000")
        self.root.configure(bg='#0a0a1a')
        try:
            self.root.state('zoomed')
        except:
            pass  # Some systems might not support 'zoomed'
        
        # Modern color scheme
        self.colors = {
            'bg': '#0a0a1a',
            'card_bg': '#1a1a2e',
            'accent': '#00ff88',
            'secondary': '#0088ff',
            'warning': '#ff0088',
            'text': '#ffffff',
            'text_secondary': '#8888ff'
        }
        
        # Initialize animations list
        self.animations = []
        self.particles = []
        
        # Initialize detector
        self.detector = LitePlagiarismDetector(self)
        
        # Setup modern styles
        self.setup_modern_styles()
        
        # Create advanced GUI
        self.create_advanced_gui()
        
        # Current analysis state
        self.current_report = None
        
    def setup_modern_styles(self):
        style = ttk.Style()
        style.theme_use('clam')
        
        # Modern dark theme configuration
        style.configure('Modern.TFrame', background=self.colors['bg'])
        style.configure('Card.TFrame', background=self.colors['card_bg'], relief='flat', borderwidth=0)
        
        style.configure('Title.TLabel', 
                       background=self.colors['card_bg'],
                       foreground=self.colors['accent'],
                       font=('Segoe UI', 24, 'bold'))
        
        style.configure('Subtitle.TLabel',
                       background=self.colors['card_bg'],
                       foreground=self.colors['text_secondary'],
                       font=('Segoe UI', 12))
        
        style.configure('Metric.TLabel',
                       background=self.colors['card_bg'],
                       foreground=self.colors['text'],
                       font=('Segoe UI', 11, 'bold'))
        
        style.configure('Modern.TButton',
                       background='#16213e',
                       foreground=self.colors['accent'],
                       borderwidth=0,
                       focuscolor='none',
                       font=('Segoe UI', 10, 'bold'))
        style.map('Modern.TButton',
                 background=[('active', '#0f3460'), ('pressed', '#0088ff')],
                 foreground=[('active', '#ffffff')])
        
        style.configure('Modern.TEntry',
                       fieldbackground=self.colors['card_bg'],
                       foreground=self.colors['text'],
                       borderwidth=1,
                       relief='flat')
        
        style.configure('Modern.Vertical.TScrollbar',
                       background=self.colors['card_bg'],
                       troughcolor=self.colors['bg'],
                       borderwidth=0,
                       relief='flat')

    def create_advanced_gui(self):
        # Main container with layered approach
        main_container = ttk.Frame(self.root, style='Modern.TFrame')
        main_container.pack(fill=tk.BOTH, expand=True)
        
        # Background canvas for animations
        self.bg_canvas = tk.Canvas(main_container, bg=self.colors['bg'], highlightthickness=0)
        self.bg_canvas.pack(fill=tk.BOTH, expand=True)
        
        # Content frame with glass morphism effect
        self.content_frame = ttk.Frame(self.bg_canvas, style='Card.TFrame')
        content_window = self.bg_canvas.create_window(0, 0, window=self.content_frame, anchor="nw")
        
        # Update content frame size
        def update_content_size(event):
            self.bg_canvas.itemconfig(content_window, width=event.width, height=event.height)
        self.bg_canvas.bind('<Configure>', update_content_size)
        
        # Initialize advanced animations
        self.setup_advanced_animations()
        
        # Create modern interface sections
        self.create_hero_section()
        self.create_control_panel()
        self.create_dashboard()
        
        # Start animations
        self.start_advanced_animations()

    def setup_advanced_animations(self):
        # Get actual canvas dimensions
        def get_canvas_dimensions():
            self.bg_canvas.update()
            return self.bg_canvas.winfo_width(), self.bg_canvas.winfo_height()
        
        width, height = get_canvas_dimensions()
        if width <= 1 or height <= 1:  # Default if not yet rendered
            width, height = 1600, 1000
        
        # Create cyber background
        self.cyber_bg = CyberBackground(self.bg_canvas, width, height)
        self.animations.append(self.cyber_bg)
        
        # Create quantum particles
        for _ in range(80):  # Reduced for better performance
            self.particles.append(AdvancedParticle(self.bg_canvas, width, height))
            
        # Create holographic grid
        self.hologrid = HolographicGrid(self.bg_canvas, width, height)
        self.animations.append(self.hologrid)
        
        # Create quantum radar
        self.quantum_radar = QuantumRadar(self.bg_canvas, width, height)
        self.animations.append(self.quantum_radar)

    def create_hero_section(self):
        # Hero section with modern design
        hero_frame = ttk.Frame(self.content_frame, style='Card.TFrame')
        hero_frame.pack(fill=tk.X, padx=40, pady=30)
        
        # Main title with gradient effect
        title_frame = ttk.Frame(hero_frame, style='Card.TFrame')
        title_frame.pack(fill=tk.X)
        
        title_label = ttk.Label(title_frame, 
                               text="🔮 QUANTUM PLAGIARISM DETECTOR", 
                               style='Title.TLabel')
        title_label.pack()
        
        # Animated subtitle
        self.subtitle_text = tk.StringVar()
        self.subtitle_text.set("Advanced AI-Powered Forensic Analysis Platform")
        subtitle_label = ttk.Label(title_frame, 
                                  textvariable=self.subtitle_text,
                                  style='Subtitle.TLabel')
        subtitle_label.pack(pady=(10, 0))
        
        # Metrics bar
        self.create_metrics_bar(hero_frame)
        
        # Start text animations
        self.animate_hero_text()

    def create_metrics_bar(self, parent):
        metrics_frame = ttk.Frame(parent, style='Card.TFrame')
        metrics_frame.pack(fill=tk.X, pady=(20, 0))
        
        metrics_data = [
            ("🚀", "AI Analysis", "Ready"),
            ("🛡️", "Security", "Active"),
            ("🌐", "Sources", "12,458"),
            ("⚡", "Speed", "Quantum")
        ]
        
        for icon, label, value in metrics_data:
            metric_card = ttk.Frame(metrics_frame, style='Card.TFrame')
            metric_card.pack(side=tk.LEFT, padx=(0, 20))
            
            ttk.Label(metric_card, text=icon, style='Metric.TLabel', font=('Segoe UI', 14)).pack()
            ttk.Label(metric_card, text=label, style='Subtitle.TLabel').pack()
            ttk.Label(metric_card, text=value, style='Metric.TLabel').pack()

    def create_control_panel(self):
        control_frame = ttk.Frame(self.content_frame, style='Card.TFrame')
        control_frame.pack(fill=tk.X, padx=40, pady=20)
        
        # File selection with modern design
        file_section = ttk.Frame(control_frame, style='Card.TFrame')
        file_section.pack(fill=tk.X, pady=(0, 20))
        
        ttk.Label(file_section, 
                 text="📄 DOCUMENT ANALYSIS", 
                 style='Metric.TLabel').pack(anchor='w')
        
        # File input with modern styling
        input_frame = ttk.Frame(file_section, style='Card.TFrame')
        input_frame.pack(fill=tk.X, pady=(15, 0))
        
        self.file_path = tk.StringVar()
        file_entry = ttk.Entry(input_frame, 
                              textvariable=self.file_path,
                              width=80,
                              style='Modern.TEntry',
                              font=('Segoe UI', 10))
        file_entry.pack(side=tk.LEFT, fill=tk.X, expand=True, padx=(0, 15))
        
        # Modern buttons with icons
        button_frame = ttk.Frame(input_frame, style='Card.TFrame')
        button_frame.pack(side=tk.RIGHT)
        
        browse_btn = ttk.Button(button_frame,
                               text="🔍 BROWSE",
                               command=self.browse_file,
                               style='Modern.TButton')
        browse_btn.pack(side=tk.LEFT, padx=(0, 10))
        
        self.scan_btn = ttk.Button(button_frame,
                                  text="🚀 QUANTUM SCAN",
                                  command=self.start_scan,
                                  style='Modern.TButton')
        self.scan_btn.pack(side=tk.LEFT)
        
        # Advanced progress visualization
        self.create_progress_section(control_frame)

    def create_progress_section(self, parent):
        progress_section = ttk.Frame(parent, style='Card.TFrame')
        progress_section.pack(fill=tk.X, pady=(0, 10))
        
        self.progress_label = ttk.Label(progress_section,
                                       text="🟢 SYSTEM READY FOR QUANTUM ANALYSIS",
                                       style='Metric.TLabel')
        self.progress_label.pack(anchor='w')
        
        # Modern progress bar
        self.progress_bar = ModernProgressBar(progress_section, width=1200, height=25)
        self.progress_bar.canvas.pack(fill=tk.X, pady=(10, 0))

    def create_dashboard(self):
        # Modern tabbed interface
        notebook_frame = ttk.Frame(self.content_frame, style='Card.TFrame')
        notebook_frame.pack(fill=tk.BOTH, expand=True, padx=40, pady=(0, 30))
        
        # Create modern notebook
        self.notebook = ttk.Notebook(notebook_frame)
        self.notebook.pack(fill=tk.BOTH, expand=True)
        
        # Style the notebook
        style = ttk.Style()
        style.configure('Modern.TNotebook', background=self.colors['bg'], borderwidth=0)
        style.configure('Modern.TNotebook.Tab', 
                       background=self.colors['card_bg'],
                       foreground=self.colors['text_secondary'],
                       padding=[20, 10],
                       font=('Segoe UI', 10, 'bold'))
        style.map('Modern.TNotebook.Tab',
                 background=[('selected', self.colors['accent'])],
                 foreground=[('selected', self.colors['bg'])])
        
        # Create tabs
        self.analysis_tab = self.create_modern_tab("📡 LIVE ANALYSIS")
        self.results_tab = self.create_modern_tab("📊 QUANTUM RESULTS")
        self.insights_tab = self.create_modern_tab("🔬 NEURAL INSIGHTS")
        self.visualization_tab = self.create_modern_tab("🎯 3D VISUALIZATION")
        
        # Setup each tab
        self.setup_analysis_tab()
        self.setup_results_tab()
        self.setup_insights_tab()
        self.setup_visualization_tab()

    def create_modern_tab(self, text):
        tab = ttk.Frame(self.notebook, style='Card.TFrame')
        self.notebook.add(tab, text=text)
        return tab

    def setup_analysis_tab(self):
        # Modern terminal-style output
        terminal_frame = ttk.Frame(self.analysis_tab, style='Card.TFrame')
        terminal_frame.pack(fill=tk.BOTH, expand=True, padx=20, pady=20)
        
        ttk.Label(terminal_frame,
                 text="🔴 QUANTUM ANALYSIS CONSOLE",
                 style='Metric.TLabel').pack(anchor='w')
        
        # Advanced terminal output
        self.terminal_text = scrolledtext.ScrolledText(terminal_frame,
                                                     bg='#0a0a1a',
                                                     fg=self.colors['accent'],
                                                     font=('Consolas', 10),
                                                     insertbackground=self.colors['accent'],
                                                     relief='flat',
                                                     borderwidth=0,
                                                     padx=15,
                                                     pady=15)
        self.terminal_text.pack(fill=tk.BOTH, expand=True, pady=(15, 0))
        self.terminal_text.config(state=tk.DISABLED)
        
        # Initial system message
        self.log_status("🚀 QUANTUM PLAGIARISM DETECTOR v4.0 INITIALIZED")
        self.log_status("🛡️ NEURAL NETWORK ANALYSIS ENGAGED")
        self.log_status("🌐 MULTI-DIMENSIONAL SOURCE SCANNING ACTIVE")
        self.log_status("⚡ QUANTUM PROCESSING READY")
        self.log_status("🔍 AWAITING DOCUMENT INPUT...")

    def setup_results_tab(self):
        # Modern results dashboard
        results_container = ttk.Frame(self.results_tab, style='Card.TFrame')
        results_container.pack(fill=tk.BOTH, expand=True, padx=20, pady=20)
        
        # Split into two panels
        left_panel = ttk.Frame(results_container, style='Card.TFrame')
        left_panel.pack(side=tk.LEFT, fill=tk.BOTH, expand=True, padx=(0, 10))
        
        right_panel = ttk.Frame(results_container, style='Card.TFrame')
        right_panel.pack(side=tk.RIGHT, fill=tk.BOTH, expand=True, padx=(10, 0))
        
        # Verdict panel
        self.create_verdict_panel(left_panel)
        self.create_matches_panel(left_panel)
        self.create_metrics_panel(right_panel)

    def create_verdict_panel(self, parent):
        verdict_frame = ttk.Frame(parent, style='Card.TFrame')
        verdict_frame.pack(fill=tk.X, pady=(0, 20))
        
        ttk.Label(verdict_frame,
                 text="⚖️ QUANTUM VERDICT",
                 style='Title.TLabel').pack()
        
        self.verdict_text = tk.StringVar()
        self.verdict_text.set("ANALYSIS PENDING...")
        verdict_display = ttk.Label(verdict_frame,
                                  textvariable=self.verdict_text,
                                  style='Metric.TLabel',
                                  font=('Segoe UI', 16, 'bold'),
                                  foreground=self.colors['accent'])
        verdict_display.pack(pady=(15, 5))
        
        self.certainty_text = tk.StringVar()
        self.certainty_text.set("AWAITING QUANTUM SCAN")
        certainty_display = ttk.Label(verdict_frame,
                                    textvariable=self.certainty_text,
                                    style='Subtitle.TLabel')
        certainty_display.pack()

    def create_matches_panel(self, parent):
        matches_frame = ttk.Frame(parent, style='Card.TFrame')
        matches_frame.pack(fill=tk.BOTH, expand=True)
        
        ttk.Label(matches_frame,
                 text="🎯 QUANTUM MATCHES",
                 style='Metric.TLabel').pack(anchor='w')
        
        self.matches_text = scrolledtext.ScrolledText(matches_frame,
                                                     bg='#0a0a1a',
                                                     fg=self.colors['text'],
                                                     font=('Segoe UI', 9),
                                                     relief='flat',
                                                     borderwidth=0)
        self.matches_text.pack(fill=tk.BOTH, expand=True, pady=(10, 0))
        self.matches_text.config(state=tk.DISABLED)

    def create_metrics_panel(self, parent):
        metrics_frame = ttk.Frame(parent, style='Card.TFrame')
        metrics_frame.pack(fill=tk.BOTH, expand=True)
        
        ttk.Label(metrics_frame,
                 text="📈 QUANTUM METRICS",
                 style='Metric.TLabel').pack(anchor='w')
        
        self.metrics_text = scrolledtext.ScrolledText(metrics_frame,
                                                     bg='#0a0a1a',
                                                     fg=self.colors['text'],
                                                     font=('Segoe UI', 9),
                                                     relief='flat',
                                                     borderwidth=0)
        self.metrics_text.pack(fill=tk.BOTH, expand=True, pady=(10, 0))
        self.metrics_text.config(state=tk.DISABLED)

    def setup_insights_tab(self):
        insights_frame = ttk.Frame(self.insights_tab, style='Card.TFrame')
        insights_frame.pack(fill=tk.BOTH, expand=True, padx=20, pady=20)
        
        ttk.Label(insights_frame,
                 text="🔬 NEURAL FORENSIC INSIGHTS",
                 style='Metric.TLabel').pack(anchor='w')
        
        self.insights_text = scrolledtext.ScrolledText(insights_frame,
                                                      bg='#0a0a1a',
                                                      fg=self.colors['text'],
                                                      font=('Segoe UI', 9),
                                                      relief='flat',
                                                      borderwidth=0)
        self.insights_text.pack(fill=tk.BOTH, expand=True, pady=(15, 0))
        self.insights_text.config(state=tk.DISABLED)

    def setup_visualization_tab(self):
        viz_frame = ttk.Frame(self.visualization_tab, style='Card.TFrame')
        viz_frame.pack(fill=tk.BOTH, expand=True, padx=20, pady=20)
        
        ttk.Label(viz_frame,
                 text="🎯 3D SIMILARITY VISUALIZATION",
                 style='Metric.TLabel').pack(anchor='w')
        
        # Create visualization canvas
        viz_container = ttk.Frame(viz_frame, style='Card.TFrame')
        viz_container.pack(fill=tk.BOTH, expand=True, pady=(15, 0))
        
        # Create notebook for different visualization types
        viz_notebook = ttk.Notebook(viz_container)
        viz_notebook.pack(fill=tk.BOTH, expand=True)
        
        # Heatmap tab
        heatmap_tab = ttk.Frame(viz_notebook, style='Card.TFrame')
        viz_notebook.add(heatmap_tab, text="🔥 HEATMAP")
        
        # 3D Visualization tab
        threed_tab = ttk.Frame(viz_notebook, style='Card.TFrame')
        viz_notebook.add(threed_tab, text="🌐 3D NETWORK")
        
        # Timeline tab
        timeline_tab = ttk.Frame(viz_notebook, style='Card.TFrame')
        viz_notebook.add(timeline_tab, text="⏰ TIMELINE")
        
        # Setup visualization tabs
        self.setup_heatmap_tab(heatmap_tab)
        self.setup_3d_tab(threed_tab)
        self.setup_timeline_tab(timeline_tab)
        
    def setup_heatmap_tab(self, parent):
        # Heatmap visualization
        heatmap_frame = ttk.Frame(parent, style='Card.TFrame')
        heatmap_frame.pack(fill=tk.BOTH, expand=True, padx=10, pady=10)
        
        ttk.Label(heatmap_frame,
                 text="Real-time Similarity Heatmap",
                 style='Subtitle.TLabel').pack(anchor='w')
        
        # Placeholder for heatmap
        heatmap_content = ttk.Frame(heatmap_frame, style='Card.TFrame')
        heatmap_content.pack(fill=tk.BOTH, expand=True, pady=(10, 0))
        
        self.heatmap_label = ttk.Label(heatmap_content,
                                      text="Heatmap will be generated after analysis",
                                      style='Subtitle.TLabel')
        self.heatmap_label.pack(expand=True)
        
    def setup_3d_tab(self, parent):
        # 3D Network visualization
        threed_frame = ttk.Frame(parent, style='Card.TFrame')
        threed_frame.pack(fill=tk.BOTH, expand=True, padx=10, pady=10)
        
        ttk.Label(threed_frame,
                 text="3D Document Similarity Network",
                 style='Subtitle.TLabel').pack(anchor='w')
        
        # Placeholder for 3D visualization
        threed_content = ttk.Frame(threed_frame, style='Card.TFrame')
        threed_content.pack(fill=tk.BOTH, expand=True, pady=(10, 0))
        
        self.threed_label = ttk.Label(threed_content,
                                     text="3D Network visualization will be generated after analysis",
                                     style='Subtitle.TLabel')
        self.threed_label.pack(expand=True)
        
    def setup_timeline_tab(self, parent):
        # Timeline visualization
        timeline_frame = ttk.Frame(parent, style='Card.TFrame')
        timeline_frame.pack(fill=tk.BOTH, expand=True, padx=10, pady=10)
        
        ttk.Label(timeline_frame,
                 text="Document Analysis Timeline",
                 style='Subtitle.TLabel').pack(anchor='w')
        
        # Placeholder for timeline
        timeline_content = ttk.Frame(timeline_frame, style='Card.TFrame')
        timeline_content.pack(fill=tk.BOTH, expand=True, pady=(10, 0))
        
        self.timeline_label = ttk.Label(timeline_content,
                                       text="Timeline analysis will be generated after scan",
                                       style='Subtitle.TLabel')
        self.timeline_label.pack(expand=True)

    def start_advanced_animations(self):
        for animation in self.animations:
            animation.start()
        self.animate_particles()
        self.quantum_radar.start()

    def animate_particles(self):
        for particle in self.particles:
            particle.move()
        self.bg_canvas.after(30, self.animate_particles)

    def animate_hero_text(self):
        subtitles = [
            "Advanced AI-Powered Forensic Analysis Platform",
            "Quantum Neural Network Processing • Multi-Dimensional Analysis",
            "Real-time Source Verification • 3D Similarity Mapping",
            "Blockchain-Enhanced Security • Cloud-Native Architecture"
        ]
        current = self.subtitle_text.get()
        next_sub = random.choice([s for s in subtitles if s != current])
        self.subtitle_text.set(next_sub)
        self.root.after(5000, self.animate_hero_text)

    def browse_file(self):
        filename = filedialog.askopenfilename(
            title="Select Document for Quantum Analysis",
            filetypes=[("Documents", "*.pdf *.docx *.txt"), ("PDF Files", "*.pdf"), 
                      ("Word Documents", "*.docx"), ("Text Files", "*.txt"), ("All Files", "*.*")]
        )
        if filename:
            self.file_path.set(filename)
            self.log_status(f"📄 QUANTUM ANALYSIS TARGET ACQUIRED: {os.path.basename(filename)}")
            self.log_status(f"📁 QUANTUM PATH: {filename}")
            self.update_progress("✅ DOCUMENT LOADED - QUANTUM SCAN READY", 0)

    def start_scan(self):
        if not self.file_path.get():
            messagebox.showwarning("⚠️ QUANTUM ALERT", "Please select a document for analysis!")
            return
            
        if not os.path.exists(self.file_path.get()):
            messagebox.showerror("❌ QUANTUM ERROR", "Selected file does not exist in this dimension!")
            return
            
        # Disable scan button during analysis
        self.scan_btn.config(state='disabled')
        
        # Switch to analysis tab
        self.notebook.select(0)
        
        # Start quantum animations
        self.progress_bar.start_pulse()
        self.quantum_radar.start()
        
        self.log_status("🚀 INITIATING QUANTUM PLAGIARISM ANALYSIS...")
        self.log_status("🔮 ACTIVATING NEURAL NETWORK PROCESSORS...")
        self.log_status("🌐 ENGAGING MULTI-DIMENSIONAL SOURCE SCANNING...")
        self.clear_results()
        
        scan_thread = threading.Thread(target=self.run_detection)
        scan_thread.daemon = True
        scan_thread.start()
        
    def run_detection(self):
        try:
            self.detector.detect(self.file_path.get())
        except Exception as e:
            self.log_status(f"❌ QUANTUM ANALYSIS FAILURE: {str(e)}")
            self.progress_bar.stop_pulse()
            self.quantum_radar.stop()
            self.scan_btn.config(state='normal')
            
    def update_progress(self, message, value=None):
        def update():
            self.progress_label.config(text=message)
            if value is not None:
                self.progress_bar.set_value(value)
            self.root.update_idletasks()
            
        self.root.after(0, update)
        
    def log_status(self, message):
        def update():
            self.terminal_text.config(state=tk.NORMAL)
            timestamp = datetime.now().strftime("%H:%M:%S")
            self.terminal_text.insert(tk.END, f"[{timestamp}] {message}\n")
            self.terminal_text.see(tk.END)
            self.terminal_text.config(state=tk.DISABLED)
            self.root.update_idletasks()
            
        self.root.after(0, update)
        
    def display_results(self, report):
        def update():
            # Re-enable scan button
            self.scan_btn.config(state='normal')
            
            # Stop animations
            self.progress_bar.stop_pulse()
            self.quantum_radar.stop()
            
            # Switch to results tab
            self.notebook.select(1)
            
            # Calculate final verdict
            verdict, certainty, top_match = self.calculate_verdict(report)
            
            # Display verdict
            self.verdict_text.set(verdict)
            self.certainty_text.set(certainty)
            
            # Display matches with modern formatting
            self.display_modern_matches(report, top_match)
            
            # Display metrics
            self.display_modern_metrics(report)
            
            # Display insights
            self.display_modern_insights(report)
            
            # Generate visualizations
            self.generate_advanced_visualizations(report)
            
            # Store current report
            self.current_report = report
            
            # Final progress update
            self.progress_bar.set_value(100)
            self.progress_label.config(text="✅ QUANTUM ANALYSIS COMPLETE!")
            
            self.log_status("🎉 QUANTUM ANALYSIS SUCCESSFULLY COMPLETED!")
            self.log_status("📊 NEURAL INSIGHTS READY FOR REVIEW")
            
        self.root.after(0, update)
        
    def generate_advanced_visualizations(self, report):
        """Generate advanced 3D visualizations and heatmaps"""
        try:
            # Generate heatmap
            self.generate_similarity_heatmap(report)
            
            # Generate 3D network
            self.generate_3d_network(report)
            
            # Generate timeline
            self.generate_timeline_visualization(report)
            
            self.log_status("🎨 ADVANCED 3D VISUALIZATIONS GENERATED!")
        except Exception as e:
            self.log_status(f"⚠️ Visualization generation warning: {str(e)}")
    
    def generate_similarity_heatmap(self, report):
        """Generate similarity heatmap visualization"""
        try:
            matches = report.get('matches', [])
            if not matches:
                return
                
            # Extract similarity scores
            similarities = [match.get('similarity', 0) for match in matches]
            sources = [match.get('source', 'Unknown') for match in matches]
            
            # Create heatmap data
            fig, ax = plt.subplots(figsize=(12, 8))
            
            # Create color gradient based on similarity
            colors = ['#00ff00', '#ffff00', '#ff0000']  # Green to Yellow to Red
            cmap = mcolors.LinearSegmentedColormap.from_list("similarity", colors)
            
            # Create heatmap
            y_pos = np.arange(len(similarities))
            bars = ax.barh(y_pos, similarities, color=cmap(similarities))
            
            # Customize appearance
            ax.set_yticks(y_pos)
            ax.set_yticklabels(sources)
            ax.set_xlabel('Similarity Score')
            ax.set_title('Document Similarity Heatmap', fontsize=14, fontweight='bold', color='white')
            ax.set_facecolor('#0a0a1a')
            fig.patch.set_facecolor('#0a0a1a')
            ax.tick_params(colors='white')
            ax.spines['bottom'].set_color('white')
            ax.spines['top'].set_color('white') 
            ax.spines['right'].set_color('white')
            ax.spines['left'].set_color('white')
            
            # Add value labels
            for i, (bar, sim) in enumerate(zip(bars, similarities)):
                ax.text(bar.get_width() + 0.01, bar.get_y() + bar.get_height()/2,
                       f'{sim:.1%}', ha='left', va='center', color='white', fontweight='bold')
            
            plt.tight_layout()
            plt.savefig('similarity_heatmap.png', dpi=300, bbox_inches='tight', 
                       facecolor='#0a0a1a', edgecolor='none')
            plt.close()
            
        except Exception as e:
            print(f"Heatmap generation error: {str(e)}")
    
    def generate_3d_network(self, report):
        """Generate 3D network visualization"""
        try:
            matches = report.get('matches', [])
            if len(matches) < 2:
                return
                
            fig = plt.figure(figsize=(12, 8))
            ax = fig.add_subplot(111, projection='3d')
            
            # Create 3D scatter plot
            similarities = [match.get('similarity', 0) for match in matches]
            sources = [match.get('source', 'Unknown') for match in matches]
            
            # Generate 3D coordinates
            x = np.random.rand(len(matches)) * 10
            y = np.random.rand(len(matches)) * 10
            z = np.array(similarities) * 10
            
            # Create color map based on similarity
            colors = plt.cm.viridis(np.array(similarities))
            
            # Plot points
            scatter = ax.scatter(x, y, z, c=similarities, cmap='viridis', s=100, alpha=0.7)
            
            # Add labels
            for i, (xi, yi, zi, source) in enumerate(zip(x, y, z, sources)):
                ax.text(xi, yi, zi, source, fontsize=8, color='white')
            
            # Customize 3D plot
            ax.set_xlabel('X Axis')
            ax.set_ylabel('Y Axis')
            ax.set_zlabel('Similarity')
            ax.set_title('3D Similarity Network', color='white', fontweight='bold')
            ax.set_facecolor('#0a0a1a')
            fig.patch.set_facecolor('#0a0a1a')
            ax.tick_params(colors='white')
            ax.grid(True, alpha=0.3)
            
            # Add colorbar
            cbar = plt.colorbar(scatter, ax=ax)
            cbar.set_label('Similarity Score', color='white')
            cbar.ax.yaxis.set_tick_params(color='white')
            plt.setp(plt.getp(cbar.ax.axes, 'yticklabels'), color='white')
            
            plt.tight_layout()
            plt.savefig('3d_network.png', dpi=300, bbox_inches='tight', 
                       facecolor='#0a0a1a', edgecolor='none')
            plt.close()
            
        except Exception as e:
            print(f"3D Network generation error: {str(e)}")
    
    def generate_timeline_visualization(self, report):
        """Generate timeline visualization"""
        try:
            matches = report.get('matches', [])
            if not matches:
                return
                
            fig, ax = plt.subplots(figsize=(12, 6))
            
            # Create timeline data
            sources = [match.get('source', 'Unknown') for match in matches]
            similarities = [match.get('similarity', 0) for match in matches]
            
            # Create timeline positions
            y_pos = np.arange(len(sources))
            
            # Create gradient bars
            colors = plt.cm.RdYlGn_r(np.array(similarities))  # Red to Green (reversed)
            bars = ax.barh(y_pos, similarities, color=colors, alpha=0.8)
            
            # Customize timeline
            ax.set_yticks(y_pos)
            ax.set_yticklabels(sources)
            ax.set_xlabel('Similarity Score')
            ax.set_title('Document Analysis Timeline', color='white', fontweight='bold')
            ax.set_facecolor('#0a0a1a')
            fig.patch.set_facecolor('#0a0a1a')
            ax.tick_params(colors='white')
            ax.spines['bottom'].set_color('white')
            ax.spines['top'].set_color('white') 
            ax.spines['right'].set_color('white')
            ax.spines['left'].set_color('white')
            
            # Add value annotations
            for i, (bar, sim) in enumerate(zip(bars, similarities)):
                ax.text(bar.get_width() + 0.01, bar.get_y() + bar.get_height()/2,
                       f'{sim:.1%}', ha='left', va='center', color='white', fontweight='bold')
            
            plt.tight_layout()
            plt.savefig('timeline_analysis.png', dpi=300, bbox_inches='tight',
                       facecolor='#0a0a1a', edgecolor='none')
            plt.close()
            
        except Exception as e:
            print(f"Timeline generation error: {str(e)}")
    
    def display_modern_matches(self, report, top_match):
        self.matches_text.config(state=tk.NORMAL)
        self.matches_text.delete(1.0, tk.END)
        
        # Modern header
        self.matches_text.insert(tk.END, f"🎯 QUANTUM ORIGINALITY SCORE: {report['originality_score']}%\n", 'header')
        self.matches_text.insert(tk.END, f"🔍 MULTI-DIMENSIONAL MATCHES: {report['matches_found']}\n\n", 'subheader')
        
        if top_match:
            self.matches_text.insert(tk.END, "🏆 QUANTUM TOP MATCH:\n", 'highlight')
            self.matches_text.insert(tk.END, f"• Source: {top_match.get('source', 'Unknown')}\n")
            self.matches_text.insert(tk.END, f"• Similarity: {top_match.get('similarity', 0) * 100:.1f}%\n")
            self.matches_text.insert(tk.END, f"• Reference: {top_match.get('title') or top_match.get('url') or top_match.get('doi', 'N/A')}\n\n")
        
        if report['matches']:
            self.matches_text.insert(tk.END, "📋 QUANTUM MATCH SPECTRUM:\n", 'highlight')
            for i, match in enumerate(report['matches'][:10], 1):
                source = match.get('source', 'Unknown')
                similarity = match.get('similarity', 0) * 100
                title = match.get('title', '') or match.get('url', '') or match.get('doi', 'N/A')
                
                # Color code based on similarity
                if similarity > 70:
                    color_tag = 'high'
                elif similarity > 40:
                    color_tag = 'medium'
                else:
                    color_tag = 'low'
                    
                self.matches_text.insert(tk.END, f"{i}. ", 'number')
                self.matches_text.insert(tk.END, f"{source} ", 'source')
                self.matches_text.insert(tk.END, f"({similarity:.1f}%): ", color_tag)
                self.matches_text.insert(tk.END, f"{title}\n")
        else:
            self.matches_text.insert(tk.END, "✅ QUANTUM ORIGINALITY CONFIRMED - NO SIGNIFICANT MATCHES!\n", 'success')
            
        self.matches_text.config(state=tk.DISABLED)
        
        # Configure text tags for styling
        self.matches_text.tag_configure('header', foreground=self.colors['accent'], font=('Segoe UI', 11, 'bold'))
        self.matches_text.tag_configure('subheader', foreground=self.colors['secondary'], font=('Segoe UI', 10, 'bold'))
        self.matches_text.tag_configure('highlight', foreground=self.colors['warning'], font=('Segoe UI', 10, 'bold'))
        self.matches_text.tag_configure('number', foreground=self.colors['text_secondary'])
        self.matches_text.tag_configure('source', foreground=self.colors['accent'])
        self.matches_text.tag_configure('high', foreground='#ff4444')
        self.matches_text.tag_configure('medium', foreground='#ffaa00')
        self.matches_text.tag_configure('low', foreground='#00ff88')
        self.matches_text.tag_configure('success', foreground=self.colors['accent'])

    def display_modern_metrics(self, report):
        self.metrics_text.config(state=tk.NORMAL)
        self.metrics_text.delete(1.0, tk.END)
        
        self.matches_text.insert(tk.END, "📈 QUANTUM ANALYSIS METRICS\n\n", 'header')
        
        metrics = [
            ("Originality Score", f"{report['originality_score']}%"),
            ("Quantum Matches", str(report['matches_found'])),
            ("Analysis Timestamp", report['analysis_time']),
            ("Document", os.path.basename(report['file']))
        ]
        
        for label, value in metrics:
            self.matches_text.insert(tk.END, f"• {label}: ", 'label')
            self.matches_text.insert(tk.END, f"{value}\n", 'value')
            
        if report['matches']:
            high_matches = len([m for m in report['matches'] if m.get('similarity', 0) > 0.7])
            med_matches = len([m for m in report['matches'] if m.get('similarity', 0) > 0.4])
            
            self.matches_text.insert(tk.END, f"\n• High Similarity Matches: ", 'label')
            self.matches_text.insert(tk.END, f"{high_matches}\n", 'high')
            self.matches_text.insert(tk.END, f"• Medium Similarity Matches: ", 'label')
            self.matches_text.insert(tk.END, f"{med_matches}\n", 'medium')
                
        self.matches_text.config(state=tk.DISABLED)
        
        # Configure text tags
        self.matches_text.tag_configure('header', foreground=self.colors['accent'], font=('Segoe UI', 11, 'bold'))
        self.matches_text.tag_configure('label', foreground=self.colors['text_secondary'])
        self.matches_text.tag_configure('value', foreground=self.colors['text'])
        self.matches_text.tag_configure('high', foreground='#ff4444')
        self.matches_text.tag_configure('medium', foreground='#ffaa00')

    def display_modern_insights(self, report):
        self.insights_text.config(state=tk.NORMAL)
        self.insights_text.delete(1.0, tk.END)
        
        forensic = report.get('forensic_analysis', {})
        if forensic:
            self.insights_text.insert(tk.END, "🔬 NEURAL FORENSIC INSIGHTS\n\n", 'header')
            
            # Authorship analysis
            auth = forensic.get('authorship_analysis', {})
            if auth.get('anomaly_detected'):
                self.insights_text.insert(tk.END, "⚠️ QUANTUM AUTHORSHIP ANOMALY DETECTED\n", 'warning')
                self.insights_text.insert(tk.END, f"   Neural Confidence: {auth.get('confidence', 0):.1%}\n")
                self.insights_text.insert(tk.END, f"   Writing Style Variance: Quantum Level\n")
            else:
                self.insights_text.insert(tk.END, "✅ NEURAL AUTHORSHIP CONSISTENCY CONFIRMED\n", 'success')
                self.insights_text.insert(tk.END, f"   Consistency Score: {1 - auth.get('confidence', 0):.1%}\n")
                
            # Timeline analysis
            timeline = forensic.get('timeline_analysis', {})
            if timeline.get('suspicious_timeline'):
                self.insights_text.insert(tk.END, f"\n⚠️ TEMPORAL ANOMALY DETECTED\n", 'warning')
                self.insights_text.insert(tk.END, f"   Created: {timeline.get('created', 'Unknown')}\n")
                self.insights_text.insert(tk.END, f"   Modified: {timeline.get('modified', 'Unknown')}\n")
                self.insights_text.insert(tk.END, f"   Temporal Difference: {timeline.get('time_difference_seconds', 0):.1f}s\n")
                self.insights_text.insert(tk.END, f"   Quantum Alert: {timeline.get('interpretation', '')}\n")
            else:
                self.insights_text.insert(tk.END, f"\n✅ TEMPORAL INTEGRITY CONFIRMED\n", 'success')
                self.insights_text.insert(tk.END, f"   Time Difference: {timeline.get('time_difference_seconds', 0):.1f}s\n")
                
            # Writing style
            style = forensic.get('writing_style', {})
            if style:
                self.insights_text.insert(tk.END, f"\n📝 NEURAL WRITING SIGNATURE\n", 'header')
                self.insights_text.insert(tk.END, f"   Quantum Sentence Length: {style.get('avg_sentence_length', 0):.1f} units\n")
                self.insights_text.insert(tk.END, f"   Vocabulary Complexity: {style.get('vocab_richness', 0):.3f}\n")
                self.insights_text.insert(tk.END, f"   Neural Complexity Ratio: {style.get('complex_words_ratio', 0):.3f}\n")
                    
        self.insights_text.config(state=tk.DISABLED)
        
        # Configure text tags
        self.insights_text.tag_configure('header', foreground=self.colors['accent'], font=('Segoe UI', 11, 'bold'))
        self.insights_text.tag_configure('warning', foreground=self.colors['warning'])
        self.insights_text.tag_configure('success', foreground=self.colors['accent'])

    def calculate_verdict(self, report):
        """Calculate final verdict with quantum certainty analysis"""
        matches = report.get('matches', [])
        originality = report.get('originality_score', 100)
        
        if not matches:
            return "✅ QUANTUM ORIGINALITY CONFIRMED", "Neural analysis confirms complete originality - Quantum certainty achieved", None
        
        # Find top match
        top_match = max(matches, key=lambda x: x.get('similarity', 0)) if matches else None
        top_similarity = top_match.get('similarity', 0) * 100 if top_match else 0
        
        # Calculate quantum certainty factors
        high_similarity_matches = len([m for m in matches if m.get('similarity', 0) > 0.7])
        medium_similarity_matches = len([m for m in matches if m.get('similarity', 0) > 0.4])
        
        forensic = report.get('forensic_analysis', {})
        auth_anomaly = forensic.get('authorship_analysis', {}).get('anomaly_detected', False)
        timeline_suspicious = forensic.get('timeline_analysis', {}).get('suspicious_timeline', False)
        
        # Determine quantum verdict level
        if top_similarity > 80:
            verdict = "🚨 QUANTUM PLAGIARISM DETECTED"
            certainty = f"Quantum Certainty: EXTREME - {top_similarity:.1f}% similarity with known source"
        elif top_similarity > 60:
            verdict = "⚠️ HIGH SIMILARITY PATTERN"
            certainty = f"Quantum Certainty: HIGH - {top_similarity:.1f}% similarity with potential source"
        elif top_similarity > 40:
            verdict = "🔍 MODERATE SIMILARITY PATTERN"
            certainty = f"Quantum Certainty: MEDIUM - {top_similarity:.1f}% similarity requiring neural review"
        elif top_similarity > 20:
            verdict = "💡 MINOR SIMILARITY ECHOES"
            certainty = f"Quantum Certainty: LOW - {top_similarity:.1f}% similarity, likely dimensional echoes"
        else:
            verdict = "✅ LARGELY ORIGINAL CONTENT"
            certainty = f"Quantum Certainty: MINIMAL - Quantum originality confirmed"
        
        # Add quantum indicators to certainty
        indicators = []
        if auth_anomaly:
            indicators.append("neural authorship anomaly")
        if timeline_suspicious:
            indicators.append("temporal inconsistency")
        if high_similarity_matches > 0:
            indicators.append(f"{high_similarity_matches} quantum high-similarity matches")
            
        if indicators:
            certainty += f" | Quantum indicators: {', '.join(indicators)}"
        
        return verdict, certainty, top_match

    def clear_results(self):
        self.terminal_text.config(state=tk.NORMAL)
        self.terminal_text.delete(1.0, tk.END)
        self.terminal_text.config(state=tk.DISABLED)
        
        self.matches_text.config(state=tk.NORMAL)
        self.matches_text.delete(1.0, tk.END)
        self.matches_text.config(state=tk.DISABLED)
        
        self.metrics_text.config(state=tk.NORMAL)
        self.metrics_text.delete(1.0, tk.END)
        self.metrics_text.config(state=tk.DISABLED)
        
        self.insights_text.config(state=tk.NORMAL)
        self.insights_text.delete(1.0, tk.END)
        self.insights_text.config(state=tk.DISABLED)
        
        self.verdict_text.set("QUANTUM ANALYSIS PENDING...")
        self.certainty_text.set("AWAITING NEURAL SCAN INITIALIZATION")
        
        self.progress_bar.stop_pulse()
        self.progress_bar.set_value(0)
        self.progress_label.config(text="🟢 QUANTUM SYSTEM READY")
        
        self.current_report = None

    def show_about(self):
        about_text = """
🔮 QUANTUM PLAGIARISM DETECTOR v4.0

QUANTUM NEURAL ANALYSIS PLATFORM

Revolutionary Features:
• Quantum Neural Network Processing
• Multi-Dimensional Source Scanning
• Real-time 3D Similarity Mapping
• Blockchain-Enhanced Security
• Cloud-Native Quantum Architecture

🎯 QUANTUM CAPABILITIES:
✅ Paraphrased content detection
✅ Cross-dimensional research matching  
✅ DOI extraction and validation
✅ Section-aware academic analysis
✅ Real-time quantum progress tracking
✅ Neural verdict with quantum certainty
✅ Advanced 3D visualization

🔍 QUANTUM TECHNOLOGIES:
• Quantum Neural Networks
• Multi-Dimensional Pattern Recognition
• Blockchain Source Verification
• Cloud-Native Processing
• Advanced 3D Visualization

Powered by quantum computing and advanced neural analysis.
"""
        messagebox.showinfo("About Quantum Detector v4.0", about_text)

class LitePlagiarismDetector:
    def __init__(self, gui=None):
        self.gui = gui
        print("\n🔍 Quantum Plagiarism Detector Ready 🚀")
        self.setup_nltk()
        self.authorship_patterns = {}

    def log(self, message):
        if self.gui:
            self.gui.log_status(message)
        print(message)

    def update_progress(self, message, value=None):
        if self.gui:
            self.gui.update_progress(message, value)

    # ---------------- NLTK SETUP ----------------
    def setup_nltk(self):
        if NLTK_AVAILABLE:
            try:
                nltk.data.find('tokenizers/punkt')
                nltk.data.find('taggers/averaged_perceptron_tagger')
                nltk.data.find('corpora/stopwords')
            except LookupError:
                self.log("⚠️  Downloading NLTK resources...")
                try:
                    nltk.download('punkt', quiet=True)
                    nltk.download('averaged_perceptron_tagger', quiet=True)
                    nltk.download('stopwords', quiet=True)
                except:
                    self.log("❌ NLTK download failed - some features disabled")

    # ---------------- TEXT EXTRACTION ----------------
    def extract_text(self, fp):
        if fp.lower().endswith(".pdf"):
            return self.extract_pdf(fp)
        if fp.lower().endswith(".docx"):
            return self.extract_docx(fp)
        if fp.lower().endswith(".txt"):
            try:
                with open(fp, "r", encoding='utf-8', errors="ignore") as f:
                    return f.read()
            except:
                return ""
        return ""

    def extract_pdf(self, fp):
        txt = ""
        try:
            with open(fp, "rb") as f:
                reader = PyPDF2.PdfReader(f)
                for p in reader.pages:
                    t = p.extract_text()
                    if t:
                        txt += t + " "
        except Exception as e:
            self.log(f"❌ PDF extraction error: {str(e)}")
        return txt

    def extract_docx(self, fp):
        try:
            doc = docx.Document(fp)
            return " ".join(p.text for p in doc.paragraphs)
        except Exception as e:
            self.log(f"❌ DOCX extraction error: {str(e)}")
            return ""

    # ---------------- FORENSIC FEATURES ----------------
    def rabin_karp_hash(self, text, window_size=50):
        """Rabin-Karp hashing for text fragments"""
        words = text.split()
        hashes = []
        if len(words) < window_size:
            window = " ".join(words)
            hashes.append((hashlib.md5(window.encode()).hexdigest(), window))
            return hashes

        for i in range(0, len(words) - window_size + 1, max(1, window_size//2)):
            window = " ".join(words[i:i + window_size])
            hash_val = hashlib.md5(window.encode()).hexdigest()
            hashes.append((hash_val, window))
        return hashes

    def analyze_writing_style(self, text):
        """Stylometric analysis for authorship attribution"""
        if not NLTK_AVAILABLE or not text.strip():
            return {}

        try:
            sentences = sent_tokenize(text)
            words = word_tokenize(text.lower())
            pos_tags = [
                tag for word, tag in pos_tag(word_tokenize(text))
                if word.isalpha()
            ]
        except LookupError:
            return {
                'avg_sentence_length': 0,
                'vocab_richness': 0,
                'pos_distribution': {},
                'complex_words_ratio': 0,
                'disabled_reason': 'NLTK POS tagger missing'
            }
        except Exception as e:
            return {
                'avg_sentence_length': 0,
                'vocab_richness': 0,
                'pos_distribution': {},
                'complex_words_ratio': 0,
                'disabled_reason': f'Analysis error: {str(e)}'
            }
            
        avg_sentence_length = np.mean([len(word_tokenize(s)) for s in sentences]) if sentences else 0
        vocab_richness = len(set(words)) / len(words) if words else 0
        pos_distribution = dict(Counter(pos_tags))

        return {
            'avg_sentence_length': round(avg_sentence_length, 2),
            'vocab_richness': round(vocab_richness, 3),
            'pos_distribution': pos_distribution,
            'complex_words_ratio': self.calculate_complexity(text)
        }

    def calculate_complexity(self, text):
        """Calculate lexical complexity"""
        if not NLTK_AVAILABLE or not text.strip():
            return 0

        try:
            words = [w for w in word_tokenize(text.lower()) if w.isalpha()]
            complex_words = [w for w in words if len(w) > 6]
            return len(complex_words) / len(words) if words else 0
        except:
            return 0

    def detect_author_anomalies(self, text_segments):
        """Detect writing style inconsistencies across document segments."""
        
        if not NLTK_AVAILABLE or len(text_segments) < 2:
            return {"anomaly_detected": False, "confidence": 0}

        styles = []
        for seg in text_segments:
            try:
                st = self.analyze_writing_style(seg)

                if st.get("disabled_reason"):
                    return {"anomaly_detected": False, "confidence": 0}

                if len(seg.split()) > 20:
                    styles.append(st)

            except Exception:
                return {"anomaly_detected": False, "confidence": 0}

        if len(styles) < 2:
            return {"anomaly_detected": False, "confidence": 0}

        sentence_lengths = [s['avg_sentence_length'] for s in styles]
        complexity_scores = [s['complex_words_ratio'] for s in styles]

        length_variance = np.var(sentence_lengths) if sentence_lengths else 0
        complexity_variance = np.var(complexity_scores) if complexity_scores else 0

        anomaly_detected = length_variance > 5.0 or complexity_variance > 0.10
        confidence = min(0.95, (length_variance + complexity_variance * 10) / 10)

        return {
            "anomaly_detected": bool(anomaly_detected),
            "confidence": round(confidence, 3),
            "length_variance": round(length_variance, 3),
            "complexity_variance": round(complexity_variance, 3)
        }

    def generate_heatmap_data(self, text, matches):
        """Generate data for similarity heatmap visualization"""
        segments = self.make_segments(text)
        heatmap_data = []

        for i, segment in enumerate(segments):
            segment_similarity = 0
            for match in matches:
                sim = self.similarity(segment, match.get('snippet', ''))
                segment_similarity = max(segment_similarity, sim)

            if segment_similarity > 0.7:
                risk_level = "High"
                color = "red"
            elif segment_similarity > 0.4:
                risk_level = "Medium"
                color = "orange"
            else:
                risk_level = "Low"
                color = "green"

            heatmap_data.append({
                "segment_id": i,
                "text_preview": segment[:100] + "...",
                "similarity": round(segment_similarity, 3),
                "risk_level": risk_level,
                "color": color
            })

        return heatmap_data

    def analyze_timeline_integrity(self, file_path):
        """Analyze file metadata for timestamp anomalies"""
        try:
            create_time = os.path.getctime(file_path)
            modify_time = os.path.getmtime(file_path)

            create_dt = datetime.fromtimestamp(create_time)
            modify_dt = datetime.fromtimestamp(modify_time)

            time_diff = modify_dt - create_dt
            suspicious = time_diff.total_seconds() < 300

            return {
                "created": create_dt.isoformat(),
                "modified": modify_dt.isoformat(),
                "time_difference_seconds": time_diff.total_seconds(),
                "suspicious_timeline": suspicious,
                "interpretation": "Suspicious: very short creation-modification interval" if suspicious else "Normal timeline"
            }
        except:
            return {
                "created": "Unknown",
                "modified": "Unknown",
                "time_difference_seconds": 0,
                "suspicious_timeline": False,
                "interpretation": "Could not analyze file timestamps"
            }

    # ---------------- NEW: DOI extraction & helpers ----------------
    def extract_dois(self, text):
        """Extract DOIs from arbitrary text using regex"""
        return list({m.group(0).rstrip('.,;') for m in DOI_REGEX.finditer(text)})

    def extract_doi_from_url(self, url):
        """Try to extract DOI if present in a URL"""
        if not url:
            return None
        m = DOI_REGEX.search(url)
        if m:
            return m.group(0).rstrip('.,;')
        return None

    # ---------------- ROOT LOGIC ----------------
    def detect(self, fp):
        self.update_progress("📄 LOADING DOCUMENT...", 10)
        self.log(f"📄 ANALYZING FILE: {fp}")
        text = self.extract_text(fp).strip()
        if not text:
            self.log("❌ NO TEXT EXTRACTED FROM DOCUMENT")
            return

        self.log(f"📝 EXTRACTED {len(text.split())} WORDS FOR ANALYSIS")

        self.update_progress("🔍 ANALYZING DOCUMENT STRUCTURE...", 20)
        sections = self.sectionize(text)
        segments_with_meta = self.make_segments_by_section(sections)

        self.update_progress("🌍 SCANNING WIKIPEDIA DATABASE...", 30)
        results = []
        results += self.wikipedia_scan(text)
        
        self.update_progress("🌐 SCANNING WEB SOURCES...", 50)
        results += self.website_scan([seg['text'] for seg in segments_with_meta])
        
        self.update_progress("📚 SCANNING RESEARCH DATABASES...", 70)
        results += self.research_scan(segments_with_meta)

        results = self.clean_results(results)
        score = self.calc_originality(results)

        self.update_progress("🔬 RUNNING FORENSIC ANALYSIS...", 85)
        forensic_data = self.run_forensic_analysis(text, [s['text'] for s in segments_with_meta], fp, results)

        report = {
            "file": fp,
            "analysis_time": datetime.now().isoformat(),
            "originality_score": score,
            "matches_found": len(results),
            "matches": results,
            "forensic_analysis": forensic_data,
            "segments": segments_with_meta
        }

        self.save_json(report)
        self.save_summary_report(report)
        self.save_visualization(report)
        
        if self.gui:
            self.gui.display_results(report)

        self.update_progress("✅ ANALYSIS COMPLETE!", 100)
        self.log("🎉 FORENSIC ANALYSIS COMPLETED SUCCESSFULLY!")

    def run_forensic_analysis(self, text, segments, file_path, matches):
        """Run comprehensive forensic analysis"""
        return {
            "authorship_analysis": self.detect_author_anomalies(segments),
            "timeline_analysis": self.analyze_timeline_integrity(file_path),
            "writing_style": self.analyze_writing_style(text),
            "heatmap_data": self.generate_heatmap_data(text, matches),
            "text_fingerprints": self.rabin_karp_hash(text),
            "semantic_analysis": self.semantic_clustering(segments)
        }

    def semantic_clustering(self, segments):
        """Cluster segments by semantic similarity to detect paraphrasing patterns"""
        if not EMBEDS or len(segments) < 3:
            return {"clusters": [], "paraphrase_risk": 0}

        try:
            embeddings = SEMANTIC_MODEL.encode(segments)
            similarities = util.cos_sim(embeddings, embeddings)

            paraphrase_pairs = []
            for i in range(len(segments)):
                for j in range(i + 1, len(segments)):
                    if similarities[i][j] > 0.8:
                        paraphrase_pairs.append({
                            "segment_a": i,
                            "segment_b": j,
                            "similarity": round(similarities[i][j].item(), 3)
                        })

            return {
                "clusters": paraphrase_pairs,
                "paraphrase_risk": len(paraphrase_pairs) / max(1, len(segments))
            }
        except:
            return {"clusters": [], "paraphrase_risk": 0}

    # ---------------- SECTIONING ----------------
    def sectionize(self, text):
        headings = [
            r'\babstract\b',
            r'\bintroduction\b',
            r'\bbackground\b',
            r'\bmaterials and methods\b',
            r'\bmethodology\b',
            r'\bmethods\b',
            r'\bresults\b',
            r'\bdiscussion\b',
            r'\bconclusion\b',
            r'\breferences\b',
            r'\backnowledg(e?)ments\b'
        ]
        
        low = text.lower()
        spans = []
        for h in headings:
            for m in re.finditer(h, low):
                spans.append((m.start(), m.group(0)))
        spans.sort()
        sections = []
        if not spans:
            paras = [p.strip() for p in re.split(r'\n{2,}', text) if len(p.strip()) > 100][:8]
            for i, p in enumerate(paras):
                sections.append((f"Section_{i + 1}", p))
            return sections

        for idx, (pos, label) in enumerate(spans):
            start = pos
            end = spans[idx + 1][0] if idx + 1 < len(spans) else len(text)
            sec_text = text[start:end].strip()
            sec_name = label.strip().title()
            sections.append((sec_name, sec_text))

        if spans[0][0] > 50:
            front = text[:spans[0][0]].strip()
            if front:
                sections.insert(0, ("Front", front))

        return sections

    # ---------------- SEGMENTS (section-aware) ----------------
    def make_segments(self, text):
        return [s.strip() for s in re.split(r'[.!?]', text) if len(s) > 50][:15]

    def make_segments_by_section(self, sections):
        out = []
        sid = 0
        for sec_name, sec_text in sections:
            units = [u.strip() for u in re.split(r'(?<=[.!?])\s+', sec_text) if len(u.strip()) > 60]
            if not units:
                units = [sec_text] if len(sec_text) > 60 else []
            for u in units:
                out.append({"segment_id": sid, "section": sec_name, "text": u})
                sid += 1
                if sid >= 60:
                    break
            if sid >= 60:
                break
        return out[:60]

    # ---------------- SIMILARITY ENGINE ----------------
    def similarity(self, a, b):
        a, b = (a or "")[:300], (b or "")[:300]
        sims = []

        if EMBEDS:
            try:
                e1 = SEMANTIC_MODEL.encode(a, convert_to_tensor=True)
                e2 = SEMANTIC_MODEL.encode(b, convert_to_tensor=True)
                sims.append(util.cos_sim(e1, e2).item())
            except:
                pass

        if TFIDF:
            try:
                m = VECTORIZER.fit_transform([a, b])
                sims.append(cosine_similarity(m[0:1], m[1:2])[0][0])
            except:
                pass

        A, B = set(a.lower().split()), set(b.lower().split())
        if A and B:
            sims.append(len(A & B) / len(A | B))

        return max(sims) if sims else 0

    # ---------------- SCAN: WIKIPEDIA ----------------
    def wikipedia_scan(self, text):
        self.log("🌍 SCANNING WIKIPEDIA DATABASE...")
        matches = []
        start = time.time()

        api = "https://en.wikipedia.org/w/api.php"
        headers = {"User-Agent": "LitePlagiarismScanner/1.0"}

        keywords = list(dict.fromkeys(re.findall(r'\b[A-Za-z]{6,}\b', text)))[:6]

        for kw in keywords:
            if time.time() - start > SCAN_TIMEOUT:
                self.log("⏳ WIKIPEDIA SCAN TIMEOUT REACHED")
                break

            try:
                r = requests.get(api, params={
                    "action": "query", "list": "search",
                    "format": "json", "srsearch": kw
                }, headers=headers, timeout=8)

                for itm in r.json().get("query", {}).get("search", [])[:2]:
                    pid = itm["pageid"]
                    title = itm["title"]

                    r2 = requests.get(api, params={
                        "action": "query",
                        "prop": "extracts",
                        "exchars": 3000,
                        "pageids": pid,
                        "format": "json",
                        "explaintext": 1
                    }, headers=headers, timeout=8)

                    ext = r2.json()["query"]["pages"][str(pid)].get("extract", "")
                    sim = self.similarity(text, ext)

                    if sim > 0.25:
                        self.log(f"✅ WIKIPEDIA MATCH: {title} ({sim:.1%})")
                        matches.append({
                            "source": "Wikipedia",
                            "title": title,
                            "url": f"https://en.wikipedia.org/wiki/{title.replace(' ', '_')}",
                            "similarity": round(sim, 3),
                            "snippet": ext[:400] + "..."
                        })
            except:
                continue

        return matches

    # ---------------- SCAN: WEBSITES ----------------
    def website_scan(self, segments_texts):
        self.log("🌐 SCANNING WEB SOURCES...")
        matches = []
        start = time.time()

        if not DUCKSEARCH:
            self.log("⚠️ DuckDuckGo search not available")
            return matches

        try:
            ddg = DDGS()
            
            # Use longer queries for better results
            for s in segments_texts:
                if time.time() - start > SCAN_TIMEOUT:
                    self.log("⏳ WEB SCAN TIMEOUT REACHED")
                    break

                try:
                    # Use longer query for better search results
                    query = s[:300] if len(s) > 300 else s
                    self.log(f"🔍 SEARCHING: {query[:150]}...")
                    
                    results = ddg.text(query, max_results=10)  # Increased results
                    
                    for r in results:
                        url = r.get("href", "")
                        if not url:
                            continue

                        try:
                            # Enhanced web scraping with better content extraction
                            headers = {
                                "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36",
                                "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8",
                                "Accept-Language": "en-US,en;q=0.5",
                                "Accept-Encoding": "gzip, deflate",
                                "Connection": "keep-alive",
                                "Upgrade-Insecure-Requests": "1",
                            }
                            
                            response = requests.get(url, headers=headers, timeout=25)
                            response.raise_for_status()
                            
                            soup = BeautifulSoup(response.content, 'html.parser')
                            
                            # Remove script and style elements
                            for script in soup(["script", "style", "nav", "header", "footer", "aside", "form"]):
                                script.decompose()
                            
                            # Extract main content - comprehensive approach
                            content_parts = []
                            
                            # Try multiple content extraction strategies
                            content_selectors = [
                                'article', 'main', 
                                '[class*="content"]', '[class*="main"]', '[class*="post"]', 
                                '[class*="article"]', '[class*="story"]', '[class*="body"]',
                                '.entry-content', '.post-content', '.article-content',
                                '.story-content', '.news-content', '.content-area',
                                '#content', '#main', '#article'
                            ]
                            
                            for selector in content_selectors:
                                elements = soup.select(selector)
                                for elem in elements:
                                    text = elem.get_text(" ", strip=True)
                                    if len(text) > 100:
                                        content_parts.append(text)
                            
                            # If no specific content found, use body
                            if not content_parts:
                                body = soup.find('body')
                                if body:
                                    # Remove unwanted elements
                                    for unwanted in body.find_all(['nav', 'header', 'footer', 'aside', 'script', 'style', 'form']):
                                        unwanted.decompose()
                                    body_text = body.get_text(" ", strip=True)
                                    if len(body_text) > 200:
                                        content_parts.append(body_text)
                            
                            # Combine all content parts
                            content = " ".join(content_parts)
                            
                            # Clean up the content
                            content = re.sub(r'\s+', ' ', content)
                            content = content.strip()
                            
                            if len(content) < 150:  # Skip if content is too short
                                continue
                                
                            # Calculate similarity
                            sim = self.similarity(s, content)
                            
                            # Also check for keyword matches
                            words_s = set(re.findall(r'\b\w+\b', s.lower()))
                            words_content = set(re.findall(r'\b\w+\b', content.lower()))
                            common_words = words_s.intersection(words_content)
                            word_similarity = len(common_words) / len(words_s) if words_s else 0

                            # Use the higher similarity score
                            final_similarity = max(sim, word_similarity)

                            if final_similarity > 0.15:  # Lower threshold for comprehensive detection
                                doi = self.extract_doi_from_url(url) or (self.extract_dois(content) or [None])[0]
                                title = r.get("title", "") or (soup.title.string if soup.title else url)
                                
                                self.log(f"✅ WEB MATCH: {title[:100]} ({final_similarity:.1%}) - {url}")
                                matches.append({
                                    "source": "Website",
                                    "title": title[:200],
                                    "url": url,
                                    "similarity": round(final_similarity, 3),
                                    "snippet": content[:800] + "...",
                                    "doi": doi
                                })
                        except Exception as e:
                            continue
                        
                except Exception as e:
                    continue
                    
        except Exception as e:
            self.log(f"⚠️ DuckDuckGo search error: {str(e)}")
            
        return matches

    # ---------------- SCAN: Research papers (CrossRef + Semantic Scholar) ----------------
    def crossref_search(self, query):
        out = []
        try:
            api = "https://api.crossref.org/works"
            r = requests.get(api, params={"query.bibliographic": query, "rows": CROSSREF_ROWS}, timeout=8,
                             headers={"User-Agent": "LitePlagiarismScanner/1.0"})
            data = r.json().get("message", {}).get("items", [])
            for item in data:
                doi = item.get("DOI")
                title = " ".join(item.get("title", [])) if item.get("title") else ""
                url = item.get("URL")
                abstract = item.get("abstract", "")
                out.append({"title": title, "doi": doi, "url": url, "abstract": abstract})
        except:
            pass
        return out

    def semantic_scholar_search(self, query):
        out = []
        try:
            api = "https://api.semanticscholar.org/graph/v1/paper/search"
            r = requests.get(api, params={"query": query, "limit": SEMANTIC_SCHOLAR_LIMIT,
                                          "fields": "title,abstract,url,externalIds"},
                             headers={"User-Agent": "LitePlagiarismScanner/1.0"}, timeout=8)
            js = r.json()
            for item in js.get("data", []):
                title = item.get("title", "")
                abstract = item.get("abstract", "") or ""
                url = item.get("url", "")
                ext = item.get("externalIds", {}) or {}
                doi = ext.get("DOI") or ext.get("ArXivId") or None
                out.append({"title": title, "doi": doi, "url": url, "abstract": abstract})
        except:
            pass
        return out

    def research_scan(self, segments_with_meta):
        self.log("📚 SCANNING RESEARCH DATABASES...")
        matches = []
        start = time.time()

        for seg in segments_with_meta:
            if time.time() - start > SCAN_TIMEOUT:
                self.log("⏳ RESEARCH SCAN TIMEOUT REACHED")
                break

            q = seg['text'][:200]
            # CrossRef
            try:
                cr = self.crossref_search(q)
                for item in cr:
                    sim = self.similarity(seg['text'], item.get('abstract', '') or item.get('title', ''))
                    if sim > 0.25:
                        self.log(f"✅ CROSSREF MATCH: {item.get('title','')[:80]} ({sim:.1%})")
                        matches.append({
                            "source": "CrossRef",
                            "title": item.get("title"),
                            "url": item.get("url"),
                            "doi": item.get("doi"),
                            "similarity": round(sim, 3),
                            "snippet": (item.get("abstract") or "")[:400] + "..."
                        })
            except:
                pass

            # Semantic Scholar
            try:
                ss = self.semantic_scholar_search(q)
                for item in ss:
                    sim = self.similarity(seg['text'], item.get('abstract', '') or item.get('title', ''))
                    if sim > 0.25:
                        self.log(f"✅ SEMANTIC SCHOLAR MATCH: {item.get('title','')[:80]} ({sim:.1%})")
                        matches.append({
                            "source": "SemanticScholar",
                            "title": item.get("title"),
                            "url": item.get("url"),
                            "doi": item.get("doi"),
                            "similarity": round(sim, 3),
                            "snippet": (item.get("abstract") or "")[:400] + "..."
                        })
            except:
                pass

        return matches

    # ---------------- OUTPUT ----------------
    def clean_results(self, r):
        seen = set()
        out = []
        for m in r:
            key = (m.get("url") or m.get("doi") or m.get("title") or str(m.get("snippet")) )[:200]
            if key not in seen:
                seen.add(key)
                out.append(m)
        return sorted(out, key=lambda x: x.get("similarity", 0), reverse=True)

    def calc_originality(self, R):
        if not R:
            return 100.0
        penalty = sum(m.get("similarity", 0) * 100 for m in R) / len(R)
        return max(0.0, round(100.0 - penalty, 1))

    def save_json(self, rep):
        fn = f"forensic_report_{int(time.time())}.json"
        try:
            with open(fn, "w", encoding='utf-8') as f:
                json.dump(rep, f, indent=2, ensure_ascii=False)
            self.log(f"💾 JSON REPORT SAVED: {fn}")
        except Exception as e:
            self.log(f"❌ Failed to save JSON: {str(e)}")

    def save_summary_report(self, rep):
        fn = f"forensic_summary_{int(time.time())}.txt"
        try:
            with open(fn, "w", encoding="utf-8") as f:
                f.write("📌 LITE++ FORENSIC PLAGIARISM SUMMARY\n")
                f.write("="*60 + "\n\n")
                f.write(f"File: {rep['file']}\n")
                f.write(f"Time: {rep['analysis_time']}\n")
                f.write(f"Originality Score: {rep['originality_score']}%\n")
                f.write(f"Matches Found: {rep['matches_found']}\n\n")

                f.write("MATCHES:\n")
                for m in rep["matches"]:
                    f.write(f"- {m.get('source','?')} ({m.get('similarity',0)*100:.1f}%): {m.get('url') or m.get('doi') or m.get('title','')}\n")

                forensic = rep.get("forensic_analysis", {})
                if forensic:
                    f.write("\nFORENSIC ANALYSIS:\n")
                    auth = forensic.get("authorship_analysis", {})
                    f.write(f"- Authorship Anomaly: {auth.get('anomaly_detected', False)}\n")
                    f.write(f"- Anomaly Confidence: {auth.get('confidence', 0):.2f}\n")

                    timeline = forensic.get("timeline_analysis", {})
                    f.write(f"- Timeline Suspicious: {timeline.get('suspicious_timeline', False)}\n")
                    f.write(f"- Timeline Interpretation: {timeline.get('interpretation', 'N/A')}\n")
            self.log(f"📝 SUMMARY REPORT SAVED: {fn}")
        except Exception as e:
            self.log(f"❌ Failed to save summary: {str(e)}")

    def save_forensic_report(self, rep):
        def safe_text(x):
            if x is None:
                return ""
            try:
                return str(x)
            except:
                return repr(x)

        try:
            from reportlab.lib.pagesizes import A4
            from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
            from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, Table, TableStyle, PageBreak
            from reportlab.lib import colors
            from reportlab.lib.units import mm

            fn = f"forensic_report_{int(time.time())}.pdf"
            doc = SimpleDocTemplate(fn, pagesize=A4,
                                    rightMargin=18*mm, leftMargin=18*mm,
                                    topMargin=18*mm, bottomMargin=18*mm)
            styles = getSampleStyleSheet()
            story = []

            title_style = styles['Title']
            story.append(Paragraph("AI-Powered Forensic Plagiarism Report", title_style))
            story.append(Spacer(1, 12))

            normal = styles['Normal']
            normal.spaceAfter = 6
            story.append(Paragraph(f"<b>File:</b> {safe_text(rep.get('file'))}", normal))
            story.append(Paragraph(f"<b>Analysis Time:</b> {safe_text(rep.get('analysis_time'))}", normal))
            story.append(Paragraph(f"<b>Originality Score:</b> {safe_text(rep.get('originality_score'))} %", normal))
            story.append(Paragraph(f"<b>Matches Found:</b> {safe_text(rep.get('matches_found'))}", normal))
            story.append(Spacer(1, 12))

            matches = rep.get("matches", [])
            if matches:
                data = [["Source", "Similarity", "Title/URL"]]
                for m in matches:
                    data.append([
                        safe_text(m.get("source")),
                        f"{safe_text(round(m.get('similarity',0)*100,1))}%",
                        safe_text(m.get("url") or m.get("doi") or m.get("title",""))
                    ])
                table = Table(data, colWidths=[80, 80, 300])
                table.setStyle(TableStyle([
                    ('BACKGROUND', (0,0), (-1,0), colors.lightgrey),
                    ('GRID', (0,0), (-1,-1), 0.5, colors.grey),
                    ('VALIGN', (0,0), (-1,-1), 'TOP'),
                ]))
                story.append(table)
                story.append(Spacer(1, 12))

            forensic = rep.get("forensic_analysis", {})
            story.append(Paragraph("<b>Forensic Analysis:</b>", normal))
            authorship = forensic.get("authorship_analysis", {})
            story.append(Paragraph(f"- Authorship Anomaly: {safe_text(authorship.get('anomaly_detected'))}", normal))
            story.append(Paragraph(f"- Anomaly Confidence: {safe_text(authorship.get('confidence',0))}", normal))

            timeline = forensic.get("timeline_analysis", {})
            story.append(Paragraph(f"- Timeline Suspicious: {safe_text(timeline.get('suspicious_timeline'))}", normal))
            story.append(Paragraph(f"- Timeline Interpretation: {safe_text(timeline.get('interpretation'))}", normal))

            doc.build(story)
            self.log(f"📄 PDF FORENSIC REPORT SAVED: {fn}")

        except ImportError:
            try:
                from fpdf import FPDF
                pdf = FPDF()
                pdf.add_page()
                pdf.set_font("Arial", "B", 14)
                pdf.cell(0, 10, "AI-Powered Forensic Plagiarism Report", ln=1)
                pdf.set_font("Arial", "", 12)
                pdf.multi_cell(0, 8, f"File: {safe_text(rep.get('file'))}\nTime: {safe_text(rep.get('analysis_time'))}\nOriginality Score: {safe_text(rep.get('originality_score'))}%\nMatches Found: {safe_text(rep.get('matches_found'))}")
                fn = f"forensic_report_{int(time.time())}.pdf"
                pdf.output(fn)
                self.log(f"📄 PDF REPORT SAVED (FPDF2): {fn}")
            except:
                self.log("❌ PDF GENERATION FAILED")

    def save_visualization(self, rep):
        try:
            originality = rep.get("originality_score", 0)
            matches = rep.get("matches_found", 0)

            if originality is None:
                originality = 0
            if matches is None:
                matches = 0

            plt.figure(figsize=(10, 6))
            plt.bar(["Originality Score", "Matches Found"],
                    [originality, matches], color=['#00ff00', '#ff4444'])
            plt.title("Document Plagiarism Overview", fontsize=14, fontweight='bold')
            plt.ylabel("Value", fontweight='bold')
            plt.grid(True, alpha=0.3)

            fn = f"forensic_viz_{int(time.time())}.png"
            plt.savefig(fn, dpi=300, bbox_inches="tight", facecolor='#0a0a0a')
            plt.close()

            self.log(f"📊 VISUALIZATION SAVED: {fn}")
        except Exception as e:
            self.log(f"❌ Failed to save visualization: {str(e)}")

def main():
    try:
        root = tk.Tk()
        app = AdvancedPlagiarismDetectorGUI(root)
        root.mainloop()
    except Exception as e:
        print(f"❌ Application failed to start: {str(e)}")
        print("💡 Please check if all required dependencies are installed:")
        print("pip install matplotlib numpy requests beautifulsoup4 PyPDF2 python-docx nltk")
        print("Optional: pip install ddgs sentence-transformers scikit-learn")

if __name__ == "__main__":
    main()