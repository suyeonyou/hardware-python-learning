import numpy as np
import matplotlib.pyplot as plt

print("="* 50)
print("노이즈 파형 생성 및 자동 PASS/FAIL 판정 시작")
print("="* 50)

# 1. 가상의 노이즈 낀 전압
x = np.linspace(0,10,200)
# DC offset
y_ideal = np.sin(x) + 2.5

# Random noise(노이즈 0.15V)
noise_amplitude = 0.15
noise = np.random.normal(0,noise_amplitude,x.size)
measured_signal = y_ideal + noise

#2. 최대, 최소 값 찾기
v_max = np.max(measured_signal)
v_min = np.min(measured_signal)
measured_vpp = v_max - v_min

# 합격 기준
spec_limit = 2.4

print(f"측정된 Max 전압 : {v_max : .2f}V")
print(f"측정된 Min 전압 : {v_min : .2f}V")
print(f"최종 Vpp : {measured_vpp:.2f}V")

print(f"합격 스펙 기준 : {spec_limit}V 이하")
print("="* 50)

# 4. PASS/FAIL 판정
if measured_vpp<=spec_limit:
    print("판정결과 : PASS")
else:
    print("판정결과 : CAP 보강 필요")

# 5. 그래프 시각화
plt.plot(x, measured_signal, label = f"Measured Signal (Vpp : {measured_vpp:.2f}V)",
         color = "darkcyan")
plt.axhline(y=v_max, color="red", linestyle = "--",
            alpha=0.5, label=f"Max ({v_max:.2f}V)")
plt.axhline(y=v_min, color="orange", linestyle = "--",
            alpha=0.5, label=f"Max ({v_min:.2f}V)")

plt.title("Automated Spec Judgment with noise Signal")
plt.grid(True)
plt.legend(loc='best')
plt.show()
