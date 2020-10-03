import openpyxl
from django.shortcuts import render, redirect
from .models import Account, Question, Answer
from .filters import QuestionFilter


# Create your views here.

def home(request):
    return render(request, 'guide/home.html', {})


def login(request):
    if request.method == 'POST':
        email = request.POST['input-email']
        name = request.POST['input-name']
        Account.objects.create(email=email, name=name)
    return redirect('guide')

# fuction to extract data from spreadsheet and upload in DB


def upload_question(request):
    # command to load the workbook
    work_book = openpyxl.load_workbook("MCQ.xlsx")

    # to keep track of the sheets
    count = 1

    # iterating over the excel sheets
    for page in work_book.sheetnames:
        # to work with the particular sheet
        sheet = work_book[page]
        if count < 11:
            print(sheet.title)
            count += 1

            # to iterate over the rows till the end of the sheet
            for row in range(1, sheet.max_row+1):

                # To check whether the first cell is not null
                if sheet.cell(row, column=1).value != None:
                    try:
                        cell1 = sheet.cell(row, column=1)
                        cell2 = sheet.cell(row, column=2)
                        s_no = cell1.value
                        question = cell2.value.lstrip().lower()
                        print(question)
                        print(s_no)
                        Question.objects.create(s_no=s_no, question=question)

                    except Exception:
                        pass
    return render(request, "guide/upload_question.html")


def upload_answer(request):
    # command to load the workbook
    work_book = openpyxl.load_workbook("MCQ.xlsx")

    # to keep track of the sheets

    # iterating over the excel sheets
    for page in work_book.sheetnames:
        # to work with the particular sheet
        sheet = work_book[page]
        if sheet.title == "Page 10" or sheet.title == "Page 11" or sheet.title == "Page 12" or sheet.title == "Page 13" or sheet.title == "Page 14":
            print(sheet.title)

            # to iterate over the rows till the end of the sheet
            for row in range(1, sheet.max_row+1):

                # To check whether the first cell is not null
                if sheet.cell(row, column=1).value != None:
                    try:
                        cell1 = sheet.cell(row, column=1)
                        cell2 = sheet.cell(row, column=2)
                        s_no = cell1.value
                        answer = cell2.value.strip().lower()
                        print(answer)
                        print(s_no)
                        Answer.objects.create(s_no=s_no, answer=answer)
                        question = Question.objects.get(s_no=s_no)
                        question.answer = answer
                        question.save()

                    except Exception:
                        pass
    return render(request, "guide/upload_answer.html")


def guide(request):

    questions = Question.objects.all()
    answers = Answer.objects.all()

    my_filter = QuestionFilter(request.GET, queryset=questions)
    questions = my_filter.qs

    context = {
        'questions': questions,
        'answers': answers,
        'my_filter': my_filter,
    }
    return render(request, 'guide/guide.html', context)
