# DREAD Risk Scoring Tool

A cybersecurity threat modelling tool that calculates risk using the DREAD methodology. This project demonstrates understanding of infrastructure security, threat analysis, and risk scoring core skills in cybersecurity engineering and SOC operations.

## Why This Project Matters
Risk modelling is essential for identifying, prioritising, and mitigating cybersecurity threats. This tool shows competency in:
- Threat modelling methodologies
- Secure system design
- Python scripting
- Risk assessment and analysis
- Cybersecurity infrastructure concepts

## Features
- Interactive command-line interface (CLI)
- Full DREAD scoring model
- Automatic risk classification (Low → Critical)
- Clean, modular architecture (Dread class + CLI interface)
- Input validation to prevent crashes
- Beginner-friendly and fully commented code

## Project Structure
```
dread-risk-analyzer
│── main.py
│── dread.py
│── sample_threats.json (coming soon)
│── README.md
│── requirements.txt (optional)
```

## Installation and Running
Clone the repository:
```bash
git clone https://github.com/YOURNAME/dread-risk-analyzer
cd dread-risk-analyzer
python main.py
```

## Example Output
```
--- DREAD Risk Scoring Tool ---

Threat: SQL Injection
Damage: 9
Reproducibility: 8
Exploitability: 7
Affected Users: 9
Discoverability: 6
Total Score: 39
Risk Level: HIGH
```

## Understanding DREAD
DREAD is a structured risk assessment model used by cybersecurity professionals to evaluate threats.

- **Damage** – The impact if the attack succeeds
- **Reproducibility** – How easily the attack can be reproduced
- **Exploitability** – How easy it is to exploit the vulnerability
- **Affected Users** – The number of affected victims
- **Discoverability** – How easy it is to find the vulnerability

The total score guides organisations in prioritising mitigation strategies.

## Future Improvements
- Add CSV and JSON export functionality
- Allow scoring multiple threats in a single session
- Implement a graphical version (Tkinter/Flask)
- Integrate MITRE ATT&CK technique mapping
- Add sample datasets for training and demonstration
- Add coloured CLI output and improved formatting

## Author
Built by **Gabriel Emenike — Cybersecurity Infrastructure Student**

## License
MIT