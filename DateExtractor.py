def detect_words(text, position, week, holiday, month, numbers):
    text = text.split()
    detected_words = []
    for i, word in enumerate(text):
        if word in position:
            if i > 0:
                prev_word = text[i-1]
                try:
                    float_next = float(prev_word)
                    is_number = True
                except ValueError:
                    is_number = False
                if prev_word == "امسال":
                    is_number = True
                if prev_word in week or prev_word in holiday :
                    detected_words.append(prev_word)
                    return detected_words
                elif is_number :  # check the word after the number
                    prev2_word = text[i-2]
                    prev3_word = text[i - 3]
                    if prev2_word in month and prev3_word in numbers:
                        detected_words.append(prev3_word+ ' '+prev2_word + ' ' + prev_word)
                        return detected_words
                    elif prev2_word in month:
                        detected_words.append(prev2_word + ' ' + prev_word)
                        return detected_words
                    else:
                        detected_words.append(prev_word)
                        return detected_words
                elif prev_word in month and i > 1:  # check the word after the number
                    prev2_word = text[i-2]
                    if prev2_word in numbers:
                        detected_words.append(prev2_word + ' ' + prev_word)
                        return detected_words
                    else:
                        detected_words.append(prev_word)
                        return detected_words
            if i < len(text) - 1:  # check the word after
                next_word = text[i+1]
                if next_word in week or next_word in holiday:
                    detected_words.append(next_word)
                elif next_word in month and i < len(text) - 1:  # check the word after the number
                    next2_word = text[i+2]
                    try:
                        float_next = float(next2_word)
                        is_number = True
                    except ValueError:
                        is_number = False
                    if next2_word == "امسال":
                        is_number=True
                    if  is_number:
                        detected_words.append(next_word + ' ' + next2_word)
                        return detected_words
                    else:
                        detected_words.append(next_word)
                        return detected_words
                elif next_word in numbers and i < len(text) - 1:  # check the word after the number
                    next2_word = text[i+2]
                    next3_word = text[i + 3]
                    try:
                        float_next = float(next3_word)
                        is_number = True
                    except ValueError:
                        is_number = False
                    if next3_word == "امسال":
                        is_number=True
                    if next2_word in month and is_number :
                        detected_words.append(next_word + ' ' + next2_word+ ' ' + next3_word)
                        return detected_words
                    elif next2_word in month:
                        detected_words.append(next_word + ' ' + next2_word)
                        return detected_words
                    else:
                        detected_words.append(next_word)
                        return detected_words


    return detected_words
week = ['شنبه', 'یکشنبه', 'دوشنبه', 'سه شنبه', 'چهارشنبه', 'پنجشنبه', 'جمعه']
month = ['مهر', 'آبان', 'آذر', 'دی', 'بهمن', 'اسفند', 'فروردین', 'اردیبهشت', 'خرداد', 'تیر', 'مرداد', 'شهریور']
spec_numbers = ['یک', 'دو', 'سه', 'چهار', 'پنج', 'شش', 'هفت', 'هشت', 'نه', 'ده', 'یازده', 'دوازده', 'سیزده', 'چهارده', 'پانزده', 'شانزده', 'هفده', 'هجده', 'نوزده', 'بیست', 'بیست و یک', 'بیست و دو', 'بیست و سه', 'بیست و چهار', 'بیست و پنج', 'بیست و شش', 'بیست و هفت', 'بیست و هشت', 'بیست و نه', '1','2','3','4','5','6','7','8','9','10','سی','11','13','14','15','16','17','18','19','12','20','23','24','25','26','27','28','29','30','21','22','31',]
holidays=['عید','تابستون','زمستون','کریسمس','بهار','پاییز','محرم']
pre=['از','شروع']
pos=['تا','پایان']
ordinal_numbers = ["یکم", "دوم", "سوم", "چهارم", "پنجم", "ششم", "هفتم", "هشتم", "نهم", "دهم",
                   "یازدهم", "دوازدهم", "سیزدهم", "چهاردهم", "پانزدهم", "شانزدهم", "هفدهم", "هجدهم", "نوزدهم", "بیستم",
                   "بیست و یکم", "بیست و دوم", "بیست و سوم", "بیست و چهارم", "بیست و پنجم", "بیست و ششم", "بیست و هفتم", "بیست و هشتم", "بیست و نهم", "سی‌ام", "سی و یکم"]
farsi_numbers = ["۱", "۲", "۳", "۴", "۵", "۶", "۷", "۸", "۹", "۱۰", "۱۱", "۱۲", "۱۳", "۱۴", "۱۵", "۱۶", "۱۷", "۱۸", "۱۹", "۲۰", "۲۱", "۲۲", "۲۳", "۲۴", "۲۵", "۲۶", "۲۷", "۲۸", "۲۹", "۳۰", "۳۱"]
concatenated_list =ordinal_numbers+spec_numbers+farsi_numbers

text="این تسک را در ۲ آذر امسال شروع و تا 3 مهر پایان رسونده کرده."

print(detect_words(text, pre, week, holidays, month, concatenated_list))  # Output: ['15 July']
print(detect_words(text, pos, week, holidays, month, concatenated_list))  # Output: ['15 July']
