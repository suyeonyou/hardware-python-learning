import matplotlib.pyplot as plt
import numpy as np

print("=" * 40)
print("✅ 라이브러리 검증을 시작합니다!")
print("=" * 40)

# 가상의 사인파(오실로스코프 파형) 데이터 생성
x = np.linspace(0, 10, 100)
y = np.sin(x)

# 그래프 그리기 테스트
plt.plot(x, y, label="Test Signal", color="green")
plt.title("Matplotlib Installation Check")
plt.grid(True)
plt.legend()

print("🎉 모든 라이브러리가 정상적으로 작동합니다!")
print("👉 이제 팝업으로 뜨는 그래프 창을 닫으면 프로그램이 종료됩니다.")
print("=" * 40)

plt.show()