import logging
import os
from dotenv import load_dotenv
from src.extract import extract_data
from src.transform import calculate_kpis
from src.load import upload_to_sheets
from src.email_sender import send_notification

# Log setup
logging.basicConfig(
    filename='logs/pipeline.log',
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s'
)

load_dotenv()


def run_pipeline():
    try:
        logging.info("Starting KPI pipeline...")

        # ETL Steps
        raw_data = extract_data("scripts/data/sample_data.csv")
        kpi_df = calculate_kpis(raw_data)

        # Load to GSheets
        sheet_id = os.getenv("GOOGLE_SHEET_ID")
        upload_to_sheets(kpi_df, sheet_id)

        # Summary for email
        latest_metrics = kpi_df.iloc[-1].to_dict()


        report_date = latest_metrics['date']

        summary = (
            f"Date: {report_date}\n"
            f"Revenue: ${latest_metrics['revenue']}\n"
            f"ROAS: {latest_metrics['roas']}\n"
            f"CAC: ${latest_metrics['cac']}"
        )


        send_notification(report_date, summary)
        logging.info("Pipeline completed successfully.")

    except Exception as e:
        logging.error(f"Pipeline failed: {str(e)}")
        print(f"Error: {e}")


if __name__ == "__main__":
    run_pipeline()