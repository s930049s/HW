# Twitch mobile web automation

pytest + Selenium. Chrome emulates iPhone 16 Pro Max.

## Demo

Local test run:

![Local test run](docs/test_run.gif)

## Folder structure

```
twitch-wap-aqa/
├── README.md
├── requirements.txt      # Python dependencies
├── pytest.ini
├── conftest.py           # Open / close Chrome around the test
├── config/
│   └── settings.py       # URL, search text, phone, timeouts
├── pages/
│   ├── base_page.py      # Shared popup handling
│   ├── home_page.py
│   ├── search_page.py
│   └── streamer_page.py
├── tests/
│   └── test_twitch_wap.py
├── utils/
│   └── driver_factory.py # Chrome + mobile emulation
├── docs/
│   └── test_run.gif      # README demo GIF
└── screenshots/          # PNG saved by the test
```

## Scenario

1. Open https://www.twitch.tv/
2. Click search
3. Search StarCraft II
4. Scroll down twice
5. Open a streamer
6. Wait for the page and take a screenshot (`screenshots/`)

## Setup

Needs Python 3.10+ and Chrome.

```bash
pip install -r requirements.txt
```

`requirements.txt`:

```
pytest>=8.0.0
selenium>=4.20.0
```

## How to run

```bash
pytest
```

No window (background):

```bash
HEADLESS=1 pytest
```

Windows PowerShell:

```powershell
$env:HEADLESS='false'
pytest
```
