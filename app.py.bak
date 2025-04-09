import streamlit as st
import pandas as pd
from datetime import datetime, timedelta
import uuid

# 페이지 설정
st.set_page_config(
    page_title="업무 리스트 관리자",
    page_icon="✅",
    layout="wide"
)

# CSS 스타일 적용
st.markdown("""
<style>
    .main {
        padding: 1.5rem;
        max-width: 1200px;
        margin: 0 auto;
    }
    .app-container {
        background-color: #f9f9f9;
        border-radius: 10px;
        padding: 20px;
        box-shadow: 0 2px 10px rgba(0,0,0,0.05);
    }
    .task-item {
        background-color: white;
        padding: 15px;
        border-radius: 8px;
        margin-bottom: 12px;
        border-left: 5px solid #e0e0e0;
        box-shadow: 0 1px 3px rgba(0,0,0,0.1);
        transition: all 0.2s ease;
    }
    .task-item:hover {
        box-shadow: 0 3px 8px rgba(0,0,0,0.15);
    }
    .important {
        color: #e53935;
        border-left-color: #e53935;
    }
    .completed {
        color: #808080;
        text-decoration: line-through;
        border-left-color: #4CAF50;
    }
    .low-priority {
        border-left-color: #2196F3;
    }
    .medium-priority {
        border-left-color: #FF9800;
    }
    .high-priority {
        border-left-color: #e53935;
    }
    .task-title {
        font-size: 32px;
        font-weight: bold;
        margin-bottom: 20px;
        color: #1E88E5;
    }
    .app-header {
        margin-bottom: 24px;
        display: flex;
        align-items: center;
    }
    .app-title {
        color: #1E88E5;
        font-weight: 800;
        font-size: 28px;
        margin: 0;
    }
    .task-content {
        font-size: 16px;
        margin: 8px 0;
        word-break: break-word;
    }
    .task-note {
        font-size: 13px;
        color: #616161;
        margin: 5px 0;
        padding: 8px 12px;
        background-color: #f5f5f5;
        border-radius: 4px;
        border-left: 3px solid #9e9e9e;
        word-break: break-word;
        position: relative;
    }
    .task-note:before {
        content: '📝';
        position: absolute;
        left: -20px;
        top: 8px;
        font-size: 14px;
    }
    .task-note-container {
        margin: 10px 0 10px 30px;
        position: relative;
    }
    .strikethrough {
        text-decoration: line-through;
    }
    .task-meta {
        display: flex;
        align-items: center;
        gap: 8px;
        margin-top: 8px;
        font-size: 12px;
        color: #757575;
    }
    .task-date {
        display: inline-flex;
        align-items: center;
        gap: 4px;
    }
    .task-date-icon {
        color: #757575;
    }
    .task-overdue {
        color: #e53935 !important;
        font-weight: 500;
        background-color: #ffebee !important;
        border: 1px solid #ffcdd2 !important;
    }
    .due-today {
        color: #f57c00 !important;
        font-weight: 500;
        background-color: #fff3e0 !important;
        border: 1px solid #ffe0b2 !important;
    }
    .due-tomorrow {
        color: #0288d1 !important;
        font-weight: 500;
        background-color: #e1f5fe !important;
        border: 1px solid #b3e5fc !important;
    }
    .due-future {
        color: #388e3c !important;
        font-weight: 500;
        background-color: #e8f5e9 !important;
        border: 1px solid #c8e6c9 !important;
    }
    .task-actions {
        margin-top: 10px;
    }
    .divider {
        margin: 20px 0;
        border-top: 1px solid #e0e0e0;
    }
    .status-section {
        background-color: white;
        padding: 15px;
        border-radius: 8px;
        margin-bottom: 20px;
        box-shadow: 0 1px 3px rgba(0,0,0,0.1);
    }
    .task-form {
        background-color: white;
        padding: 20px;
        border-radius: 8px;
        margin-bottom: 24px;
        box-shadow: 0 1px 3px rgba(0,0,0,0.1);
    }
    .category-badge {
        display: inline-block;
        padding: 3px 8px;
        border-radius: 12px;
        background-color: #f5f5f5;
        color: #555;
        font-size: 12px;
        margin-right: 5px;
    }
    .category-work {
        background-color: #bbdefb;
        color: #0d47a1;
    }
    .category-personal {
        background-color: #f8bbd0;
        color: #880e4f;
    }
    .category-shopping {
        background-color: #c8e6c9;
        color: #1b5e20;
    }
    .category-health {
        background-color: #ffecb3;
        color: #ff6f00;
    }
    .stButton > button {
        border-radius: 6px;
        font-weight: 600;
        transition: all 0.2s ease;
        height: 38px;
    }
    .primary-btn > button {
        background-color: #1976D2;
        color: white;
    }
    .primary-btn > button:hover {
        background-color: #1565C0;
    }
    .add-task-btn > button {
        width: 100% !important;
        height: 38px !important;
        background-color: #4CAF50;
        color: white;
        font-weight: 600;
        border-radius: 6px !important;
    }
    .add-task-btn > button:hover {
        background-color: #43A047;
    }
    .form-header {
        font-size: 18px;
        font-weight: 600;
        margin-bottom: 15px;
        color: #424242;
    }
    .form-input-label {
        font-size: 14px;
        font-weight: 500;
        color: #616161;
        margin-bottom: 5px;
    }
    .danger-btn > button {
        background-color: #f44336;
        color: white;
    }
    .danger-btn > button:hover {
        background-color: #d32f2f;
    }
    .success-btn > button {
        background-color: #4CAF50;
        color: white;
    }
    .stTextInput > div > div > input {
        border-radius: 6px;
        padding: 8px 12px;
        border: 1px solid #ddd;
        height: 38px;
    }
    .stTextInput > div > div > input:focus {
        border-color: #1976D2;
        box-shadow: 0 0 0 1px #1976D2;
    }
    [data-testid="column"] > [data-testid="stVerticalBlock"] > [data-testid="stButton"] {
        padding-top: 24px;
    }
    .metrics-container {
        display: flex;
        justify-content: space-between;
    }
    .metric-card {
        background-color: white;
        border-radius: 8px;
        padding: 15px;
        box-shadow: 0 1px 3px rgba(0,0,0,0.1);
        text-align: center;
    }
    .metric-value {
        font-size: 24px;
        font-weight: bold;
        color: #1976D2;
    }
    .metric-label {
        color: #757575;
        font-size: 14px;
    }
    .stDateInput > div > div > input {
        border-radius: 6px;
        height: 38px;
    }
    .stSelectbox > div > div > div {
        border-radius: 6px;
        height: 38px;
    }
    /* 테블릿 및 모바일 반응형 스타일 */
    @media (max-width: 992px) {
        .main {
            padding: 1rem;
        }
    }
    /* 사이드바 스타일 */
    .sidebar .sidebar-content {
        background-color: #f5f7f9;
    }
    /* 핵심 메트릭 스타일 */
    .metric-big {
        font-size: 36px;
        font-weight: 700;
        color: #1976D2;
    }
    /* 태그 스타일 */
    .tags-container {
        margin-top: 5px;
    }
    .icon-btn > button {
        width: 38px !important;
        height: 38px !important;
        padding: 0 !important;
        border-radius: 50% !important;
        display: flex !important;
        align-items: center !important;
        justify-content: center !important;
    }
    .star-btn > button {
        background-color: transparent;
        color: #FFB300;
        border: 1px solid #FFB300;
    }
    .star-btn > button:hover {
        background-color: #FFF8E1;
    }
    .star-filled-btn > button {
        background-color: #FFF8E1;
        color: #FFB300;
        border: 1px solid #FFB300;
    }
    .delete-btn > button {
        background-color: transparent;
        color: #f44336;
        border: 1px solid #f44336;
    }
    .delete-btn > button:hover {
        background-color: #FFEBEE;
    }
</style>
""", unsafe_allow_html=True)

# 세션 상태 초기화
if "tasks" not in st.session_state:
    st.session_state.tasks = []
if "filter" not in st.session_state:
    st.session_state.filter = "all"
if "sort" not in st.session_state:
    st.session_state.sort = "priority"
if "view" not in st.session_state:
    st.session_state.view = "list"
if "categories" not in st.session_state:
    st.session_state.categories = ["업무", "개인", "쇼핑", "건강"]
if "search_query" not in st.session_state:
    st.session_state.search_query = ""

# 사이드바 설정
with st.sidebar:
    st.image("https://img.icons8.com/fluency/96/000000/checklist.png", width=80)
    st.markdown("<h2 style='margin-top:-10px;'>업무 리스트 관리자</h2>", unsafe_allow_html=True)
    st.markdown("---")
    
    st.markdown("### 보기 모드")
    view_options = ["리스트 보기", "달력 보기", "통계 보기"]
    selected_view = st.selectbox("보기 선택", view_options, index=0, key="view_select")
    st.session_state.view = selected_view
    
    st.markdown("### 필터")
    filter_options = ["모든 업무", "미완료 업무", "오늘 할 일", "중요 업무", "완료된 업무"]
    selected_filter = st.radio("업무 필터링", filter_options, index=0)
    st.session_state.filter = selected_filter
    
    st.markdown("### 정렬")
    sort_options = ["우선순위", "생성일", "마감일"]
    selected_sort = st.selectbox("정렬 기준", sort_options, index=0)
    st.session_state.sort = selected_sort
    
    st.markdown("### 카테고리")
    selected_categories = []
    for category in st.session_state.categories:
        if st.checkbox(category, value=True):
            selected_categories.append(category)
    
    st.markdown("---")
    with st.expander("통계"):
        completed_count = sum(1 for task in st.session_state.tasks if task["completed"])
        total_count = len(st.session_state.tasks)
        if total_count > 0:
            completion_rate = round((completed_count / total_count) * 100)
        else:
            completion_rate = 0
        
        st.markdown(f"<div class='metric-big'>{completion_rate}%</div>", unsafe_allow_html=True)
        st.markdown("완료율", unsafe_allow_html=True)
        
        st.markdown("---")
        st.markdown(f"**총 업무 수:** {total_count}개")
        st.markdown(f"**완료된 업무:** {completed_count}개")
        st.markdown(f"**남은 업무:** {total_count - completed_count}개")

def generate_unique_id():
    return str(uuid.uuid4())

def add_task():
    if st.session_state.new_task.strip():
        # due_date가 datetime.date 객체이므로 문자열로 변환
        due_date = None
        if "due_date" in st.session_state:
            if isinstance(st.session_state.due_date, datetime):
                due_date = st.session_state.due_date.strftime("%Y-%m-%d %H:%M")
            else:  # datetime.date 객체인 경우
                due_date = st.session_state.due_date.strftime("%Y-%m-%d") + " 00:00"
                
        new_task = {
            "id": generate_unique_id(),
            "task": st.session_state.new_task,
            "important": False,
            "completed": False,
            "created_at": datetime.now().strftime("%Y-%m-%d %H:%M"),
            "due_date": due_date,
            "priority": st.session_state.priority if "priority" in st.session_state else "보통",
            "category": st.session_state.category if "category" in st.session_state else "업무",
            "notes": st.session_state.notes if "notes" in st.session_state else ""
        }
        st.session_state.tasks.append(new_task)
        st.session_state.new_task = ""
        if "notes" in st.session_state:
            st.session_state.notes = ""

def delete_task(task_id):
    st.session_state.tasks = [task for task in st.session_state.tasks if task["id"] != task_id]

def toggle_important(task_id):
    for task in st.session_state.tasks:
        if task["id"] == task_id:
            task["important"] = not task["important"]
            break

def toggle_completed(task_id):
    for task in st.session_state.tasks:
        if task["id"] == task_id:
            task["completed"] = not task["completed"]
            break

def filter_tasks():
    filtered_tasks = st.session_state.tasks.copy()
    
    # 검색어로 필터링
    if st.session_state.search_query:
        filtered_tasks = [task for task in filtered_tasks if st.session_state.search_query.lower() in task["task"].lower()]
    
    # 선택된 필터로 필터링
    if st.session_state.filter == "미완료 업무":
        filtered_tasks = [task for task in filtered_tasks if not task["completed"]]
    elif st.session_state.filter == "오늘 할 일":
        today = datetime.now().strftime("%Y-%m-%d")
        filtered_tasks = [task for task in filtered_tasks 
                        if task["due_date"] and task["due_date"].split()[0] == today and not task["completed"]]
    elif st.session_state.filter == "중요 업무":
        filtered_tasks = [task for task in filtered_tasks if task["important"]]
    elif st.session_state.filter == "완료된 업무":
        filtered_tasks = [task for task in filtered_tasks if task["completed"]]
    
    # 선택된 카테고리로 필터링
    if selected_categories:
        filtered_tasks = [task for task in filtered_tasks if task["category"] in selected_categories]
    
    # 정렬
    if st.session_state.sort == "우선순위":
        priority_order = {"높음": 0, "보통": 1, "낮음": 2}
        filtered_tasks = sorted(filtered_tasks, 
                              key=lambda x: (x["completed"], priority_order.get(x["priority"], 1), not x["important"]))
    elif st.session_state.sort == "생성일":
        filtered_tasks = sorted(filtered_tasks, 
                              key=lambda x: (x["completed"], datetime.strptime(x["created_at"], "%Y-%m-%d %H:%M")))
    elif st.session_state.sort == "마감일":
        # 마감일이 없는 업무는 맨 뒤로
        def get_due_date_for_sorting(task):
            if not task["due_date"]:
                return datetime.max
            try:
                return datetime.strptime(task["due_date"], "%Y-%m-%d %H:%M")
            except ValueError:
                # 날짜 형식이 다를 경우 대비
                return datetime.max
        
        filtered_tasks = sorted(filtered_tasks, 
                              key=lambda x: (x["completed"], get_due_date_for_sorting(x)))
    
    return filtered_tasks

def get_priority_class(priority):
    if priority == "낮음":
        return "low-priority"
    elif priority == "보통":
        return "medium-priority"
    elif priority == "높음":
        return "high-priority"
    return ""

def get_category_class(category):
    if category == "업무":
        return "category-work"
    elif category == "개인":
        return "category-personal"
    elif category == "쇼핑":
        return "category-shopping"
    elif category == "건강":
        return "category-health"
    return ""

# 메인 컨텐츠
st.markdown('<div class="app-container">', unsafe_allow_html=True)

# 앱 헤더
st.markdown('<div class="app-header">', unsafe_allow_html=True)
st.markdown('<h1 class="app-title">✅ 업무 리스트 관리자</h1>', unsafe_allow_html=True)
st.markdown('</div>', unsafe_allow_html=True)

# 검색 바
search_col1, search_col2 = st.columns([5, 1])
with search_col1:
    st.text_input("업무 검색", key="search_query")

# 새 업무 추가 섹션
with st.expander("새 업무 추가", expanded=True):
    st.markdown('<div class="task-form">', unsafe_allow_html=True)
    
    st.markdown('<div class="form-header">✨ 새 업무 추가</div>', unsafe_allow_html=True)
    
    # 업무 제목
    st.markdown('<div class="form-input-label">업무 제목*</div>', unsafe_allow_html=True)
    st.text_input("", key="new_task", placeholder="업무 내용을 입력하세요", label_visibility="collapsed")
    
    # 세부 정보 - 3열 레이아웃
    detail_col1, detail_col2, detail_col3 = st.columns(3)
    with detail_col1:
        st.markdown('<div class="form-input-label">마감일</div>', unsafe_allow_html=True)
        st.date_input("", key="due_date", value=datetime.now().date() + timedelta(days=1), label_visibility="collapsed")
    with detail_col2:
        st.markdown('<div class="form-input-label">우선순위</div>', unsafe_allow_html=True)
        st.selectbox("", ["낮음", "보통", "높음"], index=1, key="priority", label_visibility="collapsed")
    with detail_col3:
        st.markdown('<div class="form-input-label">카테고리</div>', unsafe_allow_html=True)
        st.selectbox("", st.session_state.categories, index=0, key="category", label_visibility="collapsed")
    
    # 메모
    st.markdown('<div class="form-input-label">메모 (선택사항)</div>', unsafe_allow_html=True)
    st.text_area("", key="notes", placeholder="추가 메모를 입력하세요", label_visibility="collapsed", height=100)
    
    # 추가 버튼
    col1, col2, col3 = st.columns([1, 1, 1])
    with col2:
        st.markdown('<div class="add-task-btn">', unsafe_allow_html=True)
        st.button("업무 추가하기", on_click=add_task, key="add_task_button")
        st.markdown('</div>', unsafe_allow_html=True)
    
    st.markdown('</div>', unsafe_allow_html=True)

# 상태 표시 섹션
filtered_tasks = filter_tasks()
completed_count = sum(1 for task in filtered_tasks if task["completed"])
remaining_count = len(filtered_tasks) - completed_count
overdue_count = sum(1 for task in filtered_tasks 
                  if not task["completed"] and task["due_date"] and 
                  datetime.strptime(task["due_date"].split()[0], "%Y-%m-%d").date() < datetime.now().date())

st.markdown('<div class="metrics-container">', unsafe_allow_html=True)
metric_cols = st.columns(4)
with metric_cols[0]:
    st.markdown("""
    <div class="metric-card">
        <div class="metric-value">{}</div>
        <div class="metric-label">총 업무</div>
    </div>
    """.format(len(filtered_tasks)), unsafe_allow_html=True)
with metric_cols[1]:
    st.markdown("""
    <div class="metric-card">
        <div class="metric-value">{}</div>
        <div class="metric-label">완료</div>
    </div>
    """.format(completed_count), unsafe_allow_html=True)
with metric_cols[2]:
    st.markdown("""
    <div class="metric-card">
        <div class="metric-value">{}</div>
        <div class="metric-label">남은 업무</div>
    </div>
    """.format(remaining_count), unsafe_allow_html=True)
with metric_cols[3]:
    st.markdown("""
    <div class="metric-card">
        <div class="metric-value" style="color: #e53935;">{}</div>
        <div class="metric-label">기한 초과</div>
    </div>
    """.format(overdue_count), unsafe_allow_html=True)
st.markdown('</div>', unsafe_allow_html=True)

# 업무 목록 표시
if st.session_state.view == "리스트 보기":
    if filtered_tasks:
        st.markdown('### 업무 목록')
        for task in filtered_tasks:
            # 스타일 클래스 결정
            task_class = ""
            if task["completed"]:
                task_class = "completed"
            elif task["important"]:
                task_class = "important"
            
            priority_class = get_priority_class(task["priority"])
            
            # 업무 카드 생성
            st.markdown(f'<div class="task-item {task_class} {priority_class}">', unsafe_allow_html=True)
            
            # 상단 행 (체크박스, 제목, 액션 버튼)
            col1, col2, col3 = st.columns([0.5, 5.5, 1])
            
            with col1:
                st.checkbox("", value=task["completed"], key=f"comp_{task['id']}", 
                          on_change=toggle_completed, args=(task['id'],))
            
            with col2:
                # 업무 내용
                st.markdown(f'<div class="task-content">{task["task"]}</div>', unsafe_allow_html=True)
            
            with col3:
                action_cols = st.columns(2)
                with action_cols[0]:
                    # 중요 버튼
                    star_btn_class = "icon-btn star-filled-btn" if task["important"] else "icon-btn star-btn"
                    st.markdown(f'<div class="{star_btn_class}">', unsafe_allow_html=True)
                    if task["important"]:
                        star_icon = "⭐"
                    else:
                        star_icon = "☆"
                    st.button(star_icon, key=f"imp_{task['id']}", on_click=toggle_important, args=(task['id'],))
                    st.markdown('</div>', unsafe_allow_html=True)
                with action_cols[1]:
                    # 삭제 버튼
                    st.markdown('<div class="icon-btn delete-btn">', unsafe_allow_html=True)
                    st.button("🗑️", key=f"del_{task['id']}", on_click=delete_task, args=(task['id'],))
                    st.markdown('</div>', unsafe_allow_html=True)
            
            # 메모 표시 (있을 경우)
            if task["notes"]:
                memo_style = "strikethrough" if task["completed"] else ""
                st.markdown(f'<div class="task-note-container">', unsafe_allow_html=True)
                st.markdown(f'<div class="task-note {memo_style}">{task["notes"]}</div>', unsafe_allow_html=True)
                st.markdown(f'</div>', unsafe_allow_html=True)
            
            # 메타 정보 행
            meta_col1, meta_col2 = st.columns([6, 2])
            
            with meta_col1:
                # 카테고리와 태그
                st.markdown('<div class="tags-container">', unsafe_allow_html=True)
                category_class = get_category_class(task["category"])
                st.markdown(f'<span class="category-badge {category_class}">{task["category"]}</span>', unsafe_allow_html=True)
                
                # 우선순위 표시
                priority_colors = {"높음": "#e53935", "보통": "#FF9800", "낮음": "#2196F3"}
                priority_icons = {"높음": "🔴", "보통": "🟠", "낮음": "🔵"}
                priority_color = priority_colors.get(task["priority"], "#757575")
                priority_icon = priority_icons.get(task["priority"], "")
                st.markdown(f'<span class="category-badge" style="background-color:{priority_color}20; color:{priority_color};">{priority_icon} {task["priority"]}</span>', unsafe_allow_html=True)
                
                # 마감일 표시
                if task["due_date"]:
                    try:
                        due_date = datetime.strptime(task["due_date"].split()[0], "%Y-%m-%d")
                        today = datetime.now()
                        tomorrow = today + timedelta(days=1)
                        
                        date_diff = (due_date.date() - today.date()).days
                        
                        if date_diff < 0 and not task["completed"]:
                            date_class = "task-overdue"
                            date_text = f"⚠️ 기한초과: {due_date.strftime('%Y-%m-%d')}"
                        elif date_diff == 0:
                            date_class = "due-today"
                            date_text = f"⏰ 오늘 마감: {due_date.strftime('%Y-%m-%d')}"
                        elif date_diff == 1:
                            date_class = "due-tomorrow"
                            date_text = f"🔔 내일 마감: {due_date.strftime('%Y-%m-%d')}"
                        else:
                            date_class = "due-future"
                            date_text = f"📅 마감: {due_date.strftime('%Y-%m-%d')}"
                            
                        if task["completed"]:
                            date_class = ""
                            date_text = f"✅ 완료: {due_date.strftime('%Y-%m-%d')}"
                        
                        st.markdown(f'<span class="category-badge {date_class}">{date_text}</span>', unsafe_allow_html=True)
                    except (ValueError, AttributeError):
                        # 날짜 형식이 유효하지 않은 경우 날짜 정보를 표시하지 않음
                        pass
                
                st.markdown('</div>', unsafe_allow_html=True)
            
            with meta_col2:
                # 생성일 표시
                created_date = task['created_at'].split()[0] if task['created_at'] else ""
                st.markdown(f'<div class="task-meta"><span class="task-date">📅 {created_date}</span></div>', unsafe_allow_html=True)
            
            st.markdown('</div>', unsafe_allow_html=True)
    else:
        if st.session_state.search_query:
            st.info("검색 결과가 없습니다. 다른 검색어를 입력해보세요.")
        else:
            st.info("현재 필터에 해당하는 업무가 없습니다. 새 업무를 추가해보세요!")

elif st.session_state.view == "통계 보기":
    st.markdown("### 업무 통계")
    
    # 카테고리별 업무 수
    category_counts = {}
    for cat in st.session_state.categories:
        category_counts[cat] = sum(1 for task in st.session_state.tasks if task["category"] == cat)
    
    if category_counts:
        st.bar_chart(category_counts)
    
    # 우선순위별 업무 수
    priority_data = {
        "높음": sum(1 for task in st.session_state.tasks if task["priority"] == "높음"),
        "보통": sum(1 for task in st.session_state.tasks if task["priority"] == "보통"),
        "낮음": sum(1 for task in st.session_state.tasks if task["priority"] == "낮음")
    }
    
    st.subheader("우선순위별 업무")
    st.bar_chart(priority_data)
    
    # 완료 vs 미완료
    completion_data = {
        "완료": completed_count,
        "미완료": len(st.session_state.tasks) - completed_count
    }
    
    st.subheader("업무 완료 상태")
    st.bar_chart(completion_data)

elif st.session_state.view == "달력 보기":
    st.markdown("### 업무 달력")
    
    # 간단한 주간 달력 뷰
    today = datetime.now()
    week_start = today - timedelta(days=today.weekday())
    
    days = []
    for i in range(7):
        days.append(week_start + timedelta(days=i))
    
    week_cols = st.columns(7)
    for i, day in enumerate(days):
        with week_cols[i]:
            day_name = ["월", "화", "수", "목", "금", "토", "일"][i]
            is_today = day.date() == today.date()
            date_style = "background-color:#e3f2fd; border-radius:5px; padding:5px;" if is_today else ""
            
            st.markdown(f"<div style='{date_style}text-align:center;'><b>{day_name}</b><br>{day.day}</div>", unsafe_allow_html=True)
            
            # 해당 날짜의 업무 표시
            today_str = day.strftime("%Y-%m-%d")
            day_tasks = []
            
            for task in st.session_state.tasks:
                if task["due_date"]:
                    try:
                        task_date = task["due_date"].split()[0]
                        if task_date == today_str:
                            day_tasks.append(task)
                    except (ValueError, AttributeError, IndexError):
                        # 잘못된 날짜 형식은 무시
                        continue
            
            for task in day_tasks:
                task_style = "text-decoration:line-through;" if task["completed"] else ""
                task_style += "color:#e53935;" if task["important"] else ""
                st.markdown(f"<div style='{task_style}padding:5px;font-size:12px;'>{task['task']}</div>", unsafe_allow_html=True)

st.markdown('</div>', unsafe_allow_html=True)  # app-container 종료 