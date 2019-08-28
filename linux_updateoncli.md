# ubuntu upgrade 16.04 -&gt; 18.04

## OS 버전 확인

```text
lsb-release -a
```

## 최신 패키지로 업그레이드

```text
sudo apt update
sudo apt upgrade
sudo apt dist-upgrade
```

## 업데이트 매니지 설치 & 릴리즈 업그레이드

```text
sudo apt install update-manager-core
sudo do-release-upgrade -d
```

