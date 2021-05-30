from playwright.sync_api import sync_playwright

def run(playwright):
    browser = playwright.chromium.launch(headless=False)
    context = browser.new_context()

    # Open new page
    page = context.new_page()

    # Go to https://www.google.com/
    page.goto("https://www.google.com/")
    page.wait_for_timeout(5000)
    # Click [aria-label="搜尋"]
    page.click("[aria-label=\"搜尋\"]")
    page.wait_for_timeout(5000)
    # Fill [aria-label="搜尋"]
    page.fill("[aria-label=\"搜尋\"]", "jamee")
    page.wait_for_timeout(5000)
    # Click text=Google 搜尋
    # with page.expect_navigation(url="https://www.google.com/search?q=jamee&source=hp&ei=-w-zYL-hDcHLmAWr4LK4AQ&iflsig=AINFCbYAAAAAYLMeC7F0xhIrrQQK0QqDaiZKZv2i6Fp-&oq=jamee&gs_lcp=Cgdnd3Mtd2l6EAwyAggAMgIIADICCAAyAggAMgIIADICCAAyAggAMgIIADICCAAyAggAOggIABCxAxCDAToFCAAQsQM6CggAELEDEIMBEApQsUhYmldg0HdoAXAAeACAATuIAecBkgEBNZgBAKABAaoBB2d3cy13aXqwAQA&sclient=gws-wiz&ved=0ahUKEwj_iuy0xPDwAhXBJaYKHSuwDBcQ4dUDCAk"):
    with page.expect_navigation():
        page.click("text=Google 搜尋")
    # assert page.url == "https://www.google.com/search?q=jamee&source=hp&ei=-w-zYL-hDcHLmAWr4LK4AQ&iflsig=AINFCbYAAAAAYLMeC7F0xhIrrQQK0QqDaiZKZv2i6Fp-&oq=jamee&gs_lcp=Cgdnd3Mtd2l6EAwyAggAMgIIADICCAAyAggAMgIIADICCAAyAggAMgIIADICCAAyAggAOggIABCxAxCDAToFCAAQsQM6CggAELEDEIMBEApQsUhYmldg0HdoAXAAeACAATuIAecBkgEBNZgBAKABAaoBB2d3cy13aXqwAQA&sclient=gws-wiz&ved=0ahUKEwj_iuy0xPDwAhXBJaYKHSuwDBcQ4dUDCAk"

    # ---------------------
    # context.close()
    # browser.close()

with sync_playwright() as playwright:
    run(playwright)