variable "ansible_connection" {
  default = "docker"
}
source "docker" "example" {
  image = "ubuntu:latest"
  commit = true
}
build {
  sources = ["source.docker.example"]
  provisioner "ansible" {
    playbook_file = "playbook.yaml"
  }
}