import os
import argparse
from datetime import datetime

from covid_data_class import CovidData
from chart_generator import ChartGenerator

def parse_arguments():
    """Parse command line arguments"""
    parser = argparse.ArgumentParser(description='Generate COVID-19 case charts')
    parser.add_argument('--input', type=str, default='covid_cases.csv',
                       help='Path to input CSV file (default: covid_cases.csv)')
    parser.add_argument('--start-date', type=str, default=None,
                       help='Start date in YYYY-MM-DD format (inclusive)')
    parser.add_argument('--end-date', type=str, default=None,
                       help='End date in YYYY-MM-DD format (inclusive)')
    parser.add_argument('--output-dir', type=str, default='charts',
                       help='Output directory for charts (default: charts/)')
    return parser.parse_args()

def main():
    # Parse command line arguments
    args = parse_arguments()
    
    # Initialize data processor and chart generator
    try:
        print(f"Loading data from {args.input}...")
        covid_data = CovidData(args.input)
        chart_gen = ChartGenerator(output_dir=args.output_dir)
        
        # Apply date filters if provided
        if args.start_date or args.end_date:
            print(f"Filtering data from {args.start_date or 'start'} to {args.end_date or 'end'}")
            covid_data.filter_by_date_range(args.start_date, args.end_date)
        
        # Process data
        print("Computing 7-day moving average...")
        covid_data.compute_moving_average(window=7)
        
        # Detect peaks
        print("Detecting significant peaks...")
        peaks = covid_data.detect_peaks(threshold=1.5)
        if peaks:
            print(f"Found {len(peaks)} significant peak(s) in the data")
        
        # Generate chart
        print("Generating chart...")
        output_file = f"covid_cases_{datetime.now().strftime('%Y%m%d_%H%M%S')}.png"
        chart_path = chart_gen.plot_daily_cases(
            df=covid_data.get_data(),
            peaks=peaks,
            title='COVID-19 Daily Cases with 7-Day Moving Average',
            filename=output_file
        )
        
        print(f"\nChart successfully generated: {os.path.abspath(chart_path)}")
        
    except FileNotFoundError as e:
        print(f"Error: {e}. Please check if the input file exists.")
        return 1
    except Exception as e:
        print(f"An error occurred: {str(e)}")
        return 1
    
    return 0

if __name__ == "__main__":
    exit(main())
