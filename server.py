from flask import Flask, render_template, request, jsonify
from utils.memory_manager import load_memory, update_memory

app = Flask(__name__)

@app.route("/")
def job_application():
    memory = load_memory()
    fields = [
        {"label": "Full Name", "key": "name", "value": memory.get("name", "")},
        {"label": "Email Address", "key": "email", "value": memory.get("email", "")},
        {"label": "Phone Number", "key": "phone", "value": memory.get("phone", "")},
        {"label": "LinkedIn Profile", "key": "linkedin", "value": memory.get("linkedin", "")},
        {"label": "GitHub URL", "key": "github", "value": memory.get("github", "")},
        {"label": "Date of Birth", "key": "dob", "value": memory.get("dob", "")},
        {"label": "Resume Link", "key": "resume", "value": memory.get("resume", "")}
    ]
    return render_template("job_application.html", fields=fields, memory=memory)

@app.route("/update-memory", methods=["POST"])
def update_memory_route():
    data = request.get_json()
    update_memory(data["key"], data["value"])
    return jsonify({"status": "updated"})

if __name__ == "__main__":
    app.run(debug=True)
