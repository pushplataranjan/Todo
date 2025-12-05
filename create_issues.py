"""
Script to help create GitHub issues from ISSUES.md
This script parses ISSUES.md and creates a JSON file that can be used with GitHub CLI
"""
import re
import json

def parse_issues_file():
    """Parse ISSUES.md and extract issue information"""
    issues = []
    
    with open('ISSUES.md', 'r', encoding='utf-8') as f:
        content = f.read()
    
    # Split by issue separator
    issue_blocks = content.split('---')
    
    for block in issue_blocks:
        if 'Issue #' not in block:
            continue
        
        issue = {}
        
        # Extract issue number and title
        title_match = re.search(r'Issue #\d+:\s*(.+)', block)
        if title_match:
            issue['title'] = title_match.group(1).strip()
        
        # Extract labels
        labels_match = re.search(r'\*\*Labels:\*\*\s*(.+)', block)
        if labels_match:
            labels_str = labels_match.group(1).strip()
            issue['labels'] = [label.strip().replace('`', '') for label in labels_str.split(',')]
        
        # Extract description
        desc_match = re.search(r'\*\*Description:\*\*\s*(.+?)(?=\*\*Acceptance|\*\*Files)', block, re.DOTALL)
        if desc_match:
            issue['body'] = desc_match.group(1).strip()
        
        # Extract acceptance criteria
        criteria_match = re.search(r'\*\*Acceptance Criteria:\*\*\s*(.+?)(?=\*\*Files|\Z)', block, re.DOTALL)
        if criteria_match:
            criteria = criteria_match.group(1).strip()
            issue['body'] += '\n\n## Acceptance Criteria\n' + criteria
        
        # Extract files to modify
        files_match = re.search(r'\*\*Files to Modify:\*\*\s*(.+?)(?=\n\n---|\Z)', block, re.DOTALL)
        if files_match:
            files = files_match.group(1).strip()
            issue['body'] += '\n\n## Files to Modify\n' + files
        
        if issue.get('title'):
            issues.append(issue)
    
    return issues

def create_github_cli_commands(issues):
    """Generate GitHub CLI commands for creating issues"""
    commands = []
    
    for i, issue in enumerate(issues, 1):
        labels = ' '.join([f'--label "{label}"' for label in issue.get('labels', [])])
        title = issue.get('title', f'Issue #{i}')
        body = issue.get('body', '').replace('"', '\\"').replace('\n', '\\n')
        
        command = f'gh issue create --title "{title}" --body "{body}" {labels}'
        commands.append(command)
    
    return commands

def main():
    """Main function"""
    print("Parsing ISSUES.md...")
    issues = parse_issues_file()
    
    print(f"Found {len(issues)} issues")
    
    # Save as JSON
    with open('issues.json', 'w', encoding='utf-8') as f:
        json.dump(issues, f, indent=2, ensure_ascii=False)
    
    print("Saved issues to issues.json")
    
    # Generate GitHub CLI commands
    commands = create_github_cli_commands(issues)
    
    with open('create_issues.sh', 'w', encoding='utf-8') as f:
        f.write('#!/bin/bash\n')
        f.write('# GitHub CLI commands to create issues\n')
        f.write('# Usage: bash create_issues.sh\n\n')
        for cmd in commands:
            f.write(cmd + '\n')
    
    print("Saved GitHub CLI commands to create_issues.sh")
    print("\nTo create issues, run:")
    print("  bash create_issues.sh")
    print("\nOr use the GitHub web interface with issues.json")

if __name__ == '__main__':
    main()

