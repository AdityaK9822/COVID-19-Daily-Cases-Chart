import pandas as pd
from datetime import datetime
from typing import Tuple, List

def validate_date_range(func):
    """Decorator to validate date range in DataFrame"""
    def wrapper(self, start_date: str = None, end_date: str = None, *args, **kwargs):
        if start_date:
            try:
                datetime.strptime(start_date, '%Y-%m-%d')
            except ValueError:
                raise ValueError("Incorrect date format for start_date, should be YYYY-MM-DD")
        if end_date:
            try:
                datetime.strptime(end_date, '%Y-%m-%d')
            except ValueError:
                raise ValueError("Incorrect date format for end_date, should be YYYY-MM-DD")
        return func(self, start_date, end_date, *args, **kwargs)
    return wrapper

class CovidData:
    def __init__(self, filepath: str):
        """Initialize with path to the CSV file"""
        self.filepath = filepath
        self.df = self._load_and_clean_data()
    
    def _load_and_clean_data(self) -> pd.DataFrame:
        """Load and clean the data"""
        df = pd.read_csv(self.filepath, parse_dates=['date'])
        # Forward fill missing values
        df['daily_cases'] = df['daily_cases'].fillna(method='ffill')
        return df
    
    @validate_date_range
    def filter_by_date_range(self, start_date: str = None, end_date: str = None) -> None:
        """Filter data by date range"""
        if start_date:
            self.df = self.df[self.df['date'] >= start_date]
        if end_date:
            self.df = self.df[self.df['date'] <= end_date]
    
    def compute_moving_average(self, window: int = 7) -> None:
        """Compute moving average with the given window size"""
        self.df['moving_avg'] = self.df['daily_cases'].rolling(window=window, min_periods=1).mean()
    
    def detect_peaks(self, threshold: float = 1.5) -> List[Tuple[str, int]]:
        """Detect peaks in the data"""
        # Calculate z-scores to find significant peaks
        mean = self.df['daily_cases'].mean()
        std = self.df['daily_cases'].std()
        self.df['is_peak'] = self.df['daily_cases'] > (mean + threshold * std)
        
        # Return list of (date, cases) for peaks
        peaks = self.df[self.df['is_peak']][['date', 'daily_cases']].values.tolist()
        return [(str(date), int(cases)) for date, cases in peaks]
    
    def get_data(self) -> pd.DataFrame:
        """Return the processed data"""
        return self.df
