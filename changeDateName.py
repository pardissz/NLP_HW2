import re

def extract_start(text):
    pattern =r"(شروع|استارت).*?(کار|تسک|ددلاین)?.*?(منتقل شد|انتقال یافت|عوض شد|تغییر کرد)?.*?به (.*?)(منتقل شد|انتقال یافت|عوض شد|تغییر کرد)"
    match = re.search(pattern, text)
    if match:
        return match.group(4).strip()
    else:
        return None
def extract_name(text):
    pattern =r"(انجام دهنده|مسئول|افراد مسئول|مسئولیت).*?(کار|تسک)?.*?(منتقل شد|انتقال یافت|عوض شد|تغییر کرد)?.*?به (.*?)(منتقل شد|انتقال یافت|عوض شد|تغییر کرد)"
    match = re.search(pattern, text)
    if match:
        return match.group(4).strip()
    else:
        return None
def extract_ending(text):
    pattern =r"(پایان|ددلاین|مهلت|اتمام).*?(کار|تسک|ددلاین)?.*?(منتقل شد|انتقال یافت|عوض شد|تغییر کرد)?.*?به (.*?)(اضافه شد|منتقل شد|انتقال یافت|عوض شد|تغییر کرد)"
    match = re.search(pattern, text)
    if match:
        return match.group(4).strip()
    else:
        return None
text = "شروع کار به 7 مهر منتقل شد"
print(extract_start(text))
text = "ددلاین کار به 5 مهر منتقل شد"
print(extract_ending(text))
text = "مسئولیت به مریم و بیتا منتقل شد"
print(extract_name(text))