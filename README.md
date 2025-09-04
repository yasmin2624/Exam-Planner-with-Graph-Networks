# 📘 Exam Planner with Graph Networks

## 📌 Overview
This project is an **Exam Planner** built using **Graph Networks**.  
It aims to schedule exams for different courses while avoiding conflicts (e.g., students having two exams at the same time).  
The idea is inspired by **Graph Coloring**, where courses are represented as nodes and conflicts between courses are represented as edges.

## 🛠️ Features
- Model exam scheduling as a **graph coloring problem**.  
- Automatically assigns time slots to exams with **minimum conflicts**.  
- Allows visualization of the network using **NetworkX & Matplotlib**.  
- Provides flexibility for handling different exam constraints.  

## 📂 Project Structure
├── Networks.ipynb # Main Jupyter Notebook containing implementation
├── data/ # (Optional) Directory for input datasets
├── images/ # (Optional) Graph visualization outputs
├── README.md # Project documentation


## 🚀 Technologies Used
- **Python 3**
- **NetworkX** → Graph representation and operations
- **Matplotlib** → Visualization
- **Jupyter Notebook** → Interactive development

## ⚡ How It Works
1. Represent each **course** as a node in a graph.  
2. Add an **edge** between two nodes if they share students (conflict).  
3. Apply a **graph coloring algorithm** to assign time slots (colors).  
4. Visualize the resulting exam schedule as a network.  

## ▶️ How to Run
1. Clone the repository:
   ```bash
   git clone https://github.com/yasmin2624/Exam-Planner-with-Graph-Networks.git
   cd Exam-Planner-with-Graph-Networks
Install dependencies:
pip install -r requirements.txt
(If requirements.txt not available, install manually: pip install networkx matplotlib jupyter)

Open Jupyter Notebook:

jupyter notebook
Run the cells inside Networks.ipynb.

📊 Example Output 
-Graph visualization showing how courses are connected.
-Assigned time slots for each course with minimal conflicts.
Graph visualization showing how courses are connected.

Assigned time slots for each course with minimal conflicts.
