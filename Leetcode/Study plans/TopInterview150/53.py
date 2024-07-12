class Solution:
    def simplifyPath(self, path: str) -> str:
        res_stack = []
        path = path.replace("//", "/")
        path = path.split("/")
        while "" in path:
            path.remove("")

        for path_element in path:
            if path_element == ".":
                continue
            elif path_element == "..":
                if res_stack:
                    res_stack.pop()
            else:
                res_stack.append(path_element)

        res = "/"
        return res + "/".join(res_stack)
