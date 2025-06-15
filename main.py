import os
import webbrowser
from agents.form_reader import extract_form_fields_from_local_file
from agents.field_mapper import map_field_label_to_key
from utils.memory_manager import get_value, update_memory
from utils.html_filler import fill_html_form

# List of testttttt multi-page HTML form files
form_pages = [
    "forms/page1.html",
    "forms/page2.html",
    "forms/page3.html"
]

for filepath in form_pages:
    print(f"\n Reading form from: {filepath}")

    # Step 1: Extract fields from HTML
    extracted_fields = extract_form_fields_from_local_file(filepath)

    print("\n Attempting to auto-fill values from memory:\n")
    updated_fields = []

    # Step 2: Map labels to profile keys & get values
    for field in extracted_fields:
        label = field["label"]
        input_type = field["type"]

        mapped_key = map_field_label_to_key(label)
        value = get_value(mapped_key)

        if value:
            print(f"{label} → [{mapped_key}] = {value}")
            override = input(" Do you want to override it? (y/n): ").strip().lower()
            if override == 'y':
                value = input(f" Enter new value for [{mapped_key}]: ").strip()
                update_memory(mapped_key, value)
                print(f" Updated [{mapped_key}] = {value} in memory.")
        else:
            value = input(f" No value found for [{mapped_key}]. Please enter it: ").strip()
            update_memory(mapped_key, value)
            print(f" Saved [{mapped_key}] = {value} to memory.")

        updated_fields.append({
            "label": label,
            "mapped_key": mapped_key,
            "value": value,
            "type": input_type
        })

    # Step 3: Inject values into a copy of the form HTML
    filled_html_path = fill_html_form(filepath, updated_fields)

    # Step 4: Display in browser
    webbrowser.open(f"file://{os.path.abspath(filled_html_path)}")

    input("\n🔹 Press Enter to proceed to next form page...\n")
