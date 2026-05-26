import streamlit as st
import random
import time

# 1. 페이지 기본 설정 (브라우저 탭 제목 및 아이콘)
st.set_page_config(page_title="오늘 뭐 먹지?", page_icon="🍕", layout="centered")

# 앱 타이틀
st.title("🔮 기분 맞춤형 초정밀 음식 추천기")
st.write("지금 당신의 감정 상태에 가장 잘 어울리는 음식을 가려 뽑아 드립니다.")
st.markdown("---")

# 2. 아주 다양해진 오늘 기분 & 음식 데이터
mood_data = {
    "🔥 스트레스 만땅! 매운 걸로 지르고 싶다": ["떡볶이 (튀김/순대 추가 필수!)", "마라탕", "매운 족발", "불닭발"],
    "🌧️ 추적추적 비가 오네... 왠지 감성 돋는 날": ["김치전 + 막걸리", "해물파전", "칼국수", "수제비"],
    "🤑 통장 잔고 두둑! 나 오늘 Flex하고 싶어": ["한우 오마카세", "킹크랩", "호텔 뷔페", "안심 스테이크"],
    "💸 지갑이 가볍다... 가성비가 최고인 날": ["편의점 꿀조합", "김밥 + 라면", "학식/구내식당", "짜장면"],
    "🥱 아무것도 하기 싫고 입맛도 전혀 없을 때": ["시원한 냉면", "새콤한 비빔국수", "간장계란밥", "본죽"],
    "🍻 으어... 어제 과음해서 해장이 절실할 때": ["뼈해장국", "짬뽕", "콩나물국밥", "베트남 쌀국수"],
    "🎉 기분이 날아갈 듯 좋아! 파티 타임!": ["치킨 + 맥주", "피자", "삼겹살 구이", "족발+보쌈 세트"],
    "🌿 요즘 살찐 듯? 양심상 식단 조절이 필요할 때": ["닭가슴살 샐러드", "포케", "샤브샤브 (야채 위주)", "그릭 요거트"]
}

# 3. 사이드바 추가 (기능 제어)
st.sidebar.header("⚙️ 추가 옵션")
show_balloons = st.sidebar.checkbox("추천할 때 축하 효과 보기", value=True)
hungry_level = st.sidebar.slider("지금 배고픈 정도는?", 1, 5, 3)

# 4. 메인 화면: 기분 선택
selected_mood = st.selectbox("👉 오늘의 기분을 선택해 주세요:", list(mood_data.keys()))

st.markdown("###") # 약간의 공백 추가

# 5. 추천 버튼 클릭 시 로직 작동
if st.button("✨ 내 기분에 딱 맞는 메뉴 뽑기 ✨", use_container_width=True):
    
    # 실제 앱처럼 보이게 하는 로딩 애니메이션 효과
    with st.spinner('당신의 감정을 정밀 분석하여 메뉴를 고르는 중...🤔'):
        time.sleep(0.8) # 0.8초 동안 멈춤
    
    # 해당 기분의 음식 리스트에서 무작위 추출
    recommended_food = random.choice(mood_data[selected_mood])
    
    # 배고픔 지수에 따른 메시지 변화
    hungry_suffix = " (배고픔 폭발 상태니 곱빼기로 가시죠! 🐷)" if hungry_level >= 4 else ""
    
    # 결과 출력 (큰 초록색 박스)
    st.success(f"오늘의 추천 메뉴는 바로...  \n## 👑 **{recommended_food}{hungry_suffix}**")
    
    # 떡볶이가 걸렸을 때만 나오는 특별 히든 메시지!
    if "떡볶이" in recommended_food:
        st.info("💡 역시 스트레스에는 매콤달콤한 떡볶이가 진리죠! 당면 사리 추가는 어떠신가요?")
    
    # 사이드바 체크박스가 켜져 있으면 펑펑 터지는 애니메이션 작동
    if show_balloons:
        st.balloons()

st.markdown("---")
st.caption("💡 메뉴가 마음에 안 들면 버튼을 다시 한번 눌러보세요! 새로운 음식을 추천합니다.")
