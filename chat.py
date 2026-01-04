"""
Jarvis Code Analyzer - Voice-activated code summarization using AST
Combines voice assistant with Abstract Syntax Tree analysis for Python code
"""

import os
import sys
import ast
import time
import tempfile
import datetime
import random
from pathlib import Path
from collections import defaultdict

# Voice/TTS libraries
import speech_recognition as sr
from googletrans import Translator
from gtts import gTTS
from pydub import AudioSegment, effects
from pydub.playback import play
import pyttsx3

# -----------------------
# Configuration
# -----------------------
WAKE_WORDS = ["jarvis", "hey jarvis", "nova"]
WAKE_TIMEOUT = 60
SPEECH_TIMEOUT = 5
PHRASE_LIMIT = 6
PREFERRED_LANG = "en"
MEDIA_TEMP_DIR = tempfile.gettempdir()

# -----------------------
# Initialize helpers
# -----------------------
recognizer = sr.Recognizer()
translator = Translator()
engine = pyttsx3.init()
engine.setProperty('rate', 165)
engine.setProperty('volume', 1.0)

# -----------------------
# Audio utilities
# -----------------------

def speak_text(text, block=True):
    """Speak text using pyttsx3 for simplicity"""
    if not text:
        return
    try:
        if block:
            engine.say(text)
            engine.runAndWait()
        else:
            engine.say(text)
            engine.runAndWait()
    except Exception as e:
        print(f"Speech error: {e}")


def take_command(timeout=SPEECH_TIMEOUT, phrase_time_limit=PHRASE_LIMIT):
    """Listen and convert speech to text"""
    with sr.Microphone() as source:
        recognizer.adjust_for_ambient_noise(source, duration=0.4)
        try:
            audio = recognizer.listen(source, timeout=timeout, phrase_time_limit=phrase_time_limit)
        except sr.WaitTimeoutError:
            return ""
    
    text = ""
    try:
        text = recognizer.recognize_google(audio, language='en-IN')
    except Exception:
        try:
            text = recognizer.recognize_google(audio)
        except Exception:
            text = ""
    
    print(f"Recognized: {text}")
    return text

# -----------------------
# AST Code Analysis
# -----------------------

class CodeAnalyzer(ast.NodeVisitor):
    """Analyzes Python code using AST"""
    
    def __init__(self):
        self.functions = []
        self.classes = []
        self.imports = []
        self.global_vars = []
        self.docstring = None
        self.complexity_score = 0
        
    def visit_Module(self, node):
        """Extract module-level docstring"""
        if ast.get_docstring(node):
            self.docstring = ast.get_docstring(node)
        self.generic_visit(node)
        
    def visit_FunctionDef(self, node):
        """Analyze function definitions"""
        func_info = {
            'name': node.name,
            'args': [arg.arg for arg in node.args.args],
            'decorators': [self._get_decorator_name(d) for d in node.decorator_list],
            'docstring': ast.get_docstring(node),
            'line_number': node.lineno,
            'is_async': isinstance(node, ast.AsyncFunctionDef)
        }
        self.functions.append(func_info)
        self.complexity_score += len(node.body)
        self.generic_visit(node)
        
    def visit_AsyncFunctionDef(self, node):
        """Handle async functions"""
        self.visit_FunctionDef(node)
        
    def visit_ClassDef(self, node):
        """Analyze class definitions"""
        methods = [n.name for n in node.body if isinstance(n, (ast.FunctionDef, ast.AsyncFunctionDef))]
        class_info = {
            'name': node.name,
            'bases': [self._get_name(base) for base in node.bases],
            'methods': methods,
            'docstring': ast.get_docstring(node),
            'line_number': node.lineno
        }
        self.classes.append(class_info)
        self.complexity_score += len(methods) * 2
        self.generic_visit(node)
        
    def visit_Import(self, node):
        """Track import statements"""
        for alias in node.names:
            self.imports.append(alias.name)
        
    def visit_ImportFrom(self, node):
        """Track from...import statements"""
        module = node.module or ''
        for alias in node.names:
            self.imports.append(f"{module}.{alias.name}")
            
    def visit_Assign(self, node):
        """Track global variable assignments"""
        for target in node.targets:
            if isinstance(target, ast.Name):
                self.global_vars.append(target.id)
        self.generic_visit(node)
        
    def _get_decorator_name(self, decorator):
        """Extract decorator name"""
        if isinstance(decorator, ast.Name):
            return decorator.id
        elif isinstance(decorator, ast.Call):
            return self._get_name(decorator.func)
        return str(decorator)
        
    def _get_name(self, node):
        """Extract name from various AST node types"""
        if isinstance(node, ast.Name):
            return node.id
        elif isinstance(node, ast.Attribute):
            return f"{self._get_name(node.value)}.{node.attr}"
        return str(node)


def analyze_python_file(filepath):
    """Analyze a Python file and return summary"""
    try:
        with open(filepath, 'r', encoding='utf-8') as f:
            code = f.read()
        
        tree = ast.parse(code, filename=filepath)
        analyzer = CodeAnalyzer()
        analyzer.visit(tree)
        
        # Count lines
        lines = code.split('\n')
        total_lines = len(lines)
        code_lines = sum(1 for line in lines if line.strip() and not line.strip().startswith('#'))
        
        summary = {
            'filename': os.path.basename(filepath),
            'total_lines': total_lines,
            'code_lines': code_lines,
            'functions': analyzer.functions,
            'classes': analyzer.classes,
            'imports': list(set(analyzer.imports)),
            'global_vars': list(set(analyzer.global_vars)),
            'docstring': analyzer.docstring,
            'complexity': analyzer.complexity_score
        }
        
        return summary
        
    except SyntaxError as e:
        return {'error': f"Syntax error in file: {e}"}
    except Exception as e:
        return {'error': f"Error analyzing file: {e}"}


def generate_summary_text(analysis):
    """Convert analysis to readable summary"""
    if 'error' in analysis:
        return analysis['error']
    
    parts = []
    
    # File info
    parts.append(f"File: {analysis['filename']}")
    parts.append(f"Total lines: {analysis['total_lines']}, Code lines: {analysis['code_lines']}")
    
    # Docstring
    if analysis['docstring']:
        parts.append(f"Description: {analysis['docstring'][:100]}")
    
    # Imports
    if analysis['imports']:
        parts.append(f"Uses {len(analysis['imports'])} libraries including: {', '.join(analysis['imports'][:5])}")
    
    # Classes
    if analysis['classes']:
        parts.append(f"Contains {len(analysis['classes'])} classes:")
        for cls in analysis['classes'][:3]:
            parts.append(f"  - {cls['name']} with {len(cls['methods'])} methods")
    
    # Functions
    if analysis['functions']:
        parts.append(f"Contains {len(analysis['functions'])} functions:")
        for func in analysis['functions'][:5]:
            args_str = ', '.join(func['args']) if func['args'] else 'no args'
            parts.append(f"  - {func['name']}({args_str})")
    
    # Complexity
    if analysis['complexity'] < 50:
        complexity_desc = "simple"
    elif analysis['complexity'] < 150:
        complexity_desc = "moderate"
    else:
        complexity_desc = "complex"
    parts.append(f"Code complexity: {complexity_desc}")
    
    return '\n'.join(parts)


def find_python_files(directory='.'):
    """Find all Python files in directory"""
    python_files = []
    for root, dirs, files in os.walk(directory):
        # Skip common non-code directories
        dirs[:] = [d for d in dirs if d not in ['.git', '__pycache__', 'venv', 'env', 'node_modules']]
        for file in files:
            if file.endswith('.py'):
                python_files.append(os.path.join(root, file))
    return python_files

# -----------------------
# Voice Commands
# -----------------------

def analyze_code_command():
    """Handle code analysis voice command"""
    speak_text("Which file should I analyze? Say the filename or say 'current directory' for all files.")
    
    response = take_command(timeout=10)
    if not response:
        speak_text("I didn't hear anything. Canceling.")
        return
    
    response = response.lower()
    
    if 'current directory' in response or 'all files' in response:
        # Analyze all Python files in current directory
        files = find_python_files('.')
        if not files:
            speak_text("No Python files found in current directory.")
            return
        
        speak_text(f"Found {len(files)} Python files. Analyzing now.")
        
        for filepath in files[:5]:  # Limit to first 5
            analysis = analyze_python_file(filepath)
            summary = generate_summary_text(analysis)
            print("\n" + "="*60)
            print(summary)
            print("="*60 + "\n")
        
        speak_text(f"Analysis complete. Analyzed {min(len(files), 5)} files. Check the console for details.")
        
    else:
        # Try to find the mentioned file
        # Clean up the response to get filename
        filename = response.replace('analyze', '').replace('file', '').strip()
        
        # Check if file exists
        if not os.path.exists(filename):
            # Try adding .py extension
            filename_py = filename + '.py'
            if os.path.exists(filename_py):
                filename = filename_py
            else:
                speak_text(f"Could not find file: {filename}")
                return
        
        speak_text(f"Analyzing {filename}")
        analysis = analyze_python_file(filename)
        summary = generate_summary_text(analysis)
        
        print("\n" + "="*60)
        print(summary)
        print("="*60 + "\n")
        
        # Speak summary (abbreviated version)
        if 'error' not in analysis:
            brief = f"File has {analysis['total_lines']} lines with {len(analysis['functions'])} functions and {len(analysis['classes'])} classes."
            speak_text(brief)
        else:
            speak_text(summary)


def compare_files_command():
    """Compare two Python files"""
    speak_text("Say the first filename")
    file1 = take_command(timeout=10)
    
    if not file1:
        speak_text("Canceling comparison.")
        return
        
    speak_text("Say the second filename")
    file2 = take_command(timeout=10)
    
    if not file2:
        speak_text("Canceling comparison.")
        return
    
    # Add .py if needed
    if not file1.endswith('.py'):
        file1 += '.py'
    if not file2.endswith('.py'):
        file2 += '.py'
    
    if not os.path.exists(file1) or not os.path.exists(file2):
        speak_text("One or both files not found.")
        return
    
    speak_text("Comparing files now.")
    
    analysis1 = analyze_python_file(file1)
    analysis2 = analyze_python_file(file2)
    
    comparison = f"""
COMPARISON REPORT
{'='*60}
File 1: {analysis1['filename']}
  Lines: {analysis1['total_lines']}
  Functions: {len(analysis1['functions'])}
  Classes: {len(analysis1['classes'])}
  
File 2: {analysis2['filename']}
  Lines: {analysis2['total_lines']}
  Functions: {len(analysis2['functions'])}
  Classes: {len(analysis2['classes'])}
  
Differences:
  Lines: {abs(analysis1['total_lines'] - analysis2['total_lines'])} difference
  Functions: {abs(len(analysis1['functions']) - len(analysis2['functions']))} difference
  Classes: {abs(len(analysis1['classes']) - len(analysis2['classes']))} difference
{'='*60}
"""
    
    print(comparison)
    speak_text(f"File 1 has {analysis1['total_lines']} lines, File 2 has {analysis2['total_lines']} lines. Check console for full comparison.")

# -----------------------
# Main Assistant Loop
# -----------------------

def wait_for_wake_word():
    """Listen for wake word"""
    print('[IDLE] Listening for wake word...')
    while True:
        try:
            with sr.Microphone() as source:
                recognizer.adjust_for_ambient_noise(source, duration=0.4)
                audio = recognizer.listen(source, timeout=None, phrase_time_limit=4)
            try:
                heard = recognizer.recognize_google(audio).lower()
            except Exception:
                continue
            
            print(f'Heard: {heard}')
            for w in WAKE_WORDS:
                if w in heard:
                    return True
        except Exception as e:
            print(f'Wake word error: {e}')
            time.sleep(0.5)


def assistant_active_session():
    """Main active session handling commands"""
    speak_text("Yes? I'm listening.")
    last_activity = time.time()
    
    while True:
        if time.time() - last_activity > WAKE_TIMEOUT:
            speak_text('Going back to sleep.')
            return
        
        text = take_command()
        if not text:
            continue
        
        last_activity = time.time()
        lower = text.lower()
        
        # Exit commands
        if any(k in lower for k in ['sleep', 'go to sleep', 'stop listening']):
            speak_text('Okay, going to sleep.')
            return
        
        if any(k in lower for k in ['exit', 'bye', 'quit', 'goodbye']):
            speak_text('Goodbye!')
            sys.exit(0)
        
        # Code analysis commands
        if 'analyze' in lower or 'summarize' in lower or 'summary' in lower:
            analyze_code_command()
            continue
        
        if 'compare' in lower:
            compare_files_command()
            continue
        
        # Time/date
        if 'time' in lower:
            t = datetime.datetime.now().strftime('%I:%M %p')
            speak_text(f"Current time is {t}")
            continue
        
        if 'date' in lower:
            d = datetime.datetime.now().strftime('%A, %B %d, %Y')
            speak_text(f"Today is {d}")
            continue
        
        # Help
        if 'help' in lower or 'what can you do' in lower:
            speak_text("I can analyze Python code, compare files, tell time and date. Say 'analyze code' to start.")
            continue
        
        # Default
        speak_text("I heard: " + text)


def main_loop():
    """Main application loop"""
    speak_text("Code analyzer is running. Say 'Jarvis' to wake me.")
    
    try:
        while True:
            woke = wait_for_wake_word()
            if woke:
                assistant_active_session()
    except KeyboardInterrupt:
        print('\nExiting...')
        sys.exit(0)


if __name__ == '__main__':
    main_loop()