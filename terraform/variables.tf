variable "project_id" {
  description = "GCP project ID"
  type        = string
}

variable "region" {
  description = "GCP region to deploy the cluster"
  type        = string
}

variable "cluster_name" {
  description = "Dataproc cluster name"
  type        = string
}

variable "service_account" {
  description = "Service account for Dataproc nodes"
  type        = string
}

variable "internal_ip_only" {
  description = "Whether VMs should have internal IP only (equivalent to --no-address)"
  type        = bool
  default     = true
}

variable "enable_component_gateway" {
  description = "Enable Dataproc Component Gateway"
  type        = bool
  default     = true
}

variable "master_machine_type" {
  description = "Master node machine type"
  type        = string
}

variable "master_boot_disk_type" {
  description = "Master node boot disk type"
  type        = string
  default     = "pd-ssd"
}

variable "master_boot_disk_size" {
  description = "Master node boot disk size in GB"
  type        = number
}

variable "num_workers" {
  description = "Number of worker nodes"
  type        = number
}

variable "worker_machine_type" {
  description = "Worker node machine type"
  type        = string
}

variable "worker_boot_disk_type" {
  description = "Worker node boot disk type"
  type        = string
  default     = "pd-ssd"
}

variable "worker_boot_disk_size" {
  description = "Worker node boot disk size in GB"
  type        = number
}

variable "image_version" {
  description = "Dataproc image version"
  type        = string
}
