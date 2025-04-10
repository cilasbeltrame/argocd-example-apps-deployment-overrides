# ArgoCD Example Apps Deployment Overrides

This repository contains deployment overrides and configurations for ArgoCD applications across different environments and cloud providers. It provides a structured way to manage application deployments with environment-specific configurations.

## Repository Structure

```
.
├── aws/                   # AWS-specific configurations
│   └── 1030/              # Environment ID
│       └── dev1/          # Environment name
│           ├── applications.yaml    # Application configurations
│           └── helm-guestbook.yaml  # Helm chart overrides
│           └── ...         # Helm chart overrides
│ 
└── .github/               # GitHub Actions workflows
```

## Configuration Files

### applications.yaml
The `applications.yaml` file contains environment-specific configurations:
- Cloud provider information
- Environment details (ID and name)
- Helm chart repository configuration
- Target revision for Helm charts

Example:
```yaml
cloud: aws
env:
  id: 1030
  name: dev1
helmChartsRepoURL: https://github.com/cilasbeltrame/argocd-example-apps
helmChartsTargetRevision: 0.5.0
```

## Usage

1. Navigate to the appropriate environment directory (e.g., `aws/1030/dev1/`)
2. Modify the `applications.yaml` file with your environment-specific configurations
3. Update Helm chart overrides in the respective YAML files
4. Commit and push changes to trigger ArgoCD sync

## Prerequisites

- ArgoCD installed and configured
- Access to the target Kubernetes cluster
- Appropriate permissions to modify ArgoCD applications
- Helm charts repository access

## Contributing

1. Create a new branch for your changes
2. Make your modifications in the appropriate environment directory
3. Test your changes in a development environment
4. Submit a pull request with a clear description of your changes

## Best Practices

1. Keep environment-specific configurations separate
2. Use consistent naming conventions across environments
3. Document any specific requirements or dependencies
4. Test configurations before applying to production
5. Maintain version control for all changes

## TODO: Pipeline Implementation (Draft)

> **Note**: This section outlines the initial strategy for the pipeline implementation. The actual implementation in `.github/workflows/pipeline.yaml` may evolve based on testing and feedback.

### Deployment Flow Overview

```
PR Created
    │
    ▼
Changes Merged
    │
    ▼
Pre-build Phase
    │
    ▼
Identify Changed Files
    │
    ▼
For Each Changed File
    │
    ▼
Process Config (deploy.py)
    │
    ▼
Generate Manifest
    │
    ▼
Deploy Release (deploy-release.sh)
    │
    ▼
Verify Deployment
```

1. **Configuration Processing** (`deploy.py`):
   - Input: Environment-specific `applications.yaml`
   - Process: Jinja2 templating
   - Template: `templates/application.j2`
   - Output: Processed Kubernetes manifest

2. **Release Deployment** (`deploy-release.sh`):
   - Setup: AWS credentials and kubectl context
   - Action: Apply generated manifest
   - Verification: Check deployment status
   - Rollback: Handle failed deployments

### Pipeline Steps
1. Create PR targeting the main branch
2. Merge changes
3. Pre-build phase:
   - Trigger pipeline to identify changed environment paths
   - Example paths:
     - `aws/1030/dev1/applications.yaml` (cluster: dev1)
     - `aws/1030/stg1/applications.yaml` (cluster: stg1)
4. For each modified file:
   - Set up kubectl for the affected cluster using AWS credentials
   - Process the configuration using the deploy script:
     ```bash
     .github/workflows/scripts/deploy.py <path-to-changed-file> | kubectl apply -f -
     ```

### Initial Prerequisites (Subject to Change)
- AWS credentials configured in GitHub (preferred to be AWS roles) to reach the target clusters
- Jinja2 template files in the `templates` directory
