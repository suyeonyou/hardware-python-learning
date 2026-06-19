from playwright.sync_api import sync_playwright
import time
import re
import requests

TARGET_DATE = "2026-06-24"
TARGET_TIMES = ["10:30"]

TELEGRAM_BOT_TOKEN = "8175216021:AAF99qFDKXia-4rCykFaybB7n5cA04EpHW4"
TELEGRAM_CHAT_ID = "8907841220"


BASE_URL = (
    "https://m.booking.naver.com/booking/13/bizes/1464504/items/6935568"
    "?area=ple&lang=ko&startDate={date}&tab=book&theme=place"
)

def get_available_times(page):
    available_times = []

    buttons = page.locator("button").all()

    for btn in buttons:
        try:
            txt = btn.inner_text().strip()
            disabled = btn.is_disabled()
            cls = btn.get_attribute("class") or ""

            if not re.match(r"^\d{1,2}:\d{2}$", txt):
                continue

            if disabled:
                continue

            if "unselectable" in cls:
                continue

            available_times.append(txt)

        except Exception:
            pass

    return available_times

def check_once():
    url = BASE_URL.format(date=TARGET_DATE)

    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)
        page = browser.new_page(viewport={"width": 430, "height": 900})

        page.goto(url, wait_until="domcontentloaded")
        time.sleep(8)

        available_times = get_available_times(page)
        matched_times = [t for t in available_times if t in TARGET_TIMES]

        browser.close()

        return len(matched_times) > 0, matched_times, available_times

def send_telegram(message):
    url = f"https://api.telegram.org/bot{TELEGRAM_BOT_TOKEN}/sendMessage"

    response = requests.post(
        url,
        data={
            "chat_id": TELEGRAM_CHAT_ID,
            "text": message
        }
    )

    print(response.text)



if __name__ == "__main__":
    while True:
        print(f"[확인 중] 날짜: {TARGET_DATE}, 원하는 시간: {TARGET_TIMES}")

        available, matched_times, available_times = check_once()

        print("현재 예약 가능한 시간:", available_times)

        if available:
                message = (
                    f"🎉 난영 예약 가능!\n\n"
                    f"날짜 : {TARGET_DATE}\n"
                    f"시간 : {', '.join(matched_times)}\n\n"
                    f"지금 바로 예약하세요!"
                    )

                print(message)

                send_telegram(message)
                break
        else:
            print("아직 원하는 시간 예약 불가")

        print("5분 후 다시 확인합니다.")
        time.sleep(300)

