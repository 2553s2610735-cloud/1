import streamlit as st
import random
import time

# 페이지 설정
st.set_page_config(
    page_title="음식 추천 앱",
    page_icon="🍔",
    layout="centered"
)

# ---------------------------
# CSS 꾸미기
# ---------------------------
st.markdown("""
<style>

.main {
    background-color: #fff8f0;
}

.title {
    text-align: center;
    font-size: 50px;
    font-weight: bold;
    color: #ff4b4b;
}

.subtitle {
    text-align: center;
    font-size: 20px;
    color: #555;
    margin-bottom: 30px;
}

.food-card {
    background: linear-gradient(135deg, #ff9966, #ff5e62);
    padding: 40px;
    border-radius: 25px;
    text-align: center;
    color: white;
    font-size: 40px;
    font-weight: bold;
    box-shadow: 0px 8px 20px rgba(0,0,0,0.2);
    animation: fadeIn 1s ease-in-out;
    margin-top: 20px;
}

.comment-box {
    background-color: white;
    padding: 15px;
    border-radius: 15px;
    text-align: center;
    font-size: 20px;
    color: #333;
    margin-top: 15px;
    box-shadow: 0px 4px 10px rgba(0,0,0,0.1);
}

@keyframes fadeIn {
    from {
        opacity: 0;
        transform: scale(0.8);
    }
    to {
        opacity: 1;
        transform: scale(1);
    }
}

.stButton>button {
    width: 100%;
    height: 60px;
    font-size: 24px;
    font-weight: bold;
    border-radius: 15px;
    background-color: #ff4b4b;
    color: white;
    border: none;
}

.stButton>button:hover {
    background-color: #ff1e1e;
    color: white;
}

</style>
""", unsafe_allow_html=True)

# ---------------------------
# 제목
# ---------------------------
st.markdown('<p class="title">🍽 오늘 뭐 먹지?</p>', unsafe_allow_html=True)
st.markdown('<p class="subtitle">기분에 맞는 음식을 추천해드립니다 😋</p>', unsafe_allow_html=True)

# ---------------------------
# 기분 리스트
# ---------------------------
moods = [
    "😄 신나는 날",
    "😌 편안한 날",
    "🥱 귀찮은 날",
    "😢 우울한 날",
    "🔥 스트레스 받는 날",
    "🥳 특별한 날",
    "💪 든든하게 먹고 싶은 날",
    "🌧 비 오는 날",
    "❄ 추운 날",
    "☀ 더운 날",
    "💕 달달한 게 땡기는 날",
    "🤔 새로운 음식 먹고 싶은 날",
    "🍺 야식 먹고 싶은 날",
    "🧘 건강하게 먹고 싶은 날",
    "🎬 혼자 쉬는 날"
]

# ---------------------------
# 음식 데이터
# ---------------------------
food_dict = {
    "😄 신나는 날": ["🍕 피자", "🍔 햄버거", "🍗 치킨", "🌮 타코"],
    "😌 편안한 날": ["🍝 파스타", "🥗 샐러드", "🍜 우동", "🥪 샌드위치"],
    "🥱 귀찮은 날": ["🍜 컵라면", "🍙 김밥", "🥡 도시락", "🥪 토스트"],
    "😢 우울한 날": ["🍫 초콜릿", "🍨 아이스크림", "🥩 삼겹살", "🍕 치즈피자"],
    "🔥 스트레스 받는 날": ["🌶 엽떡", "🔥 불닭볶음면", "🍖 곱창", "🍲 마라탕"],
    "🥳 특별한 날": ["🥩 스테이크", "🍣 초밥", "🦞 랍스터", "🍷 파인다이닝"],
    "💪 든든하게 먹고 싶은 날": ["🍚 국밥", "🍖 제육볶음", "🍛 카레", "🍱 덮밥"],
    "🌧 비 오는 날": ["🥘 파전", "🍜 칼국수", "🍲 수제비", "🌶 짬뽕"],
    "❄ 추운 날": ["🍲 부대찌개", "🍢 어묵탕", "🥘 전골", "🍜 라멘"],
    "☀ 더운 날": ["🍜 냉면", "🥣 콩국수", "🍧 빙수", "🍣 초밥"],
    "💕 달달한 게 땡기는 날": ["🧇 와플", "🍰 케이크", "🍩 도넛", "🍪 쿠키"],
    "🤔 새로운 음식 먹고 싶은 날": ["🌮 타코", "🍛 인도커리", "🥙 케밥", "🥗 포케"],
    "🍺 야식 먹고 싶은 날": ["🍗 치킨", "🍜 라면", "🥓 족발", "🍕 피자"],
    "🧘 건강하게 먹고 싶은 날": ["🥗 샐러드", "🍅 포케", "🐟 연어덮밥", "🥑 아보카도"],
    "🎬 혼자 쉬는 날": ["🍜 라면", "🍛 카레", "🍱 덮밥", "🍔 햄버거"]
}

# ---------------------------
# 기분 선택
# ---------------------------
selected_mood = st.selectbox(
    "오늘 기분을 선택하세요 👇",
    moods
)

# ---------------------------
# 추천 버튼
# ---------------------------
if st.button("🎲 음식 추천 받기"):

    with st.spinner("맛있는 음식 찾는 중... 🍳"):
        time.sleep(2)

    recommended_food = random.choice(food_dict[selected_mood])

    comments = [
        "오늘은 이거 먹으면 행복해질 거예요 😋",
        "완벽한 선택입니다 🔥",
        "지금 딱 생각나는 메뉴네요 🍽",
        "맛있게 먹고 힘내세요 💪",
        "오늘의 행운 음식입니다 🍀"
    ]

    # 풍선 효과
    st.balloons()

    # 음식 카드 출력
    st.markdown(
        f"""
        <div class="food-card">
            🎉 {recommended_food} 🎉
        </div>
        """,
        unsafe_allow_html=True
    )

    # 멘트 출력
    st.markdown(
        f"""
        <div class="comment-box">
            {random.choice(comments)}
        </div>
        """,
        unsafe_allow_html=True
    )

# 하단
st.write("")
st.caption("🍴 Made with Streamlit")
