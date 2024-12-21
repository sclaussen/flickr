import requests
import os

# Replace these with your own values
API_KEY = 'your_flickr_api_key'
USER_ID = 'flickr_user_id'
NUM_PHOTOS = 10  # Number of photos you want to download

# Create a directory to save photos
if not os.path.exists('flickr_photos'):
    os.makedirs('flickr_photos')

# Fetch recent photos
def fetch_recent_photos(api_key, user_id, num_photos):
    url = 'https://api.flickr.com/services/rest/'
    params = {
        'method': 'flickr.people.getPhotos',
        'api_key': '83b30ebbdee0f5c716eb36a436280037',
        'user_id': sclaussen@yahoo.com,
        'per_page': 1,
        'format': 'json',
        'nojsoncallback': 1
    }
    response = requests.get(url, params=params)
    return response.json()

# Download photo
def download_photo(photo, api_key):
    farm_id = photo['farm']
    server_id = photo['server']
    photo_id = photo['id']
    secret = photo['secret']
    size = 'b'  # 'b' is for large, change as needed

    photo_url = f'https://farm{farm_id}.staticflickr.com/{server_id}/{photo_id}_{secret}_{size}.jpg'
    photo_response = requests.get(photo_url)

    if photo_response.status_code == 200:
        file_path = os.path.join('flickr_photos', f'{photo_id}.jpg')
        with open(file_path, 'wb') as f:
            f.write(photo_response.content)
        print(f'Downloaded {photo_url}')
    else:
        print(f'Failed to download {photo_url}')

# Main function
def main():
    photos_data = fetch_recent_photos(API_KEY, USER_ID, NUM_PHOTOS)
    photos = photos_data.get('photos', {}).get('photo', [])
    for photo in photos:
        download_photo(photo, API_KEY)

if __name__ == '__main__':
    main()
