import streamlit as st
import random

# 제목
st.title("🍔 음식 추천 앱")

# 음식 리스트
foods = [
    "🍕 피자",
    "🍔 햄버거",
    "🍜 라면",
    "🍣 초밥",
    "🍗 치킨",
    "🥗 샐러드",
    "🌮 타코",
    "🍝 파스타"
]

# 버튼
if st.button("음식 추천 받기"):
    food = random.choice(foods)
    st.success(f"오늘의 추천 음식은: {food}")
