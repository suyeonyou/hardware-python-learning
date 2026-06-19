
print("=== 헤더 건너뛰기 시작 ===")

# 진짜 데이터가 시작되었는지 감시하는 '깃발' 변수 (기본값은 거짓)
is_data_started = False

with open("keysight_oscilloscope_data.csv", "r", encoding="utf-8") as file:
    for line in file:
        clean_line = line.strip()
        
        # 1. 깃발이 아직 '거짓'일 때
        if not is_data_started:
            # 줄 바꿈 밑에 진짜 데이터 헤더인 "Time,Channel1"이 등장했는지 검사합니다.
            if "Time,Channel1" in clean_line:
                is_data_started = True # 이제부터 들어오는 줄은 다 진짜 데이터
            continue # 이 줄(컬럼명)까지는 출력하지 않고 패스
            
        # 2. 깃발이 '참(True)'으로 바뀌면 이 아래 코드가 무조건 실행됩니다.
        print(f"▶ 자동 추출된 데이터: {clean_line}")

print("=== 데이터 읽기 종료 ===")