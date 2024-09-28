import json
import requests

data = "" # input data

url = "" # public Api or local Api

data = json.dumps(data)

response = requests.post(url, data)

print(response.json())

"""sumary_line

another exampl

    # Return the paths in a JSON response
    return JSONResponse(content={
        'video_input': VIDEO_INPUT_PATH,
        'image_back': IMAGE_BACK_PATH,
        'output_path': VIDEO_OUTPUT_PATH
    })

"""

# URL of the FastAPI endpoint that returns file paths
url = 'http://your-api-url/file_paths'

try:
    # Make a GET request to the FastAPI endpoint
    response = requests.get(url)
    
    # Check if the request was successful
    response.raise_for_status()
    
    # Parse the JSON response
    data = response.json()
    
    # Access specific paths from the JSON response
    video_input_path = data.get('video_input')
    image_back_path = data.get('image_back')
    output_path = data.get('output_path')

    # Print or use the file paths
    print("Video Input Path:", video_input_path)
    print("Image Background Path:", image_back_path)
    print("Output Path:", output_path)

except requests.exceptions.RequestException as e:
    # Handle any HTTP request errors
    print(f"An error occurred: {e}")
