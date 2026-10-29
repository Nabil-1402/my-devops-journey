# IAM

## Key Concepts

- Users and groups
- Policies
- Multi-Factor Authentication (MFA)
- Access

## Commands

| Command | Description |
| --- | --- |
| `aws --version` | Check the installed version of the AWS CLI. |
| `aws configure` | Configure the AWS CLI to access your account. |
| `aws sts get-caller-identity` | Check which identity the CLI is using to access AWS. |
| `aws iam list-users` | List all IAM users. |

## Examples

Example permissions policy:

```json
{
  "Version": "2012-10-17",
  "Id": "S3-Account-Permissions",
  "Statement": [
    {
      "Sid": "1",
      "Effect": "Allow",
      "Principal": {
        "AWS": ["arn:aws:iam::123456789012:root"]
      },
      "Action": [
        "s3:GetObject",
        "s3:PutObject"
      ],
      "Resource": ["arn:aws:s3:::mybucket/*"]
    }
  ]
}
```

Policies follow a defined structure. The `Version` appears at the top, followed by an optional `Id`, which identifies the policy or provides additional context.

The main part is the `Statement`. A policy can contain one or more statements, each describing the permissions it grants or denies.

A statement consists of:

- **Sid:** An optional identifier for the statement.
- **Effect:** Whether the statement allows or denies access (`Allow` or `Deny`).
- **Principal:** The account, user or role to which the statement applies.
- **Action:** The actions the statement allows or denies.
- **Resource:** The resources to which those actions apply.
- **Condition:** Optional conditions that determine when the statement takes effect.

## What I Learned

I learned how AWS IAM controls access through users, groups, policies and roles, including why individual IAM users should be used instead of the root account for everyday tasks. I developed a better understanding of account and service security, particularly the importance of MFA and protecting access keys. I also explored how the AWS CLI supports scripting, automation and service management, and how developers can use AWS SDKs to integrate AWS services directly into their applications.

## Notes

### Users, Groups and Permissions

IAM users and groups are the building blocks for controlling access in AWS.

When you create an AWS account, you receive a root user. You should avoid using or sharing this account for day-to-day tasks. Instead, create individual users for people in your organisation.

Groups make it easier to organise users into teams, such as developers, operations or auditors. Instead of assigning permissions to each person individually, you can assign permissions to the whole group.

- Users do not have to belong to a group.
- A user can belong to multiple groups.
- **Groups contain users, not other groups.**

Users and groups receive permissions through **policies**. These are JSON documents that define which actions are allowed or denied.

AWS follows the **principle of least privilege**: only give users the permissions they need to do their jobs. This helps keep the environment secure while providing sufficient access.

Inline policies are specific to the identity they are attached to rather than being shared policies. Users also receive permissions through their group memberships.

When assigning permissions, consider groups first, then use inline policies where needed.

A policy defines **who can do what, to which resources and under what conditions**.

### Passwords and Multi-Factor Authentication

Password policies help ensure that users choose strong, secure passwords.

You can configure a password policy to:

- Set a minimum password length.
- Require uppercase letters, lowercase letters, numbers and non-alphanumeric characters.
- Allow IAM users to change their own passwords.
- Require password changes after a specified period.
- Prevent password reuse.

**Multi-Factor Authentication (MFA)** adds an extra layer of protection to root and IAM users. If a password is stolen, an attacker would still need the second authentication factor to sign in.

MFA combines:

- **Something you know:** Your password.
- **Something you have:** A security device.

Types of MFA devices include:

- **Virtual MFA devices:** Smartphone apps, such as Google Authenticator or Authy, that generate a one-time code to enter alongside your password.
- **Universal 2nd Factor (U2F) security keys:** Physical devices that connect to your computer’s USB port and authenticate you without requiring a code.
- **Hardware key fobs:** Physical devices that generate a new code every 30 seconds.

### Accessing AWS and Protecting Access Keys

There are three main ways to access AWS:

| Access Method | Purpose |
| --- | --- |
| **AWS Management Console** | A web interface accessed using a password and, ideally, MFA. Useful for manual tasks such as launching EC2 instances, sometimes called “ClickOps”. |
| **AWS Command Line Interface (CLI)** | A terminal tool for managing resources, scripting and automating tasks through AWS services’ public APIs. |
| **AWS Software Development Kit (SDK)** | A set of language-specific APIs that developers use to interact with AWS services directly from application code. |

For example, an application can use an SDK to store files in S3 or launch EC2 instances directly from its code.

Access keys can be managed through the console, with each user responsible for managing their own keys. The access key ID is similar to a username, while the secret access key is similar to a password.

- **Never share access keys.**
- Rotate access keys as a security best practice.

### IAM Roles and Security Tools

AWS services sometimes need to perform actions on your behalf. For example, an EC2 instance may need to read from an S3 bucket, or a Lambda function may need to write logs to CloudWatch.

**IAM roles** provide temporary access to other AWS services without hard-coding long-term credentials, such as access keys or passwords.

Two useful IAM security tools help you review users and permissions:

| Tool | Scope | Purpose |
| --- | --- | --- |
| **IAM Credentials Report** | Account level | Provides a snapshot of the users in your account and the status of their credentials, helping you review account security. |
| **IAM Access Advisor** | User level | Shows which services a user has permission to access and when they were last accessed, helping identify unnecessary permissions. |

### IAM Guidelines and Best Practices

- Avoid using the root account except for AWS account setup.
- Create a separate IAM user for each person.
- Assign users to groups and permissions to groups.
- Create a strong password policy.
- Enable and enforce MFA.
- Use roles to give permissions to AWS services.
- Protect access keys used for programmatic access through the CLI or SDK.
- Audit permissions using IAM Credentials Report and IAM Access Advisor.
- Never share IAM users or access keys.