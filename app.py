import streamlit as st
import pandas as pd

# 페이지 설정
st.set_page_config(
    page_title="업무 리스트 관리자",
    page_icon="✅",
    layout="centered"
)

# CSS 스타일 적용
st.markdown("""
<style>
    .main {
        padding: 2rem;
    }
    .task {
        padding: 10px;
        border-radius: 5px;
        margin-bottom: 10px;
    }
    .important {
        color: #ff4b4b;
        font-weight: bold;
    }
    .completed {
        color: #808080;
        text-decoration: line-through;
    }
    .task-title {
        font-size: 32px;
        font-weight: bold;
        margin-bottom: 20px;
        color: #1E88E5;
    }
    .divider {
        margin: 20px 0;
        border-top: 1px solid #e0e0e0;
    }
    .status-section {
        background-color: #f8f9fa;
        padding: 15px;
        border-radius: 5px;
        margin-bottom: 20px;
    }
    .stButton > button {
        width: 100%;
        border-radius: 5px;
        background-color: #1E88E5;
        color: white;
        font-weight: bold;
    }
    .stTextInput > div > div > input {
        border-radius: 5px;
    }
    /* 버튼 컨테이너와 텍스트 입력 필드 컨테이너의 정렬을 맞춤 */
    [data-testid="column"] > [data-testid="stVerticalBlock"] > [data-testid="stButton"] {
        padding-top: 24px;
    }
</style>
""", unsafe_allow_html=True)

# 세션 상태 초기화
if "tasks" not in st.session_state:
    st.session_state.tasks = []

def add_task():
    if st.session_state.new_task.strip():
        st.session_state.tasks.append({
            "task": st.session_state.new_task,
            "important": False,
            "completed": False
        })
        st.session_state.new_task = ""

def delete_task(index):
    st.session_state.tasks.pop(index)

def toggle_important(index):
    st.session_state.tasks[index]["important"] = not st.session_state.tasks[index]["important"]

def toggle_completed(index):
    st.session_state.tasks[index]["completed"] = not st.session_state.tasks[index]["completed"]

# 앱 헤더
st.markdown('<p class="task-title">업무 리스트 관리자</p>', unsafe_allow_html=True)

# 새 업무 추가 섹션
st.subheader("새 업무 추가")
col1, col2 = st.columns([4, 1])
with col1:
    st.text_input("새 업무를 입력하세요", key="new_task")
with col2:
    st.button("추가", on_click=add_task, key="add_task_button")

st.markdown('<div class="divider"></div>', unsafe_allow_html=True)

# 상태 표시 섹션
completed_count = sum(1 for task in st.session_state.tasks if task["completed"])
remaining_count = len(st.session_state.tasks) - completed_count

st.markdown('<div class="status-section">', unsafe_allow_html=True)
col1, col2 = st.columns(2)
with col1:
    st.metric("완료된 업무", f"{completed_count}개")
with col2:
    st.metric("남은 업무", f"{remaining_count}개")
st.markdown('</div>', unsafe_allow_html=True)

# 업무 정렬
if st.session_state.tasks:
    sorted_tasks = sorted(
        enumerate(st.session_state.tasks),
        key=lambda x: (x[1]["completed"], not x[1]["important"])
    )
else:
    sorted_tasks = []

# 업무 목록 표시
if sorted_tasks:
    st.subheader("업무 목록")
    for original_idx, task in sorted_tasks:
        col1, col2, col3, col4 = st.columns([0.7, 0.7, 4, 0.7])
        
        # 스타일 클래스 결정
        task_class = ""
        if task["important"] and not task["completed"]:
            task_class = "important"
        elif task["completed"]:
            task_class = "completed"
        
        with col1:
            st.checkbox("중요", value=task["important"], key=f"imp_{original_idx}", 
                        on_change=toggle_important, args=(original_idx,))
        
        with col2:
            st.checkbox("완료", value=task["completed"], key=f"comp_{original_idx}", 
                        on_change=toggle_completed, args=(original_idx,))
        
        with col3:
            st.markdown(f'<div class="{task_class}">{task["task"]}</div>', unsafe_allow_html=True)
        
        with col4:
            st.button("삭제", key=f"del_{original_idx}", on_click=delete_task, args=(original_idx,))
        
        st.markdown('<div class="divider"></div>', unsafe_allow_html=True)
else:
    st.info("업무가 없습니다. 위에서 새 업무를 추가해보세요!")

# 앱 푸터
st.markdown('<div class="divider"></div>', unsafe_allow_html=True)
st.caption("© 2023 업무 리스트 관리자 - Streamlit으로 만들어짐") 