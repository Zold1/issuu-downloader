/* JavaScript Code for Console */

// Select all publication links
let links = document.querySelectorAll('div[data-testid="publication-card"] a');

// Loop through each link and log the href attribute
links.forEach((link, index) => {
    console.log(`Link ${index + 1}: ${link.href}`);
});