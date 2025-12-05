provider "google-beta" {
  project = var.project_id
  region  = var.region
}

resource "google_dataproc_cluster" "cluster" {
  name   = var.cluster_name
  region = var.region

  cluster_config {
    gce_cluster_config {
      service_account        = var.service_account
      service_account_scopes = ["https://www.googleapis.com/auth/cloud-platform"]
      internal_ip_only       = var.internal_ip_only
    }

    endpoint_config {
      enable_http_port_access = var.enable_component_gateway
    }

    master_config {
      num_instances = 1
      machine_type  = var.master_machine_type

      disk_config {
        boot_disk_type    = var.master_boot_disk_type
        boot_disk_size_gb = var.master_boot_disk_size
      }
    }

    worker_config {
      num_instances = var.num_workers
      machine_type  = var.worker_machine_type

      disk_config {
        boot_disk_type    = var.worker_boot_disk_type
        boot_disk_size_gb = var.worker_boot_disk_size
      }
    }

    software_config {
      image_version = var.image_version
    }
  }
}
