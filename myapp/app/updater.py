import numpy as np
import pandas as pd
import streamlit as st
import pandas as pd
from pathlib import Path

def updater(upload_file):
    # Get the extension to decide which reader to use
    suffix = Path(upload_file).suffix.lower()
    
    if suffix == '.csv':
        df = pd.read_csv(upload_file) # Pass the URL/Path, not the suffix
    elif suffix == ".xlsx":
        df = pd.read_excel(upload_file)
    elif suffix == ".json":
        df = pd.read_json(upload_file)
    else:
        # Default fallback or error handling
        df = pd.read_csv(upload_file) 
    
    return df

# This will now work correctly

