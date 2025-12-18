import re
from playwright.sync_api import Playwright, sync_playwright, expect


def run(playwright: Playwright) -> None:
    browser = playwright.chromium.launch(headless=False)

    context = browser.new_context(
        permissions=["clipboard-read", "clipboard-write"]
    )

    page = context.new_page()
    page = context.new_page()
    page.goto("https://dev.3snet.info/eventswidget/")
    page.locator("div").filter(has_text=re.compile(r"^Выбрать тематику$")).locator("div").click()
    page.locator("label").filter(has_text="Affiliate").click()
    page.get_by_text("Очистить").first.click()
    page.locator("div").filter(has_text=re.compile(r"^Выбрать тематику$")).locator("div").click()
    page.get_by_text("Выбрать все").first.click()
    page.locator("div").filter(has_text=re.compile(r"^Выбрано: 8$")).locator("div").click()
    page.locator("div").filter(has_text=re.compile(r"^Все страны$")).locator("div").click()
    page.get_by_text("Выбрать все").nth(1).click()
    page.locator("div").filter(has_text=re.compile(r"^Выбрано: 1$")).locator("div").click()
    page.locator("input[name=\"width\"]").click()
    page.locator("input[name=\"width\"]").fill("1234")
    page.locator("input[name=\"height\"]").click()
    page.locator("input[name=\"height\"]").fill("212")
    page.locator("label").filter(has_text="на всю высоту блока").locator("div").first.click()
    page.locator("label:nth-child(3) > .radio__square").first.click()
    page.get_by_role("button", name="Сгенерировать превью").click()
    page.get_by_role("button", name="Скопировать код").click()
    page.wait_for_timeout(500)

    copied_code = page.evaluate("navigator.clipboard.readText()")

    print("\n===== СКОПИРОВАННЫЙ КОД =====\n")
    print(copied_code)
    print("\n============================\n")


    # ---------------------
    context.close()
    browser.close()


with sync_playwright() as playwright:
    run(playwright)