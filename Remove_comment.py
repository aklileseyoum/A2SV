class Solution:
    def removeComments(self, source: List[str]) -> List[str]:
        answers = []
        in_comment_section = 0
        answer = ""
        for line in source:
            index = 0
            while index < len(line):
                if index < len(line) - 1 and line[index] == '/' and line[index+1] == '/' and in_comment_section == 0:
                    index = len(line)
                elif index < len(line) - 1 and line[index] == '/' and line[index+1] == '*' and in_comment_section == 0:
                    in_comment_section = 1
                    index += 1
                elif index < len(line) - 1 and line[index] == '*' and line[index+1] == '/' and in_comment_section == 1:
                    in_comment_section = 0
                    index += 1
                elif in_comment_section == 0:
                    answer += line[index]
                index += 1

            if answer and in_comment_section == 0:
                answers.append(answer)
                answer = ""


        return answers
