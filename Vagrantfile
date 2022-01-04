

Vagrant.configure("2") do |config|
  config.vm.box = "generic/ubuntu2004"
  config.ssh.insert_key = false
  config.vm.network :public_network,:bridge=>'vnet0'


(1..3).each do |i|
  config.vm.define "node#{i}" do |node|
    node.vm.hostname = "v#{i}"

    node.ssh.private_key_path="~\\.vagrant.d\\insecure_private_key"

    node.vm.provision "shell",
       run: "always",
       inline: "echo 'ssh-rsa AAAAB3NzaC1yc2EAAAADAQABAAABgQCkbNkG6CFXWT/CpG1QSG2UMU+bhQkji4BouPmWXcK91xPbtixPJUne6BEVF3UnT510TKW89ftbue1jAQ/Fvr4MrzdqGESD3M7o1h0VCqWKLfHsQlKbv11aXl47qs5DzsQ8Ror6MqBpipoa/1bzz/hj0WwSSEkRmE2zO2duFJtqFBAyXCDy2jkKlVzOyuEhBTmDFmxmVfA02YI3qBz3uVrQwBP2LZzLVUEEXgeOEqe9gQ+WsdqNnciw0mZPDOtofI9T3vvz7j7SjhR72M27jjcj4yQUIVgmsNR8uskdM+nTlBC/Q1rEQyLlxX59eqjsLg5uyt4MjkHjG3ntt1906CVAyecEYHCj/myPr7hvjQnFLlGMh/8vxh4kFTxd+qOveR1SDym/b0ZOkCMHSYQcFXMd/x2PQtfj1ICUZHpIEuEFCqzKmcx4EiAnOjzLcU/+KSwVRRdIb1BwWNptCpH3OHD4KVP2+w1D9WWTOIlxtMg/jVjd9Dnbb43QTbCNAJMYa/k= x' >> /home/vagrant/.ssh/authorized_keys"
    
    node.vm.provision "shell",
       run: "always",
       inline: "ip add add 172.16.2.24#{i}/22 dev eth0"
    
    #node.vm.provision "shell",
    #   run: "always",
    #   inline: "ip route add default via 172.16.0.1  dev eth0"
       

    node.vm.provision "shell",
       run: "always",
       inline: "sed  -i  's/nameserver 127.0.0.53/nameserver 8.8.8.8/g' /etc/resolv.conf"
    
    


    
    end
  end
end


