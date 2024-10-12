import requests
import os
import img2pdf
import re

def download_single_document(username, document_id, output_filename):
    json_url = f"https://reader3.isu.pub/{username}/{document_id}/reader3_4.json"
    response = requests.get(json_url)
    if response.status_code != 200:
        print(f"Failed to fetch JSON data for {document_id}. Status code: {response.status_code}")
        return False

    try:
        data = response.json()
    except ValueError:
        print(f"Failed to parse JSON data for {document_id}.")
        return False

    pages = data.get('document', {}).get('pages', [])
    if not pages:
        print(f"No pages found in the document data for {document_id}.")
        return False

    temp_dir = f'temp_images_{document_id}'
    if not os.path.exists(temp_dir):
        os.makedirs(temp_dir)

    image_files = []
    for i, page in enumerate(pages):
        image_url = page.get('imageUri')
        if not image_url:
            print(f"Could not find image URL for page {i+1} of {document_id}")
            continue
        
        response = requests.get('https://'+image_url)
        if response.status_code == 200:
            filename = f'{temp_dir}/page_{i+1}.jpg'
            with open(filename, 'wb') as f:
                f.write(response.content)
            image_files.append(filename)
            print(f"Downloaded page {i+1} of {document_id}")
        else:
            print(f"Failed to download page {i+1} of {document_id}")

    if not image_files:
        print(f"No pages were successfully downloaded for {document_id}.")
        return False

    with open(output_filename, 'wb') as f:
        f.write(img2pdf.convert(image_files))

    for file in image_files:
        os.remove(file)
    os.rmdir(temp_dir)

    print(f"PDF saved as {output_filename}")
    return True

def process_url(url):
    match = re.search(r'issuu\.com/([^/]+)/docs/([^/]+)', url)
    if not match:
        print(f"Invalid Issuu document URL format: {url}")
        return
    username, document_id = match.groups()
    output_filename = f"{document_id}.pdf"
    download_single_document(username, document_id, output_filename)

def main():
    while True:
        url = input("Enter the Issuu PDF URL (or press Enter to input a file path): ").strip()
        if url:
            process_url(url)
        else:
            file_path = input("Enter the path to the file containing Issuu URLs: ").strip()
            if not os.path.exists(file_path):
                print("File not found. Please enter a valid file path.")
                continue
            
            with open(file_path, 'r') as file:
                urls = file.readlines()
            
            for url in urls:
                process_url(url.strip())
        
        another = input("Do you want to download another document or process another file? (y/n): ").lower()
        if another != 'y':
            break

    print("Download process completed.")

if __name__ == "__main__":
    main()