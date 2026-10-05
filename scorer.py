import questions

def judge(question: str, expects: str, answer: str, results) -> bool:
    
    if not expects:
        return False
    return expects.strip().lower() in (answer or "".lower)

'''
takes question
expects answer
and returns true or false 
'''

