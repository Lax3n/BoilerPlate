import asyncio
import random
from datetime import timedelta
from pathlib import Path
import rnet


def load_proxies(file_path: str = "proxies.txt") -> list[str]:
    """Load proxies from file."""
    path = Path(file_path)
    if not path.exists():
        return []

    proxies = []
    for line in path.read_text().strip().split("\n"):
        line = line.strip()
        if not line:
            continue
        # Convert ip:port:user:pwd to http://user:pwd@ip:port
        if not line.startswith(("http://", "https://", "socks5://")):
            parts = line.split(":")
            if len(parts) == 4:
                ip, port, user, pwd = parts
                line = f"http://{user}:{pwd}@{ip}:{port}"
            elif len(parts) == 2:
                line = f"http://{line}"
        proxies.append(line)
    return proxies


async def main():
    # Load proxies
    proxies = load_proxies()
    proxy_url = random.choice(proxies) if proxies else None

    # Cookie jar for session persistence
    jar = rnet.Jar()

    # HTTP/2 configuration (optional)
    http2_opts = rnet.http2.Http2Options(
        initial_window_size=65535,
        max_frame_size=16384,
        max_concurrent_streams=100,
        enable_push=False,
        adaptive_window=True,
    )

    # Create client with all available parameters
    client = rnet.Client(
        # Browser emulation
        emulation=rnet.EmulationOption(rnet.Emulation.Chrome143, rnet.EmulationOS.Windows),
        # Cookies
        cookie_provider=jar,
        # Proxy
        proxies=[rnet.Proxy.all(proxy_url)] if proxy_url else None,
        # Redirects
        redirect=rnet.redirect.Policy.limited(10),
        # Timeouts
        timeout=timedelta(seconds=30),
        connect_timeout=timedelta(seconds=10),
        read_timeout=timedelta(seconds=30),
        # Connection pool
        pool_max_idle_per_host=100,
        pool_idle_timeout=timedelta(seconds=90),
        # Compression
        gzip=True,
        brotli=True,
        deflate=True,
        zstd=True,
        # HTTP/2
        http2_options=http2_opts,
        # Default headers (optional)
        # headers=rnet.HeaderMap({"X-Custom": "value"}),
        # TLS (optional)
        # tls_info=True,
        # danger_accept_invalid_certs=False,
        # min_tls_version=rnet.TlsVersion.TLS_1_2,
        # max_tls_version=rnet.TlsVersion.TLS_1_3,
        # Network (optional)
        # local_address="0.0.0.0",
        # interface="eth0",
    )

    # Example request
    response = await client.get("https://httpbin.org/get")
    print(f"Status: {response.status}")
    print(await response.json())


if __name__ == "__main__":
    asyncio.run(main())
