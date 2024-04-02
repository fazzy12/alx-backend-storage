#!/usr/bin/env python3

from pymongo import MongoClient

def top_students(mongo_collection):
    """Returns all students sorted by average score."""
    students = mongo_collection.find()

    top_students = []
    for student in students:
        scores = [topic['score'] for topic in student['topics']]
        average_score = sum(scores) / len(scores) if scores else 0
        student['averageScore'] = round(average_score, 2)
        top_students.append(student)

    top_students.sort(key=lambda x: x['averageScore'], reverse=True)
    return top_students
