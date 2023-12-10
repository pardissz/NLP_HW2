class StatusChecker:
    finish_status = ['تموم شد', 'اتمام یافت', 'تمام شد', 'تمام است', 'پایان یافت', 'تمومه', 'تمام شده', 'اوکی شد',
                     'اوکی شده', 'تموم شده', 'به اتمام رسید']
    urgency_status = ['حتما', 'فورا', 'سریعا', 'به سرعت', 'به شدت', 'حتماً', 'فوراً', 'سریعاً', 'قطعاً']

    @staticmethod
    def check_status(text):
        is_done = False
        is_urgent = False
        text_words = text.split()
        for bigram in StatusChecker.finish_status:
            if bigram in text:
                is_done = True
                break
        if any(word in text_words for word in StatusChecker.urgency_status):
            is_urgent = True
        return is_done, is_urgent


if __name__ == '__main__':
    text = 'من حتما  میگم که تموم شده '
    is_done, is_urgent = StatusChecker.check_status(text)
    print('is_done:', is_done, ', is_urgent:', is_urgent)

    text = 'تسک به اتمام رسید'
    is_done, is_urgent = StatusChecker.check_status(text)
    print('is_done:', is_done, ', is_urgent:', is_urgent)
