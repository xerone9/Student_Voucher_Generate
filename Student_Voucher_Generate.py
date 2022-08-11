import PIL
from PIL import Image, ImageFont, ImageDraw
from amount_to_million import amount_to_million
import datetime
import os

datex = str(datetime.datetime.now().strftime("%d,%b,%y")).split(".")
date_and_time = str(datex[0]).split(" ")
date = date_and_time[0]
print_date = str(date).replace(",","-")

def print_voucher(receipt_no, student_id, student_name, amount, type_of_fee, due_date):
    amount_in_words = str(amount_to_million(amount)).replace("  ", " ") + " Rupees Only"


    im = Image.open("voucher.jpg")
    draw = ImageDraw.Draw(im)
    font = PIL.ImageFont.truetype('arial-bold.ttf', 22)

    # SET STUDENT RECEIPT NO
    draw.text((112, 123), str(receipt_no), font=font, fill='black')
    draw.text((526, 123), str(receipt_no), font=font, fill='black')
    draw.text((940, 123), str(receipt_no), font=font, fill='black')
    draw.text((1354, 123), str(receipt_no), font=font, fill='black')

    # SET STUDENT ID
    draw.text((90, 461), str(student_id), font=font, fill='black')
    draw.text((504, 461), str(student_id), font=font, fill='black')
    draw.text((918, 461), str(student_id), font=font, fill='black')
    draw.text((1332, 461), str(student_id), font=font, fill='black')

    # SET STUDENT Name
    # draw.line((90, 512, 90 + int(len(student_name)) * 13, 512), fill='black', width=3)
    draw.text((90, 490), str(student_name[:25]), font=font, fill='black')
    draw.text((504, 490), str(student_name[:25]), font=font, fill='black')
    draw.text((918, 490), str(student_name[:25]), font=font, fill='black')
    draw.text((1332, 490), str(student_name[:25]), font=font, fill='black')

    # SET Total Amount
    draw.text((290, 632), '{:,}'.format(int(amount)), font=font, fill='black')
    draw.text((704, 632), '{:,}'.format(int(amount)), font=font, fill='black')
    draw.text((1118, 632), '{:,}'.format(int(amount)), font=font, fill='black')
    draw.text((1532, 632), '{:,}'.format(int(amount)), font=font, fill='black')

    font = PIL.ImageFont.truetype('arial.ttf', 20)
    if len(amount_in_words) > 36:
        amount_in_words = str(amount_in_words[:35] + '-\n' + amount_in_words[35:])

    # SET Total Amount In Words
    draw.text((5, 670), str(amount_in_words), font=font, fill='black')
    draw.text((419, 670), str(amount_in_words), font=font, fill='black')
    draw.text((833, 670), str(amount_in_words), font=font, fill='black')
    draw.text((1247, 670), str(amount_in_words), font=font, fill='black')

    # SET Total Amount In Tuition Fee
    draw.text((290, 600), '{:,}'.format(int(amount)), font=font, fill='black')
    draw.text((704, 600), '{:,}'.format(int(amount)), font=font, fill='black')
    draw.text((1118, 600), '{:,}'.format(int(amount)), font=font, fill='black')
    draw.text((1532, 600), '{:,}'.format(int(amount)), font=font, fill='black')

    # SET Tuition Fee
    draw.text((20, 602), str(type_of_fee), font=font, fill='black')
    draw.text((430, 602), str(type_of_fee), font=font, fill='black')
    draw.text((844, 602), str(type_of_fee), font=font, fill='black')
    draw.text((1258, 602), str(type_of_fee), font=font, fill='black')

    font = PIL.ImageFont.truetype('Arial_Italic.ttf', 20)


    # SET Current Date
    draw.text((130, 286), str(print_date), font=font, fill='black')
    draw.text((544, 286), str(print_date), font=font, fill='black')
    draw.text((958, 286), str(print_date), font=font, fill='black')
    draw.text((1372, 286), str(print_date), font=font, fill='black')

    # SET Current Date
    draw.text((130, 318), str(due_date), font=font, fill='black')
    draw.text((544, 318), str(due_date), font=font, fill='black')
    draw.text((958, 318), str(due_date), font=font, fill='black')
    draw.text((1372, 318), str(due_date), font=font, fill='black')


    im.save(r'voucher.pdf')
    os.startfile('voucher.pdf')

