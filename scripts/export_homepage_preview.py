"""Export a standalone homepage preview from a Jekyll build.

Usage: python scripts/export_homepage_preview.py BUILD_DIRECTORY OUTPUT.html
"""
from pathlib import Path
import base64
import mimetypes
import re
import sys
from urllib.parse import urlparse


def export(build_directory, output, page_path="index.html"):
    root = Path(build_directory)
    html = (root / page_path).read_text()

    def inline_stylesheet(match):
        href = match.group(1)
        source = root / urlparse(href).path.lstrip("/")
        if source.is_file():
            return "<style>" + source.read_text() + "</style>"
        return match.group(0)

    # Jekyll's relative_url produces root-relative paths, while the older
    # theme uses full canonical URLs. Both need embedding in a local file.
    html = re.sub(
        r'<link\b[^>]*rel="stylesheet"[^>]*href="([^"]+)"[^>]*>',
        inline_stylesheet,
        html,
    )

    def inline_image(match):
        src = match.group(1)
        source = root / urlparse(src).path.lstrip("/")
        if not source.is_file():
            return match.group(0)
        mime = mimetypes.guess_type(source.name)[0] or "application/octet-stream"
        data = base64.b64encode(source.read_bytes()).decode()
        return 'src="data:' + mime + ';base64,' + data + '"'

    html = re.sub(r'src="([^"]+\.(?:jpg|jpeg|png))"', inline_image, html)

    def inline_script(match):
        source = root / urlparse(match.group(1)).path.lstrip("/")
        if source.is_file():
            return "<script>" + source.read_text() + "</script>"
        return match.group(0)

    html = re.sub(r'<script src="([^"]+)"></script>', inline_script, html)
    if page_path == "index.html":
        assert ".academic-home__book { background:" in html
        assert html.count('class="academic-home__paper"') == 5
    assert not re.search(r'<link[^>]*href="[^"]*academic-home\.css"', html)
    Path(output).write_text(html)


if __name__ == "__main__":
    export(sys.argv[1], sys.argv[2], sys.argv[3] if len(sys.argv) > 3 else "index.html")
