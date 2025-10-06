from playwright.sync_api import sync_playwright

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

# Write the HTML file
with open("index.html", "w", encoding="utf-8") as f:
    f.write(html_header + cards + html_footer)

print("✅ Webpage created! Open 'index.html' in your browser.")
