terraform {
  required_providers {
    google = {
      source  = "hashicorp/google"
      version = "5.12.0"
    }
  }
}

provider "google" {

  credentials = file(var.credentials)
  project     = var.project_id
  region      = "us-central1"
}

resource "google_storage_bucket" "flood-bucket24" {
  name          = var.google_storage_bucket_name
  location      = var.location
  force_destroy = true

  lifecycle_rule {
    condition {
      age = 1
    }
    action {
      type = "AbortIncompleteMultipartUpload"
    }
  }
  }
  
  resource "google_bigquery_dataset" "flood_dataset" {
  dataset_id = var.bq_dataset_name
}
