
target_voltage = 3.3
allow_margin = 0.05

spec_limit_max = target_voltage + allow_margin
print("=== 2단계 최종장 : 불량 시점 추적 시스템 가동 ===")

is_data_started = False

with open("keysight_oscilloscope_data.csv", "r", encoding ="utf-8") as file:
    for line in file:
        clean_line = line.strip()

        if not is_data_started :
            if "Time,Channel1" in clean_line:
                is_data_started = True
            continue

        split_data = clean_line.split(",")

        time_val = split_data[0]
        voltage_str = split_data[1]

        voltage_num = float(voltage_str)

        if voltage_num > spec_limit_max :
            print(f"[Fail 감지] 시간 : {time_val}| 측정값 : {voltage_num}V 스펙 {spec_limit_max}V 초과")

        
    print("=== 검증 종료 ===")

