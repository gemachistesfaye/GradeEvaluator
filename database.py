import os
import datetime
from supabase_client import supabase



# ---------- Student helpers ----------

def create_student(name: str, email: str, password_hash: str, joined_date: str) -> None:
    """Create a new student record in Supabase."""
    supabase.table('students').insert({
        'name': name,
        'email': email,
        'password_hash': password_hash,
        'joined_date': joined_date,
    }).execute()


def get_student_by_email(email: str):
    """Retrieve a single student by email. Returns a dict or None.
    Handles cases where the Supabase request fails or returns no data.
    """
    try:
        resp = supabase.table('students').select('*').eq('email', email).maybe_single().execute()
    except Exception:
        return None
    if not resp or not getattr(resp, 'data', None):
        return None
    return resp.data


def get_student_by_id(student_id: int):
    """Retrieve a single student by id.
    Handles cases where the Supabase request fails or returns no data.
    """
    try:
        resp = supabase.table('students').select('*').eq('id', student_id).maybe_single().execute()
    except Exception:
        return None
    if not resp or not getattr(resp, 'data', None):
        return None
    return resp.data


def update_user_password(user_id: int, new_password_hash: str) -> None:
    """Update the password_hash for a given user."""
    supabase.table('students').update({
        'password_hash': new_password_hash
    }).eq('id', user_id).execute()


def get_user_profile(user_id: int):
    """Return the student profile dict for the given user id."""
    return get_student_by_id(user_id)


def get_grade_count(user_id: int) -> int:
    """Return the number of grades recorded for a user."""
    resp = supabase.table('grades').select('id', count='exact').eq('student_id', user_id).execute()
    # Supabase returns count in 'count' header; fallback to len of data
    if hasattr(resp, 'count') and resp.count is not None:
        return resp.count
    if resp.data:
        return len(resp.data)
    return 0

# ---------- Grade helpers ----------

def add_grade(student_id: int, subject: str, score: float, letter_grade: str, gpa_points: float, ai_feedback: str) -> None:
    """Insert a new grade record for a student."""
    supabase.table('grades').insert({
        'student_id': student_id,
        'subject': subject,
        'score': score,
        'letter_grade': letter_grade,
        'gpa_points': gpa_points,
        'ai_feedback': ai_feedback,
        'date': datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S'),
    }).execute()


def get_grades_by_student(student_id: int):
    """Return a list of grade dicts for the given student, ordered newest first."""
    resp = supabase.table('grades').select('*').eq('student_id', student_id).order('id', desc=True).execute()
    return resp.data if resp.data else []


def delete_grade_db(grade_id: int, student_id: int) -> None:
    """Delete a specific grade belonging to a student."""
    supabase.table('grades').delete().eq('id', grade_id).eq('student_id', student_id).execute()

def delete_grade(grade_id: int, student_id: int) -> None:
    """Compatibility wrapper – calls delete_grade_db for legacy imports."""
    delete_grade_db(grade_id, student_id)


def clear_grades_db(student_id: int) -> None:
    """Delete all grades for a given student."""
    supabase.table('grades').delete().eq('student_id', student_id).execute()

def clear_grades(student_id: int) -> None:
    """Compatibility wrapper – calls clear_grades_db for legacy imports."""
    clear_grades_db(student_id)
