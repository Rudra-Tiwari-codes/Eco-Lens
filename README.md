# EcoLens - AI-powered Sustainability Lifecycle Tracker

## 🌱 Overview

EcoLens is an AI-powered web application that reveals the hidden environmental impact of everyday items. By simply entering an item name, users get a comprehensive lifecycle analysis including sustainability scores, environmental metrics, and engaging story-like narratives.

## ✨ Features

- **AI-Powered Analysis**: Uses ChatGPT to analyze environmental impact
- **5 Environmental Metrics**: CO₂ Footprint, Water Usage, Landfill Time, Recyclability, Environmental Impact
- **Real-time Weekly Tracking**: Monitor your sustainability impact over time
- **Elegant Story Formatting**: Beautifully formatted lifecycle stories with highlighted metrics
- **Harsh Scoring System**: Realistic environmental impact scoring (0-10 scale)
- **Mobile Responsive**: Works perfectly on all devices

## 🚀 Quick Start

### Prerequisites
- Python 3.11+
- OpenAI API Key

### Installation

1. **Clone and navigate to the EcoLens directory:**
   ```bash
   cd EcoLens
   ```

2. **Create a virtual environment:**
   ```bash
   python -m venv .venv
   ```

3. **Activate the virtual environment:**
   - Windows: `.venv\Scripts\activate`
   - macOS/Linux: `source .venv/bin/activate`

4. **Install dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

5. **Set up your OpenAI API key:**
   - Edit `src/ecolens/main.py`
   - Replace the API key in the `get_openai_client()` function

6. **Run the application:**
   ```bash
   python run.py
   ```

7. **Open your browser:**
   Navigate to `http://127.0.0.1:8000`

## 📁 Project Structure

```
EcoLens/
├── src/
│   └── ecolens/
│       ├── __init__.py
│       ├── main.py              # FastAPI server
│       └── static/
│           └── index.html       # Web interface
├── requirements.txt             # Python dependencies
├── pyproject.toml              # Project configuration
├── run.py                      # Application entry point
└── README.md                   # This file
```

## 🎯 Usage

1. **Enter an item name** in the search box (e.g., "water", "plastic bottle", "banana")
2. **Click "Discover Story"** to analyze the item
3. **View the results**:
   - Sustainability score (1-10)
   - Environmental impact score (1-10)
   - Detailed metrics (CO₂, Water, Landfill, Recyclability)
   - Complete lifecycle story
4. **Track your weekly impact** in the sidebar
5. **Review your history** of analyzed items

## 🔧 Configuration

### API Key Setup
Edit `src/ecolens/main.py` and update the OpenAI API key:
```python
def get_openai_client():
    """Initialize OpenAI client with API key."""
    api_key = "your-openai-api-key-here"
    return AsyncOpenAI(api_key=api_key)
```

### Customization
- **Scoring System**: Modify the scoring functions in `main.py`
- **UI Styling**: Edit `static/index.html` CSS
- **AI Prompts**: Customize the analysis prompt in `main.py`

## 📊 Environmental Metrics

### Sustainability Score (1-10)
- **10**: Excellent (organic produce, water)
- **9**: Very Good (sustainable materials)
- **8**: Good (eco-friendly products)
- **7**: Above Average
- **6**: Average
- **5**: Below Average
- **4**: Poor
- **3**: Very Poor
- **2**: Terrible
- **1**: Extremely Harmful (plastics, toxic materials)

### Environmental Impact Score (1-10)
Similar scale but focused on overall environmental friendliness.

## 🛠️ Development

### Running in Development Mode
```bash
python run.py
```

### Project Structure
- **`main.py`**: FastAPI server with AI integration
- **`static/index.html`**: Complete web interface (HTML, CSS, JavaScript)
- **`run.py`**: Application entry point

### Key Functions
- `get_product_analysis()`: AI-powered item analysis
- `calculate_sustainability_score()`: Environmental scoring
- `calculate_environmental_impact_score()`: Impact assessment
- `extract_metrics_from_story()`: Metric extraction from AI response

## 🌟 Features in Detail

### AI Analysis
- Uses GPT-4o-mini for comprehensive environmental analysis
- Generates engaging, story-like narratives
- Extracts specific environmental metrics
- Provides fallback data for reliability

### Real-time Updates
- Weekly impact tracking updates immediately
- Visual animations for data changes
- Automatic history management
- Local storage for persistence

### Responsive Design
- Mobile-first approach
- Beautiful gradients and animations
- Professional UI/UX
- Accessibility considerations

## 🤝 Contributing

1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Test thoroughly
5. Submit a pull request

## 📄 License

This project is licensed under the MIT License.

## 🙏 Acknowledgments

- OpenAI for providing the AI capabilities
- FastAPI for the robust web framework
- The sustainability research community for environmental data

---

**EcoLens** - Making environmental impact visible, one item at a time. 🌍
