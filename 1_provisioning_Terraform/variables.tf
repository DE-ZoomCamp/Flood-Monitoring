variable "credentials" {
  description = "The path to the service account key file"
  default     = "./keys/keys.json"

}

variable "project_id" {
  description = "The ID of the project in which the resources will be created"
  type        = string
  default     = "flood-monitoring-project"

}

variable "location" {
  description = "The location of the bucket"
  type        = string
  default     = "US"

}

variable "bq_dataset_name" {
  description = "The name of the dataset to create in BigQuery"
  type        = string
  default     = "floodmonitoring"

}
variable "google_storage_bucket_name" {
  description = "The name of the bucket to create in Google Cloud Storage"
  type        = string
  default     = "flood-bucket24"


}
variable "gcs_storage_class" {
  description = "The storage class of the bucket"
  type        = string
  default     = "STANDARD"

}
