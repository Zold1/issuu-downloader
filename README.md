# Issuu Downloader

This repository contains two scripts for downloading and extracting content from publicly accessible Issuu pages. These scripts are intended for educational purposes only. Please ensure you comply with Issuu's terms of service when using these tools.

## Files

1. **`downloader.py`** – A Python script to download an Issuu document as a PDF by fetching individual pages and converting them into a single PDF.
2. **`url-scraper.js`** – A JavaScript snippet to be executed in the browser console to extract all project URLs from an Issuu user's page.

---

## 1. `downloader.py`

The Python script downloads pages from an Issuu document (provided via a URL) as images and converts them into a single PDF file. The tool supports both individual URLs and batch processing from a file.

### Dependencies

- Python 3.x
- `requests` library
- `img2pdf` library
- `re` and `os` (built-in modules)

You can install the necessary dependencies by running:

```bash
pip install requests img2pdf
```

### How to Use

1. **Direct URL input**:
   - When prompted, input an Issuu document URL in the format:
     ```
     https://issuu.com/username/docs/document_id
     ```

2. **Batch processing**:
   - If you have a file containing multiple Issuu URLs (one per line), you can input the file path when prompted.

3. The downloaded PDF will be saved in the current directory with the name based on the document ID.

### Example:

```bash
Enter the Issuu PDF URL (or press Enter to input a file path): https://issuu.com/someuser/docs/document_id
```

The output file will be saved as `document_id.pdf`.

### Script Flow:

- The script first fetches the document's JSON data.
- It then extracts the image URLs of the document pages.
- The images are downloaded and combined into a single PDF.
- Temporary images are cleaned up after conversion.

---

## 2. `url-scraper.js`

This JavaScript snippet can be used to extract all publication URLs from an Issuu user's page. It needs to be run in the browser's console on an Issuu user profile page.

### How to Use

1. Open the developer console (press `F12` or `Ctrl + Shift + I` in most browsers).
2. Navigate to the Issuu user's page (e.g., `https://issuu.com/jotunpaintsarabia`).
3. Paste the contents of `url-scraper.js` into the console and press Enter.
4. The console will output the URLs of all publications found on the page.

### Script Example:

```javascript
/* JavaScript Code for Console */

// Select all publication links
let links = document.querySelectorAll('div[data-testid="publication-card"] a');

// Loop through each link and log the href attribute
links.forEach((link, index) => {
    console.log(`Link ${index + 1}: ${link.href}`);
});
```

---

## Notes

- **Educational Use Only**: These tools are intended for educational purposes. Always respect the terms of service of Issuu and other websites.
- **Responsibility**: The repository author is not responsible for any misuse of these tools.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
