import matplotlib.pyplot as plt
import pandas as pd
from typing import List, Tuple
import os

class ChartGenerator:
    def __init__(self, output_dir: str = 'charts'):
        """Initialize with output directory for saving charts"""
        self.output_dir = output_dir
        os.makedirs(self.output_dir, exist_ok=True)
    
    def plot_daily_cases(self, df: pd.DataFrame, peaks: List[Tuple[str, int]] = None, 
                        title: str = 'Daily COVID-19 Cases', filename: str = 'daily_cases.png') -> None:
        """
        Plot daily cases with optional moving average and peaks
        
        Args:
            df: DataFrame containing 'date', 'daily_cases', and optionally 'moving_avg'
            peaks: List of (date, value) tuples for peak annotations
            title: Chart title
            filename: Output filename
        """
        plt.figure(figsize=(12, 6))
        
        # Plot daily cases
        plt.plot(df['date'], df['daily_cases'], 
                label='Daily Cases', 
                color='#1f77b4', 
                alpha=0.7)
        
        # Plot moving average if available
        if 'moving_avg' in df.columns:
            plt.plot(df['date'], df['moving_avg'], 
                    label='7-Day Moving Average', 
                    color='#ff7f0e', 
                    linewidth=2)
        
        # Highlight peaks if provided
        if peaks:
            peak_dates = [pd.to_datetime(date) for date, _ in peaks]
            peak_values = [value for _, value in peaks]
            plt.scatter(peak_dates, peak_values, 
                       color='red', 
                       zorder=5, 
                       label='Peak Cases',
                       s=100,
                       edgecolor='black')
        
        # Customize the plot
        plt.title(title, fontsize=14, pad=20)
        plt.xlabel('Date', fontsize=12)
        plt.ylabel('Number of Cases', fontsize=12)
        plt.grid(True, linestyle='--', alpha=0.7)
        plt.legend()
        plt.xticks(rotation=45)
        plt.tight_layout()
        
        # Save the figure
        output_path = os.path.join(self.output_dir, filename)
        plt.savefig(output_path, dpi=300, bbox_inches='tight')
        plt.show()
        return output_path
