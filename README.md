# Enterprise-Application-Database-Migration-to-AWS


##  Project Description
This project demonstrates migrating an enterprise application from on-premise infrastructure to AWS using modern DevOps and cloud practices.

##  Architecture
- EC2 → App Hosting
- RDS → Database
- DMS → Migration
- S3 → Storage
- Docker → Containerization
- Terraform → Infra provisioning

##  Setup Instructions

### 1. Clone Repo
git clone https://github.com/yourusername/enterprise-aws-migration.git

### 2. Run Locally
docker-compose up --build

### 3. Deploy Infra
cd terraform
terraform init
terraform apply

##  Migration Steps
- Configure AWS DMS
- Run migration
- Validate data

##  Future Improvements
- Add Kubernetes (EKS)
- Add Monitoring (CloudWatch)
- Add Auto Scaling
