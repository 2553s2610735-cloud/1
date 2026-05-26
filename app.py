import streamlit as st
import random
import time

# -----------------------------------
# 페이지 설정
# -----------------------------------
st.set_page_config(
    page_title="🍔 음식 추천 앱",
    page_icon="🍕",
    layout="centered"
)

# -----------------------------------
# CSS 스타일
# -----------------------------------
st.markdown("""
<style>

html, body, [class*="css"] {
    font-family: 'Arial';
}

.main {
    background: linear-gradient(to bottom, #fff7f0, #ffe8d6);
}

/* 제목 */
.title {
    text-align: center;
    font-size: 55px;
    font-weight: bold;
    color: #ff4b4b;
    animation: glow 2s infinite alternate;
}

.subtitle {
    text-align: center;
    font-size: 22px;
    color: #444;
    margin-bottom: 30px;
}

/* 추천 카드 */
.food-card {
    background: linear-gradient(135deg, #ff6a00, #ee0979);
    padding: 45px;
    border-radius: 30px;
    text-align: center;
    color: white;
    font-size: 42px;
    font-weight: bold;
    box-shadow: 0px 10px 30px rgba(0,0,0,0.25);
    margin-top: 25px;
    animation: pop 0.8s ease;
}

/* 코멘트 */
.comment-box {
    background: white;
    padding: 18px;
    border-radius: 20px;
    text-align: center;
    font-size: 22px;
    color: #333;
    margin-top: 18px;
    box-shadow: 0px 5px 15px rgba(0,0,0,0.1);
    animation: fade 1.5s ease;
}

/* 버튼 */
.stButton > button {
    width: 100%;
    height: 65px;
    font-size: 24px;
    font-weight: bold;
    border-radius: 18px;
    background: linear-gradient(90deg, #ff512f, #dd2476);
    color: white;
    border: none;
    transition: 0.3s;
}

.stButton > button:hover {
    transform: scale(1.05);
    background: linear-gradient(90deg, #ff9966, #ff5
