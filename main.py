from pypresence import Presence
from time import time
 
RPC = Presence("966397796825567243")
btns = [
    {
        "label": "Discord Server",
        "url": "https://discord.gg/VPtDfkRHgA"
    },
    {
        "label": "VK",
        "url": "https://vk.com/maximochka14"
    }
]
 
RPC.connect()
RPC.update(
    state="sweeter than your life",
    details="Sladk1y Discord Bot Dev",
    start=time(),
    buttons=btns,
    large_image="cat",
    small_image="python",
    large_text="Sladk1y | Dev",
    small_text="Python Dev"
)

input()
