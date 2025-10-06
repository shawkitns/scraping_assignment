from playwright.sync_api import sync_playwright



with sync_playwright() as p:
    browser = p.chromium.launch(headless=True)
    page = browser.new_page()
    page.goto("https://www.siasat.com/list-of-12-pakistani-dramas-with-1-billion-views-until-2024-3095991/")

    headings = page.query_selector_all("h3")

    cards = ""
    for hd in headings:
        text = hd.text_content().strip()
        if "Billion Views" in text:
            img = hd.query_selector("img")
            img_url = img.get_attribute("src") if img else None
            if not img_url:
                img2 = hd.evaluate_handle("el => el.parentElement.querySelector('img')")
                if img2:
                    img_url = img2.get_attribute("src")

            if img_url:
                cards += f'<div class="card"><img src="{img_url}" alt="{text}"><p>{text}</p></div>\n'

    browser.close()

# # Write the HTML file
# with open("index.html", "w", encoding="utf-8") as f:
#     f.write(html_header + cards + html_footer)

# print("✅ Webpage created! Open 'index.html' in your browser.")

data = []

with open("names_and_titles.txt", "r", encoding="utf-8") as f:
    content = f.read().split("---")
    for block in content:
        lines = block.strip().split("\n")
        if len(lines) >= 2:
            title = lines[0].replace("Title: ", "").strip()
            img_url = lines[1].replace("Image URL: ", "").strip()
            data.append({"title": title, "image": img_url})

html_header = """
<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>Reasons My Mom Won't Talk To Me</title>
<style>
    body {
        font-family: 'Comic Sans MS', cursive, sans-serif;
        background-color: #fff7f2;
        color: #333;
        text-align: center;
    }
    h1 {
        color: #ff5c8d;
        font-size: 3em;
        margin-top: 50px;
    }
    .container {
        display: flex;
        flex-wrap: wrap;
        justify-content: center;
        gap: 30px;
        padding: 20px;
    }
    .card {
        background: white;
        border-radius: 20px;
        box-shadow: 0 4px 10px rgba(0,0,0,0.1);
        width: 250px;
        padding: 10px;
        transition: transform 0.2s ease;
    }
    .card:hover {
        transform: translateY(-5px);
    }
    img {
        width: 100%;
        border-radius: 15px;
        height: auto;
        object-fit: cover;
    }
    p {
        font-weight: bold;
        margin: 10px 0 0 0;
    }
</style>
</head>
<body>
<h1>Reasons My Mom Won't Talk To Me</h1>
<div class="container">
"""

html_footer = """
</div>
</body>
</html>
"""

# Build cards from data
cards = ""
for item in data:
    if item["image"]:  # make sure we have a valid image URL
        cards += f'<div class="card"><img src="{item["image"]}" alt="{item["title"]}"><p>{item["title"]}</p></div>\n'

# Write the HTML file
with open("index.html", "w", encoding="utf-8") as f:
    f.write(html_header + cards + html_footer)

print("✅ Webpage created from names_and_titles.txt! Open 'index.html' to see it.")
