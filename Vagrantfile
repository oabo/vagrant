

Vagrant.configure("2") do |config|
  config.vm.box = "generic/ubuntu2004"
  config.ssh.insert_key = false


(1..3).each do |i|
  config.vm.define "node#{i}" do |node|
    node.vm.hostname = "v#{i}"
    node.ssh.private_key_path="~/.vagrant.d/insecure_private_key"
    
    node.vm.network  "public_network",
      bridge:'enp3s0' ,
      auto_config: false  
      

    node.vm.provision "ansible" do |ansible|
      ansible.playbook = "playbook.yml"
      end
    node.vm.provision "shell",
      run: "always",
      inline: "cat <<EOF>/etc/netplan/00-installer-config.yaml

  network:
   ethernets:
    eth1:   
     addresses: [172.16.2.24#{i}/22]  
     dhcp4: no 
     optional: true
     gateway4: 172.16.0.1 
     nameservers:
       addresses: [8.8.8.8] 
   version: 2
   renderer: networkd  
EOF
  sudo netplan apply
  "

    end
  end
end


