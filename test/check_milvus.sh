# Test DNS and TCP 443 (serverless uses HTTPS)
# Replace HOST with domain from your URI (in03-7b3b56e59d62e9d.serverless.aws-eu-central-1.cloud.zilliz.com)
HOST=in03-7b3b56e59d62e9d.serverless.aws-eu-central-1.cloud.zilliz.com

# DNS
nslookup $HOST

# TCP connect on 443
# Linux/macOS
nc -vz $HOST 443
# PowerShell
Test-NetConnection -ComputerName $HOST -Port 443

# Optional: simple HTTPS GET (may require Authorization header)
curl -v "https://$HOST/" --insecure