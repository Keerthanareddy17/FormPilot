from bs4 import BeautifulSoup
from utils.memory_manager import load_memory

def fill_html_form(filepath: str, field_mappings: list) -> str:
    """
    Injects values from memory into the form HTML and saves a new temp file.
    """
    with open(filepath, "r", encoding="utf-8") as f:
        soup = BeautifulSoup(f, "html.parser")

    memory = load_memory()

    for field in field_mappings:
        key = field["mapped_key"]
        value = memory.get(key)
        if not value:
            continue

        # Try finding an input near the matching label
        inputs = soup.find_all("input")
        for input_tag in inputs:
            label = get_nearby_label(input_tag)
            if label and label.strip().lower() == field["label"].strip().lower():
                input_tag["value"] = value
                break

    # Save the modified version to a new temp file
    modified_path = filepath.replace(".html", "_filled.html")
    with open(modified_path, "w", encoding="utf-8") as f:
        f.write(str(soup))

    return modified_path

def get_nearby_label(input_tag):
    for sibling in input_tag.find_all_previous():
        if sibling.name in ["label", "p", "div", "span"]:
            text = sibling.get_text(strip=True)
            if 2 < len(text) < 100:
                return text
    return None
