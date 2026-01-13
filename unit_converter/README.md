# Unit Converter Web Application

A simple and intuitive web application for converting between different units of measurement built with Python FastAPI.

## Features

- **Length Conversion**: Millimeter, Centimeter, Meter, Kilometer, Inch, Foot, Yard, Mile
- **Weight Conversion**: Milligram, Gram, Kilogram, Ounce, Pound
- **Temperature Conversion**: Celsius, Fahrenheit, Kelvin
- **User-Friendly Interface**: Clean, responsive design with clear navigation
- **Quick Conversion References**: Useful conversion facts on each page
- **Real-time Results**: Instant conversion without page reloads

## Technology Stack

- **Backend**: Python FastAPI
- **Frontend**: HTML5, CSS3, JavaScript (vanilla)
- **Templating**: Jinja2
- **Styling**: Custom CSS with Font Awesome icons

## Installation

### Prerequisites
- Python 3.8 or higher
- pip (Python package manager)

### Step-by-Step Installation

1. **Clone or download the project files**

2. **Create and activate a virtual environment (optional but recommended):**

   ```bash
   # On Windows
   python -m venv venv
   venv\Scripts\activate

   # On macOS/Linux
   python3 -m venv venv
   source venv/bin/activate
   ```

3. **Install required dependencies:**

   ```bash
   pip install -r requirements.txt
   ```

4. **Project Structure:**

   ```
   unit-converter/
   ├── main.py              # FastAPI application
   ├── requirements.txt     # Python dependencies
   ├── templates/          # HTML templates
   │   ├── base.html
   │   ├── index.html
   │   ├── length.html
   │   ├── weight.html
   │   └── temperature.html
   └── static/            # CSS and static files
       └── style.css
   ```

## Running the Application

### Development Server

1. **Start the FastAPI server:**

   ```bash
   python main.py
   ```

   Or using uvicorn directly:
   ```bash
   uvicorn main:app --reload
   ```

2. **Open your browser and navigate to:**

   ```
   http://localhost:8000
   ```

### Production Deployment

For production deployment, consider using:

```bash
# Using gunicorn with uvicorn workers
gunicorn -w 4 -k uvicorn.workers.UvicornWorker main:app

# Or using uvicorn with multiple workers
uvicorn main:app --host 0.0.0.0 --port 8000 --workers 4
```

## Usage Guide

### 1. Home Page
- Navigate between different conversion types using the top menu
- Each conversion type has a dedicated card with a quick access button

### 2. Length Conversion
- Accessible via `/length` or the "Length" menu item
- Convert between: millimeter, centimeter, meter, kilometer, inch, foot, yard, mile
- Enter value, select "from" and "to" units, click "Convert"

### 3. Weight Conversion
- Accessible via `/weight` or the "Weight" menu item
- Convert between: milligram, gram, kilogram, ounce, pound

### 4. Temperature Conversion
- Accessible via `/temperature` or the "Temperature" menu item
- Convert between: Celsius (°C), Fahrenheit (°F), Kelvin (K)

## API Endpoints

| Endpoint | Method | Description |
|----------|--------|-------------|
| `/` | GET | Home page with all conversion options |
| `/length` | GET | Length converter form |
| `/length` | POST | Perform length conversion |
| `/weight` | GET | Weight converter form |
| `/weight` | POST | Perform weight conversion |
| `/temperature` | GET | Temperature converter form |
| `/temperature` | POST | Perform temperature conversion |

## Conversion Formulas

### Length Conversions
- Base unit: Meter
- All conversions go through meters as intermediate unit

### Weight Conversions
- Base unit: Kilogram
- All conversions go through kilograms as intermediate unit

### Temperature Conversions
- Special formulas for each temperature scale:
  - Celsius to Fahrenheit: `(°C × 9/5) + 32`
  - Fahrenheit to Celsius: `(°F - 32) × 5/9`
  - Celsius to Kelvin: `°C + 273.15`

## Development

### Adding New Conversion Types

To add a new conversion type (e.g., Volume):

1. Add conversion functions in `main.py`:
   ```python
   @staticmethod
   def convert_volume(value: float, from_unit: str, to_unit: str) -> float:
       # Implementation
   ```

2. Create new routes:
   ```python
   @app.get("/volume")
   @app.post("/volume")
   ```

3. Create HTML template in `templates/volume.html`
4. Update navigation in `templates/base.html`

### Testing

Run the application and test all conversion types:
1. Test basic conversions
2. Test edge cases (negative values, zero)
3. Test unit preservation (converting to same unit)
4. Verify responsive design on different screen sizes

## Troubleshooting

### Common Issues

1. **"Module not found" error:**
   ```bash
   pip install -r requirements.txt
   ```

2. **Port already in use:**
   ```bash
   # Kill process on port 8000 (Windows)
   netstat -ano | findstr :8000
   taskkill /PID [PID] /F

   # Kill process on port 8000 (macOS/Linux)
   lsof -ti:8000 | xargs kill
   ```

3. **CSS not loading:**
   - Check if static files are properly mounted
   - Clear browser cache
   - Check browser console for errors

4. **Form not submitting:**
   - Ensure all required fields are filled
   - Check browser console for JavaScript errors

### Debug Mode

Run with debug mode enabled:
```bash
uvicorn main:app --reload --log-level debug
```

## Dependencies

List of main dependencies (see `requirements.txt` for complete list):

- `fastapi==0.104.1`: Web framework
- `uvicorn==0.24.0`: ASGI server
- `jinja2==3.1.2`: Templating engine
- `python-multipart==0.0.6`: Form handling

## Browser Compatibility

- Chrome 60+
- Firefox 55+
- Safari 12+
- Edge 79+
- Opera 47+

## Contributing

1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Test thoroughly
5. Submit a pull request

## License

This project is open source and available under the MIT License.

## Support

For issues, questions, or suggestions:
1. Check the Troubleshooting section
2. Review the code documentation
3. Submit an issue in the repository

## Screenshots

*(Add screenshots of your application here)*

1. Home Page
2. Length Converter
3. Weight Converter
4. Temperature Converter

---

**Enjoy converting!** 📏⚖️🌡️