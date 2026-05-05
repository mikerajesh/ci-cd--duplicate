import sys
import os
import pytest

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__),'../src')))
from main import load_and_process_data

def test_no_duplicates():
    # These two lines MUST be indented (4 spaces)
    df = load_and_process_data("data/dataset.csv","data/test_processed_dataset.csv")
    assert df.duplicated().sum() == 0, "Duplicate rows were not fully removed"
