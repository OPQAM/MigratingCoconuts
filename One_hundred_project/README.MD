<div align="center">
  <img src="Images/cover.jpg" alt="My Project Banner" width="50%">
</div>

# General Notes for the One-Hundred Day Suite

## Overview

This project is a 100-day journey to develop Python tools that assist in my Reverse Engineering (RE) studies. The goal is to combine Python practice with RE workflows, resulting in a suite of useful scripts while documenting my daily progress.

### Key Objectives
- **Learn by Doing**: Use this project as a hands-on way to strengthen Python fundamentals and explore automation.
- **Develop Practical Tools**: Build a set of scripts to streamline common RE tasks, such as binary analysis and debugging.
- **Document Progress**: Journal daily to track learning and challenges, culminating in a detailed public portfolio.
- **Personal Goals**: Celebrate milestones and incorporate Japanese learning as part of the journey.

---

## Preparation

### Automation Setup
To streamline journaling and project organization, a Bash script initializes daily folders and readme files:
```bash
for i in {001..100}; do
  mkdir -p Day_$i
  cat <<EOF > Day_$i/readme.md
# Readme for Day $i

## Goals for Today

## Progress Update

### Japanese Tidbits

EOF
done
```

---

## Planned Tools

#### This set of tools isn't set in stone. It's an idea and a WIP.

1. Automated Symbol Extraction and Organization Tool: Parses ELF binaries to extract and organize symbols (e.g., function names, variables) into structured formats like JSON.
2. File Header and Metadata Analyzer: Analyzes headers and metadata of binaries to identify file types, magic numbers, and protections.
3. Automated GDB Scripting Assistant: Simplifies GDB workflows by automating common debugging tasks via Python scripts.
4. Entropy Visualizer and Analyzer: Provides visual and numerical entropy analysis for binary files, aiding malware research.
5. Patch Automation Tool (stretch goal): Automates small binary modifications, streamlining patching and testing workflows.

---

## Get Involved

-[Mastodon](https://mastodon.social/@opqam)

-[Twitter](https://twitter.com/opqamNotSpace)

-[LinkedIn](https://www.linkedin.com/in/ricardo-alves-opqam/)

-[GitHub](https://github.com/OPQAM)

---
