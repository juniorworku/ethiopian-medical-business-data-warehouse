# Ethiopian Medical Business Data Pipeline

This project implements a data pipeline for collecting, cleaning, and transforming data related to Ethiopian medical businesses. The pipeline involves two main tasks:

## Task 1: Data Scraping and Collection Pipeline

### Overview
Task 1 focuses on collecting data from various sources, primarily public Telegram channels related to Ethiopian medical businesses. Additionally, images are collected from these channels for object detection purposes.

### Steps
1. **Telegram Scraping:** Utilize the Telegram API or custom scripts to extract data from public Telegram channels relevant to Ethiopian medical businesses.
   - Channels include: DoctorsET, Chemed, lobelia4cosmetics, yetenaweg, EAHCI, and more.
2. **Image Scraping:** Collect images from selected Telegram channels for object detection.
3. **Storing Raw Data:** Store the scraped data in a temporary storage location, such as a local database or files, before further processing.
4. **Monitoring and Logging:** Implement logging to track the scraping process, capture errors, and monitor progress.

## Task 2: Data Cleaning and Transformation

### Overview
Task 2 involves cleaning and transforming the raw scraped data to prepare it for analysis and visualization.

### Steps
1. **Data Cleaning:**
   - Remove duplicates, handle missing values, and standardize formats.
   - Perform data validation to ensure data quality.
2. **Storing Cleaned Data:**
   - Store the cleaned data in a database for further analysis and reporting.
3. **DBT for Data Transformation:**
   - Set up a DBT (Data Build Tool) project and define transformation models using SQL.
   - Run DBT models to perform transformations and load data into a data warehouse.
   - Test and document the transformations to ensure data quality and provide context for the transformations.
4. **Monitoring and Logging:**
   - Implement logging to track the cleaning and transformation process, capture errors, and monitor progress.

## Usage

1. Clone the repository to your local machine.
2. Follow the instructions in the respective task directories (`scraping/README.md` and `cleaning_transforming/README.md`) to perform data scraping and cleaning/transformation steps.
3. Ensure you have the necessary dependencies installed (see `requirements.txt`).
4. Customize configuration settings as needed for your environment.




