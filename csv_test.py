
# 실습용 Keysight 오실로스코프 데이터 파일을 생성하는 코드입니다.

csv_content = """[Header Info]
Model,MSOS804A High-Definition Oscilloscope
Firmware,06.30.00801
Sample Rate,20.00GSa/s
Time Base,200.0ns/div
Date,2026-06-01 20:35:00

[Data]
Time,Channel1
-1.00E-03,3.31
-0.80E-03,3.29
-0.60E-03,3.42
-0.40E-03,3.35
-0.20E-03,3.28
0.00E+00,3.30
0.20E-03,3.32
0.40E-03,3.48
0.60E-03,3.27
0.80E-03,3.31
1.00E-03,3.29
"""

# keysight_oscilloscope_data.csv 라는 이름으로 파일 저장
with open("keysight_oscilloscope_data.csv", "w", encoding="utf-8") as file:
    file.write(csv_content)

print("🎉 실습용 'keysight_oscilloscope_data.csv' 파일이 현재 폴더에 성공적으로 생성되었습니다!")