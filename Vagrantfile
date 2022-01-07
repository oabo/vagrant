

Vagrant.configure("2") do |config|
  config.vm.box = "generic/ubuntu2004"
  config.ssh.insert_key = false


(1..1).each do |i|
  config.vm.define "node#{i}" do |node|
    node.vm.hostname = "v#{i}"
    node.ssh.private_key_path="~/.vagrant.d/insecure_private_key"
    
    node.vm.network  "public_network",
      bridge:'enp3s0' ,
      auto_config: false  
      

    node.vm.provision "ansible" do |ansible|
      ansible.playbook = "playbook.yml"
      end


    end
  end
end


