# Install Docker And Running Project

Step 1: update ubuntu

```bash
sudo apt-get update
```

Step 2:Copy all until step 7. All this step is adding repository and download from the repository was added.

```bash
sudo apt-get install \
    ca-certificates \
    curl \
    gnupg \
    lsb-release
```

Step 3:

```bash
sudo mkdir -p /etc/apt/keyrings
```

Step 4:

```bash
curl -fsSL https://download.docker.com/linux/ubuntu/gpg | sudo gpg --dearmor -o /etc/apt/keyrings/docker.gpg
```

Step 5:

```bash
echo \
  "deb [arch=$(dpkg --print-architecture) signed-by=/etc/apt/keyrings/docker.gpg] https://download.docker.com/linux/ubuntu \
  $(lsb_release -cs) stable" | sudo tee /etc/apt/sources.list.d/docker.list > /dev/null
```

Step 6: update ubuntu

```bash
sudo apt-get update
```

Step 7:

```bash
sudo apt-get install docker-ce docker-ce-cli containerd.io docker-compose-plugin
```

Step 8:

```bash
sudo apt install docker-compose
```

Step 9:

```bash
sudo docker pull mongo
```

Step 10: Building containers from docker-compose

```bash
docker-compose build
```

Step 11: Running docker

```bash
docker-compose up -d
```

Step 12: Checking logs from container. Maybe the name is flask or something

```bash
docker logs 
```
