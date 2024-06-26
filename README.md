# Ethiopian Medical Business Data Warehouse

## Overview

This project involves the development of a robust data warehouse to store and analyze data from Ethiopian medical businesses. It includes data scraping from various sources including Telegram channels, data cleaning, object detection using YOLO, and API exposure using FastAPI. The goal is to facilitate comprehensive data analysis and decision-making in the healthcare sector.

## Business Need

Kara Solutions aims to centralize data on Ethiopian medical businesses to enable stakeholders to derive valuable insights through advanced analytics. The data warehouse enhances operational efficiency and strategic planning by providing a unified platform for data integration and analysis.

## Project Components

### Data Scraping and Collection Pipeline

- **Telegram Scraping:** Utilize Telegram API and custom scripts to extract data from relevant channels such as DoctorsET, Chemed, lobelia4cosmetics, yetenaweg, and others listed on [et.tgstat.com/medicine](https://et.tgstat.com/medicine).
- **Image Scraping:** Collect images from specified Telegram channels for object detection.
- **Storing Raw Data:** Store scraped data in a temporary storage location (e.g., local database) before further processing.
- **Monitoring and Logging:** Implement logging to track scraping progress, errors, and monitor pipeline performance.

#### Setup Instructions Data Scraping

1. **Clone the Repository:**
   ```bash
   git clone https://github.com/juniorworku/ethiopian-medical-business-data-warehouse.git
   cd ethiopian-medical-business-data-warehouse

2. **Install Dependencies:**
   ```bash
   pip install -r requirements.txt

3. **Telegram Scraping Setup:**
   -Create a Telegram API account and generate API credentials.
   -Update telegram_scraper.py with your API credentials and channels to scrape.
4. **Image Scraping Setup:**
   -Ensure Python packages like telethon are installed for Telegram image scraping.
   -Modify download_images.py to specify image collection from relevant Telegram channels.
5. **Logging Setup:**
   -Implement logging in telegram_scraping.py and image_scraping.py to monitor scraping processes.

### Data Cleaning and Transformation

- **Data Cleaning:** Remove duplicates, handle missing values, standardize formats, and validate data integrity.
- **Database Storage:** Design database schemas for cleaned data and use DBT for transformation tasks.
- **DBT for Data Transformation:** Define SQL models to transform data and ensure quality using testing and documentation features.
- **Monitoring and Logging:** Continue logging practices to monitor cleaning and transformation processes.

#### Setup Instructions for Data Cleaning and Transformation

1. **Ensure Database Setup:**
   -Configure database.py with your database connection URL (e.g., PostgreSQL).
   ```bash
   DATABASE_URL = "postgresql://user:password@localhost/dbname"

2. **Install DBT (Data Build Tool):**
   ```bash
   pip install dbt
   dbt init ethiopian_medical_project

3. **Define DBT Models:**
   -Create SQL files in the models directory for data transformations.
   -Use dbt run to execute transformations and load data into the data warehouse.
4. **Testing and Documentation:**
   -Implement tests (dbt test) and generate documentation (dbt docs generate) for transformed data.

### Object Detection Using YOLO

- **Environment Setup:** Install YOLO dependencies (e.g., OpenCV, TensorFlow/PyTorch) and clone the YOLO model repository.
- **Data Preparation:** Collect images from designated Telegram channels and use pre-trained YOLO models for object detection.
- **Processing and Storing Results:** Extract object data (bounding boxes, confidence scores, labels) and store in a structured format.
- **Monitoring and Logging:** Implement logging to monitor object detection tasks and ensure accuracy.

#### Setup Instructions for Object Detection Using YOLO

1. **Clone YOLO Repository:**
   ```bash
   git clone https://github.com/ultralytics/yolov5.git
   cd yolov5
   pip install -r requirements.txt

2. **Prepare Data for Object Detection:**
   -Modify YOLO scripts (object_detection.py) to specify image input paths from Telegram channels.
   -Use YOLO models (yolov5) to detect objects and extract relevant data.

3. **Store Detection Results:**
   -Implement database integration in YOLO scripts (object_detection.py) to store detection data (e.g., bounding boxes, labels).

### Expose Data Using FastAPI

- **Environment Setup:** Install FastAPI and Uvicorn for API development.
- **Database Configuration:** Configure SQLAlchemy for database connections.
- **Data Models and Schemas:** Define SQLAlchemy models and Pydantic schemas for data validation and serialization.
- **CRUD Operations:** Implement CRUD operations in FastAPI to manage data interactions.
- **API Endpoint Definition:** Define and expose API endpoints for seamless data access and manipulation.

#### Setup Instructions Expose Data Using FastAPI

1. **Install FastAPI and Uvicorn:**
   ```bash
   pip install fastapi uvicorn

2. **Database Configuration:**
   -Update database.py with SQLAlchemy database connection details.

   ```bash
   DATABASE_URL = "postgresql://user:password@localhost/dbname"

3. **Define Data Models and Schemas:**
   -Create SQLAlchemy models (models.py) and Pydantic schemas (schemas.py) for data validation and serialization.

4. **CRUD Operations Setup:**
   -Implement CRUD operations (crud.py) using SQLAlchemy for database interactions.

5. **Start the FastAPI Application:**
   ```bash
   uvicorn my_project.main:app --reload

6. **Access API Documentation:**

Open your browser and go to http://127.0.0.1:8000/docs to view and interact with the API using Swagger UI.

## Documentation

## Insights and Recommendations

### Insights
   -Data Enrichment: Object detection enhances data insights, enabling deeper analytics and decision-making.
   -Operational Efficiency: FastAPI facilitates real-time data interaction through robust API endpoints.

### Recommendations for Future Work
   -Enhanced Object Detection: Explore transfer learning techniques to improve YOLO model accuracy for medical equipment recognition.
   -Real-Time Data Processing: Implement stream processing for continuous updates from Telegram channels.
   -Advanced Analytics: Introduce predictive analytics models for forecasting and trend analysis in medical supply demand.
   -Data Governance and Security: Strengthen data governance and security measures to comply with healthcare regulations.

## Conclusion
This project lays a solid foundation for data-driven insights and operational efficiency in Ethiopian medical businesses. By integrating advanced technologies and methodologies, Kara Solutions aims to deliver transformative impacts through innovative data engineering and analytics.