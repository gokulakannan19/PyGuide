import openpyxl
from django.http import HttpResponse
from django.shortcuts import render


# Create your views here.


def home(request):
    if request.method == 'POST':
        email = request.POST['input-email']
        name = request.POST['input-name']
        print(email)
        print(name)

    else:
        return render(request, 'guide/home.html', {})


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
        if count < 10:
            print(sheet.title)
            count += 1

            # to iterate over the rows till the end of the sheet
            for row in range(1, sheet.max_row+1):

                # To check whether the first cell is not null
                if sheet.cell(row, column=1).value != None:
                    try:

                        # To extract data from a specific cell from the sheet and assigning it to a variable
                        cell = sheet.cell(row, column=2)
                        print(cell.value.lstrip())
                    except Exception:
                        pass
    return render(request, "guide/upload.html")


def guide(request):
    return render(request, 'guide/guide.html', {})
