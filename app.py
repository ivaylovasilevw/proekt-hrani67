import streamlit as st
import easyocr
from PIL import Image
import numpy as np

st.set_page_config(page_title="Здравен скенер", page_icon="🛡️")

st.title("🛡️ AI Здравен Скенер")
st.write("Сканирай етикет и провери дали продуктът е подходящ за теб.")

harmful_e = [
    "E621", "E102", "E110", "E250",
    "E122", "E124", "E951", "E954",
    "E150d", "E211", "E955", "E950",
    "E220", "E228"
]

diabetes_words = [
    "sugar", "glucose", "fructose",
    "glucose-fructose syrup",
    "dextrose", "maltodextrin",
    "захар", "глюкозен сироп",
    "фруктоза"
]

high_blood_pressure = [
    "salt", "sodium", "натрий",
    "сол", "sodium benzoate"
]

allergens = [
    "milk", "soy", "gluten",
    "wheat", "peanut", "nuts",
    "мляко", "соя", "глутен",
    "фъстъци", "ядки", "яйца"
]

    if found_diabetes:
        score += len(found_diabetes)

        st.warning(
            "🍬 Внимание за диабетици: " +
            ", ".join(found_diabetes)
        )

    if found_pressure:
        score += len(found_pressure)

        st.warning(
            "❤️ Високо съдържание на сол/натрий: " +
            ", ".join(found_pressure)
        )

    if found_allergens:
        score += len(found_allergens)

        st.warning(
            "🤧 Алергени: " +
            ", ".join(found_allergens)
        )

    st.subheader("⭐ Оценка на продукта")

    if score == 0:
        st.success("✅ Изглежда като добър избор.")
    elif score <= 3:
        st.warning("⚠️ Продуктът е със среден риск.")
    else:
        st.error("❌ Продуктът не е особено здравословен.")
