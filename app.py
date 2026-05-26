import streamlit as st
import random

# 1. 페이지 설정
st.set_page_config(page_title="오늘 뭐 먹지?", page_icon="🍕")

st.title("🔮 기분 맞춤형 확실한 음식 추천기")
st.write("지금 기분을 고르고 버튼을 누르면 추천 메뉴가 아래에 딱 고정됩니다!")
st.markdown("---")

# 2. 더 다양해진 기분 & 음식 데이터 (떡볶이 포함!)
mood_data = {
    "🔥 스트레스 폭발! 매운 게 당긴다": ["엽기 떡볶이", "마라탕", "매운 족발", "불닭볶음면"],
    "🌧️ 비가 주룩주룩... 감성 터지는 날": ["김치전 + 막걸리", "해물파전", "따뜻한 칼국수", "수제비"],
    "🤑 월급날! 나 오늘 Flex하고 싶어": ["한우 오마카세", "대게 찜", "양갈비 스테이크", "고급 초밥"],
    "💸 지갑이 텅 빈... 가성비가 최고인 날": ["편의점 도시락", "김밥 + 라면", "짜장면", "한식 뷔페"],
    "🥱 입맛도 없고 만사가 다 귀찮을 때": ["시원한 물냉면", "새콤한 비빔국수", "간장계란밥", "본죽"],
    "🍻 어제 과음해서 해장이 급할 때": ["뼈해장국", "얼큰한 짬뽕", "콩나물국밥", "쌀국수"],
    "🎉 기분 최고! 신나게 파티하고 싶다": ["후라이드 치킨", "콤비네이션 피자", "삼겹살 구이", "족발 보쌈"]
}

# 3. [중요] 값이 사라지지 않도록 저장 공간(Session State) 만들어두기
if "result_food" not in st.session_state:
    st.session_state.result_food = None

# 4. 기분 선택 드롭다운
selected_mood = st.selectbox("👉 오늘의 기분은 어떠신가요?", list(mood_data.keys()))

# 5. 추천 버튼
if st.button("✨ 오늘의 메뉴 추천받기 ✨", use_container_width=True):
    # 무작위로 음식을 뽑아 저장 공간에 안전하게 저장
    st.session_state.result_food = random.choice(mood_data[selected_mood])

st.markdown("---")

# 6. 결과 출력 (저장 공간에 음식 이름이 있을 때만 화면에 표시)
if st.session_state.result_food:
    st.header("🎉 오늘의 추천 메뉴")
    
    # 에러 방지를 위해 깔끔하게 배경 박스로만 출력
    st.info(f"오늘 당신에게 딱 맞는 음식은 바로 **[{st.session_state.result_food}]** 입니다!")
    
    # 떡볶이가 걸렸을 때만 나오는 특별 보너스 멘트!
    if "떡볶이" in st.session_state.result_food:
        st.success("💡 역시 기분 풀 땐 떡볶이가 최고죠! 튀김이랑
