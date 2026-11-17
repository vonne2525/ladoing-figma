import os
from flask import Flask, jsonify, render_template
from dotenv import load_dotenv

# Load environment variables from a .env file if present
load_dotenv()

app = Flask(__name__)

# Configuration
FIGMA_ACCESS_TOKEN = os.getenv("FIGMA_ACCESS_TOKEN")

@app.route("/")
def home():
    """Render a simple home page or status check."""
    return jsonify({
        "status": "success",
        "message": "Welcome to your Codespace Python App!",
        "figma_connected": bool(FIGMA_ACCESS_TOKEN)
    })

@app.route("/api/health")
def health_check():
    """Health check endpoint for the app."""
    return {"status": "healthy"}

if __name__ == "__main__":
    # Run the app on port 5000, accessible externally in Codespaces
    app.run(host="0.0.0.0", port=5000, debug=True)
