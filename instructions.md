# 📘 INSTRUCTIONS
## Meaning‑Based AI Translator — Setup & Usage Guide

This guide explains exactly how to install, run, and use the Meaning‑Based AI Translator.  
It is written for beginners — no coding experience required.

---

# ✅ 1. Download & Install Ollama

Ollama is the AI engine that powers the translations.

Download it here:

👉 https://ollama.com/download

After installing, open a terminal and run:

```bash
ollama run qwen2.5
```

This downloads the AI model used by the translator.

---

# ✅ 2. Install Python (if you don’t already have it)

Download Python here:

👉 https://www.python.org/downloads/

During installation, make sure to check:

✔️ **Add Python to PATH**

---

# ✅ 3. Create the project folder

Your project should contain these files:

```
index.html
script.js
server.py
requirements.txt
styles/
    dark.css
    minimal.css
    mobile.css
    pastel.css
```

If any file is missing, create it manually.

---

# ✅ 4. Copy the code into the correct files

You MUST copy the full contents of the following files from the GitHub repository:

### ✔️ Copy **ALL** of `server.py`  
Paste the entire code into your local `server.py` file.

### ✔️ Copy **ALL** of `script.js`  
Paste the entire code into your local `script.js` file.

### ✔️ Copy **ALL** CSS files  
Paste each stylesheet into its matching file inside the `styles/` folder.

### ✔️ Copy `index.html`  
Paste the full HTML into your local `index.html`.

> **Important:**  
> These files must match exactly or the app will not work.

---

# ✅ 5. Install required Python packages

Open a terminal **inside the project folder** and run:

```bash
pip install -r requirements.txt
```

This installs Flask and any other needed libraries.

---

# ✅ 6. Start the backend server

In the same terminal, run:

```bash
python server.py
```

You should see:

```
Running on http://127.0.0.1:5000
```

Leave this window open — this is the backend.

---

# ✅ 7. Open the app (frontend)

Open the file:

```
index.html
```

Double‑click it or open it in your browser.

This is the actual translator interface.

---

# ✅ 8. How to use the translator

1. Type any English phrase  
2. Click **Translate**  
3. The app will show:
   - The meaning  
   - A natural Japanese translation  
   - A cultural/context explanation  

---

# 🛠️ Troubleshooting

### ❗ “Cannot connect to server”
Make sure `server.py` is running.

### ❗ “Model not found”
Run:

```bash
ollama run qwen2.5
```

### ❗ Nothing happens when clicking Translate
Restart both:
- the backend (`server.py`)
- the model (`ollama run qwen2.5`)

---

# 🛑 Stopping the app

To stop the backend server:

```bash
CTRL + C
```

To stop Ollama:  
Close the terminal running it.

---

# 🎉 You’re all set!

Your Meaning‑Based AI Translator is now fully installed and ready to use.
