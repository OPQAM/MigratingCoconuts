<div align="center">
  <img src="Images/cover.jpg" alt="My Project Banner" width="50%">
</div>

# 100 Days of Code: Creating the LazySuite 

## What's This About?

The LazySuite is a personal project where I commit to building a set of Python tools designed to assist in my Reverse Engineering (RE) studies. Over the next 100 days, I will focus on creating, refining, and documenting these tools while also improving my Python programming skills. This project serves as both a learning opportunity and a portfolio to showcase my progress in Python, automation, and low-level programming.

### Objectives
- **Python Practice**: Strengthen my Python funcamentals by applying them to practical, tool-oriented programming.
- **RE Tools**: Develop tools that are relevant to RE tasks, aiming to simplify and automate common workflows.
- **Portfolio Development**: Build a repository of scripts and tools that demonstrate my skills and thought processes.
- **Public Sharing**: Share daily updates on social media (Twitter, LinkedIn, Mastodon) and weekly blog posts to document progress and insights.

---

## Why LazySuite?
The LazySuite is named after my philosophy of automating tedious, repetitive tasks. The goal is to create a collection of lightweight, effective scripts that aid RE efforts, even for a beginner. It’s about working smarter, not harder.

---

## Preparation

### Automation Setup
To streamline journaling and project organization, a Bash script initializes daily folders and readme files:
```bash
for i in {001..100}; do
  mkdir -p Day_$i
  cat <<EOF > Day_$i/readme.md
<div align="center">
  <img src="../../Images/image_$i.jpg" alt="Day $i Banner" width="50%">
</div>

# Readme for Day $i

## Goals for Today

## Progress Update

### Japanese Tidbits

EOF
done
```

---

## Planned Tools

#### Here are some of the tools I plan to include in the LazySuite:

1. Binary Analysis Helpers
- Automate disassembly, symbol extraction, and binary comparisons.
2. Debugger Integration
- Scripts to streamline GDB workflows and set up hooks dynamically.
3. File Analysis Utilities
- Tools for inspecting file headers, entropy analysis, and metadata extraction.
4. Documentation Generators
- Automated report or markdown generation from analysis outputs.

---

## Get Involved
Contributions are welcome! Whether it’s feedback, ideas, or code improvements, feel free to open an issue or submit a pull request. This project is beginner-friendly, so don’t hesitate to jump in.

#### How to Use the LazySuite
Each tool in the LazySuite will include detailed documentation on its usage, purpose, and installation requirements. Check the individual tool directories for more information.


#### Sharing my progress on:
-[Mastodon](https://mastodon.social/@opqam)

-[Twitter](https://twitter.com/opqamNotSpace)

-[LinkedIn](https://www.linkedin.com/in/ricardo-alves-opqam/)

-[GitHub](https://github.com/OPQAM)

---

Deactivating Virtual environment: deactivate
source /home/opqam/Projects/Python/One_hundred_project/myenv/bin/activate

