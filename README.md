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
