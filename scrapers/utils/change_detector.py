import hashlib
import json
import logging
from pathlib import Path
from bs4 import BeautifulSoup   # ← Added

class ChangeDetector:
    def __init__(self):
        self.logger = logging.getLogger("ChangeDetector")
        self.signatures_file = Path("data/page_signatures.json")
        self.signatures_file.parent.mkdir(exist_ok=True)
        self.load_signatures()

    def load_signatures(self):
        if self.signatures_file.exists():
            with open(self.signatures_file) as f:
                self.signatures = json.load(f)
        else:
            self.signatures = {}

    def save_signatures(self):
        with open(self.signatures_file, 'w') as f:
            json.dump(self.signatures, f, indent=2)

    def get_signature(self, html):
        soup = BeautifulSoup(html, 'lxml')
        text = html[:5000]
        tag_count = len(soup.find_all(['a', 'div', 'h1', 'h2']))
        signature = f"{hashlib.md5(text.encode()).hexdigest()}_{tag_count}"
        return signature

    def detect_change(self, site_name, html):
        current_sig = self.get_signature(html)
        old_sig = self.signatures.get(site_name)

        if old_sig and old_sig != current_sig:
            self.logger.warning(f"⚠️ Structure change detected on {site_name}!")
            print(f"⚠️ WARNING: Website structure changed for {site_name}")
        else:
            self.logger.info(f"No structure change detected for {site_name}")

        self.signatures[site_name] = current_sig
        self.save_signatures()
