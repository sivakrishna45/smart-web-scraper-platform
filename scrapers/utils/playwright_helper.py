from playwright.sync_api import sync_playwright


class PlaywrightHelper:

    @staticmethod
    def fetch(url):

        with sync_playwright() as p:

            browser = p.chromium.launch(
                headless=True
            )

            page = browser.new_page()

            # Prevent long hangs
            page.set_default_timeout(15000)

            page.goto(
                url,
                wait_until="domcontentloaded"
            )

            page.wait_for_timeout(2000)

            html = page.content()

            browser.close()

            return html