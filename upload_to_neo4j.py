import pandas as pd
import networkx as nx
from py2neo import Graph as NeoGraph, Node, Relationship

# ---------- إعداد الاتصال بـ Neo4j ----------
graphdb = NeoGraph("bolt://localhost:7687", auth=("neo4j", "10001000"))

# ---------- حذف البيانات القديمة ----------
graphdb.run("MATCH (n) DETACH DELETE n")

# ---------- تحميل ملف الإكسل ----------
file_path = "C:\\Users\\Hello\\output_file.xlsx"
sheets = pd.read_excel(file_path, sheet_name=None)  # None = كل الشيتات

# ---------- بناء وتخزين الجراف في Neo4j ----------
for sheet_name, df in sheets.items():
    print(f"Processing sheet: {sheet_name}")
    
    students_courses = {}
    for _, row in df.iterrows():
        student_id = row.iloc[1]
        course = row.iloc[2]
        students_courses.setdefault(student_id, set()).add(course)

    # بناء الجراف
    G = nx.Graph()
    for courses in students_courses.values():
        for course1 in courses:
            for course2 in courses:
                if course1 != course2:
                    node1 = f"{sheet_name}:{course1}"
                    node2 = f"{sheet_name}:{course2}"
                    G.add_edge(node1, node2)

    # رفع النودز إلى Neo4j
    for node in G.nodes():
        course_name = node.split(":")[1]
        graphdb.merge(
            Node("Course", name=node, course=course_name, sheet=sheet_name),
            "Course", "name"
        )

    # رفع العلاقات إلى Neo4j
    for edge in G.edges():
        node1, node2 = edge
        course1 = graphdb.nodes.match("Course", name=node1).first()
        course2 = graphdb.nodes.match("Course", name=node2).first()
        if course1 and course2:
            rel = Relationship(course1, "CONFLICTS_WITH", course2)
            graphdb.create(rel)

print("✅ Intermediate graph successfully stored in Neo4j (before coloring).")
