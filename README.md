# HelloCortex
RSS feed combinator to merge Hello Internet and Cortex into chronological order (embarassing hack)

main.py combines
  "Hello Internet" http://www.hellointernet.fm/podcast?format=rss)
  "Hello Internet Archive" (for episodes more than 100 behind current) https://raw.githubusercontent.com/yottalogical/hello-internet-archive/master/HelloInternetArchive.rss
  "Cortex" https://www.relay.fm/cortex/feed
into hello_cortex.xml (which is likely not up-to-date)
