# RNET Boilerplate with Rotating Proxy

Minimal HTTP request example using [rnet](https://github.com/0x676e67/rnet) (v3.0.0-rc17) with browser emulation and authenticated rotating proxies.

## Requirements

- Python >= 3.14
- `uv` recommended (or classic `pip`)
- A `proxies.txt` file at root with one proxy per line:
  - `http://user:pwd@ip:port`
  - `ip:port:user:pwd` (auto-converted)

## Installation

With `uv` (recommended):

```bash
uv venv
uv pip install -r pyproject.toml
```

With `pip`:

```bash
python -m venv .venv
.venv\Scripts\activate
pip install -r pyproject.toml
```

## Usage

```bash
uv run main.py
```

The script:
- Loads a random proxy from `proxies.txt`
- Configures an rnet client with Chrome 142 emulation on Windows
- Makes a GET request to https://probe.velys.software/ and displays the response

## Project Structure

- `main.py` - Main logic (proxy loading, rnet client, test request)
- `pyproject.toml` - Metadata and dependencies (`aiofiles`, `rnet`)
- `proxies.txt` - Proxy list (create your own, not versioned)

## Notes

- Don't commit `proxies.txt` if it contains sensitive credentials
- For connection errors, verify proxy format and HTTP protocol support
- Change the test URL in `main.py` as needed
