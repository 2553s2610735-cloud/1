import streamlit as st
import random

st.set_page_config(
    page_title="자기관리 운동 추천기",
    page_icon="🏆",
    layout="centered"
)

# 운동 데이터
exercise_data = {
    "상": [
        {
            "name": "버피 테스트",
            "time": "15분",
            "effect": "전신 지방 연소",
            "desc": "대표적인 고강도 전신 운동"
        },
        {
            "name": "HIIT",
            "time": "20분",
            "effect": "체지방 감소",
            "desc": "짧고 강하게 반복하는 인터벌 운동"
        },
        {
            "name": "점핑 런지",
            "time": "15분",
            "effect": "하체 근력 강화",
            "desc": "하체와 심폐 기능을 동시에 자극"
        },
        {
            "name": "스프린트",
            "time": "10분",
            "effect": "순발력 및 체력 향상",
            "desc": "짧고 강하게 달리는 운동"
        },
        {
            "name": "마운틴 클라이머",
            "time": "15분",
            "effect": "복부 강화",
            "desc": "코어와 유산소 운동 효과"
        },
        {
            "name": "배틀 로프",
            "time": "15분",
            "effect": "전신 근력 향상",
            "desc": "상체와 심폐 능력 강화"
        }
    ],
    "중": [
        {
            "name": "조깅",
            "time": "30분",
            "effect": "체력 향상",
            "desc": "대표적인 유산소 운동"
        },
        {
            "name": "줄넘기",
            "time": "20분",
            "effect": "심폐지구력 향상",
            "desc": "칼로리 소모가 높은 운동"
        },
        {
            "name": "자전거 타기",
            "time": "40분",
            "effect": "하체 강화",
            "desc": "관절 부담이 적은 운동"
        },
        {
            "name": "계단 오르기",
            "time": "20분",
            "effect": "하체 근력 강화",
            "desc": "생활 속 유산소 운동"
        },
        {
            "name": "맨몸 스쿼트",
            "time": "20분",
            "effect": "하체 근육 발달",
            "desc": "기본적인 근력 운동"
        },
        {
            "name": "빠른 걷기",
            "time": "40분",
            "effect": "체지방 감소",
            "desc": "가볍지만 효과적인 유산소"
        }
    ],
    "하": [
        {
            "name": "걷기",
            "time": "40분",
            "effect": "건강 유지",
            "desc": "누구나 쉽게 실천 가능"
        },
        {
            "name": "요가",
            "time": "30분",
            "effect": "유연성 향상",
            "desc": "몸과 마음의 균형"
        },
        {
            "name": "스트레칭",
            "time": "15분",
            "effect": "근육 이완",
            "desc": "부상 예방에 도움"
        },
        {
            "name": "필라테스",
            "time": "30분",
            "effect": "코어 강화",
            "desc": "자세 교정에 효과적"
        },
        {
            "name": "가벼운 산책",
            "time": "30분",
            "effect": "스트레스 해소",
            "desc": "정신 건강에도 도움"
        },
        {
            "name": "명상 걷기",
            "time": "20분",
            "effect": "집중력 향상",
            "desc": "마음 챙김 운동"
        }
    ]
}

missions = [
    "물 2L 마시기",
    "30분 일찍 자기",
    "10분 독서하기",
    "야식 먹지 않기",
    "엘리베이터 대신 계단 이용하기",
    "오늘 감사한 일 3가지 적기",
    "스마트폰 사용시간 30분 줄이기",
    "하루 5분 명상하기"
]

st.title("🏆 자기관리 운동 추천기")
st.write("건강한 습관 형성을 위한 운동과 자기관리 미션을 추천합니다.")

goal = st.selectbox(
    "🎯 자기관리 목표",
    [
        "체중 감량",
        "근력 향상",
        "체력 향상",
        "건강 관리",
        "스트레스 해소",
        "습관 만들기"
    ]
)

level = st.radio(
    "🔥 운동 강도 선택",
    ["상", "중", "하"],
    horizontal=True
)

if st.button("운동 추천 받기"):
    try:
        exercise = random.choice(exercise_data[level])
        mission = random.choice(missions)

        st.success("오늘의 추천이 준비되었습니다!")

        st.subheader(f"🏃 {exercise['name']}")

        st.metric("운동 강도", level)

        st.write(f"**추천 시간:** {exercise['time']}")
        st.write(f"**기대 효과:** {exercise['effect']}")
        st.write(f"**설명:** {exercise['desc']}")

        st.divider()

        st.subheader("🎯 오늘의 자기관리 미션")
        st.info(mission)

    except Exception as e:
        st.error(f"오류가 발생했습니다: {e}")

st.divider()

if st.button("🎲 랜덤 운동 추천"):
    try:
        all_exercises = []

        for items in exercise_data.values():
            all_exercises.extend(items)

        exercise = random.choice(all_exercises)

        st.subheader("랜덤 추천 결과")
        st.write(f"**운동명:** {exercise['name']}")
        st.write(f"**추천 시간:** {exercise['time']}")
        st.write(f"**효과:** {exercise['effect']}")
        st.write(f"**설명:** {exercise['desc']}")

    except Exception as e:
        st.error(f"오류가 발생했습니다: {e}")

st.divider()

st.subheader("📊 운동 강도 가이드")

col1, col2, col3 = st.columns(3)

with col1:
    st.error("""
    상 (고강도)

    • 버피 테스트
    • HIIT
    • 스프린트
    • 점핑 런지
    """)

with col2:
    st.warning("""
    중 (중강도)

    • 조깅
    • 줄넘기
    • 자전거
    • 계단 오르기
    """)

with col3:
    st.success("""
    하 (저강도)

    • 걷기
    • 요가
    • 스트레칭
    • 필라테스
    """)

st.divider()

st.caption("꾸준한 운동 + 작은 습관 변화 = 최고의 자기관리")
