# Industry Use Case Demos - NVIDIA Technology

This repository gathers clear, runnable demos of projects that apply NVIDIA technology to real research and industry needs. It gives colleagues and partners one place to browse, clone, and reuse working examples, so they can adopt the same tools with less effort. Each folder holds:

- A short "why it matters" note
- A quick-start script (usually a single `docker run` or `make deploy`)
- A concise README that lists hardware, software stack, and expected results

The collection covers work done by our internal teams and by external collaborators in higher-education, research labs, and industry.

## How to Use This Repo

1. **Pick a project** that matches your interest
2. **Follow the README** to launch the demo on the required compute
3. **Study the concise notes** on design choices and performance tuning
4. **Fork or clone** the code into your own workspace and adapt it

## Repository Structure

```
industry-use-case-demos/
├── projects/              # Individual demo projects
│   ├── test project 1/    # Sample project for testing
│   └── test project 2/    # Another sample project
├── .gitignore             # Git ignore file
└── README.md              # This file
```

## Current Projects

- **Test Project 1**: Sample project template for NVIDIA technology demonstrations
- **Test Project 2**: Another sample project showcasing different implementation approaches

## Prerequisites

- NVIDIA GPU with appropriate drivers
- Docker with NVIDIA Container Runtime
- CUDA Toolkit (version specified per project)
- Git

## Contributing

When adding a new demo:
1. Create a new folder under `projects/`
2. Include a clear README with hardware requirements
3. Provide a one-command deployment option
4. Document performance metrics and optimization notes
5. Submit a pull request

## Support

For questions about specific demos, please check the individual project README files first. For general repository questions, open an issue in this repository. 