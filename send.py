import requests

webhook_url = "https://discord.com/api/webhooks/1493948841479770263/H8ZV4ft4l5AtgrAxfd0mH5p6Nx7D8XR8UY0T-MPkGp6-wbsmAeRUrQtvIVLvFp-9EGH4"

data = {
    "content": "Test message from GitHub"
}

requests.post(webhook_url, json=data)
