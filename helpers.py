import json

with open("quran_data.json", "r", encoding="utf-8") as f:
    DATA = json.load(f)

def get_rizq_answer(question):
    question = question.lower()

    for item in DATA:
        keywords = item.get("keywords", []) + item.get("tags", [])

        for word in keywords:
            if word.lower() in question:
                return {
                    "surah": item["surah"],
                    "ayah": item["ayah"],
                    "translation": item["translation"]
                }

    return {
        "surah": None,
        "ayah": None,
        "translation": "No matching ayah found. Try asking about halal rizq, tawakkul, patience, tests, or gratitude."
    }
