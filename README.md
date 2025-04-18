# 업무 리스트 관리자

Streamlit으로 만든 현대적이고 사용자 친화적인 업무 리스트 관리 웹 애플리케이션입니다.

![업무 리스트 관리자 스크린샷](https://github.com/yourusername/todo-manager/raw/main/screenshot.png)

## 주요 기능

- **현대적인 UI/UX**: 카드 기반 디자인과 직관적인 인터페이스
- **다양한 업무 속성**: 제목, 중요도, 완료 여부, 마감일, 우선순위, 카테고리, 메모
- **다중 보기 모드**: 리스트 보기, 달력 보기, 통계 보기
- **필터링 및 정렬**: 다양한 조건으로 업무 필터링 및 정렬
- **검색 기능**: 업무 제목 검색
- **직관적인 업무 상태 표시**: 색상 코드로 중요도와 완료 상태 구분
- **카테고리 및 태그**: 업무 분류 및 관리
- **통계 및 분석**: 카테고리별, 우선순위별 업무 통계
- **반응형 디자인**: 다양한 화면 크기에 최적화
- **세션 상태 저장**: 브라우저 세션 동안 데이터 유지

## 설치 및 실행 방법

1. 필요한 라이브러리 설치:
```
pip install -r requirements.txt
```

2. 애플리케이션 실행:
```
streamlit run app.py
```

3. 웹 브라우저에서 애플리케이션 접속 (기본 주소: http://localhost:8501)

## 사용 방법

1. **업무 추가**: "새 업무 추가" 섹션에서 업무 제목, 마감일, 우선순위, 카테고리, 메모를 입력하고 "추가하기" 버튼을 클릭합니다.
2. **업무 관리**: 
   - 체크박스를 클릭하여 업무 완료 상태 변경
   - 별표 아이콘을 클릭하여 중요 업무로 표시/해제
   - "삭제" 버튼으로 업무 제거
3. **필터링 및 정렬**: 
   - 사이드바의 필터 옵션을 사용하여 특정 업무만 표시
   - 정렬 기준을 선택하여 업무 목록 정렬
4. **보기 모드 변경**: 사이드바에서 리스트 보기, 달력 보기, 통계 보기 중 선택
5. **검색**: 상단 검색창에 키워드를 입력하여 업무 검색

## 요구사항

- Python 3.7 이상
- requirements.txt에 명시된 라이브러리들

## 개발자 정보

이 프로젝트는 업무 관리 효율성을 높이기 위해 개발되었으며, Todoist, Asana, Trello 등의 인기 있는 업무 관리 도구를 참고하여 디자인되었습니다.

## 라이선스

이 프로젝트는 MIT 라이선스를 따릅니다. 