# Terraform Config

To deploy Google Dataproc that run spark jobs.

create a `terraform.tfvars` file.

```terraform
project_id        = "<value>"
region            = "<value>"
cluster_name      = "<value>"

service_account   = "<value>"

master_machine_type  = "<value>"
master_boot_disk_size = 50

num_workers          = 2
worker_machine_type  = "<value>"
worker_boot_disk_size = 50

image_version = "<value>"
```