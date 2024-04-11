import random
import pandas as pd
from openpyxl import Workbook
from openpyxl.styles import Font, PatternFill, Alignment, Border, Side


def assign_roles(cleaner_list, fixed_cleaners, fixed_roles, role_list):
    """
    일부 청소원에게는 역할을 고정하고, 나머지 청소원에게는 남은 역할 중에서 랜덤하게 할당하는 함수
    """
    # 역할 할당 딕셔너리 초기화
    role_assignment = {}

    # 고정된 역할을 할당
    for cleaner, fixed_role in zip(fixed_cleaners, fixed_roles):
        role_assignment[cleaner] = fixed_role

    # 나머지 청소원에게 역할 할당
    remaining_cleaners = [cleaner for cleaner in cleaner_list if cleaner not in fixed_cleaners]
    random.shuffle(remaining_cleaners)

    # 역할을 순서대로 할당
    for cleaner in remaining_cleaners:
        next_role = role_list.pop(0)  # 역할 리스트의 맨 앞 역할 할당
        role_assignment[cleaner] = next_role

    # 결과를 리스트로 변환하여 반환
    result = [['Role', 'Name']]
    for cleaner, role in role_assignment.items():
        result.append([role, cleaner])

    return result


# 청소원들의 리스트
cleaner_list = ["봉준호", "이규빈", "김하랑", "조서윤", "박유나", "박소망", "김지혜", "임세중",
                "임호준", "장시훈", "오민아", "나현준", "김선휘", "이은빈"]

# 학생들을 무작위로 섞음
random.shuffle(cleaner_list)

# 고정된 역할을 할당할 청소원들
fixed_roles = ["소강당 정리", "소강당 정리"]
fixed_cleaners = ["임세중", "임호준"]

# 남은 역할들의 리스트 (순서대로)
role_list = ["쓸기 1", "쓸기 2", "쓸기 3", "닦기 1", "닦기 2", "닦기 3", "신발장 닦기", "컴퓨터/AC/청정기 끄기",
             "정문 및 창문닦기", "스코어키", "책상닦기", "환기"]

# 역할 할당
assigned_roles = assign_roles(cleaner_list, fixed_cleaners, fixed_roles, role_list)

# 결과 출력
print("오늘의 역할 분배:")
df = pd.DataFrame(assigned_roles[1:], columns=assigned_roles[0])

# 엑셀에 너비 설정하여 내보내기
excel_file = "assigned_roles.xlsx"
with pd.ExcelWriter(excel_file, engine='openpyxl') as writer:
    df.to_excel(writer, index=False, sheet_name="Sheet1")
    workbook = writer.book
    worksheet = writer.sheets["Sheet1"]
    header_font = Font(bold=True, size=14)
    cell_font = Font(bold=True, size=12)  # 모든 셀의 글꼴을 굵게 설정

    # 역할 열의 너비 설정
    worksheet.column_dimensions["A"].width = 40
    # 이름 열의 너비 설정
    worksheet.column_dimensions["B"].width = 18

    # C1과 D1에 "1주"와 "2주" 입력 및 색 입히기
    for col_letter, week in zip(["C", "D"], ["1주", "2주"]):
        cell = worksheet[f"{col_letter}1"]
        cell.value = week
        cell.font = Font(bold=True)  # 굵은 글꼴로 변경
        cell.alignment = Alignment(horizontal='center', vertical='center')  # 가운데 정렬

    # 표의 테두리 설정
    border = Border(left=Side(border_style='thin', color='000000'),
                    right=Side(border_style='thin', color='000000'),
                    top=Side(border_style='thin', color='000000'),
                    bottom=Side(border_style='thin', color='000000'))
    for row in worksheet.iter_rows(min_row=1, min_col=1, max_row=len(df) + 1, max_col=len(df.columns)+2):
        for cell in row:
            cell.border = border
            # 각 셀의 높이를 늘림
            cell.alignment = Alignment(wrap_text=True, horizontal='center', vertical='center')
            worksheet.row_dimensions[cell.row].height = 40  # 높이 설정
            cell.font = cell_font  # 모든 셀의 글꼴을 굵게 설정

print("엑셀 파일이 성공적으로 생성되었습니다.")
