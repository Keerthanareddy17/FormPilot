from bs4 import BeautifulSoup

def extract_form_fields_from_local_file(filepath: str):
    print(f"\n📄 Reading form from: {filepath}")
    with open(filepath, "r", encoding="utf-8") as f:
        soup = BeautifulSoup(f, "html.parser")

    input_fields = []

    for input_tag in soup.find_all("input"):
        input_type = input_tag.get("type", "text")
        if input_type in ["hidden", "submit", "button"]:
            continue  # Skip non-visible fields

        label_text = get_nearby_label(input_tag)
        input_fields.append({
            "label": label_text or "Unknown",
            "type": input_type,
        })

    for field in input_fields:
        print(f"Label: {field['label']}\nType: {field['type']}\n---")

    return input_fields

def get_nearby_label(input_tag):
    """
    Tries to get a nearby <label> or <p> element before the input as the label.
    """
    for sibling in input_tag.find_all_previous():
        if sibling.name in ["label", "p", "div", "span"]:
            text = sibling.get_text(strip=True)
            if 2 < len(text) < 100:
                return text
    return None
