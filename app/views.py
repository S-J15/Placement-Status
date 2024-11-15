from django.shortcuts import render, redirect, get_object_or_404
from .models import Student, Status, Division
from .forms import DataForm
from django.contrib import messages

# Home page view (for displaying pie charts and division counts)
def home(request):
    divisions = Division.objects.all()
    statuses = Status.objects.all()
    
    # Convert the divisions and statuses QuerySets to lists of names
    division_names = [division.div for division in divisions]
    status_names = [status.status for status in statuses]  # Extract the status names
    
    # Pie chart data for each division by status
    division_counts = {
        division: {
            status: Student.objects.filter(div__div=division, status__status=status).count() 
            for status in status_names
        }
        for division in division_names
    }

    # Pie chart data for each status across divisions
    placed_counts = [Student.objects.filter(div__div=division, status__status="Placed").count() for division in division_names]
    not_placed_counts = [Student.objects.filter(div__div=division, status__status="Not_Placed").count() for division in division_names]
    backlog_counts = [Student.objects.filter(div__div=division, status__status="Backlog").count() for division in division_names]

    t_placed=sum(placed_counts)
    t_nplaced=sum(not_placed_counts)
    t_backlogs=sum(backlog_counts)

    context = {
        'division_counts': division_counts,  # For division-specific charts
        'placed_counts': placed_counts,
        'not_placed_counts': not_placed_counts,
        'backlog_counts': backlog_counts,
        'divisions': division_names,  # Pass only division names here
        'statuses': status_names,  # Pass only status names here
        't_placed': t_placed,  # Pass only status names here
        't_nplaced': t_nplaced,  # Pass only status names here
        't_backlogs': t_backlogs,  # Pass only status names here
    }
    return render(request, 'home.html', context)

# View to add or update student data
def addData(request, student_id=None):
    # If student_id is provided, update the existing student
    if student_id:
        student = get_object_or_404(Student, id=student_id)
    else:
        student = None

    if request.method == 'POST':
        form = DataForm(request.POST, request.FILES, instance=student)
        if form.is_valid():
            form.save()
            return redirect('home')  # Redirect to the placed students page after saving
    else:
        form = DataForm(instance=student)  # Pre-fill the form if updating an existing student

    return render(request, 'add.html', {'form': form, 'student': student})

# View to display placed students grouped by division
def placed(request):
    placed_status = Status.objects.get(status='Placed')
    placed_students = Student.objects.filter(status=placed_status)

    # Group students by division (A, B, C)
    divisions = Division.objects.all()
    division_wise_students = {
        division.div: placed_students.filter(div=division)  # Corrected lookup
        for division in divisions
    }

    return render(request, 'placed.html', {
        'division_wise_students': division_wise_students,
    })

# View to display not-placed students grouped by division
def not_placed(request):
    not_placed_status = Status.objects.get(status='Not_Placed')
    not_placed_students = Student.objects.filter(status=not_placed_status)

    # Group students by division (A, B, C)
    divisions = Division.objects.all()
    division_wise_students = {
        division.div: not_placed_students.filter(div=division)  # Corrected lookup
        for division in divisions
    }

    return render(request, 'not_placed.html', {
        'division_wise_students': division_wise_students,
    })

# View to display backlog students grouped by division
def backlog(request):
    backlog_status = Status.objects.get(status='Backlog')
    backlog_students = Student.objects.filter(status=backlog_status)

    # Group students by division (A, B, C)
    divisions = Division.objects.all()
    division_wise_students = {
        division.div: backlog_students.filter(div=division)  # Corrected lookup
        for division in divisions
    }

    return render(request, 'backlog.html', {
        'division_wise_students': division_wise_students,
    })

def delete_student(request, student_id):

    student = get_object_or_404(Student, id=student_id)
    if request.method == "POST":
        student.delete()
        messages.success(request, f"Student with PRN {student.prn} has been successfully deleted.")
        # Redirect back to the referring page or a default page
        return redirect(home)
    else:
        messages.error(request, "Invalid request.")
        return redirect('home')
