# Laptop Price Analyzer

A complete ML mini-project aligned to the required ML report format, implemented in four Jupyter notebooks with up to 12 combined plots.

## Dataset
We use the dataset already present in this repo:
- Raw: `/workspace/data/raw/laptop_data.csv`
- Processed (optional reference): `/workspace/data/processed/cleaned_laptops.csv`

## Structure
- `notebooks/`
  - `01_Cover_Intro_Data_Description.ipynb`
  - `02_Data_Analysis.ipynb`
  - `03_Modelling.ipynb`
  - `04_Validation_Conclusion.ipynb`
- `outputs/` figures and artifacts written by notebooks

## How to run
1. Create and activate a virtual environment (recommended)
   - Linux/macOS: `python3 -m venv .venv && source .venv/bin/activate`
   - Windows (PowerShell): `python -m venv .venv; .venv\\Scripts\\Activate.ps1`
2. Install dependencies: `pip install -r requirements.txt`
3. Launch Jupyter: `jupyter lab` (or `jupyter notebook`)
4. Open notebooks in the `notebooks/` folder in order (01 → 04).

## Notes
- The notebooks never modify existing repo files in `data/`. All outputs are saved under `laptop-price-analyzer/outputs/`.
- Fill in your Cover Page details (name, enrollment, roll, batch) inside `01_Cover_Intro_Data_Description.ipynb`.