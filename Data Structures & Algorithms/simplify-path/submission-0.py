class Solution:
    def simplifyPath(self, path: str) -> str:
        stack = []

        for txt in path.split("/") :
            if txt == ".." :
                if stack : stack.pop()
                
            elif txt != "" and txt != "." :
                stack.append(txt)

        return "/" + "/".join(stack)
