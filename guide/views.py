import openpyxl
from django.shortcuts import render, redirect
from .models import Account, Guide


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


def upload(request):
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
                        cell = sheet.cell(row, column=2)
                        question = cell.value.lstrip().lower()
                        print(question)

                        Guide.objects.create(question=question)

                    except Exception:
                        pass
    return render(request, "guide/upload.html")


def guide(request):
    if request.method == "POST":
        question = request.POST.get('input-question')
        print(question)

        question = Guide.objects.get(question=question)
        answer = question.answer
        question = question.question

        return render(request, 'guide/guide.html', {'question': question, 'answer': answer})
    else:
        return render(request, 'guide/guide.html', {})
