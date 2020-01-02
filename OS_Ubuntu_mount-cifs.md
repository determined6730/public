# 
```bash
sudo apt-get install cifs-utils
sudo mkdir /mnt/<local_share>
sudo mount -t cifs //<vpsa_ip_address>/<export_share> /mnt/<local_share>
# using nas access control(id,pwd)
sudo mount -t cifs -o user=<user on VPSA> //<vpsa_ip_address>/<export_share> /mnt/<local_share>
# add to /etc/fstab file:
//<vpsa_ip_address>/<export_share> /mnt/<local_share> cifs user=<user on VPSA>,pass=<passwd on VPSA>,file_mode=0777,dir_mode=0777 0 0
```