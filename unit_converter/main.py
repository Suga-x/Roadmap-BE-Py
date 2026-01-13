from fastapi import FastAPI, Request, Form
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from typing import Optional

app = FastAPI(title="Unit Converter")

# Mount static files and templates
app.mount("/static", StaticFiles(directory="static"), name="static")
templates = Jinja2Templates(directory="templates")

# Conversion functions
class UnitConverter:
    @staticmethod
    def convert_length(value: float, from_unit: str, to_unit: str) -> float:
        """Convert length units"""
        # Convert to meters first
        to_meter = {
            'millimeter': value / 1000,
            'centimeter': value / 100,
            'meter': value,
            'kilometer': value * 1000,
            'inch': value * 0.0254,
            'foot': value * 0.3048,
            'yard': value * 0.9144,
            'mile': value * 1609.34
        }
        
        meters = to_meter.get(from_unit, value)
        
        # Convert from meters to target unit
        from_meter = {
            'millimeter': meters * 1000,
            'centimeter': meters * 100,
            'meter': meters,
            'kilometer': meters / 1000,
            'inch': meters / 0.0254,
            'foot': meters / 0.3048,
            'yard': meters / 0.9144,
            'mile': meters / 1609.34
        }
        
        return from_meter.get(to_unit, value)
    
    @staticmethod
    def convert_weight(value: float, from_unit: str, to_unit: str) -> float:
        """Convert weight units"""
        # Convert to kilograms first
        to_kilogram = {
            'milligram': value / 1000000,
            'gram': value / 1000,
            'kilogram': value,
            'ounce': value * 0.0283495,
            'pound': value * 0.453592
        }
        
        kilograms = to_kilogram.get(from_unit, value)
        
        # Convert from kilograms to target unit
        from_kilogram = {
            'milligram': kilograms * 1000000,
            'gram': kilograms * 1000,
            'kilogram': kilograms,
            'ounce': kilograms / 0.0283495,
            'pound': kilograms / 0.453592
        }
        
        return from_kilogram.get(to_unit, value)
    
    @staticmethod
    def convert_temperature(value: float, from_unit: str, to_unit: str) -> float:
        """Convert temperature units"""
        if from_unit == to_unit:
            return value
            
        # Convert to Celsius first
        if from_unit == 'celsius':
            celsius = value
        elif from_unit == 'fahrenheit':
            celsius = (value - 32) * 5/9
        elif from_unit == 'kelvin':
            celsius = value - 273.15
        
        # Convert from Celsius to target unit
        if to_unit == 'celsius':
            return celsius
        elif to_unit == 'fahrenheit':
            return (celsius * 9/5) + 32
        elif to_unit == 'kelvin':
            return celsius + 273.15
        
        return value

converter = UnitConverter()

# Routes
@app.get("/", response_class=HTMLResponse)
async def home(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})

@app.get("/length", response_class=HTMLResponse)
async def length_converter(request: Request):
    return templates.TemplateResponse("length.html", {
        "request": request,
        "result": None,
        "from_value": "",
        "from_unit": "meter",
        "to_unit": "kilometer"
    })

@app.post("/length", response_class=HTMLResponse)
async def convert_length(
    request: Request,
    from_value: float = Form(...),
    from_unit: str = Form(...),
    to_unit: str = Form(...)
):
    try:
        result = converter.convert_length(from_value, from_unit, to_unit)
        return templates.TemplateResponse("length.html", {
            "request": request,
            "result": round(result, 6),
            "from_value": from_value,
            "from_unit": from_unit,
            "to_unit": to_unit
        })
    except Exception as e:
        return templates.TemplateResponse("length.html", {
            "request": request,
            "result": f"Error: {str(e)}",
            "from_value": from_value,
            "from_unit": from_unit,
            "to_unit": to_unit
        })

@app.get("/weight", response_class=HTMLResponse)
async def weight_converter(request: Request):
    return templates.TemplateResponse("weight.html", {
        "request": request,
        "result": None,
        "from_value": "",
        "from_unit": "kilogram",
        "to_unit": "gram"
    })

@app.post("/weight", response_class=HTMLResponse)
async def convert_weight(
    request: Request,
    from_value: float = Form(...),
    from_unit: str = Form(...),
    to_unit: str = Form(...)
):
    try:
        result = converter.convert_weight(from_value, from_unit, to_unit)
        return templates.TemplateResponse("weight.html", {
            "request": request,
            "result": round(result, 6),
            "from_value": from_value,
            "from_unit": from_unit,
            "to_unit": to_unit
        })
    except Exception as e:
        return templates.TemplateResponse("weight.html", {
            "request": request,
            "result": f"Error: {str(e)}",
            "from_value": from_value,
            "from_unit": from_unit,
            "to_unit": to_unit
        })

@app.get("/temperature", response_class=HTMLResponse)
async def temperature_converter(request: Request):
    return templates.TemplateResponse("temperature.html", {
        "request": request,
        "result": None,
        "from_value": "",
        "from_unit": "celsius",
        "to_unit": "fahrenheit"
    })

@app.post("/temperature", response_class=HTMLResponse)
async def convert_temperature(
    request: Request,
    from_value: float = Form(...),
    from_unit: str = Form(...),
    to_unit: str = Form(...)
):
    try:
        result = converter.convert_temperature(from_value, from_unit, to_unit)
        return templates.TemplateResponse("temperature.html", {
            "request": request,
            "result": round(result, 6),
            "from_value": from_value,
            "from_unit": from_unit,
            "to_unit": to_unit
        })
    except Exception as e:
        return templates.TemplateResponse("temperature.html", {
            "request": request,
            "result": f"Error: {str(e)}",
            "from_value": from_value,
            "from_unit": from_unit,
            "to_unit": to_unit
        })

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)