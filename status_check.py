
text="من حتما  میگم که تموم شده "
def check_status_in_text(text):
    finish_status = ['تموم شد', 'اتمام یافت', 'تمام شد', 'تمام است', 'پایان یافت', 'تمومه', 'تمام شده', 'اوکی شد',
                     'اوکی شده', 'تموم شده']
    urgency_status = ['حتما', 'فورا', 'سریعا', 'به سرعت', 'به شدت', 'حتماً', 'فوراً', 'سریعاً', 'قطعاً']
    isDone = False
    isUrgent = False
    text_words = text.split()
    for bigram in finish_status:
        if bigram in text:
            isDone=True
            break
    if any(word in text_words for word in urgency_status):
        isUrgent=True
    return isDone,isUrgent
print(check_status_in_text(text))