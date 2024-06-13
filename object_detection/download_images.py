import os
import logging
import yaml
from telethon.sync import TelegramClient
from telethon.tl.types import InputMessagesFilterPhotos

# Ensure logs directory exists
os.makedirs('object_detection/logs', exist_ok=True)

# Set up logging
logging.basicConfig(filename='object_detection/logs/download_images.log', level=logging.INFO,
                    format='%(asctime)s %(levelname)s:%(message)s')

# Load configuration
try:
    with open('config.yaml', 'r') as config_file:
        config = yaml.safe_load(config_file)
except Exception as e:
    logging.error(f"Error loading config.yaml: {str(e)}")
    raise e

# Extract Telegram API credentials
try:
    api_id = config['telegram']['api_id']
    api_hash = config['telegram']['api_hash']
    phone = config['telegram']['phone']
except KeyError as e:
    logging.error(f"Missing key in config.yaml: {str(e)}")
    raise KeyError(f"Missing key in config.yaml: {str(e)}")

# Destination directory to save downloaded images
image_directory = "images"

# List of channels to fetch images from
telegram_channels = [
    "https://t.me/ChemedTelegramChannel",
    "https://t.me/lobelia4cosmetics"
]

# Function to download images from a Telegram channel
def download_images_from_telegram(api_id, api_hash, channel_url):
    client = TelegramClient('session_name', api_id, api_hash)
    client.start()

    # Fetch messages from channel
    try:
        messages = client.get_messages(channel_url, filter=InputMessagesFilterPhotos)

        # Download and save images
        for msg in messages:
            try:
                for photo in msg.photo:
                    image_name = f"{msg.date.strftime('%Y-%m-%d_%H-%M-%S')}.jpg"
                    image_path = os.path.join(image_directory, image_name)
                    client.download_media(photo, file=image_path)
                    logging.info(f"Downloaded {image_name} from {channel_url}")
            except Exception as e:
                logging.error(f"Error downloading from {channel_url}: {str(e)}")
    except Exception as e:
        logging.error(f"Error fetching messages from {channel_url}: {str(e)}")

    client.disconnect()

# Create the image directory if it doesn't exist
os.makedirs(image_directory, exist_ok=True)

# Download images from each channel
for channel in telegram_channels:
    download_images_from_telegram(api_id, api_hash, channel)
