import streamlit as st
import random

st.set_page_config(
    page_title="운동 추천기",
    page_icon="🏋️",
    layout="centered"
)

# 운동 데이터
exercise_data = {
    "상": [
        {
            "name": "버피 테스트",
            "desc": "전신을 사용하는 대표적인 고강도 운동",
            "time": "15~20분"
        },
        {
            "name": "점핑 런지",
            "desc": "하체와 심폐지구력을 동시에 강화",
            "time": "15분"
        },
        {
            "name": "마운틴 클라이머",
            "desc": "복부와 유산소 능력 향상",
            "time": "10~15분"
        },
        {
            "name": "스프린트",
            "desc": "짧고 강하게 달리는 고강도 운동",
            "time": "10분"
        },
        {
            "name": "배틀 로프",
            "desc": "전신 근력과 체력 향상",
            "time": "15분"
        }
    ],
    "중": [
        {
            "name": "조깅",
            "desc": "체력 향상과 지방 연소에 효과적",
            "time": "30분"
        },
        {
            "name": "자전거 타기",
            "desc": "관절 부담이 적은 유산소 운동",
            "time": "30~40분"
        },
        {
            "name": "줄넘기",
            "desc": "심폐지구력 향상에 도움",
            "time": "20분"
        },
        {
            "name": "계단 오르기",
            "desc": "하체 근력 및 체력 향상",
            "time": "20분"
        },
        {
            "name": "맨몸 스쿼트",
            "desc": "대표적인 하체 강화 운동",
            "time": "20분"
        }
    ],
    "하": [
        {
            "name": "걷기",
            "desc": "누구나 쉽게 할 수 있는 기본 운동",
            "time": "30~60분"
        },
        {
            "name": "요가",
            "desc": "유연성과 균형감 향상",
            "time": "20~40분"
        },
        {
            "name": "스트레칭",
            "desc": "근육 이완 및 부상 예방",
            "time": "15~20분"
        },
        {
            "name": "필라테스",
            "desc": "코어 강화와 자세 개선",
            "time": "30분"
        },
        {
            "name": "가벼운 산책",
            "desc": "스트레스 해소와 건강 관리",
            "time": "30분"
        }
    ]
}

st.title("🏋️ 운동 추천기")
st.markdown("운동 강도와 목적을 선택하면 운동을 추천해드립니다.")

intensity = st.selectbox(
    "운동 강도 선택",
    ["상", "중", "하"]
)

goal = st.selectbox(
    "운동 목적 선택",
    [
        "다이어트",
        "근력 향상",
        "체력 향상",
        "건강 관리",
        "스트레스 해소"
    ]
)

if st.button("운동 추천 받기"):
    try:
        exercise = random.choice(exercise_data[intensity])

        st.success("추천 운동이 생성되었습니다!")

        st.subheader(f"🏃 추천 운동: {exercise['name']}")

        st.write(f"**운동 강도:** {intensity}")
        st.write(f"**운동 목적:** {goal}")
        st.write(f"**설명:** {exercise['desc']}")
        st.write(f"**추천 시간:** {exercise['time']}")

    except Exception as e:
        st.error(f"오류가 발생했습니다: {e}")

st.divider()

if st.button("🎲 랜덤 운동 추천"):
    try:
        all_exercises = []

        for level in exercise_data.values():
            all_exercises.extend(level)

        exercise = random.choice(all_exercises)

        st.subheader("랜덤 추천 결과")
        st.write(f"**운동명:** {exercise['name']}")
        st.write(f"**설명:** {exercise['desc']}")
        st.write(f"**추천 시간:** {exercise['time']}")

    except Exception as e:
        st.error(f"오류가 발생했습니다: {e}")

st.divider()

st.subheader("📊 운동 강도 기준")

col1, col2, col3 = st.columns(3)

with col1:
    st.info("""
    상(고강도)
    - 버피
    - 스프린트
    - 점핑 운동
    """)

with col2:
    st.warning("""
    중(중강도)
    - 조깅
    - 줄넘기
    - 자전거
    """)

with col3:
    st.success("""
    하(저강도)
    - 걷기
    - 요가
    - 스트레칭
    """)
