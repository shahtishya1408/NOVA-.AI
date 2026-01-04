# NOVA-.AI
# 🤖 NOVA Code Analyzer

A voice-activated Python code analysis tool that uses Abstract Syntax Tree (AST) to provide intelligent code summaries.

## 🌟 Features

### Voice-Activated Assistant
- Wake-word detection ("Jarvis", "Nova", "Hey Jarvis")
- Natural language voice commands
- Text-to-speech responses
- Automatic sleep mode after inactivity

### AST-Based Code Analysis
- **Function Analysis**: Detects functions, parameters, decorators, return types
- **Class Analysis**: Identifies classes, methods, inheritance, attributes
- **Import Tracking**: Lists all imported libraries and modules
- **Complexity Metrics**: Calculates cyclomatic complexity
- **Line Statistics**: Code lines, comments, blank lines
- **Docstring Extraction**: Captures module, class, and function documentation

### Capabilities
- Analyze single Python files
- Batch analyze all files in a directory
- Compare two Python files side-by-side
- Interactive text-based interface (no voice required)

## 📋 Requirements

```bash
pip install SpeechRecognition
pip install googletrans==4.0.0rc1
pip install gTTS
pip install pydub
pip install pyttsx3
pip install pywhatkit
pip install PyAudio  # For microphone input
```

### System Requirements
- Python 3.7+
- Microphone (for voice mode)
- Internet connection (for Google Speech Recognition and translation)

### Additional Dependencies
- **Linux**: `sudo apt-get install portaudio19-dev python3-pyaudio`
- **macOS**: `brew install portaudio`
- **Windows**: PyAudio wheels available at [Unofficial Windows Binaries](https://www.lfd.uci.edu/~gohlke/pythonlibs/#pyaudio)

## 🚀 Quick Start

### Option 1: Text-Based Demo (No Voice Required)

```bash
python code_analyzer_demo.py
```

This runs an interactive menu where you can:
1. Analyze specific files
2. Analyze all Python files in a directory
3. Compare two files
4. No microphone needed!

### Option 2: Voice-Activated Mode

```bash
python jarvis_code_analyzer.py
```

Then say:
- "Jarvis" or "Nova" to wake the assistant
- "Analyze code" to start code analysis
- "Compare files" to compare two files
- "Help" to hear available commands
- "Sleep" to put it back to idle mode

## 📖 Usage Examples

### Example 1: Analyze Your Original Jarvis File

```bash
python code_analyzer_demo.py
```

Choose option 1, then enter:
```
Enter Python file path: jarvis2.2_universal.py
```

You'll get a detailed report like:
```
📄 FILE ANALYSIS: jarvis2.2_universal.py
======================================================================

📊 LINE STATISTICS:
   Total Lines:    450
   Code Lines:     320
   Comment Lines:  85
   Blank Lines:    45

📦 IMPORTS (15):
   • ast
   • datetime
   • googletrans
   • pyttsx3
   • speech_recognition
   ...

⚙️  FUNCTIONS (25):
   • speak_text(text, lang_code, voice_style, block)
     Line: 95 | Complexity: 8
     Doc: Speak text. Try gTTS in target language...

🌍 GLOBAL VARIABLES (8):
   • WAKE_WORDS
   • WAKE_TIMEOUT
   • recognizer
   ...

📈 COMPLEXITY METRICS:
   Total Complexity:   142
   Conditionals (if):  45
   Loops (for/while):  12
   Rating: 🟡 Moderate - Reasonably maintainable
```

### Example 2: Voice Command

1. Run: `python jarvis_code_analyzer.py`
2. Say: **"Jarvis"** (wait for response)
3. Say: **"Analyze code"**
4. Say: **"current directory"** (or say a specific filename)
5. Check the console for detailed output

### Example 3: Compare Files

```bash
python code_analyzer_demo.py
```

Choose option 3, then:
```
Enter first Python file: version1.py
Enter second Python file: version2.py
```

Get a side-by-side comparison:
```
📊 FILE COMPARISON
======================================================================

Metric               File 1               File 2               Difference     
---------------------------------------------------------------------------
Total Lines          450                  520                  +70            
Code Lines           320                  380                  +60            
Functions            25                   32                   +7             
Classes              3                    5                    +2             
Complexity           142                  185                  +43            
```

## 🎯 Voice Commands

When Jarvis is awake:

| Command | Action |
|---------|--------|
| "Analyze code" | Start code analysis workflow |
| "Compare files" | Compare two Python files |
| "Time" | Get current time |
| "Date" | Get current date |
| "Help" | List available commands |
| "Sleep" / "Stop listening" | Return to idle mode |
| "Exit" / "Goodbye" | Quit the program |

## 🔧 Configuration

Edit these variables in `jarvis_code_analyzer.py`:

```python
WAKE_WORDS = ["jarvis", "nova", "hey jarvis"]  # Add your wake words
WAKE_TIMEOUT = 60  # Seconds before auto-sleep
SPEECH_TIMEOUT = 5  # Seconds to wait for speech
```

## 📊 What the Analyzer Detects

### Functions
- Function names and parameters
- Decorators (e.g., @staticmethod, @property)
- Return type annotations
- Async functions
- Docstrings
- Cyclomatic complexity

### Classes
- Class names and inheritance
- All methods
- Class attributes
- Docstrings

### Code Structure
- All imports (standard library, third-party, local)
- Global variables and constants
- Conditionals (if/else)
- Loops (for/while)

### Metrics
- Total lines of code
- Code vs. comments vs. blank lines
- Complexity score (simple/moderate/complex)
- Number of functions and classes

## 🐛 Troubleshooting

### Microphone Not Working
```bash
# Test microphone
python -c "import speech_recognition as sr; print(sr.Microphone.list_microphone_names())"
```

### PyAudio Installation Fails
- **Linux**: `sudo apt-get install python3-pyaudio`
- **Windows**: Download wheel from [here](https://www.lfd.uci.edu/~gohlke/pythonlibs/#pyaudio)
- **macOS**: `brew install portaudio && pip install pyaudio`

### Speech Recognition Not Working
- Check internet connection (Google Speech API requires internet)
- Verify microphone permissions
- Try speaking louder and clearer
- Reduce background noise

### Code Analysis Errors
- Ensure Python file has valid syntax
- Check file permissions
- Make sure file encoding is UTF-8

## 🎨 Example Output

```
================================================================================
📄 FILE ANALYSIS: example_script.py
================================================================================

📊 LINE STATISTICS:
   Total Lines:    156
   Code Lines:     112
   Comment Lines:  28
   Blank Lines:    16

📝 MODULE DESCRIPTION:
   A utility module for data processing and analysis with support for 
   multiple file formats...

📦 IMPORTS (8):
   • json
   • os
   • pandas
   • pathlib.Path
   • requests
   • sys
   • typing.Dict
   • typing.List

🏛️  CLASSES (2):
   • DataProcessor (line 45)
     Methods: __init__, load_data, process, save, validate
     Doc: Main class for processing data files with validation...

   • ResultFormatter (line 98)
     Methods: __init__, format_json, format_csv
     Doc: Formats processing results into various output formats...

⚙️  FUNCTIONS (7):
   • load_config(config_path: str) -> Dict
     Line: 15 | Complexity: 4
     Doc: Load configuration from JSON file...

   • @staticmethod validate_input(data: List) -> bool
     Line: 25 | Complexity: 6
     Doc: Validate input data structure...

🌍 GLOBAL VARIABLES (4):
   • DEFAULT_CONFIG
   • MAX_BATCH_SIZE
   • SUPPORTED_FORMATS
   • VERSION

📈 COMPLEXITY METRICS:
   Total Complexity:   45
   Conditionals (if):  18
   Loops (for/while):  6
   Rating: 🟡 Moderate - Reasonably maintainable

================================================================================
```

## 🔮 Future Enhancements

- [ ] Support for more languages (JavaScript, Java, etc.)
- [ ] Visual complexity graphs
- [ ] Export analysis to HTML/PDF reports
- [ ] Integration with Git for tracking code evolution
- [ ] Custom complexity thresholds
- [ ] Plugin system for custom analyzers

## 📄 License

This project is provided as-is for educational and personal use.

## 🤝 Contributing

Feel free to fork, modify, and improve! Suggestions welcome.

## 📞 Support

If you encounter issues:
1. Check the troubleshooting section above
2. Ensure all dependencies are installed
3. Try the demo version first (no voice required)
4. Check Python version compatibility (3.7+)

---

**Built with ❤️ using Python AST and Speech Recognition**
