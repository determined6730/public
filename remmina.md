# remmina 

ubuntu RDP   

## install 
```
sudo apt-add-repository ppa:remmina-ppa-team/remmina-next
sudo apt update
sudo apt install remmina remmina-plugin-rdp remmina-plugin-secret remmina-plugin-spice
```

## issues 
- "You requested an H264 GFX mode for ser X@X.com, but your libfreedp does not support H264. Please check colour depth settings."
  prifile setting -> color depth -> GFX RFX (32bpp)

