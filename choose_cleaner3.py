import random
import texttable as tt


def assign_roles(cleaner_list, fixed_cleaners, fixed_roles, role_list):
    """
    일부 청소원에게는 역할을 고정하고, 나머지 청소원에게는 남은 역할 중에서 순서대로 할당하는 함수
    """
    # 고정된 청소원들에게는 역할을 할당
    role_assignment = {cleaner: role for role, cleaner in zip(fixed_roles, fixed_cleaners)}

    # 청소원 리스트를 복사한 후 섞음
    random_cleaner_list = cleaner_list.copy()
    random.shuffle(random_cleaner_list)

    # 역할을 순서대로 할당
    for cleaner in random_cleaner_list:
        if cleaner not in fixed_cleaners:
            # 다음 역할을 할당
            next_role = next((role for role in role_list if role not in role_assignment.values()), None)
            if next_role:
                role_assignment[cleaner] = next_role

    # 결과를 리스트로 변환하여 반환
    result = [['Role', 'Name']]
    for cleaner, role in role_assignment.items():
        result.append([role, cleaner])

    return result


# 청소원들의 리스트
cleaner_list = ["봉준호", "이규빈", "김하랑", "조서윤", "박유나", "박소망", "김지혜", "임세중",
                "임호준", "장시훈", "오민아", "나현준", "김선휘", "이은빈"]

# 고정된 역할을 할당할 청소원들
fixed_roles = ["소강당 정리", "소강당 정리"]
fixed_cleaners = ["임세중", "임호준", ""]

# 남은 역할들의 리스트
role_list = ["쓸기 1", "쓸기 2", "쓸기 3", "닦기 1", "닦기 2", "닦기 3", "신발장 닦기", "컴퓨터/AC/청정기 끄기",
             "정문 및 창문닦기", "스코어키", "책상닦기", "환기"]

# 역할 할당
assigned_roles = assign_roles(cleaner_list, fixed_cleaners, fixed_roles, role_list)

# 결과 출력
print("오늘의 역할 분배:")
tab = tt.Texttable()
tab.set_cols_align(['l', 'l'])
tab.add_rows(assigned_roles)
print(tab.draw())
