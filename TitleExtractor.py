import re


class TaskExtractor:
    def __init__(self):
        self.title_patterns = [
            r"باید\s+(.*?)\s+را",
            r"باید\s+(.*?)\s+انجام دهیم",
            r"باید\s+(.*?)\s+شروع کنیم",
            r"تسک\s+(.*?)\s+است",
            r"وظیفه\s+(.*?)\s+است",
            r"ضروری است\s+(.*?)\s+را",
            r"نیاز به\s+(.*?)\s+داریم",
            r"مهم است\s+(.*?)\s+را",
            r"در دستور کار\s+(.*?)\s+است",
        ]

        self.subtask_patterns = [
            r"ابتدا\s+(.*?)\s+و\s+سپس\s+(.*)",
            r"اول\s+(.*?)\s+و بعد\s+(.*)",
            r"اول\s+(.*?)\s+بعد\s+(.*)",
            r"در مرحله اول\s+(.*?)\s+سپس\s+(.*)",
            r"از یک سو\s+(.*?)\s+و از سوی دیگر\s+(.*)",
            r"شروع با\s+(.*?)\s+و در نهایت\s+(.*)",
        ]

        self.change_patterns = [
            r"عنوان\s+(.*?)\s+به\s+(.*?)\s+تغییر (کرد|یافت)",
            r"عنوان\s+(.*?)\s+به\s+(.*?)\s+عوض (کرد|یافت)",
        ]

    def extract_title(self, text):
        for pattern in self.title_patterns:
            match = re.search(pattern, text)
            if match:
                return match.group(1)
        return None

    def extract_subtasks(self, text):
        for pattern in self.subtask_patterns:
            match = re.search(pattern, text)
            if match:
                return match.groups()
        return []

    def extract_changes(self, text):
        for pattern in self.change_patterns:
            match = re.search(pattern, text)
            if match:
                return match.group(1)
        return None


task_extractor = TaskExtractor()

text_example = 'باید تسک حل تمرین دوم درس را در یک آذر شروع کنیم و تا ده آذر تمام کنیم. برای اینکار باید اول موضوع را مشخص کنیم و بعد پیادەسازی را انجام دهیم.'

title = task_extractor.extract_title(text_example)
subtasks = task_extractor.extract_subtasks(text_example)

print("عنوان وظیفه:", title)
print("زیر وظایف:", subtasks)
