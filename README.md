# place finder

A **Flask** web application that integrates with **Google’s Places API** to search and display information about nearby places.:contentReference[oaicite:1]{index=1}

## 🚀 Features

- ✨ Search for places using Google Places API
- 📍 Display place information in a web UI
- 🗺️ Flask-based backend with Jinja2 templates
- 📦 Static assets served for UI styling and layout
- Easy to expand with search types and filters

## 🧠 Tech Stack

| Purpose | Tech |
|----------|------|
| Backend | Python, Flask |
| API Integration | Google Places API |
| Frontend | HTML + CSS + JavaScript (templates) |
| Template Engine | Flask Jinja2 |

## 🔧 Requirements

Before you begin, ensure you have the following installed:

- Python 3.7+
- Flask
- (Optional) Virtual environment (recommended)

## 💾 Installation

1. **Clone the repository**

   ```bash
   git clone https://github.com/charmythedev/place_finder.git
   cd place_finder
   
2. **Create and activate a virtual environment** (optional but recommended)
  ```bash
   python3 -m venv venv
   source venv/bin/activate   # macOS/Linux
   venv\Scripts\activate      # Windows
```

3. ***Install Python dependencies***
```

pip install -r requirements.txt
```

4. ***Set your Google Places API key***

Create a .env or export the key directly:
```
export GOOGLE_API_KEY="YOUR_GOOGLE_PLACES_API_KEY"
```

(If you use a .env file, load it in your app with python-dotenv or similar.)


🚀 Running the App
```
export FLASK_APP=main.py
export FLASK_ENV=development  # optional for debug mode
flask run
```

This will start the server locally (e.g., http://127.0.0.1:5000) where you can use the search interface.

Project Structure
```
place_finder/
├── main.py                # Flask app entrypoint
├── templates/             # Jinja2 HTML templates
├── static/                # CSS, JS, images
├── requirements.txt       # Python dependencies
└── README.md              # This file

```


🧪 Example Usage

Navigate to the app in your browser.

Enter a location, keyword, or criteria.

Submit to see results fetched from the Google Places API.

Results may include business names, addresses, ratings, etc.

Note: You must enable the Google Places API in your Google Cloud Console and set appropriate billing/quotas for requests.

📌 Notes

API responses and usage are subject to Google’s API quota and billing policies.

Make sure your API key has the correct permissions (Places API, Maps JavaScript API if needed).

🛠️ Contributing

Contributions are welcome! If you add features, fix bugs, or improve the UI, please open a pull request.

📄 License

MIT
