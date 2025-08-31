#!/usr/bin/env python3
"""FastAPI server for EcoLens - AI-powered Sustainability Lifecycle Tracker."""

import os
import json
import re
from typing import Dict, Any, Optional
from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from fastapi.staticfiles import StaticFiles
from fastapi.responses import FileResponse
from pydantic import BaseModel
from openai import AsyncOpenAI

app = FastAPI(
    title="EcoLens API",
    description="AI-powered Sustainability Lifecycle Tracker API",
    version="1.0.0"
)

# Configure CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Mount static files
import os
static_dir = os.path.join(os.path.dirname(__file__), "static")
app.mount("/static", StaticFiles(directory=static_dir), name="static")

# Initialize OpenAI client
def get_openai_client():
    """Initialize OpenAI client with API key."""
    api_key = "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"
    return AsyncOpenAI(api_key=api_key)

class ItemAnalysisRequest(BaseModel):
    item_name: str

class ItemAnalysisResponse(BaseModel):
    success: bool
    message: str
    data: Dict[str, Any]

def extract_metrics_from_story(story_text: str) -> Dict[str, Any]:
    """Extract environmental metrics from the AI-generated story."""
    metrics = {
        "carbon_footprint_kg": 5.0,
        "water_usage_liters": 500.0,
        "landfill_years": 50.0,
        "recyclability": 50.0
    }
    
    # Extract carbon footprint
    carbon_match = re.search(r'(\d+(?:\.\d+)?)\s*kg\s*CO2', story_text, re.IGNORECASE)
    if carbon_match:
        metrics["carbon_footprint_kg"] = float(carbon_match.group(1))
    
    # Extract water usage
    water_match = re.search(r'(\d+(?:,\d+)?)\s*liters?\s*water', story_text, re.IGNORECASE)
    if water_match:
        water_str = water_match.group(1).replace(',', '')
        metrics["water_usage_liters"] = float(water_str)
    
    # Extract landfill time
    landfill_match = re.search(r'(\d+(?:\.\d+)?)\s*years?\s*landfill', story_text, re.IGNORECASE)
    if landfill_match:
        metrics["landfill_years"] = float(landfill_match.group(1))
    
    # Extract recyclability
    recycle_match = re.search(r'(\d+(?:\.\d+)?)%\s*recyclable', story_text, re.IGNORECASE)
    if recycle_match:
        metrics["recyclability"] = float(recycle_match.group(1))
    
    return metrics

def calculate_sustainability_score(carbon_footprint: float, water_usage: float, landfill_years: float, recyclability: float) -> int:
    """Calculate sustainability score (1-10) based on environmental metrics - REALISTIC & BALANCED SCORING."""
    
    # Carbon footprint scoring (lower is better) - REALISTIC RANGES
    # Based on real-world data: organic produce (0.1-0.5), processed foods (0.5-2), electronics (10-50+)
    if carbon_footprint <= 0.1:
        carbon_score = 10  # Excellent: organic local produce
    elif carbon_footprint <= 0.3:
        carbon_score = 9   # Very good: most fruits/vegetables
    elif carbon_footprint <= 0.8:
        carbon_score = 8   # Good: grains, legumes
    elif carbon_footprint <= 2.0:
        carbon_score = 7   # Above average: dairy, eggs
    elif carbon_footprint <= 5.0:
        carbon_score = 6   # Average: meat, processed foods
    elif carbon_footprint <= 10.0:
        carbon_score = 5   # Below average: electronics, plastics
    elif carbon_footprint <= 20.0:
        carbon_score = 4   # Poor: heavy manufacturing
    elif carbon_footprint <= 50.0:
        carbon_score = 3   # Very poor: luxury items, cars
    else:
        carbon_score = 2   # Extremely poor: high-impact items
    
    # Water usage scoring (lower is better) - REALISTIC RANGES
    # Based on real data: fruits (50-200L), vegetables (100-500L), meat (1000-5000L)
    if water_usage <= 50:
        water_score = 10   # Excellent: low-water crops
    elif water_usage <= 150:
        water_score = 9    # Very good: most fruits
    elif water_usage <= 300:
        water_score = 8    # Good: vegetables, grains
    elif water_usage <= 600:
        water_score = 7    # Above average: dairy
    elif water_usage <= 1200:
        water_score = 6    # Average: eggs, some meats
    elif water_usage <= 3000:
        water_score = 5    # Below average: beef, cotton
    elif water_usage <= 8000:
        water_score = 4    # Poor: high-water manufacturing
    else:
        water_score = 3    # Very poor: extremely water-intensive
    
    # Landfill time scoring (lower is better) - REALISTIC RANGES
    # Organic waste (weeks-months), paper (months-years), plastic (decades-centuries)
    if landfill_years <= 0.1:
        landfill_score = 10  # Excellent: compostable, weeks
    elif landfill_years <= 0.5:
        landfill_score = 9   # Very good: paper, cardboard
    elif landfill_years <= 2:
        landfill_score = 8   # Good: wood, natural fibers
    elif landfill_years <= 10:
        landfill_score = 7   # Above average: some plastics
    elif landfill_years <= 50:
        landfill_score = 6   # Average: most plastics
    elif landfill_years <= 200:
        landfill_score = 5   # Below average: styrofoam, some plastics
    elif landfill_years <= 500:
        landfill_score = 4   # Poor: long-lasting plastics
    else:
        landfill_score = 3   # Very poor: centuries to decompose
    
    # Recyclability scoring (higher is better) - REALISTIC RANGES
    # Glass/metal (90-95%), paper (70-80%), plastics (varies widely)
    if recyclability >= 90:
        recycle_score = 10  # Excellent: glass, aluminum
    elif recyclability >= 80:
        recycle_score = 9   # Very good: paper, cardboard
    elif recyclability >= 70:
        recycle_score = 8   # Good: steel, some plastics
    elif recyclability >= 60:
        recycle_score = 7   # Above average: PET plastics
    elif recyclability >= 50:
        recycle_score = 6   # Average: mixed plastics
    elif recyclability >= 40:
        recycle_score = 5   # Below average: some plastics
    elif recyclability >= 30:
        recycle_score = 4   # Poor: hard-to-recycle plastics
    elif recyclability >= 20:
        recycle_score = 3   # Very poor: composite materials
    else:
        recycle_score = 2   # Extremely poor: non-recyclable
    
    # Calculate weighted average with balanced weighting
    weighted_score = (
        carbon_score * 0.35 +    # Carbon footprint is most important
        water_score * 0.25 +     # Water usage is significant
        landfill_score * 0.25 +  # Waste impact matters
        recycle_score * 0.15     # Recyclability is a bonus
    )
    
    # Apply realistic bonuses for truly sustainable items
    if carbon_footprint <= 0.3 and water_usage <= 200 and landfill_years <= 1:
        weighted_score += 0.5  # Bonus for excellent overall sustainability
    
    # Apply realistic penalties for extremely harmful items
    if carbon_footprint > 50 or water_usage > 10000 or landfill_years > 1000:
        weighted_score *= 0.8  # 20% penalty for extremely bad items
    
    return max(1, min(10, round(weighted_score)))

def calculate_environmental_impact_score(carbon_footprint: float, water_usage: float, landfill_years: float, recyclability: float) -> int:
    """Calculate environmental impact score (1-10) - REALISTIC scale where 10 = very good for environment, 1 = very bad."""
    
    # Realistic environmental impact calculation
    # Based on real-world sustainability data and consumer expectations
    
    # Base score starts at 5 (neutral)
    base_score = 5.0
    
    # Carbon impact (heavily weighted) - REALISTIC RANGES
    if carbon_footprint <= 0.1:
        carbon_impact = 2.5  # Excellent: organic produce
    elif carbon_footprint <= 0.3:
        carbon_impact = 2.0  # Very good: fruits/vegetables
    elif carbon_footprint <= 0.8:
        carbon_impact = 1.5  # Good: grains, legumes
    elif carbon_footprint <= 2.0:
        carbon_impact = 1.0  # Above average: dairy, eggs
    elif carbon_footprint <= 5.0:
        carbon_impact = 0.0  # Average: meat, processed foods
    elif carbon_footprint <= 10.0:
        carbon_impact = -1.0 # Below average: electronics, plastics
    elif carbon_footprint <= 20.0:
        carbon_impact = -2.0 # Poor: heavy manufacturing
    elif carbon_footprint <= 50.0:
        carbon_impact = -3.0 # Very poor: luxury items
    else:
        carbon_impact = -4.0 # Extremely poor: high-impact items
    
    # Water impact - REALISTIC RANGES
    if water_usage <= 50:
        water_impact = 1.5   # Excellent: low-water crops
    elif water_usage <= 150:
        water_impact = 1.0   # Very good: most fruits
    elif water_usage <= 300:
        water_impact = 0.5   # Good: vegetables, grains
    elif water_usage <= 600:
        water_impact = 0.0   # Above average: dairy
    elif water_usage <= 1200:
        water_impact = -0.5  # Average: eggs, some meats
    elif water_usage <= 3000:
        water_impact = -1.0  # Below average: beef, cotton
    elif water_usage <= 8000:
        water_impact = -1.5  # Poor: high-water manufacturing
    else:
        water_impact = -2.0  # Very poor: extremely water-intensive
    
    # Landfill impact - REALISTIC RANGES
    if landfill_years <= 0.1:
        landfill_impact = 1.0  # Excellent: compostable
    elif landfill_years <= 0.5:
        landfill_impact = 0.5  # Very good: paper, cardboard
    elif landfill_years <= 2:
        landfill_impact = 0.0  # Good: wood, natural fibers
    elif landfill_years <= 10:
        landfill_impact = -0.5 # Above average: some plastics
    elif landfill_years <= 50:
        landfill_impact = -1.0 # Average: most plastics
    elif landfill_years <= 200:
        landfill_impact = -1.5 # Below average: styrofoam
    elif landfill_years <= 500:
        landfill_impact = -2.0 # Poor: long-lasting plastics
    else:
        landfill_impact = -2.5 # Very poor: centuries to decompose
    
    # Recyclability impact - REALISTIC RANGES
    if recyclability >= 90:
        recycle_impact = 1.0  # Excellent: glass, aluminum
    elif recyclability >= 80:
        recycle_impact = 0.8  # Very good: paper, cardboard
    elif recyclability >= 70:
        recycle_impact = 0.5  # Good: steel, some plastics
    elif recyclability >= 60:
        recycle_impact = 0.2  # Above average: PET plastics
    elif recyclability >= 50:
        recycle_impact = 0.0  # Average: mixed plastics
    elif recyclability >= 40:
        recycle_impact = -0.2 # Below average: some plastics
    elif recyclability >= 30:
        recycle_impact = -0.5 # Poor: hard-to-recycle plastics
    elif recyclability >= 20:
        recycle_impact = -0.8 # Very poor: composite materials
    else:
        recycle_impact = -1.0 # Extremely poor: non-recyclable
    
    # Calculate total impact with balanced weighting
    total_impact = base_score + (carbon_impact * 0.4) + (water_impact * 0.25) + (landfill_impact * 0.25) + (recycle_impact * 0.1)
    
    # Apply realistic scaling for meaningful differences
    if total_impact >= 8.5:
        return 10  # Excellent for environment
    elif total_impact >= 7.5:
        return 9   # Very good
    elif total_impact >= 6.5:
        return 8   # Good
    elif total_impact >= 5.5:
        return 7   # Above average
    elif total_impact >= 4.5:
        return 6   # Average
    elif total_impact >= 3.5:
        return 5   # Below average
    elif total_impact >= 2.5:
        return 4   # Poor
    elif total_impact >= 1.5:
        return 3   # Very poor
    elif total_impact >= 0.5:
        return 2   # Terrible
    else:
        return 1   # Extremely harmful

async def get_product_analysis(product_name: str) -> Dict[str, Any]:
    """Get product analysis using ChatGPT API."""
    
    prompt = f"""You are an expert environmental scientist with deep knowledge of lifecycle assessment. Analyze the environmental impact of "{product_name}".

Write a comprehensive lifecycle story that includes:

1. Raw Materials: Describe where the materials come from and their environmental extraction impact
2. Production: Detail the manufacturing process and energy/water requirements
3. Transportation: Explain the supply chain and distribution environmental costs
4. Usage: Describe how people use it and any ongoing environmental impact
5. Disposal: Detail what happens when it's thrown away and waste management

IMPORTANT: Use REALISTIC, RESEARCH-BASED metrics. Here are typical ranges:
- Organic produce: 0.1-0.5 kg CO2, 50-300L water, 0.1-1 year landfill, 90-95% recyclable
- Processed foods: 0.5-2 kg CO2, 300-1000L water, 1-10 years landfill, 70-90% recyclable
- Plastics: 2-10 kg CO2, 500-2000L water, 50-500 years landfill, 20-60% recyclable
- Electronics: 10-50 kg CO2, 1000-5000L water, 100-1000 years landfill, 30-70% recyclable

Format your story with clear paragraphs separated by double line breaks. Make it engaging and educational. Focus on the hidden environmental impacts that most people don't see.

Return ONLY a JSON response with:
{{
    "story": "Your complete lifecycle story here with proper paragraph breaks",
    "carbon_footprint_kg": <realistic_number>,
    "water_usage_liters": <realistic_number>,
    "landfill_years": <realistic_number>,
    "recyclability_percent": <realistic_number>
}}"""

    try:
        client = get_openai_client()
        response = await client.chat.completions.create(
            model="gpt-4o-mini",
            messages=[{"role": "user", "content": prompt}],
            temperature=0.7,
            max_tokens=2000,
            timeout=30.0
        )
        
        result_text = response.choices[0].message.content
        
        # Parse JSON response
        json_match = re.search(r'\{.*\}', result_text, re.DOTALL)
        if json_match:
            result = json.loads(json_match.group())
        else:
            raise Exception("Invalid JSON response")
        
        # Extract metrics from story as backup
        story = result.get("story", "")
        extracted_metrics = extract_metrics_from_story(story)
        
        # Use provided metrics or extracted ones
        carbon_footprint = result.get("carbon_footprint_kg", extracted_metrics["carbon_footprint_kg"])
        water_usage = result.get("water_usage_liters", extracted_metrics["water_usage_liters"])
        landfill_years = result.get("landfill_years", extracted_metrics["landfill_years"])
        recyclability = result.get("recyclability_percent", extracted_metrics["recyclability"])
        
        # Calculate sustainability score
        sustainability_score = calculate_sustainability_score(
            carbon_footprint, water_usage, landfill_years, recyclability
        )
        
        # Calculate environmental impact score
        environmental_impact_score = calculate_environmental_impact_score(
            carbon_footprint, water_usage, landfill_years, recyclability
        )
        
        return {
            "item_name": product_name,
            "sustainability_score": sustainability_score,
            "environmental_impact_score": environmental_impact_score,
            "carbon_footprint_kg": carbon_footprint,
            "water_usage_liters": water_usage,
            "landfill_years": landfill_years,
            "recyclability": recyclability,
            "story": story
        }
        
    except Exception as e:
        print(f"Error analyzing {product_name}: {e}")
        # Return fallback data
        return {
            "item_name": product_name,
            "sustainability_score": 5,
            "environmental_impact_score": 5,
            "carbon_footprint_kg": 5.0,
            "water_usage_liters": 500.0,
            "landfill_years": 50.0,
            "recyclability": 50.0,
            "story": f"Analysis of {product_name} based on general environmental impact data."
        }

@app.get("/")
async def root():
    """Serve the main HTML interface."""
    static_file = os.path.join(os.path.dirname(__file__), "static", "index.html")
    return FileResponse(static_file)

@app.get("/api")
async def api_root():
    """API root endpoint."""
    return {
        "message": "🌱 EcoLens API - AI-powered Sustainability Lifecycle Tracker",
        "version": "1.0.0",
        "status": "running"
    }

@app.post("/api/analyze-item", response_model=ItemAnalysisResponse)
async def analyze_item(request: ItemAnalysisRequest):
    """Analyze an item and generate its sustainability lifecycle story."""
    try:
        print(f"Analyzing item: {request.item_name}")
        
        # Get AI analysis
        product_data = await get_product_analysis(request.item_name)
        
        response_data = {
            "item_name": product_data["item_name"],
            "sustainability_score": product_data["sustainability_score"],
            "environmental_impact_score": product_data["environmental_impact_score"],
            "carbon_footprint_kg": product_data["carbon_footprint_kg"],
            "water_usage_liters": product_data["water_usage_liters"],
            "landfill_years": product_data["landfill_years"],
            "recyclability": product_data["recyclability"],
            "story": product_data["story"]
        }
        
        print(f"Analysis complete for {request.item_name}")
        return ItemAnalysisResponse(
            success=True,
            message="Item analyzed successfully",
            data=response_data
        )
        
    except Exception as e:
        print(f"Error analyzing item {request.item_name}: {str(e)}")
        raise HTTPException(status_code=500, detail=f"Analysis failed: {str(e)}")

if __name__ == "__main__":
    import uvicorn
    print("Starting EcoLens API Server...")
    print("Web interface: http://127.0.0.1:8000")
    uvicorn.run(app, host="127.0.0.1", port=8000)

