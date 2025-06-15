# 🧠 FormPilot – A Memory-Driven Agentic Form Filler

> **NOTE:** This is **not a plug-and-play repo**..... it’s still under development. I haven’t uploaded the test forms or sample data and the updated agents yet, and several improvements are pending. Once everything is stabilized, I’ll update this repository accordingly.

---

## 📌 Project Overview

**FormPilot** is a memory-enhanced agentic system designed to intelligently fill out multi-step forms using context, memory, and DOM parsing. It's not just a wrapper around LLMs..... the system simulates real world decision-making through LangGraph’s state transitions, memory lookups, and fallbacks.

### 🧭 Key Objectives

- Automatically parse forms
- Identify input fields and match them with stored memory
- Fill known fields from memory
- Gracefully handle missing values using fallback placeholders
- Allow live field editing that syncs back to memory
- Provide a backend flow that is modular, traceable, and extendable

---

## 🧱 Core Architecture

This project combines the following components:

- **LangGraph**: To model a multi-step reasoning process for parsing, memory lookup, and fallback filling.
- **LangChain**: Used for field mapping.
- **Flask**: Lightweight server to render forms and handle frontend updates. Used for testing the overall flow and memory updating capabilities!!
- **Local Memory (JSON)**: Persistent state to simulate long-term memory and track field values.\## 🔰 Tech Stack

![Python](https://img.shields.io/badge/Python-3.11-green?logo=python)
![Flask](https://img.shields.io/badge/Flask-%20Microframework-yellow?logo=flask)
![LangGraph](https://img.shields.io/badge/LangGraph-State_Machine-orange?logo=langgraph)
![LangChain](https://img.shields.io/badge/LangChain-lightblue?logo=langchain)


---

## 🧠 LangGraph Flow

The form filling logic is orchestrated via a **LangGraph pipeline** with the following nodes:

1. **`label_mapper`**
   - Maps raw field labels (e.g. "Full Name") to memory keys (e.g. `name`)
   - Uses a predefined mapping dictionary

2. **`memory_fetcher`**
   - Looks up each mapped key in `memory.json`
   - Retrieves corresponding values if available

3. **`missing_detector`**
   - Identifies fields that are still unfilled (value is empty or `None`)

4. **`fallback_generator`**
   - For missing fields, injects a placeholder like `[Please fill Email]`
   - Also **updates memory** with this placeholder to ensure consistent rendering

5. **`final_consolidator`**
   - Merges filled and fallback fields into a unified list

<img width="275" alt="Screenshot 2025-06-15 at 19 38 24" src="https://github.com/user-attachments/assets/60266060-42c0-4ad3-befc-c474918fad79" />

---

## 🔧 Features Implemented

- ✅ DOM field extraction from any HTML form.
- ✅ Label-to-memory mapping with fallback support
- ✅ Dynamic form rendering via Flask 
- ✅ Auto-filling known fields from memory
- ✅ Placeholders for missing fields
- ✅ Live editing of field values with real-time memory updates.

---

## 🧪 Use Case
Imagine you're applying for a job online. The form asks for:

- Name
- Email
- Phone
- LinkedIn
- GitHub
- Resume
- Motivation
- Fit Reason etc etc.....
  
**FormPilot will**:

- Fill in what it already knows from memory
- Insert prompts for what it doesn’t (e.g., [Please fill LinkedIn])
- Let you edit fields, which immediately updates memory
- Reduce redundant typing across different forms or sessions

<img width="1685" alt="Screenshot 2025-06-15 at 19 10 29" src="https://github.com/user-attachments/assets/24c5b07e-cca6-4628-9686-38f77520fb8f" />

---

## 📌 Limitations & To-Do

- Improve label-to-key mapping with LLM or fuzzy logic
- Support for checkboxes, dropdowns, and file uploads
- Improve DOM
- Upgrade memory from JSON to database or vector store
- Update the whole repo and make it suitable to clone and execute :)

---

Drop in a mail or a text on linkeidn if there's anything you'd like to discuss about this repo!!

- Email: katasanikeerthanareddy@gmail.com
- LinkedIn: https://www.linkedin.com/in/keerthana-reddy-katasani-b07238268
