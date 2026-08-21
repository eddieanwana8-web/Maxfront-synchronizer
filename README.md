# Maxfront Global Time-Zone Synchronizer

A lightweight, responsive web utility built to eliminate scheduling friction for remote teams operating across Nigeria (WAT), Southeast Asia (MYT), and Timor-Leste (TLT) hubs.

## 🚀 Live Demo & Code Architecture
*   **Production Frontend:** View the active interface layout in [`index.html`](index.html)
*   **Core Logic Prototype:** View the standalone backend calculation engine in [`timezone_sync.py`](timezone_sync.py)

## 🛠️ How It Works (Technical Overview)
The application takes the local Nigerian time (WAT) and maps it across Maxfront's primary operational regions. 

To handle calculations that cross over into a new calendar day cleanly without breaking, both the frontend script and the backend prototype utilize a **modulo 24 operation** (`hour % 24`). This ensures that if a meeting is set for 18:00 in Lagos, the Timor-Leste hub correctly displays 02:00 with a `(Next Day)` tag, rather than outputting an invalid time like 26:00.

## 💻 Tech Stack & Concepts Applied
- **Frontend:** Semantic HTML5, CSS3 (Flexbox architecture), and JavaScript (ES6 DOM manipulation).
- **Backend / Scripting:** Python 3 (Dictionaries, user-input validation, and functional loops).
- **Workflow Tools:** Git version control, GitHub Pages deployment framework.