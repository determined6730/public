# ubuntu upgrade 16.04 -> 18.04

### OS 버전 확인 
```
lsb-release -a
```

### 최신 패키지로 업그레이드 
```
sudo apt update
sudo apt upgrade
sudo apt dist-upgrade
```

### 업데이트 매니지 설치 & 릴리즈 업그레이드 
```
sudo apt install update-manager-core
sudo do-release-upgrade -d
```

