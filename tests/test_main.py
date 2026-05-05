import pytest
from src.main import load_and_process_data

def test_duplicate_removal():
    # Fixed indentation and the broken string literal
    df = load_and_process_data("data/dataset.csv", "data/processed_dataset.csv")
    assert df.duplicated().sum() == 0, "Duplicate rows were not fully removed"
